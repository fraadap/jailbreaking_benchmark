# 🤖 Guida Completa ai Parametri GitHub Models API

## 📋 Indice
1. [Panoramica Generale](#panoramica-generale)
2. [Parametri di Base](#parametri-di-base)
3. [Controllo della Creatività](#controllo-della-creatività)
4. [Controllo delle Ripetizioni](#controllo-delle-ripetizioni)
5. [Controllo dell'Output](#controllo-delloutput)
6. [Riproducibilità](#riproducibilità)
7. [Combinazioni Pratiche](#combinazioni-pratiche)
8. [Esempi per Caso d'Uso](#esempi-per-caso-duso)

---

## 📊 Panoramica Generale

I parametri delle API GitHub Models permettono di controllare precisamente il comportamento del modello AI. Ogni parametro influenza aspetti diversi della generazione del testo.

### Struttura Base della Richiesta
```python
payload = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Il tuo prompt"}],
    # Parametri aggiuntivi qui...
}
```

---

## 🔧 Parametri di Base

### 1. **MODEL** (Obbligatorio)
```python
"model": "gpt-4o-mini"
```

**Funzione**: Specifica quale modello AI utilizzare.

**Modelli Disponibili** (testati):
- `gpt-4o` - GPT-4 Omni (massima qualità)
- `gpt-4o-mini` - GPT-4 Omni Mini (veloce ed economico)
- `meta-llama-3.1-405b-instruct` - Llama 3.1 405B (molto potente)
- `meta-llama-3.1-70b-instruct` - Llama 3.1 70B (bilanciato)
- `meta-llama-3.1-8b-instruct` - Llama 3.1 8B (veloce)
- `phi-3-medium-4k-instruct` - Microsoft Phi-3 Medium
- `phi-3.5-mini-instruct` - Microsoft Phi-3.5 Mini
- `mistral-nemo` - Mistral Nemo
- `jamba-1.5-large` - AI21 Jamba Large

### 2. **MESSAGES** (Obbligatorio)
```python
"messages": [
    {"role": "system", "content": "Sei un assistente utile"},
    {"role": "user", "content": "Ciao, come stai?"}
]
```

**Funzione**: Definisce la conversazione tra utente e AI.

**Ruoli Disponibili**:
- `system`: Istruzioni per il comportamento del modello
- `user`: Messaggi dell'utente
- `assistant`: Risposte precedenti del modello

---

## 🌡️ Controllo della Creatività

### 3. **TEMPERATURE** (0.0 - 2.0)
```python
"temperature": 0.7
```

**Funzione**: Controlla la creatività e randomness delle risposte.

**Valori e Effetti**:
- **0.0**: Completamente deterministico, sempre la stessa risposta
- **0.1-0.3**: Molto preciso, ideale per codice e matematica
- **0.7-1.0**: Bilanciato, buono per conversazioni generali
- **1.2-1.5**: Creativo, buono per storytelling
- **1.8-2.0**: Molto creativo ma può essere incoerente

**Esempi Pratici** con prompt: *"Descrivi un gatto"*

| Temperature | Risposta |
|-------------|----------|
| 0.0 | "Un gatto è un mammifero domestico della famiglia dei felini." |
| 0.5 | "Un gatto è un animale domestico elegante con pelo morbido e occhi espressivi." |
| 1.0 | "Il gatto è una creatura affascinante che si muove con grazia felina." |
| 1.5 | "Un misterioso felino dalle movenze sinuose, guardiano di segreti domestici." |
| 2.0 | "Creature eteree che danzano tra dimensioni parallele di coccole e graffi." |

### 4. **TOP_P** (0.0 - 1.0)
```python
"top_p": 0.9
```

**Funzione**: Nucleus sampling - considera solo i token che cumulativamente rappresentano top_p% di probabilità.

**Valori e Effetti**:
- **0.1**: Solo token più probabili (molto focalizzato)
- **0.5**: Moderatamente focalizzato
- **0.9**: Bilanciato (raccomandato)
- **0.95**: Ampia varietà lessicale
- **1.0**: Considera tutti i token possibili

**Esempi Pratici** con prompt: *"Il cielo è"*

| Top_P | Possibili Completamenti |
|-------|-------------------------|
| 0.1 | "blu", "sereno", "nuvoloso" |
| 0.5 | "azzurro", "luminoso", "coperto", "stellato" |
| 0.9 | "infinito", "maestoso", "tempestoso", "cristallino" |
| 1.0 | "psichedelico", "quantico", "onirico" |

---

## 🚫 Controllo delle Ripetizioni

### 5. **FREQUENCY_PENALTY** (-2.0 - 2.0)
```python
"frequency_penalty": 0.3
```

**Funzione**: Penalizza token in base alla loro frequenza nel testo già generato.

**Valori e Effetti**:
- **-1.0**: Incoraggia ripetizioni (raramente utile)
- **0.0**: Nessuna penalità (default)
- **0.2-0.5**: Riduce ripetizioni eccessive
- **0.8-1.0**: Forte varietà lessicale
- **1.5-2.0**: Massima varietà (può compromettere coerenza)

**Esempi Pratici** con prompt: *"Descrivi un giardino colorato"*

| Frequency Penalty | Risposta |
|-------------------|----------|
| 0.0 | "Un giardino pieno di fiori colorati. I fiori sono bellissimi. I colori dei fiori..." |
| 0.3 | "Un giardino rigoglioso con fiori variopinti. Le aiuole mostrano tulipani rossi..." |
| 0.6 | "Un'esplosione cromatica di botanica: petali scarlatti, steli verdi..." |
| 1.0 | "Kaleidoscopio vegetale: cromie vermiglie, tonalità cerulee, sfumature ocra..." |

### 6. **PRESENCE_PENALTY** (-2.0 - 2.0)
```python
"presence_penalty": 0.6
```

**Funzione**: Penalizza token già apparsi, indipendentemente dalla frequenza.

**Valori e Effetti**:
- **-1.0**: Incoraggia riuso temi (focus specifico)
- **0.0**: Nessuna penalità (default)
- **0.3-0.6**: Incoraggia varietà tematica
- **0.8-1.0**: Massima diversità concettuale
- **1.5-2.0**: Può rendere il testo frammentato

**Esempi Pratici** con prompt: *"Racconta di un viaggio"*

| Presence Penalty | Focus Tematico |
|------------------|----------------|
| 0.0 | Rimane sul viaggio, dettagli del trasporto |
| 0.3 | Viaggio + paesaggi + persone incontrate |
| 0.6 | Viaggio + cultura + cibo + arte + storia |
| 1.0 | Salta tra temi diversi: filosofia, natura, tecnologia |

---

## 📏 Controllo dell'Output

### 7. **MAX_TOKENS** (1 - 4096+)
```python
"max_tokens": 150
```

**Funzione**: Limita la lunghezza massima della risposta in token.

**Conversione Approssimativa**:
- 1 token ≈ 0.75 parole (inglese)
- 1 token ≈ 0.5 parole (italiano)

**Linee Guida**:
- **10-30**: Titoli, etichette
- **50-100**: Paragrafi brevi
- **150-300**: Spiegazioni dettagliate
- **500-1000**: Articoli, analisi
- **1000+**: Documenti lunghi

**Esempi Pratici** con prompt: *"Spiega la fotosintesi"*

| Max Tokens | Lunghezza Risposta |
|------------|-------------------|
| 20 | "La fotosintesi è il processo..." (1 frase) |
| 50 | Definizione + processo base (1 paragrafo) |
| 150 | Definizione + fasi + importanza (3 paragrafi) |
| 300 | Spiegazione completa + esempi + impatto ecologico |

### 8. **STOP** (String o Array)
```python
"stop": [".", "4.", "\n\n"]
```

**Funzione**: Ferma la generazione quando incontra sequenze specifiche.

**Casi d'Uso Comuni**:
- Liste numerate: `["4.", "5."]`
- Formattazione: `["\n\n", "---"]`
- Codice: `["```", "</code>"]`
- Conversazioni: `["Utente:", "Bot:"]`

**Esempi Pratici** con prompt: *"Lista pianeti: 1. Mercurio 2."*

| Stop Sequence | Risultato |
|---------------|-----------|
| `null` | Lista completa di tutti i pianeti |
| `["4."]` | Si ferma dopo i primi 3 pianeti |
| `["Giove"]` | Si ferma quando trova "Giove" |
| `["\n\n"]` | Si ferma al primo doppio a capo |

### 9. **RESPONSE_FORMAT**
```python
"response_format": {"type": "json_object"}
```

**Funzione**: Forza output in formato specifico.

**Opzioni Disponibili**:
- `{"type": "json_object"}`: Output JSON valido
- `null`: Formato libero (default)

**Esempi Pratici** con prompt: *"Info su Roma"*

| Format | Output |
|--------|--------|
| `null` | "Roma è la capitale d'Italia, fondata nel..." |
| `json_object` | `{"nome": "Roma", "popolazione": 2800000, "nazione": "Italia"}` |

---

## 🎲 Riproducibilità

### 10. **SEED** (Integer)
```python
"seed": 42
```

**Funzione**: Garantisce riproducibilità delle risposte.

**Come Funziona**:
- Con `temperature=0.0` + `seed` fisso = sempre stessa risposta
- Utile per testing e debugging
- Non garantisce identità tra modelli diversi

**Esempio**:
```python
# Questi 3 chiamate daranno risultati identici
params = {"temperature": 0.0, "seed": 42}
result1 = api_call("Conta da 1 a 3", **params)
result2 = api_call("Conta da 1 a 3", **params)  # Identico a result1
result3 = api_call("Conta da 1 a 3", **params)  # Identico a result1
```

### 11. **N** (Integer)
```python
"n": 3
```

**Funzione**: Genera multiple risposte alternative.

**Nota**: Aumenta i costi e tempi di risposta proporzionalmente.

---

## 🎯 Combinazioni Pratiche

### 💻 Per Programmazione
```python
{
    "temperature": 0.1,
    "top_p": 0.9,
    "frequency_penalty": 0.2,
    "max_tokens": 500,
    "stop": ["```", "# Fine"]
}
```

### 🎨 Per Creatività
```python
{
    "temperature": 1.3,
    "top_p": 0.95,
    "presence_penalty": 0.6,
    "frequency_penalty": 0.4,
    "max_tokens": 300
}
```

### 📊 Per Dati Strutturati
```python
{
    "temperature": 0.3,
    "response_format": {"type": "json_object"},
    "top_p": 0.9,
    "max_tokens": 800
}
```

### 💬 Per Conversazioni
```python
{
    "temperature": 0.8,
    "top_p": 0.9,
    "frequency_penalty": 0.1,
    "presence_penalty": 0.1,
    "max_tokens": 200
}
```

### 📝 Per Contenuti Tecnici
```python
{
    "temperature": 0.4,
    "top_p": 0.9,
    "frequency_penalty": 0.3,
    "max_tokens": 600
}
```

---

## 🔍 Esempi per Caso d'Uso

### 1. **Generazione Codice**
```python
prompt = "Scrivi una funzione Python per ordinare una lista"
params = {
    "model": "gpt-4o",
    "temperature": 0.0,  # Deterministico
    "top_p": 0.9,
    "frequency_penalty": 0.1,
    "max_tokens": 300,
    "stop": ["```", "# Esempio d'uso"]
}
```

### 2. **Creative Writing**
```python
prompt = "Scrivi l'inizio di un racconto fantastico"
params = {
    "model": "gpt-4o-mini",
    "temperature": 1.4,  # Alta creatività
    "top_p": 0.95,
    "presence_penalty": 0.7,  # Varietà tematica
    "frequency_penalty": 0.3,
    "max_tokens": 400
}
```

### 3. **Analisi Dati**
```python
prompt = "Analizza questi dati di vendita e fornisci insights in JSON"
params = {
    "model": "gpt-4o",
    "temperature": 0.3,  # Preciso ma non rigido
    "response_format": {"type": "json_object"},
    "top_p": 0.9,
    "max_tokens": 600
}
```

### 4. **FAQ/Supporto Clienti**
```python
prompt = "Come posso resettare la mia password?"
params = {
    "model": "gpt-4o-mini",
    "temperature": 0.2,  # Consistente
    "top_p": 0.9,
    "max_tokens": 150,
    "stop": ["\n\nDomanda:", "Altro:"]
}
```

### 5. **Brainstorming**
```python
prompt = "Genera 10 idee innovative per un'app mobile"
params = {
    "model": "meta-llama-3.1-70b-instruct",
    "temperature": 1.1,  # Creativo
    "presence_penalty": 0.8,  # Massima varietà
    "frequency_penalty": 0.4,
    "max_tokens": 500,
    "stop": ["11."]
}
```

---

## 🎯 Consigli Finali

### ⚡ Per Performance Ottimali:
1. **Inizia con valori moderati** e aggiusta gradualmente
2. **Temperature 0.7-0.9** funziona bene per la maggior parte dei casi
3. **Top_p 0.9** è quasi sempre una buona scelta
4. **Frequency_penalty 0.1-0.3** previene ripetizioni senza compromettere qualità

### 🧪 Per Sperimentazione:
1. **Testa un parametro alla volta** per capire gli effetti
2. **Usa seed fisso** durante i test per risultati comparabili
3. **Documenta le combinazioni** che funzionano bene per i tuoi casi d'uso

### 🎨 Per Creatività:
1. **Temperature alte** (1.2-1.8) + **presence_penalty alto** (0.6-0.8)
2. **Evita frequency_penalty troppo alto** che può frammentare il testo
3. **Usa stop sequences** per controllare il formato senza limitare la creatività

### 💻 Per Applicazioni Produttive:
1. **Temperature basse** (0.0-0.4) per consistenza
2. **Response_format JSON** per integrazione con sistemi
3. **Max_tokens appropriati** per controllare costi
4. **Stop sequences** per evitare output non necessario

---

## 📚 Riferimenti Rapidi

| Parametro | Range | Default | Uso Principale |
|-----------|-------|---------|----------------|
| temperature | 0.0-2.0 | 1.0 | Creatività |
| top_p | 0.0-1.0 | 1.0 | Varietà lessicale |
| frequency_penalty | -2.0-2.0 | 0.0 | Anti-ripetizione |
| presence_penalty | -2.0-2.0 | 0.0 | Varietà tematica |
| max_tokens | 1-4096+ | ∞ | Lunghezza |
| top_k | 1-100 | - | Focus token |
| seed | int | random | Riproducibilità |
| n | 1+ | 1 | Multiple risposte |

---

**🚀 Buona sperimentazione con GitHub Models API!**
