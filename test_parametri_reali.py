"""
🤖 TEST PARAMETRI REALI GITHUB MODELS API
==========================================

Testa solo i parametri effettivamente supportati dall'API GitHub Models
basandoci sui risultati dei test precedenti.
"""

import requests
import json
import time
import os
from dotenv import load_dotenv

class GitHubModelsTest:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Access the TOKEN
        self.token = os.getenv('TOKEN')
        self.base_url = "https://models.inference.ai.azure.com"
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
    
    def make_request(self, prompt: str, **kwargs) -> str:
        """Fa una richiesta con parametri personalizzati"""
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "messages": [{"role": "user", "content": prompt}],
            "model": kwargs.get("model", "gpt-4o-mini"),
            **{k: v for k, v in kwargs.items() if k != "model" and v is not None}
        }
        
        print(f"🔍 Payload inviato: {json.dumps(payload, indent=2)}")
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                return data['choices'][0]['message']['content']
            else:
                return f"❌ Errore {response.status_code}: {response.text}"
        except Exception as e:
            return f"❌ Errore: {e}"

def test_supported_parameters():
    """
    Testa i parametri che sappiamo essere supportati
    """
    print("🧪 TEST PARAMETRI SUPPORTATI")
    print("="*60)
    
    client = GitHubModelsTest()
    base_prompt = "Scrivi una breve poesia"
    
    # Test parametri sicuramente supportati
    tests = [
        {
            "name": "Solo parametri base",
            "params": {}
        },
        {
            "name": "Temperature",
            "params": {"temperature": 0.7}
        },
        {
            "name": "Max tokens",
            "params": {"max_tokens": 50}
        },
        {
            "name": "Temperature + Max tokens",
            "params": {"temperature": 0.5, "max_tokens": 80}
        },
        {
            "name": "Top_p",
            "params": {"top_p": 0.9}
        },
        {
            "name": "Frequency penalty",
            "params": {"frequency_penalty": 0.3}
        },
        {
            "name": "Presence penalty", 
            "params": {"presence_penalty": 0.2}
        },
        {
            "name": "Stop sequences",
            "params": {"stop": ["fine", "."]}
        },
        {
            "name": "Seed per riproducibilità",
            "params": {"seed": 42, "temperature": 0.0}
        },
        {
            "name": "Response format JSON",
            "params": {
                "response_format": {"type": "json_object"},
                "temperature": 0.3
            }
        }
    ]
    
    for test in tests:
        print(f"\n🎯 Test: {test['name']}")
        print("-" * 50)
        
        # Modifica il prompt per JSON se necessario
        prompt = base_prompt
        if "response_format" in test["params"]:
            prompt = "Scrivi informazioni su un gatto in formato JSON con campi: nome, colore, caratteristiche"
        
        result = client.make_request(prompt, **test["params"])
        print(f"✅ Risultato: {result}")
        print()
        time.sleep(1)

def test_potentially_unsupported():
    """
    Testa parametri che potrebbero non essere supportati
    """
    print("\n🔬 TEST PARAMETRI POTENZIALMENTE NON SUPPORTATI")
    print("="*60)
    
    client = GitHubModelsTest()
    prompt = "Ciao"
    
    # Parametri da testare singolarmente
    unsure_params = [
        {"name": "top_k", "params": {"top_k": 20}},
        {"name": "user", "params": {"user": "test_user"}},
        {"name": "stream", "params": {"stream": False}},  # Test con false prima
        {"name": "repetition_penalty", "params": {"repetition_penalty": 1.1}},
        {"name": "n (multiple choices)", "params": {"n": 2}},
    ]
    
    for test in unsure_params:
        print(f"\n🧪 Test parametro: {test['name']}")
        print("-" * 40)
        result = client.make_request(prompt, **test["params"])
        
        if "Errore 400" in result and "Unrecognized request argument" in result:
            print(f"❌ {test['name']}: NON SUPPORTATO")
        else:
            print(f"✅ {test['name']}: SUPPORTATO")
            print(f"   Risposta: {result}")
        
        time.sleep(1)

def test_model_availability():
    """
    Testa diversi modelli disponibili
    """
    print(f"\n🤖 TEST MODELLI DISPONIBILI")
    print("="*60)
    
    client = GitHubModelsTest()
    prompt = "Saluta brevemente"
    
    models = [
        "gpt-4o-mini",
        "gpt-4o", 
        "meta-llama-3.1-8b-instruct",
        "phi-3-mini-4k-instruct"
    ]
    
    for model in models:
        print(f"\n🔧 Test modello: {model}")
        print("-" * 40)
        result = client.make_request(prompt, model=model, max_tokens=50)
        
        if "Errore" not in result:
            print(f"✅ {model}: FUNZIONA")
            print(f"   Risposta: {result}")
        else:
            print(f"❌ {model}: ERRORE")
            print(f"   {result}")
        
        time.sleep(1)

if __name__ == "__main__":
    print("🚀 GITHUB MODELS API - TEST PARAMETRI REALI")
    print("="*60)
    print("Questo script testa solo i parametri effettivamente supportati")
    print("dall'API GitHub Models, evitando errori 400.\n")
    
    # Test base
    test_supported_parameters()
    
    # Test parametri incerti  
    test_potentially_unsupported()
    
    # Test modelli
    test_model_availability()
    
    print("\n✅ Test completati!")
    print("📋 Usa i parametri che hanno funzionato per le tue applicazioni.")
