import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class CompleteModelTester:
    def __init__(self):
        self.token = ""
        self.base_url = "https://models.inference.ai.azure.com"
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
    
    def test_model(self, model_name):
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "messages": [{"role": "user", "content": "Hello, respond with just 'OK'"}],
            "model": model_name,
            "max_tokens": 10
        }
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            return response.status_code == 200
        except:
            return False

# Lista completa da testare
ALL_MODELS = [
    # OpenAI
    "gpt-4o", "gpt-4o-mini", "gpt4", "gpt-4-turbo", "gpt-3.5-turbo",
    
    # Anthropic Claude
    "claude-3-5-sonnet-20241022", "claude-3-5-sonnet-20240620",
    "claude-3-opus-20240229", "claude-3-sonnet-20240229", 
    "claude-3-haiku-20240307", "claude-2.1", "claude-2.0",
    
    # Meta Llama
    "meta-llama-3.1-405b-instruct", "meta-llama-3.1-70b-instruct",
    "meta-llama-3.1-8b-instruct", "meta-llama-3.2-90b-vision-instruct",
    "meta-llama-3.2-11b-vision-instruct", "meta-llama-3.2-3b-instruct",
    
    # Microsoft Phi
    "phi-3-medium-4k-instruct", "phi-3-mini-4k-instruct",
    "phi-3.5-mini-instruct", "phi-3.5-moe-instruct",
    
    # Mistral
    "mistral-large", "mistral-nemo", "mistral-small",
    "mixtral-8x7b-instruct", "codestral-22b",
    
    # Cohere
    "command-r", "command-r-plus",
    
    # AI21
    "jamba-1.5-large", "jamba-1.5-mini"
]

if __name__ == "__main__":
    tester = CompleteModelTester()
    
    print("🧪 Testing all available models...")
    print("=" * 60)
    
    available_models = []
    
    for model in ALL_MODELS:
        print(f"Testing {model}...", end=" ")
        if tester.test_model(model):
            print("✅ AVAILABLE")
            available_models.append(model)
        else:
            print("❌ NOT AVAILABLE")
    
    print(f"\n🎯 Available models ({len(available_models)}):")
    for model in available_models:
        print(f"  - {model}")