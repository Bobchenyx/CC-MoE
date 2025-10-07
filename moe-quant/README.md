## MoE Mixed Precision Quantization with llama.cpp
We here provide guidance for reproducing Mixed Precision Quantization using [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) 

---

### 1. Installation Guide

We provide a submodule reference for the llama.cpp b6700 release.

However, we strongly recommend cloning the latest version for best compatibility.

```
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp

cmake -B build -DGGML_CUDA=ON -DBUILD_SHARED_LIBS=OFF -DLLAMA_CURL=OFF
cmake --build build --config Release -j --clean-first

# Verify that the installation succeeded.
build/bin/llama-cli --version 
```

---

### 2. Convert Safetensors to GGUF
This step is required before running any PyTorch model with llama.cpp. 

Please make sure that your model is supported for conversion by the version of llama.cpp you previously cloned and built.

```
conda create -n cc-moe python=3.10 -y
conda actiavte cc-moe

cd llama.cpp
pip install requirements/requirements-convert_hf_to_gguf.txt

python3 llama.cpp/convert_hf_to_gguf.py \
  <Path-To-HF-Model> \
  --outfile <Path-To-Output-GGUF> \
  --outtype bf16 \
  --split-max-size 50G ## maximun allowed for hf upload.
```

---

### 3. Imatrix Guide
For extremely low-bit quantization, an imatrix file must be generated before running the actual quantization process.
```
build/bin/llama-imatrix -m <Path-To-GGUF-Model> -f some-text.txt -o <Name-Of-Imatrix>.gguf \
#    [--save-frequency 0] \
#    [--parse-special] \
#    [--show-statistics] [...]
```

---

### 4. LLM Quantization
For running mixed-precision quantization, you can replace the original code with our llama-quant patch and rebuild the project.

However, for models with architectures other than DeepSeek-V3, you may encounter issues during quantization.
Therefore, for users who are new to llama.cpp, we recommend using the built-in `--tensor-type` option to perform mixed-precision quantization.

We provide a sample command for quantization below.
```
# A folder is required before running any quant.
mkdir <Dir-For-Quantized-Model> 

CUDA_VISIBLE_DEVICES="" llama.cpp/build/bin/llama-quantize \
    --imatrix <Path-To-Imatrix>.gguf_file \
    <Path-To-BF16-GGUF-Model> \
    <Path-To-Quantized-Model> \
    IQ1_M ## quant options
#    --token-embedding-type <Type-Name>
#    --output-tensor-type <Type-Name>
#    --tensor-type "<Tensor-Regex>=<Type-Name>"
#    96 2>&1 | tee DeepSeek-V3-IQ1_M.log

```

---

### Citation

If this work is helpful, please kindly cite as:

```bibtex
@article{chen2025collaborative,
  title={Collaborative Compression for Large-Scale MoE Deployment on Edge},
  author={Chen, Yixiao and Xie, Yanyue and Yang, Ruining and Jiang, Wei and Wang, Wei and He, Yong and Chen, Yue and Zhao, Pu and Wang, Yanzhi},
  journal={arXiv preprint arXiv:2509.25689},
  year={2025}
}
```

### Acknowledgements

This repository builds upon the outstanding work of the following open-source authors and projects:

- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
- [unsloth.ai](https://unsloth.ai/)  
- [bartowski](https://github.com/bartowski1182)  
- [ikawrakow/ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)  
- [ikawrakow](https://github.com/ikawrakow)  
- [ubergarm](https://github.com/ubergarm)

We sincerely thank them for their excellent contributions to the open-source community.


