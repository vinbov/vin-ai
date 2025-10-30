# 🍷 Vin-AI - Intelligent Wine Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Un assistente AI intelligente per il mondo del vino - analisi, raccomandazioni e gestione documenti!**

## 🎯 Panoramica

Vin-AI è una piattaforma web intuitiva che permette agli appassionati di vino e professionisti del settore di:

- 🍇 **Chatbot specializzato nel vino** con conoscenze enologiche avanzate
- 📄 **Analisi documenti vinicoli** (schede tecniche, note di degustazione, certificazioni)
- 🔍 **Ricerca intelligente** in database di vini e cantine
- ⚙️ **Configurare provider AI** multipli (OpenAI, Google Gemini, Anthropic)
- 📊 **Analytics e reporting** per cantine e distributori

### 🤖 Assistente Vino Intelligente
- Consigli personalizzati sui vini
- Analisi di abbinamenti cibo-vino
- Informazioni su regioni vinicole e vitigni
- Supporto per sommelier e wine lover

### 📄 Gestione Documenti Vinicoli
- Upload di schede tecniche, certificazioni, etichette
- Analisi automatica con AI specializzata
- Estrazione di dati chiave (annata, gradazione, note)
- Organizzazione intelligente della documentazione

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

### 1. 🍷 Chat Vino
- Seleziona "Chat Vino" dalla sidebar
- Fai domande sui vini, abbinamenti, regioni
- L'AI risponderà con expertise enologica

### 2. 📑 Analisi Documenti
- Vai su "Analisi Documenti"
- Carica schede tecniche, etichette, certificazioni
- Visualizza l'analisi AI automatica

### 3. ⚙️ Configurazione
- Imposta le tue API keys nei Settings
- Scegli il provider AI preferito
- Personalizza le impostazioni

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
- **AI Providers**: OpenAI GPT, Google Gemini, Anthropic Claude
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

**Creato con 🍷 per gli amanti del vino e la tecnologia AI**