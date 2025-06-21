import jailbreakbench as jbb
import json

# Carica l'artifact
artifact = jbb.read_artifact(
    method="PAIR",
    model_name="vicuna-13b-v1.5"
)

# Estrai i parametri generali (una volta sola, sono fuori da .jailbreaks[])
parameters = artifact.parameters.model_dump()

print("=== Parameters ===")
for key, value in parameters.items():
    print(f"{key}:\n{json.dumps(value, indent=2) if isinstance(value, dict) else value}\n")

# Crea la lista di oggetti jailbreak con i campi aggiuntivi
jailbreak_list = []

# Estrai i valori dai parametri per i campi aggiuntivi
model_name = parameters.get('model')
attack_type = parameters.get('attack_type')
method = parameters.get('method')

# Crea la lista iterando su tutti i jailbreaks
for jailbreak in artifact.jailbreaks:
    # Converti il jailbreak in dizionario
    jailbreak_dict = jailbreak.model_dump()
      # Filtra solo gli elementi con jailbroken: true
    if jailbreak_dict.get('jailbroken') == True:
        # Rimuovi i campi non desiderati
        fields_to_remove = [
            "response", 
            "number_of_queries", 
            "queries_to_jailbreak", 
            "prompt_tokens", 
            "response_tokens", 
            "jailbroken_llama_guard1"
        ]
        
        for field in fields_to_remove:
            jailbreak_dict.pop(field, None)  # pop con None evita errori se il campo non esiste
        
        # Aggiungi i tre campi aggiuntivi
        jailbreak_dict['model'] = model_name
        jailbreak_dict['attack_type'] = attack_type
        jailbreak_dict['method'] = method
        
        # Aggiungi alla lista
        jailbreak_list.append(jailbreak_dict)

print(f"=== Lista creata con {len(jailbreak_list)} elementi (solo quelli con jailbroken: true) ===")
print(f"Totale jailbreaks nell'artifact: {len(artifact.jailbreaks)}")
print(f"Jailbreaks con jailbroken=true: {len(jailbreak_list)}")

# Mostra un esempio (l'elemento all'indice 75 come nel codice originale)
if len(jailbreak_list) > 75:
    print("=== Esempio: Jailbreak #75 con campi aggiuntivi ===")
    example = jailbreak_list[75]
    for key, value in example.items():
        print(f"{key}:\n{value}\n")
else:
    print("=== Esempio: Primo elemento con campi aggiuntivi ===")
    if jailbreak_list:
        example = jailbreak_list[0]
        for key, value in example.items():
            print(f"{key}:\n{value}\n")

# Opzionale: salva la lista in un file JSON
with open('jailbreak_data.json', 'w', encoding='utf-8') as f:
    json.dump(jailbreak_list, f, indent=2, ensure_ascii=False)

print(f"Lista salvata in 'jailbreak_data.json' con {len(jailbreak_list)} elementi")

# Mostra la struttura dei primi 3 elementi per verifica
print("=== Struttura dei primi 3 elementi ===")
for i, item in enumerate(jailbreak_list[:3]):
    print(f"Elemento {i}:")
    print(f"  Chiavi: {list(item.keys())}")
    print(f"  model: {item.get('model')}")
    print(f"  attack_type: {item.get('attack_type')}")
    print(f"  method: {item.get('method')}")
    print()
