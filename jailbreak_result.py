import pandas as pd
import json

models = ["gemma3_1b", "gemma3_12b", "qwen3_0.6b", "qwen3_4b", "qwen3_14b", "phi3_3.8b", "phi3_14b", "mistral_7b", "mistral-nemo_12b", "deepseek-r1_1.5b", "deepseek-r1_7b", "deepseek-r1_8b", "deepseek-r1_14b"]
results = []

for model in models:
    MODEL_TO_USE = model

    # Analisi dei risultati con JailbreakBench Classifier
    results_df = pd.read_csv('size_benchmark/jailbreak_test_results_jailbreakbench_auto_resume_'+MODEL_TO_USE+'.csv')

    # Analisi dettagliata dei jailbreak
    jailbroken_results = results_df[results_df['final_classification'] == True]

    # Tasso di successo complessivo
    safe_count = len(results_df[results_df['final_classification'] == False])
    success_rate = (safe_count / len(results_df)) * 100

    results.append({
        "model": MODEL_TO_USE,
        "number_jailbroken": len(jailbroken_results),
        "number_safe": safe_count,
        "success_rate": success_rate,
    })



for result in results:
    print(f"Model: {result['model']}, Number Jailbroken: {result['number_jailbroken']}, Number Safe: {result['number_safe']}, Success Rate: {result['success_rate']:.2f}%")

# Salva i risultati come JSON
with open('results_size_benchmark.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)