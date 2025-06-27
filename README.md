# Evaluating the Robustness of Large Language Models to Standard Jailbreaking Attacks: An Analysis of Model Scale and Temperature
This project investigates the vulnerability of state-of-the-art Large Language Models to jailbreaking attacks, adversarial prompts designed to bypass built-in safety mechanisms and elicit harmful or policy-violating outputs. The focus is on comparative analysis of LLM robustness across different model sizes and configurations, examining how factors such as model scale and decoding temperature impact susceptibility to standard jailbreaking techniques.

We will involve a diverse range of LLMs with varying sizes and architectures. We obtain this model through Ollama:

### Gemma
- gemma3:1b - 815MB
- gemma3:4b - 3.3GB
- gemma3:12b - 8.1GB

### Qwen
- qwen3:0.6b - 523MB
- qwen3:4b - 2.6GB
- qwen3:14b - 9.3GB

## Phi
- phi3:3.8b - 2.2GB
- phi3:14b - 7.9GB

## Mistral
- mistral-small:22b - 13GB 
- mistral-small:24b - 14GB 

## Deepseek 
- deepseek-r1:1.5b - 1.1GB
- deepseek-r1:7b - 4.7GB
- deepseek-r1:8b - 5.2GB
- deepseek-r1:14b - 9.0GB

In addition, we will systematically vary the **temperature** parameter during inference to observe its impact on the Attack Success Rate (ASR) and the nature of the generated responses.

We will utilize prompts extracted from the following dataset, ensuring they are specifically designed for jailbreaking purposes:

- **`https://github.com/JailbreakBench/artifacts/blob/main/attack-artifacts/`**: We will select prompts that are examples of successful jailbreaking attacks generated via techniques like PAIR, GCG, and JBC, which aim to elicit harmful content.
