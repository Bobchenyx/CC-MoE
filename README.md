# Collaborative Compression for Large-Scale MoE Deployment on Edge

Authors: Yixiao Chen, Yanyue Xie, Ruining Yang, Pu Zhao *et al.*

[![arXiv](https://img.shields.io/badge/arXiv-2509.25689-df2a2a?logo=arxiv&logoColor=white)](https://www.arxiv.org/abs/2509.25689)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-bobchenyx-FFD21F?logo=huggingface&logoColor=yellow)](https://huggingface.co/bobchenyx/DeepSeek-V3-0324-MLA-GGUF)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-Reference-0078D7?labelColor=555555&logoColor=white)](https://github.com/deepseek-ai/DeepSeek-V3)
[![llama.cpp](https://img.shields.io/badge/llama.cpp-Reference-4CAF50?labelColor=555555&logo=github&logoColor=white)](https://github.com/ggml-org/llama.cpp)

---

## Intro
The Mixture of Experts (MoE) architecture enables scaling Large Language Models (LLMs) efficiently by increasing capacity without raising computation cost. However, ultra-large MoEs like DeepSeek-V3 still pose challenges for deployment on memory-constrained edge devices.  
We introduce a collaborative compression framework that integrates expert pruning, activation adjustment, and mixed-precision quantization, reducing DeepSeek-V3’s storage from 1.3 TB to 103 GB while maintaining considerable accuracy. 

---

## Framework Overview
<div align="center">
  <img src="assets/main.png"/>
</div><br/>
The overall framework architecture of CC-MoE. The middle part shows a block-level schematic of DeepSeek MoE. The left part highlights our Performance-Aware Expert Reduction and Pruning-Aware Activation Adjustment for FFN layers, while the right part illustrates the mixed-precision quantization process applied to the remaining model.

---

### Usage Guide

---

### Model Download

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

- [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3).
- [tflsxyy](https://github.com/tflsxyy).
- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp), [unsloth.ai](https://unsloth.ai/), [bartowski](https://github.com/bartowski1182).  
- [ikawrakow/ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp), [ikawrakow](https://github.com/ikawrakow), [ubergarm](https://github.com/ubergarm).
- [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness).

We sincerely thank them for their excellent contributions to the open-source community.


