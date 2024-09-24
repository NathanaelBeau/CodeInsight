from huggingface_hub import HfApi, Repository

# Set repository details
hf_repo_name = "Nbeau/CodeInsight"

# Initialize the Hugging Face API
api = HfApi()

# Clone the repository locally if it doesn't already exist
repo = Repository(local_dir=".", clone_from=hf_repo_name)

# Add all files and push to the repository
repo.git_add(".")
repo.git_commit("Initial commit of CodeInsight dataset")
repo.git_push()
