Title: Evaluating the Robustness of Large Language Models to Standard Jailbreaking Attacks: An Analysis of Model Scale and Temperature

The topic addressed: This project investigates the vulnerability of state-of-the-art Large Language Models to jailbreaking attacks, adversarial prompts designed to bypass built-in safety mechanisms and elicit harmful or policy-violating outputs. The focus is on comparative analysis of LLM robustness across different model sizes and configurations, examining how factors such as model scale and decoding temperature impact susceptibility to standard jailbreaking techniques.

the results of the preliminary analysis about:

- *existing literatur:*
    - **Taxonomies of Jailbreaking Attacks:**  Common categorizations include:
        - **Prompt-based attacks:** These are the most common, involving crafting specific input text to bypass safety filters. Sub-categories include:
            - **Instruction Following Exploitation:** Leveraging the LLM's inherent ability to follow instructions, even if those instructions are malicious.
            - **Context Manipulation:** Creating a fictional scenario where the LLM is encouraged to generate harmful content under a different persona or ethical framework.
            - **Obfuscation and Encoding:** Using techniques like character substitution, foreign languages, or specialized encodings to hide malicious intent from safety filters.
            - **Indirect/Covert Attacks:** Embedding harmful requests within seemingly benign tasks, requiring the model to covertly fulfill the malicious request.
            - **Multi-turn Attacks:** Gradually guiding the model towards harmful content over several conversational turns.
    - **Attack Generation Methodologies:** A significant body of work focuses on automated or semi-automated methods for generating effective jailbreaking prompts:
        - **Gradient-based Optimization:** These methods treat jailbreaking as an optimization problem, finding a sequence of tokens  that maximizes the probability of the LLM generating an unsafe response. This requires access to model gradients, often making it a white-box or gray-box attack.
        - **Optimization-Free Methods:** These techniques rely on clever prompt engineering without direct access to model gradients. They are highly effective for black-box scenarios.
        - **LLM-as-a-Hacker:** Recent research explores using one LLM to generate jailbreaking prompts for another, effectively automating the red-teaming process.
- *existing datasets/benchmarks:*
    - **AdvBench:** AdvBench is a collection of adversarial prompts designed to elicit harmful content. https://huggingface.co/datasets/walledai/AdvBench
    - **HarmBench:** It contains a diverse set of harmful prompts across various categories. https://www.harmbench.org/explore
- *existing paper with code*
    - https://arxiv.org/abs/2307.15043:  The paper introduced **GCG**, a highly effective method for generating "universal and transferable" adversarial suffixes that can jailbreak aligned LLMs.
    - https://arxiv.org/html/2311.03348: 
    This paper introduces **PAIR**, an attack method that leverages role-playing and impersonation to craft effective jailbreak prompts.

For the homework project, existing systems and datasets to be involved in your comparative experimental setting:

We will involve a diverse range of LLMs with varying sizes and architectures. We obtain this model through API REST from github copilot student pack:`gpt-4o, gpt-4o-mini, meta-llama-3.1-405b-instruct, meta-llama-3.1-70b-instruct, meta-llama-3.1-8b-instruct, phi-3-medium-4k-instruct, phi-3-mini-4k-instruct, phi-3.5-mini-instruct, phi-3.5-moe-instruct, mistral-nemo, mistral-small, jamba-1.5-large, jamba-1.5-mini`

For each of these models, we will systematically vary the **temperature** parameter during inference to observe its impact on the Attack Success Rate (ASR) and the nature of the generated responses.

We will utilize prompts extracted from the following datasets, ensuring they are specifically designed for jailbreaking purposes:

- **`https://github.com/JailbreakBench/artifacts/blob/main/attack-artifacts/`**: We will select prompts that are examples of successful jailbreaking attacks generated via techniques like PAIR, GCG, and JBC, which aim to elicit harmful content.
- **`https://github.com/verazuo/jailbreak_llms/tree/main`**: From this repository, we will specifically extract prompts marked as `true` (indicating a successful jailbreaking attempt) to ensure we are testing against known effective adversarial examples.