# !pip install huggingface_hub hf_transfer
import os
# os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download

print("Starting download...")

snapshot_download(
    repo_id = "bobchenyx/DeepSeek-V3-0324-MLA-GGUF",
    local_dir = "bobchenyx/DeepSeek-V3-0324-MLA-GGUF",
    allow_patterns = ["*IQ1_M*"],
)

print("Download finished.")