import json
from peft import PeftModel

import os
import sys

import torch
from peft import (
    LoraConfig,
    get_peft_model,
    get_peft_model_state_dict,
    set_peft_model_state_dict,
)

from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq
from codeinsight import CodeInsightDataset


train_dataset = CodeInsightDataset(source_dir="CodeInsight", mode="fine_tuning", split="train")
eval_dataset = CodeInsightDataset(source_dir="CodeInsight", mode="fine_tuning", split="test")


## Load model

base_model = "CodeLlama-13b-hf"
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    load_in_8bit=True,
    torch_dtype=torch.float16,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-13b-hf")

### 3. Check base model


eval_prompt = """You are a powerful code generation model. Your job is to convert a given natural language prompt into Python function and return the result.
Extract the part (either 'upper' or 'lower') triangular part of the matrix mat0.
import numpy as np
def test(mat0, part='upper'):
"""
model_input = tokenizer(eval_prompt, return_tensors="pt")

model.eval()
with torch.no_grad():
    print(tokenizer.decode(model.generate(**model_input, max_new_tokens=100)[0], skip_special_tokens=True))

### 4. Tokenization

tokenizer.add_eos_token = True
tokenizer.pad_token_id = 0
tokenizer.padding_side = "left"

def tokenize(prompt):
    result = tokenizer(
        prompt,
        truncation=True,
        max_length=512,
        padding=False,
        return_tensors=None,
    )

    # "self-supervised learning" means the labels are also the inputs:
    result["labels"] = result["input_ids"].copy()

    return result

def generate_and_tokenize_prompt(data_point):
    full_prompt = f"""You are a powerful code generation model. Your job is to convert a given natural language prompt into Python function and return the result.
{data_point["nl"]}
{data_point["code"]}
"""
    return tokenize(full_prompt)

tokenized_train_dataset = train_dataset._dataset.map(generate_and_tokenize_prompt)
tokenized_eval_dataset = eval_dataset._dataset.map((generate_and_tokenize_prompt))

### 5. Setup Lora

model.train() # put model back into training mode

config = LoraConfig(
    r=16,
    lora_alpha=16,
    target_modules=[
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)
model = get_peft_model(model, config)

resume_from_checkpoint = "" # set this to the adapter_model.bin file you want to resume from

if resume_from_checkpoint:
    if os.path.exists(resume_from_checkpoint):
        print(f"Restarting from {resume_from_checkpoint}")
        adapters_weights = torch.load(resume_from_checkpoint)
        set_peft_model_state_dict(model, adapters_weights)
    else:
        print(f"Checkpoint {resume_from_checkpoint} not found")


if torch.cuda.device_count() > 1:
    # keeps Trainer from trying its own DataParallelism when more than 1 gpu is available
    model.is_parallelizable = True
    model.model_parallel = True

### 6. Training arguments

batch_size = 128
per_device_train_batch_size = 32
gradient_accumulation_steps = batch_size // per_device_train_batch_size
output_dir = "python-code-llama"

training_args = TrainingArguments(
        per_device_train_batch_size=per_device_train_batch_size,
        gradient_accumulation_steps=gradient_accumulation_steps,
        warmup_steps=100,
        max_steps=300,
        learning_rate=3e-5,
        fp16=True,
        logging_steps=10,
        optim="adamw_torch",
        evaluation_strategy="steps", # if val_set_size > 0 else "no",
        save_strategy="steps",
        eval_steps=20,
        save_steps=20,
        output_dir=output_dir,
        # save_total_limit=3,
        load_best_model_at_end=False,
        # ddp_find_unused_parameters=False if ddp else None,
        group_by_length=True, # group sequences of roughly the same length together to speed up training
        report_to="none", # if use_wandb else "none",
        run_name=None, # if use_wandb else None,
    )

trainer = Trainer(
    model=model,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset,
    args=training_args,
    data_collator=DataCollatorForSeq2Seq(
        tokenizer, pad_to_multiple_of=8, return_tensors="pt", padding=True
    ),
)

model.config.use_cache = False

old_state_dict = model.state_dict
model.state_dict = (lambda self, *_, **__: get_peft_model_state_dict(self, old_state_dict())).__get__(
    model, type(model)
)
if torch.__version__ >= "2" and sys.platform != "win32":
    print("compiling the model")
    model = torch.compile(model)

trainer.train()

model.save_pretrained('python-code-llama')

### EVAL ###
base_model = "CodeLlama-13b-hf"
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    load_in_8bit=True,
    torch_dtype=torch.float16,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("CodeLlama-13b-hf")

model.eval()

model = PeftModel.from_pretrained(model, 'python-code-llama/checkpoint-300/')

generated_codes = {}
for index, example in enumerate(eval_dataset):
    code_generated = tokenizer.decode(model.generate(example['prompt'], max_new_tokens=100)[0], skip_special_tokens=True)
    tokenizer.decode(model.generate(**model_input, max_new_tokens=100)[0], skip_special_tokens=True)

    generated_codes[index] = code_generated
    print(code_generated)

with open('returned_codes_finetuned_80_20.json', 'w') as f:
    json.dump(generated_codes, f)