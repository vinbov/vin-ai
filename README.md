# 🚀 Vin-AI - Intelligent Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Un assistente AI intelligente e versatile - chatbot, analisi documenti e gestione AI con interfaccia user-friendly!**

## 🎯 Panoramica

Vin-AI è una piattaforma web intuitiva che permette a chiunque di utilizzare AI avanzate senza competenze tecniche:

- 🤖 **Chatbot intelligente** personalizzabile con diversi template
- 📄 **Analisi documenti** automatica (PDF, DOCX, TXT, MD, CSV)
- 🔍 **Ricerca intelligente** e elaborazione testi
- ⚙️ **Multi-provider AI** (OpenAI, Google Gemini, Anthropic Claude, Mistral)
- 📊 **Analytics e monitoring** delle conversazioni
- 🎨 **Interface user-friendly** senza necessità di programmazione

### 🤖 Assistente Intelligente
- Template personalizzabili per diversi use case
- Conversazioni naturali con memoria di contesto
- Supporto per domande complesse e analisi
- Cronologia e gestione delle chat

### 📄 Gestione Documenti
- Upload multiplo di file in vari formati
- Analisi automatica con AI specializzata
- Estrazione di informazioni chiave
- Organizzazione intelligente della documentazione
- Export e condivisione risultati

## 🚀 Avvio Rapido

### Prerequisiti
- Python 3.8 o superiore
- pip (package manager Python)

### Installazione

1. **Clona il repository**
```bash
git clone https://github.com/vinbov/vin-ai.git
cd vin-ai
```

2. **Installa le dipendenze**
```bash
pip install -r requirements.txt
```

3. **Avvia l'applicazione**
```bash
streamlit run streamlit_app.py
```

4. **Apri nel browser**
   - L'app sarà disponibile su: http://localhost:8501

## 🎮 Come Usare

### 1. 💬 Chat AI
- Seleziona "Chat" dalla sidebar
- Scegli un template o crea conversazioni personalizzate
- L'AI risponderà con intelligenza avanzata

### 2. 📑 Analisi Documenti
- Vai su "Analisi Documenti"
- Carica i tuoi file (PDF, Word, etc.)
- Visualizza l'analisi AI automatica

### 3. ⚙️ Configurazione
- Imposta le tue API keys nei Settings
- Scegli il provider AI preferito
- Personalizza template e comportamenti

## 📁 Struttura Progetto

```
vin-ai/
├── streamlit_app.py      # Applicazione principale
├── demo_data.py          # Dati demo per testing
├── requirements.txt      # Dipendenze Python
├── README.md            # Questo file
├── LICENSE              # Licenza MIT
└── .gitignore           # Regole Git
```

## 🔧 Tecnologie

- **Frontend**: Streamlit (Python web framework)
- **AI Providers**: OpenAI GPT, Google Gemini, Anthropic Claude, Mistral AI
- **Document Processing**: PyPDF2, python-docx, pandas
- **Visualizations**: Plotly, matplotlib
- **Data**: JSON, CSV, pickle

## 🤝 Contribuire

1. Fork del progetto
2. Crea un branch (`git checkout -b feature/amazing-feature`)
3. Commit delle modifiche (`git commit -m 'Add amazing feature'`)
4. Push al branch (`git push origin feature/amazing-feature`)
5. Apri una Pull Request

## 📄 Licenza

Questo progetto è sotto licenza MIT. Vedi il file [LICENSE](LICENSE) per dettagli.

## 🙋‍♂️ Supporto

Per domande o supporto:
- Apri una [Issue](https://github.com/vinbov/vin-ai/issues)
- Contatta il team di sviluppo

---

**Creato con 🚀 per democratizzare l'accesso all'AI**