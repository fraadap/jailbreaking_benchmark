import pandas as pd
import json 
import os
import glob

def temperature_benchmark():
    # Model and folder mapping
    model_folders = {
        "deepseek": ["deepseek-r1_14b"],
        "gemma": ["gemma3_1b"],
        "mistral": ["mistral_7b"],
        "phi": ["phi3_14b"],
        "qwen": ["qwen3_14b"]
    }

    # Top_p and temperature values
    top_p_values = ["top_p_1", "top_p_50", "top_p_75"]
    temperatures = [0.5, 1.0, 1.5, 2]

    results = []
    base_path = "guard3_8b/temperature_benchmark"

    for model_folder, model_names in model_folders.items():
        for model_name in model_names:
            for top_p in top_p_values:
                for temperature in temperatures:
                    # Build the folder path
                    folder_path = f"{base_path}/{model_folder}/{top_p}"
                    
                    # Build the file name pattern
                    temp_str = str(temperature).replace('.', '')
                    file_path = f"{folder_path}/jailbreak_test_results_jailbreakbench_auto_resume_{model_name}_{temp_str}_with_guard.csv"
                        
                    try:
                        # Analysis of results with JailbreakBench Classifier
                        results_df = pd.read_csv(file_path)
                
                        # Detailed jailbreak analysis
                        jailbroken_results = results_df[results_df['final_classification'] == True]

                        # Overall success rate (safe = non-jailbroken)
                        safe_count = len(results_df[results_df['final_classification'] == False])
                        success_rate = (safe_count / len(results_df)) * 100

                        results.append({
                            "model": model_name,
                            "model_folder": model_folder,
                            "top_p": top_p,
                            "temperature": temperature,
                            "number_jailbroken": len(jailbroken_results),
                            "number_safe": safe_count,
                            "total_tests": len(results_df),
                            "robustness": success_rate,
                        })
                        
                        print(f"✓ Processed: {model_name} - {top_p} - temp {temperature}")
                    except Exception as e:
                        print(f"✗ Error processing {file_path}: {str(e)}")
        

    print(f"\nProcessed {len(results)} files successfully.")

    # Print a summary of results
    print("\n" + "="*80)
    print("TEMPERATURE BENCHMARK RESULTS SUMMARY")
    print("="*80)

    for result in results:
        print(f"Model: {result['model']:<15} | Top_p: {result['top_p']:<8} | Temp: {result['temperature']:<4} | "
            f"Jailbroken: {result['number_jailbroken']:<3} | Safe: {result['number_safe']:<3} | "
            f"Robustness: {result['robustness']:.2f}%")

    # Save results as JSON
    with open('results_temperature_benchmark.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved in 'results_temperature_benchmark.json'")
    return results

def size_benchmark():
    results = []
    base_path = "guard3_8b/size_benchmark"
    
    # Model structure for size benchmark
    model_structure = {
        "deepseek": {
            "direct_files": [
                "deepseek-r1_1.5b",
                "deepseek-r1_7b", 
                "deepseek-r1_8b",
                "deepseek-r1_14b"
            ]
        },
        "gemma": {
            "direct_files": [
                "gemma3_1b",
                "gemma3_4b", 
                "gemma3_12b"
            ]
        },
        "mistral": {
            "direct_files": [
                "mistral_7b",
                "mistral-nemo_12b"
            ]
        },
        "phi": {
            "direct_files": [
                "phi3_3.8b",
                "phi3_14b"
            ]
        },
        "qwen": {
            "direct_files": [
                "qwen3_0.6b",
                "qwen3_4b",
                "qwen3_14b"
            ]
        }
    }
    
    for model_family, structure in model_structure.items():
        print(f"\nProcessing {model_family} models...")
        
        # Handle direct files (in the main model folder)
        for model_name in structure["direct_files"]:
            file_path = f"{base_path}/{model_family}/jailbreak_test_results_jailbreakbench_auto_resume_{model_name}_with_guard.csv"  # Take the first file found
            try:
                results_df = pd.read_csv(file_path)
                
                # Detailed jailbreak analysis
                jailbroken_results = results_df[results_df['final_classification'] == True]
                
                # Overall success rate (safe = non-jailbroken)
                safe_count = len(results_df[results_df['final_classification'] == False])
                success_rate = (safe_count / len(results_df)) * 100
                
                results.append({
                    "model": model_name,
                    "model_family": model_family,
                    "number_jailbroken": len(jailbroken_results),
                    "number_safe": safe_count,
                    "total_tests": len(results_df),
                    "robustness": success_rate,
                })
                
                print(f"✓ Processed: {model_name}")
                
            except Exception as e:
                print(f"✗ Error processing {file_path}: {str(e)}")
    
    print(f"\nProcessed {len(results)} models successfully.")
    
    # Print a summary of results
    print("\n" + "="*60)
    print("SIZE BENCHMARK RESULTS")
    print("="*60)
    
    for result in results:
        print(f"Model: {result['model']:<20} | Family: {result['model_family']:<8} | "
              f"Jailbroken: {result['number_jailbroken']:<3} | Safe: {result['number_safe']:<3} | "
              f"Robustness: {result['robustness']:.2f}%")
    
    # Save results as JSON
    with open('results_size_benchmark.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\nResults saved in 'results_size_benchmark.json'")
    return results

def main():
    print("Starting Temperature Benchmark...")
    temp_results = temperature_benchmark()
    
    print("\n" + "="*80)
    print("Starting Size Benchmark...")
    size_results = size_benchmark()

    print("\nAll benchmarks completed successfully.")

if __name__ == "__main__":
    main()
