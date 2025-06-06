"""
🚀 TEST RAPIDO PARAMETRI GITHUB MODELS
======================================

Script per testare rapidamente l'effetto dei parametri sulle risposte.
Modifica i valori e confronta i risultati!
"""

import requests
import json

class ParameterTester:
    def __init__(self):
        self.token = ""
        self.base_url = "https://models.inference.ai.azure.com"
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
    
    def test_parameter(self, prompt, param_name, values, base_params=None):
        """Testa un parametro con diversi valori"""
        if base_params is None:
            base_params = {
                "model": "gpt-4o-mini",
                "temperature": 0.7,
                "max_tokens": 150
            }
        
        print(f"\n🧪 TESTING PARAMETER: {param_name.upper()}")
        print("="*60)
        print(f"Prompt: '{prompt}'\n")
        
        results = []
        
        for value in values:
            params = base_params.copy()
            params[param_name] = value
            
            response = self._make_request(prompt, **params)
            results.append((value, response))
            
            print(f"📊 {param_name}: {value}")
            print("-" * 30)
            print(response)
            print()
        
        return results
    
    def _make_request(self, prompt, **kwargs):
        """Fa la richiesta API"""
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "messages": [{"role": "user", "content": prompt}],
            **kwargs
        }
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                return data['choices'][0]['message']['content']
            else:
                return f"Errore {response.status_code}"
        except Exception as e:
            return f"Errore: {e}"

def main():
    tester = ParameterTester()
    
    # Test 1: Temperature
    print("🌡️ TEST 1: TEMPERATURE")
    tester.test_parameter(
        prompt="Scrivi 3 aggettivi per descrivere il mare",
        param_name="temperature",
        values=[0.0, 0.5, 1.0, 1.5, 2.0],
        base_params={"model": "gpt-4o-mini", "max_tokens": 50}
    )
    
    input("Premi INVIO per continuare...")
    
    # Test 2: Top_p
    print("\n🎯 TEST 2: TOP_P")
    tester.test_parameter(
        prompt="Completa la frase: Il tramonto era",
        param_name="top_p",
        values=[0.1, 0.3, 0.6, 0.9, 1.0],
        base_params={"model": "gpt-4o-mini", "temperature": 0.8, "max_tokens": 30}
    )
    
    input("Premi INVIO per continuare...")
    
    # Test 3: Frequency Penalty
    print("\n🚫 TEST 3: FREQUENCY PENALTY")
    tester.test_parameter(
        prompt="Descrivi una foresta usando molti aggettivi",
        param_name="frequency_penalty",
        values=[0.0, 0.3, 0.6, 1.0, 1.5],
        base_params={"model": "gpt-4o-mini", "temperature": 0.8, "max_tokens": 100}
    )
    
    input("Premi INVIO per continuare...")
    
    # Test 4: Max Tokens
    print("\n📏 TEST 4: MAX TOKENS")
    tester.test_parameter(
        prompt="Spiega cosa sono i buchi neri",
        param_name="max_tokens",
        values=[20, 50, 100, 200, 500],
        base_params={"model": "gpt-4o-mini", "temperature": 0.7}
    )
    
    input("Premi INVIO per continuare...")
    
    # Test 5: Presence Penalty
    print("\n🎭 TEST 5: PRESENCE PENALTY")
    tester.test_parameter(
        prompt="Racconta una breve avventura in una città misteriosa",
        param_name="presence_penalty",
        values=[0.0, 0.2, 0.4, 0.6, 0.8],
        base_params={"model": "gpt-4o-mini", "temperature": 0.8, "max_tokens": 120}
    )
    
    print("\n✅ Test completati!")
    print("\n💡 CONSIGLI:")
    print("- Temperature basse (0.0-0.3) per precisione")
    print("- Temperature medie (0.7-1.0) per conversazioni")
    print("- Temperature alte (1.2-2.0) per creatività")
    print("- Top_p 0.9 è un buon valore di partenza")
    print("- Frequency_penalty 0.2-0.5 evita ripetizioni")
    print("- Presence_penalty 0.3-0.6 incoraggia varietà")

if __name__ == "__main__":
    main()
