"""
🤖 GUIDA COMPLETA AI PARAMETRI GITHUB MODELS API
==================================================

Questa guida spiega tutti i parametri disponibili per le API GitHub Models
con esempi pratici per capire come ogni parametro influenza le risposte.
"""

import requests
import json
import time
from typing import Dict, Any, List
import os
from dotenv import load_dotenv


class GitHubModelsGuide:
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
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                return data['choices'][0]['message']['content']
            else:
                return f"Errore {response.status_code}: {response.text}"
        except Exception as e:
            return f"Errore: {e}"

def demonstrate_temperature():
    """
    🌡️ TEMPERATURE (0.0 - 2.0)
    ===========================
    
    DEFINIZIONE:
    Controlla la "creatività" o "randomness" delle risposte.
    - 0.0 = Deterministico, sempre la stessa risposta
    - 1.0 = Bilanciato (default)
    - 2.0 = Molto creativo e imprevedibile
    
    QUANDO USARE:
    - 0.0-0.3: Per codice, matematica, fatti precisi
    - 0.7-1.0: Per conversazioni generali
    - 1.2-2.0: Per creatività, storytelling, brainstorming
    """
    
    print("🌡️ ESEMPI TEMPERATURE")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Scrivi una breve descrizione di un gatto"
    
    temperatures = [0.0, 0.5, 1.0, 1.5, 2.0]
    
    for temp in temperatures:
        print(f"\n📊 Temperature: {temp}")
        print("-" * 30)
        result = client.make_request(prompt, temperature=temp, max_tokens=100)
        print(result)
        time.sleep(1)  # Rate limiting

def demonstrate_top_p():
    """
    🎯 TOP_P (0.0 - 1.0) - Nucleus Sampling
    =======================================
    
    DEFINIZIONE:
    Considera solo i token che cumulativamente rappresentano top_p% di probabilità.
    - 0.1 = Solo i token più probabili (deterministico)
    - 0.9 = Buon bilanciamento (raccomandato)
    - 1.0 = Considera tutti i token possibili
    
    QUANDO USARE:
    - 0.1-0.5: Per risposte precise e focalizzate
    - 0.8-0.95: Per conversazioni naturali
    - 0.95-1.0: Per massima varietà lessicale
    """
    
    print("\n🎯 ESEMPI TOP_P")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Elenca 3 aggettivi per descrivere una montagna"
    
    top_p_values = [0.1, 0.3, 0.6, 0.9, 1.0]
    
    for top_p in top_p_values:
        print(f"\n📊 Top_p: {top_p}")
        print("-" * 30)
        result = client.make_request(prompt, top_p=top_p, temperature=0.8, max_tokens=50)
        print(result)
        time.sleep(1)

def demonstrate_frequency_penalty():
    """
    🚫 FREQUENCY_PENALTY (-2.0 - 2.0)
    =================================
    
    DEFINIZIONE:
    Penalizza i token in base alla loro frequenza nel testo già generato.
    - Valori negativi: Incoraggiano ripetizioni
    - 0.0: Nessuna penalità (default)
    - Valori positivi: Scoraggiano ripetizioni
    
    QUANDO USARE:
    - 0.0-0.5: Per evitare ripetizioni eccessive
    - 0.5-1.0: Per massima varietà lessicale
    - Valori negativi: Raramente utili
    """
    
    print("\n🚫 ESEMPI FREQUENCY_PENALTY")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Descrivi un giardino usando molti aggettivi colorati"
    
    penalties = [-0.5, 0.0, 0.5, 1.0, 1.5]
    
    for penalty in penalties:
        print(f"\n📊 Frequency Penalty: {penalty}")
        print("-" * 30)
        result = client.make_request(prompt, frequency_penalty=penalty, max_tokens=100)
        print(result)
        time.sleep(1)

def demonstrate_presence_penalty():
    """
    🎭 PRESENCE_PENALTY (-2.0 - 2.0)
    ================================
    
    DEFINIZIONE:
    Penalizza i token che sono già apparsi nel testo, indipendentemente dalla frequenza.
    - Valori negativi: Incoraggiano il riuso di token
    - 0.0: Nessuna penalità (default)
    - Valori positivi: Incoraggiano nuovi token
    
    QUANDO USARE:
    - 0.3-0.6: Per incoraggiare varietà nei temi
    - 0.6-1.0: Per massima diversità concettuale
    - Valori negativi: Per enfatizzare temi ricorrenti
    """
    
    print("\n🎭 ESEMPI PRESENCE_PENALTY")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Scrivi una storia breve su un viaggio"
    
    penalties = [-0.5, 0.0, 0.3, 0.6, 1.0]
    
    for penalty in penalties:
        print(f"\n📊 Presence Penalty: {penalty}")
        print("-" * 30)
        result = client.make_request(prompt, presence_penalty=penalty, max_tokens=120)
        print(result)
        time.sleep(1)

def demonstrate_max_tokens():
    """
    📏 MAX_TOKENS (1 - 4096+)
    =========================
    
    DEFINIZIONE:
    Limita il numero massimo di token nella risposta.
    - Token ≈ 0.75 parole in inglese, ~0.5 parole in italiano
    - Controlla la lunghezza della risposta
    
    QUANDO USARE:
    - 10-50: Per risposte brevi, titoli
    - 100-300: Per paragrafi, spiegazioni
    - 500-1000: Per articoli, analisi dettagliate
    - 1000+: Per documenti lunghi
    """
    
    print("\n📏 ESEMPI MAX_TOKENS")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Spiega cos'è l'intelligenza artificiale"
    
    token_limits = [20, 50, 100, 200, 400]
    
    for tokens in token_limits:
        print(f"\n📊 Max Tokens: {tokens}")
        print("-" * 30)
        result = client.make_request(prompt, max_tokens=tokens, temperature=0.7)
        print(f"Risposta ({len(result.split())} parole): {result}")
        time.sleep(1)

def demonstrate_stop_sequences():
    """
    ⏹️ STOP (String o Array di String)
    ==================================
    
    DEFINIZIONE:
    Token o sequenze che fermano la generazione quando incontrati.
    - Utile per controllare il formato output
    - Può essere una stringa singola o array di stringhe
    
    QUANDO USARE:
    - Per liste numerate: ["3.", "4.", "5."]
    - Per separatori: ["\n\n", "---"]
    - Per formati specifici: ["```", "</xml>"]
    """
    
    print("\n⏹️ ESEMPI STOP SEQUENCES")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Elenca i colori dell'arcobaleno: 1. Rosso 2."
    
    stop_examples = [
        None,                    # Nessun stop
        ["4."],                 # Ferma al quarto elemento
        ["3.", "4."],           # Ferma al terzo o quarto
        ["\n\n"],               # Ferma al doppio newline
        ["Blu"]                 # Ferma quando trova "Blu"
    ]
    
    for i, stop in enumerate(stop_examples):
        print(f"\n📊 Stop: {stop}")
        print("-" * 30)
        result = client.make_request(prompt, stop=stop, max_tokens=200)
        print(result)
        time.sleep(1)

def demonstrate_response_format():
    """
    📋 RESPONSE_FORMAT
    ==================
    
    DEFINIZIONE:
    Forza il modello a rispondere in un formato specifico.
    - {"type": "json_object"}: Forza output JSON valido
    - Utile per strutturare dati
    
    QUANDO USARE:
    - Per API responses strutturate
    - Per elaborazione automatica dei dati
    - Per configurazioni e settings
    """
    
    print("\n📋 ESEMPI RESPONSE_FORMAT")
    print("="*60)
    
    client = GitHubModelsGuide()
    
    examples = [
        {
            "prompt": "Fornisci informazioni su Roma",
            "format": None,
            "description": "Formato libero"
        },
        {
            "prompt": "Fornisci informazioni su Roma in formato JSON con campi: nome, popolazione, nazione, attrazioni",
            "format": {"type": "json_object"},
            "description": "Formato JSON forzato"
        }
    ]
    
    for example in examples:
        print(f"\n📊 {example['description']}")
        print("-" * 30)
        result = client.make_request(
            example["prompt"], 
            response_format=example["format"],
            max_tokens=200
        )
        print(result)
        time.sleep(1)

def demonstrate_seed():
    """
    🎲 SEED (Integer)
    =================
    
    DEFINIZIONE:
    Valore numerico per garantire riproducibilità delle risposte.
    - Con temperature=0.0 + seed fisso = sempre stessa risposta
    - Utile per testing e debugging
    
    QUANDO USARE:
    - Per test automatizzati
    - Per debugging di comportamenti specifici
    - Per riproducibilità scientifica
    """
    
    print("\n🎲 ESEMPI SEED")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Genera un numero casuale tra 1 e 100 e spiega perché l'hai scelto"
    
    # Test con stesso seed (dovrebbe dare risultati simili)
    print("📊 Stesso seed (42), temperature 0.0 - Dovrebbe essere identico:")
    for i in range(3):
        print(f"\nTentativo {i+1}:")
        result = client.make_request(prompt, seed=42, temperature=0.0, max_tokens=50)
        print(result)
        time.sleep(1)
    
    # Test con seed diversi
    print(f"\n📊 Seed diversi, temperature 0.0:")
    seeds = [42, 123, 999]
    for seed in seeds:
        print(f"\nSeed {seed}:")
        result = client.make_request(prompt, seed=seed, temperature=0.0, max_tokens=50)
        print(result)
        time.sleep(1)

def demonstrate_n_choices():
    """
    🔄 N (Integer)
    ==============
    
    DEFINIZIONE:
    Numero di risposte alternative da generare.
    - Permette di ottenere multiple varianti
    - Utile per confrontare approcci diversi
    
    QUANDO USARE:
    - Per brainstorming e creatività
    - Per scegliere la migliore tra più opzioni
    - Per A/B testing di contenuti
    """
    
    print("\n🔄 ESEMPI N CHOICES")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Scrivi un titolo accattivante per un articolo sulla pizza"
    
    # Nota: Per semplicità mostreremo l'effetto con chiamate multiple
    # poiché l'handling di multiple choices richiede parsing diverso
    
    print("📊 Generazione di 5 titoli diversi:")
    for i in range(5):
        print(f"\nTitolo {i+1}:")
        result = client.make_request(prompt, temperature=0.9, max_tokens=30)
        print(result)
        time.sleep(1)

def demonstrate_top_k():
    """
    🔢 TOP_K (Integer)
    ==================
    
    DEFINIZIONE:
    Limita il campionamento ai K token più probabili ad ogni step.
    - Valori bassi (1-10): Output più deterministico
    - Valori medi (20-50): Bilanciamento tra varietà e coerenza
    - Valori alti (100+): Maggiore varietà lessicale
    
    QUANDO USARE:
    - 1-5: Per risposte molto precise e deterministiche
    - 10-40: Per conversazioni naturali bilanciate
    - 50-100: Per creatività controllata
    """
    
    print("\n🔢 ESEMPI TOP_K")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Descrivi un tramonto usando aggettivi creativi"
    
    top_k_values = [1, 5, 20, 50, 100]
    
    for top_k in top_k_values:
        print(f"\n📊 Top_k: {top_k}")
        print("-" * 30)
        result = client.make_request(prompt, top_k=top_k, temperature=0.8, max_tokens=80)
        print(result)
        time.sleep(1)

def demonstrate_user_parameter():
    """
    👤 USER (String)
    ===============
    
    DEFINIZIONE:
    Identificatore dell'utente per tracking e monitoring.
    - Utile per analytics e debugging
    - Aiuta a tracciare pattern di utilizzo
    - Non influenza la risposta del modello
    
    QUANDO USARE:
    - Per applicazioni multi-utente
    - Per tracking e analytics
    - Per debugging di problemi specifici utente
    """
    
    print("\n👤 ESEMPI USER PARAMETER")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Scrivi un saluto personalizzato"
    
    user_ids = [
        None,           # Nessun user ID
        "user_001",     # ID numerico
        "alice123",     # Username
        "guest_session", # Sessione guest
        "premium_user"  # Tipo utente
    ]
    
    for user_id in user_ids:
        print(f"\n📊 User ID: {user_id}")
        print("-" * 30)
        result = client.make_request(prompt, user=user_id, max_tokens=50)
        print(result)
        time.sleep(1)

def demonstrate_stream_parameter():
    """
    📡 STREAM (Boolean)
    ==================
    
    DEFINIZIONE:
    Abilita lo streaming incrementale della risposta.
    - true: Ricevi la risposta pezzo per pezzo (real-time)
    - false: Ricevi la risposta completa alla fine (default)
    
    QUANDO USARE:
    - Per interfacce chat real-time
    - Per migliorare perceived performance
    - Per risposte lunghe che richiedono tempo
    
    NOTA: Richiede gestione Server-Sent Events
    """
    
    print("\n📡 ESEMPI STREAM PARAMETER")
    print("="*60)
    
    client = GitHubModelsGuide()
    prompt = "Racconta una breve favola"
    
    print("📊 Stream: False (normale)")
    print("-" * 30)
    result = client.make_request(prompt, stream=False, max_tokens=150)
    print(f"Risposta completa: {result}")
    time.sleep(1)
    
    print(f"\n📊 Stream: True (simulazione)")
    print("-" * 30)
    print("Simulazione di streaming (carattere per carattere):")
    # Simuliamo lo streaming mostrando la risposta carattere per carattere
    result = client.make_request(prompt, max_tokens=100)
    for char in result:
        print(char, end='', flush=True)
        time.sleep(0.02)  # Simula ritardo streaming
    print("\n")

def demonstrate_advanced_parameters():
    """
    🔬 PARAMETRI AVANZATI AGGIUNTIVI
    ================================
    
    Altri parametri meno comuni ma utili in casi specifici.
    """
    
    print("\n🔬 ALTRI PARAMETRI AVANZATI")
    print("="*60)
    
    client = GitHubModelsGuide()
    
    # Test parameter: user (for tracking)
    print("📊 USER PARAMETER (per tracking)")
    print("-" * 30)
    result = client.make_request(
        "Scrivi un saluto breve", 
        user="user_123",
        max_tokens=30
    )
    print(f"Risposta con user tracking: {result}")
    time.sleep(1)
    
    # Test parameter: stream simulation
    print(f"\n📊 STREAM PARAMETER (simulazione)")
    print("-" * 30)
    print("Lo streaming richiederebbe gestione eventi Server-Sent Events")
    print("Esempio di implementazione:")
    print("""
    payload = {
        "stream": True,
        "messages": [...],
        # altri parametri...
    }
    
    response = requests.post(url, headers=headers, json=payload, stream=True)
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line.decode('utf-8').replace('data: ', ''))
            print(chunk['choices'][0]['delta']['content'])
    """)

def demonstrate_combined_effects():
    """
    🎯 COMBINAZIONI DI PARAMETRI
    ============================
    
    Esempi di come combinare parametri per casi d'uso specifici.
    """
    
    print("\n🎯 COMBINAZIONI PRATICHE")
    print("="*60)
    
    client = GitHubModelsGuide()
    
    scenarios = [
        {
            "name": "Codice Deterministico",
            "prompt": "Scrivi una funzione Python per calcolare il fattoriale",
            "params": {
                "temperature": 0.1,
                "top_p": 0.9,
                "frequency_penalty": 0.2,
                "max_tokens": 200
            }
        },
        {
            "name": "Creatività Massima",
            "prompt": "Scrivi una poesia surreale",
            "params": {
                "temperature": 1.5,
                "top_p": 0.95,
                "presence_penalty": 0.6,
                "frequency_penalty": 0.4,
                "max_tokens": 150
            }
        },
        {
            "name": "Analisi Strutturata",
            "prompt": "Analizza i pro e contro dell'energia solare in formato JSON",
            "params": {
                "temperature": 0.3,
                "response_format": {"type": "json_object"},
                "max_tokens": 300
            }
        },
        {
            "name": "Lista Controllata",
            "prompt": "Elenca i primi 3 presidenti USA: 1.",
            "params": {
                "temperature": 0.0,
                "stop": ["4."],
                "max_tokens": 100
            }
        }
    ]
    
    for scenario in scenarios:
        print(f"\n🎨 {scenario['name']}")
        print("-" * 40)
        print(f"Parametri: {scenario['params']}")
        result = client.make_request(scenario["prompt"], **scenario["params"])
        print(f"Risultato: {result}")
        time.sleep(1)

def print_parameter_summary():
    """
    📚 RIASSUNTO PARAMETRI
    ======================
    """
    
    summary = """
    
📚 RIASSUNTO COMPLETO PARAMETRI GITHUB MODELS
=============================================

🔧 PARAMETRI PRINCIPALI:
------------------------
• model: Specifica il modello da usare (es. "gpt-4o-mini")
• messages: Array di messaggi per la conversazione
• temperature (0.0-2.0): Creatività delle risposte
• max_tokens (1-4096+): Lunghezza massima risposta

🎯 CONTROLLO SAMPLING:
---------------------
• top_p (0.0-1.0): Nucleus sampling, considera top % probabilità
• top_k (integer): Considera solo top K token più probabili
• seed (integer): Per riproducibilità delle risposte

🚫 CONTROLLO RIPETIZIONI:
------------------------
• frequency_penalty (-2.0-2.0): Penalizza token frequenti
• presence_penalty (-2.0-2.0): Penalizza token già presenti

📋 CONTROLLO OUTPUT:
-------------------
• response_format: {"type": "json_object"} per JSON
• stop: Token/sequenze che fermano la generazione
• n (integer): Numero di risposte alternative

⚙️ PARAMETRI AGGIUNTIVI:
-----------------------
• user (string): ID utente per tracking
• stream (boolean): Streaming incrementale delle risposte

⚙️ COMBINAZIONI CONSIGLIATE:
---------------------------

CODICE/MATEMATICA:
{
    "temperature": 0.0-0.3,
    "top_p": 0.9,
    "frequency_penalty": 0.1-0.3
}

CONVERSAZIONE NATURALE:
{
    "temperature": 0.7-1.0,
    "top_p": 0.9,
    "presence_penalty": 0.1
}

CREATIVITÀ/STORYTELLING:
{
    "temperature": 1.2-1.8,
    "top_p": 0.95,
    "presence_penalty": 0.6,
    "frequency_penalty": 0.3
}

OUTPUT STRUTTURATO:
{
    "temperature": 0.3,
    "response_format": {"type": "json_object"},
    "top_p": 0.9
}

LISTE CONTROLLATE:
{
    "temperature": 0.0,
    "stop": ["termine_fine"],
    "top_p": 0.9
}
    """
    
    print(summary)

# MAIN EXECUTION
if __name__ == "__main__":
    print("🤖 GUIDA PARAMETRI GITHUB MODELS API")
    print("="*60)
    print("Questa demo mostrerà tutti i parametri con esempi pratici.")
    print("Ogni sezione includerà 5 esempi comparativi.\n")
    input("\nPremi INVIO per continuare con TOP_K...")
    demonstrate_top_k()
    
    input("\nPremi INVIO per continuare con USER PARAMETER...")
    demonstrate_user_parameter()
    
    input("\nPremi INVIO per continuare con STREAM PARAMETER...")
    demonstrate_stream_parameter()

    input("Premi INVIO per iniziare con TEMPERATURE...")
    demonstrate_temperature()
    
    input("\nPremi INVIO per continuare con TOP_P...")
    demonstrate_top_p()
    
    input("\nPremi INVIO per continuare con FREQUENCY_PENALTY...")
    demonstrate_frequency_penalty()
    
    input("\nPremi INVIO per continuare con PRESENCE_PENALTY...")
    demonstrate_presence_penalty()
    
    input("\nPremi INVIO per continuare con MAX_TOKENS...")
    demonstrate_max_tokens()
    
    input("\nPremi INVIO per continuare con STOP SEQUENCES...")
    demonstrate_stop_sequences()
    
    input("\nPremi INVIO per continuare con RESPONSE_FORMAT...")
    demonstrate_response_format()
    
    input("\nPremi INVIO per continuare con SEED...")
    demonstrate_seed()
    input("\nPremi INVIO per continuare con N CHOICES...")
    demonstrate_n_choices()
    
    input("\nPremi INVIO per vedere PARAMETRI AVANZATI...")
    demonstrate_advanced_parameters()
    
    input("\nPremi INVIO per vedere COMBINAZIONI PRATICHE...")
    demonstrate_combined_effects()
    
    print_parameter_summary()
    
    print("\n✅ Guida completata!")
    print("🔗 Usa questi esempi per ottimizzare le tue richieste AI!")
