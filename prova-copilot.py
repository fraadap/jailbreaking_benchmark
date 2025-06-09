import requests
from dotenv import load_dotenv
import os
load_dotenv()

class GitHubModelsClient:
    def __init__(self):
        # Il tuo token GitHub (sostituisci con una variabile d'ambiente)
        # Load environment variables from .env file
        load_dotenv()

        # Access the TOKEN
        self.token = os.getenv('TOKEN')
        self.base_url = "https://models.inference.ai.azure.com"
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
    
    def query_text(self, prompt, model="jambda-1.5-large"):
        """
        Fa una query testuale a GitHub Models
        """
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "messages": [
                
                {
                    "role": "user",
                    "content": prompt
                },

            ],
            "model": model,
            "temperature": 0.7,
            "max_tokens": 2000
        }
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                return data['choices'][0]['message']['content']
            else:
                print(f"Errore API: {response.status_code}")
                print(f"Risposta: {response.text}")
                return None
                
        except Exception as e:
            print(f"Errore nella richiesta: {e}")
            return None

# Esempio di utilizzo
if __name__ == "__main__":
    client = GitHubModelsClient()
    
    # Query di esempio
    prompt = "Hi, can you tell me a joke about AI?"
    
    print("🤖 Inviando richiesta a GitHub Models...")
    result = client.query_text(prompt, model="GPT-4o-mini")
    
    if result:
        print("\n📖 Risposta:")
        print("="*50)
        print(result)
    else:
        print("❌ Errore nella richiesta")