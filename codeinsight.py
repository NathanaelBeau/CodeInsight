import torch

import os
from typing import List, Union
from pathlib import Path

import configparser

import signal
import multiprocessing
from multiprocessing import Queue
from queue import Empty
import os

import numpy as np
import pandas as pd
import sklearn

from typing import Optional
from datasets import Dataset

def check_cpu_count(num_procs: int):
    from multiprocessing import cpu_count
    import warnings

    if 2 * num_procs > cpu_count():
        warnings.warn(
            f"You have {cpu_count()} cpus but are using {num_procs} processes to run the evaluation!",
            Warning,
        )


class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException


def exec_wrapper(queue, combined_code):
    try:
        exec(combined_code)
        queue.put("Success")
    except Exception as e:
        queue.put(e)

def run_code_with_timeout(combined_code, timeout_duration):

    queue = Queue()
    process = multiprocessing.Process(target=exec_wrapper, args=(queue, combined_code))
    process.start()
    process.join(timeout_duration)

    if process.is_alive():
        process.terminate()
        process.join()
        return "Timeout or resource limit exceeded"

    try:
        result = queue.get_nowait()
    except Empty:  # Correctly catch the Empty exception
        return "No result returned"

    if isinstance(result, Exception):
        raise result
    return result


class CoNaLaExecProblem():
    def __init__(
            self,
            problem_path: Union[str, Path]
    ):
        self.problem_path = Path(problem_path)
        self.problem_id = int(self.problem_path.name.replace("q", ""))
        self.data = dict()

        # load meta information in .cfg
        problem_config = configparser.RawConfigParser()
        problem_config.read(self.problem_path / ".cfg")
        for args in [
            ("library", "lib"),
            ("test", "test_case_cnt"),
            ("origin", "source"),
            ("labels", "labels")
        ]:
            self.data[args[1]] = problem_config.get(*args)

        # read problem content files
        for file_name in [
            "prompt.txt",
            "test_reference.py",
            "nl.txt",
            "code.txt",
        ]:
            with open(self.problem_path / file_name, "r", encoding="UTF-8") as f:
                self.data[file_name.split(".")[0]] = f.read()

    def test(self, generated_code, timeout_duration=10):  # default timeout is 10 seconds
        test_files = [f for f in os.listdir(self.problem_path / "unit_tests") if f.startswith("test_")]

        all_tests_passed = True

        globals_dict = {"np": np,
                        "pd": pd,
                        "sklearn": sklearn}

        import_packages = "import numpy\nimport math\nimport pandas\nimport string\nimport datetime\nimport json\nimport itertools\nimport random\nimport functools\nimport collections\nimport sklearn\nimport bs4\nimport re\n"

        for test_file in test_files:
            with open(os.path.join(self.problem_path / "unit_tests", test_file), 'r') as f:
                test_content = f.read()

            # Combine test content with generated_code
            # combined_code = import_packages + generated_code + "\n" + test_content
            combined_code = import_packages+ "\n" + generated_code + "\n" + test_content

            # Set the signal timeout alarm
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout_duration)  # set the timeout

            # exec(combined_code, globals_dict)
            try:
                print(combined_code)
                exec(combined_code, globals_dict)
            # except TimeoutException:
            #     all_tests_passed = False
            #     print(f"Tests in {test_file} timed out for example {self.problem_id}!")
            #     continue  # skip the current test and move to the next one
            # except AssertionError:
            #     all_tests_passed = False
            #     print(f"Tests in {test_file} failed for example {self.problem_id}!")
            #     continue  # skip the current test and move to the next one
            # except SyntaxError:
            #     all_tests_passed = False
            #     print(f"Syntax error in {test_file} for example {self.problem_id}!")
            #     continue
            # except NameError:
            #     all_tests_passed = False
            #     print(f"Name error in {test_file} for example {self.problem_id}!")
            #     continue
            # except TypeError:
            #     all_tests_passed = False
            #     print(f"Type error in {test_file} for example {self.problem_id}!")
            #     continue
            # except ValueError:
            #     all_tests_passed = False
            #     print(f"Value error in {test_file} for example {self.problem_id}!")
            #     continue
            # except ImportError:
            #     all_tests_passed = False
            #     print(f"Import error in {test_file} for example {self.problem_id}!")
            #     continue
            # except Exception as e:
            #     all_tests_passed = False
            #     print(f"Unexpected error occurred in {test_file} for example {self.problem_id}: {e}")
            #     continue
            finally:
                signal.alarm(0)  # reset the alarm in all cases

        return all_tests_passed

    def __getitem__(self, key):
        return self.data[key]

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()
class CoNaLaExecDataset(torch.utils.data.Dataset):
    def __init__(self,
                 source_dir: Union[str, Path] = "CoNaLaExec",
                 mode: str = 'fine_tuning',
                 split: Optional[str] = None):

        self.source_dir = source_dir
        self.mode = mode  # can be "fine_tuning" or "all_eval"

        source_path = Path(source_dir)
        self.data_list = []

        if self.mode == "fine_tuning":
            if split not in ["train", "test"]:
                raise ValueError(f"Invalid split: {split} for mode {mode}. Split should be 'train' or 'test'.")
            folder_path = source_path / split
            problems = sorted(os.listdir(folder_path), key=lambda x: int(str(x).replace("q", "")))
            for index, problem in enumerate(problems):
                new_problem = CoNaLaExecProblem(folder_path / problem)
                self.data_list.append(new_problem)

        elif self.mode == "all":
            data_folders = ["train", "test"]
            for data_folder in data_folders:
                folder_path = source_path / data_folder
                problems = sorted(os.listdir(folder_path), key=lambda x: int(str(x).replace("q", "")))
                for index, problem in enumerate(problems):
                    new_problem = CoNaLaExecProblem(folder_path / problem)
                    self.data_list.append(new_problem)

        else:
            raise ValueError(f"Unknown mode: {mode}")

    def __getitem__(self, idx):
        return self.data_list[idx]

    def __len__(self):
        return len(self.data_list)

    def __iter__(self):
        return iter(self.data_list)




if __name__ == '__main__':
    dataset = CoNaLaExecDataset('./CoNaLaExec', mode_eval='finetuning')

