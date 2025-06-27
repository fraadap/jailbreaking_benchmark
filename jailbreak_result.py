import pandas as pd
import json 

models = ["gemma3_1b", "qwen3_14b", "phi3_14b", "mistral_7b", "deepseek-r1_14b"]
results = []

for model in models:
    MODEL_TO_USE = model

    for temperature in [0.5, 1.0, 1.5, 2]:
        try:
            # Analisi dei risultati con JailbreakBench Classifier
            results_df = pd.read_csv('temperature_benchmark/jailbreak_test_results_jailbreakbench_auto_resume_'+MODEL_TO_USE+'_'+str(temperature).replace('.','')+'.csv')

            # Analisi dettagliata dei jailbreak
            jailbroken_results = results_df[results_df['final_classification'] == True]

            # Tasso di successo complessivo
            safe_count = len(results_df[results_df['final_classification'] == False])
            success_rate = (safe_count / len(results_df)) * 100

            results.append({
                "model": MODEL_TO_USE,
                "temperature": temperature,
                "number_jailbroken": len(jailbroken_results),
                "number_safe": safe_count,
                "success_rate": success_rate,
            })
        except FileNotFoundError:
            print(f"File not found for model {MODEL_TO_USE} at temperature {temperature}. Skipping...")


for result in results:
    print(f"Model: {result['model']}, Temperature: {result['temperature']}, Number Jailbroken: {result['number_jailbroken']}, Number Safe: {result['number_safe']}, Success Rate: {result['success_rate']:.2f}%")

# Salva i risultati come JSON
with open('results_size_benchmark.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)