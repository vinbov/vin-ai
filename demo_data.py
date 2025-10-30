#!/usr/bin/env python3
"""
Demo Data Generator for Vin-AI Interface
Popola l'interfaccia con dati di esempio per testing
"""

import streamlit as st
from datetime import datetime
import json

def load_demo_data():
    """Carica dati demo nell'interfaccia"""

    # Demo documenti
    demo_documents = [
        {
            'name': 'Relazione_Trimestrale_Q3_2024.pdf',
            'type': 'application/pdf',
            'size': 2547392,  # ~2.5MB
            'status': 'Analizzato',
            'path': '/tmp/demo_quarterly_report.pdf',
            'content': """
RELAZIONE TRIMESTRALE Q3 2024 - VIN-AI

SOMMARIO ESECUTIVO
Il terzo trimestre 2024 ha registrato una crescita significativa del 45% rispetto al trimestre precedente.        
Le nostre soluzioni AI hanno processato oltre 2.3 milioni di documenti, generando insights strategici
per 847 clienti enterprise in 23 paesi.

RISULTATI CHIAVE
• Ricavi: €8.4M (+45% YoY)
• Clienti Enterprise: +127 nuovi contratti
• Retention Rate: 94.7%
• NPS Score: 73 (+8 punti)

INNOVAZIONI TECNOLOGICHE
Il lancio del nostro motore di analisi documenti multilingue ha rivoluzionato il mercato europeo.
L'integrazione con 15 nuovi provider AI ha ampliato le capacità di elaborazione del 200%.

PROSPETTIVE Q4
Prevediamo di superare i €12M di ricavi nel Q4, con focus su espansione mercato asiatico e
lancio della piattaforma no-code per PMI.

SFIDE E OPPORTUNITÀ
La principale sfida rimane la scalabilità dell'infrastruttura cloud. Investimenti di €3.2M
in architettura serverless sono previsti per Q1 2025.

CONCLUSIONI
Vin-AI si conferma leader nel settore GenAI enterprise, con solide basi per crescita sostenibile.
            """,
            'analysis': {
                'summary': 'Relazione trimestrale che evidenzia crescita del 45% e risultati positivi nelle metriche chiave',
                'key_points': [
                    'Crescita ricavi 45% YoY',
                    'Alto retention rate (94.7%)',
                    'Espansione tecnologica significativa',
                    'Pianificazione strategica Q4'
                ],
                'entities': ['Q3 2024', 'DataPizza AI', '€8.4M', '847 clienti', '23 paesi'],
                'sentiment': 'Positivo',
                'language': 'Italiano',
                'confidence': 0.94,
                'processing_time': 2.3,
                'timestamp': '2024-10-29 14:32:17'
            }
        },
        {
            'name': 'Technical_Documentation_EN.docx',
            'type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'size': 1847293,
            'status': 'Completato',
            'path': '/tmp/demo_tech_docs.docx',
            'content': """
VIN-AI TECHNICAL ARCHITECTURE DOCUMENTATION

OVERVIEW
This document outlines the technical architecture of Vin-AI platform, designed for enterprise-grade
AI document processing and intelligent chatbot capabilities.

SYSTEM ARCHITECTURE
The platform follows a microservices architecture with the following core components:

1. API Gateway Layer
   - Authentication & Authorization
   - Rate Limiting
   - Request Routing
   - Load Balancing

2. Processing Engine
   - Document Parser (PDF, DOCX, TXT, MD)
   - OCR Capabilities  
   - Text Extraction & Preprocessing
   - Multi-language Support (15+ languages)

3. AI Engine
   - Multi-provider Integration (OpenAI, Google, Anthropic, Mistral)
   - Prompt Engineering Framework
   - Response Optimization
   - Context Management

4. Data Layer
   - Document Storage (S3 Compatible)
   - Metadata Database (PostgreSQL)
   - Cache Layer (Redis)
   - Search Index (Elasticsearch)

SCALABILITY FEATURES
- Horizontal auto-scaling based on demand
- Distributed processing with Apache Kafka
- CDN integration for global content delivery
- Multi-region deployment support

SECURITY MEASURES
- End-to-end encryption (AES-256)
- OAuth 2.0 / SAML integration
- API key management
- Audit logging
- Data privacy compliance (GDPR, CCPA)

PERFORMANCE METRICS
- Average response time: <200ms
- Document processing: 1000+ docs/minute
- 99.9% uptime SLA
- Auto-scaling up to 10,000 concurrent users

DEPLOYMENT OPTIONS
1. Cloud-native (AWS, Azure, GCP)
2. On-premises installation
3. Hybrid cloud deployment
4. Edge computing support

INTEGRATION CAPABILITIES
- RESTful APIs
- Webhooks
- SDKs (Python, JavaScript, Java)
- Third-party connectors (Slack, Teams, Salesforce)

MONITORING & ANALYTICS
- Real-time dashboards
- Performance metrics
- Usage analytics
- Error tracking
- Health checks

FUTURE ROADMAP
Q1 2025: Advanced ML models integration
Q2 2025: Voice processing capabilities
Q3 2025: Augmented reality features
Q4 2025: Quantum computing research
            """,
            'analysis': {
                'summary': 'Documentazione tecnica completa dell\'architettura Vin-AI con focus su scalabilità e sicurezza',
                'key_points': [
                    'Architettura microservizi',
                    'Multi-provider AI integration',
                    'Sicurezza enterprise-grade',
                    'Scalabilità automatica'
                ],
                'entities': ['API Gateway', 'PostgreSQL', 'Redis', 'Elasticsearch', 'AWS', 'Azure', 'GCP'],
                'sentiment': 'Neutrale/Tecnico',
                'language': 'Inglese',
                'confidence': 0.98,
                'processing_time': 3.1,
                'timestamp': '2024-10-29 15:45:32'
            }
        }
    ]

    # Demo chat history
    demo_chat_history = [
        {
            'session_id': 'demo_session_001',
            'timestamp': '2024-10-29 16:20:15',
            'messages': [
                {
                    'role': 'user',
                    'content': 'Puoi analizzare il documento sulla relazione trimestrale?',
                    'timestamp': '2024-10-29 16:20:15'
                },
                {
                    'role': 'assistant', 
                    'content': '''Certamente! Ho analizzato la relazione trimestrale Q3 2024 e posso fornirti un riassunto dettagliato:

**📈 Risultati Principali:**
- Crescita eccezionale del 45% rispetto al trimestre precedente
- Ricavi raggiunti: €8.4M (+45% anno su anno)
- 127 nuovi contratti enterprise acquisiti
- Retention rate molto elevato: 94.7%

**🚀 Innovazioni Tecnologiche:**
- Lancio motore di analisi documenti multilingue
- Integrazione con 15 nuovi provider AI
- Capacità di elaborazione aumentate del 200%

**🎯 Prospettive Q4:**
- Obiettivo ricavi: >€12M
- Focus su espansione mercato asiatico
- Lancio piattaforma no-code per PMI

**⚠️ Sfide Identificate:**
- Scalabilità infrastruttura cloud
- Investimenti previsti: €3.2M per architettura serverless

Il documento mostra una crescita solida e sostenibile con una strategia ben definita per il futuro.''',
                    'timestamp': '2024-10-29 16:20:28'
                },
                {
                    'role': 'user',
                    'content': 'Quali sono i principali KPI menzionati?',
                    'timestamp': '2024-10-29 16:21:45'
                },
                {
                    'role': 'assistant',
                    'content': '''Ecco i principali KPI evidenziati nella relazione:

**💰 KPI Finanziari:**
- Ricavi Q3: €8.4M
- Crescita YoY: +45%
- Previsione Q4: >€12M

**👥 KPI Clienti:**
- Nuovi contratti enterprise: +127
- Cliente totali enterprise: 847
- Retention Rate: 94.7%
- NPS Score: 73 (+8 punti)

**🌍 KPI Operativi:**
- Documenti processati: 2.3M+
- Paesi serviti: 23
- Capacità elaborazione: +200%
- Provider AI integrati: 15

**📊 Metriche di Performance:**
- Tutti i KPI mostrano trend positivi
- Il retention rate del 94.7% è eccellente per il settore enterprise
- L'NPS di 73 indica alta soddisfazione clienti

Questi indicatori suggeriscono un business in forte crescita con basi solide.''',
                    'timestamp': '2024-10-29 16:21:52'
                }
            ]
        }
    ]

    # Demo chatbot configurations
    demo_chatbot_configs = [
        {
            'name': 'Assistente Generale',
            'description': 'Chatbot general-purpose per domande varie',
            'system_prompt': 'Sei un assistente AI utile e professionale. Rispondi sempre in modo chiaro e preciso.',
            'model': 'gpt-4',
            'temperature': 0.7,
            'max_tokens': 1500,
            'active': True,
            'created_at': '2024-10-25 10:00:00'
        },
        {
            'name': 'Analista Documenti',
            'description': 'Specializzato nell\'analisi e sintesi di documenti',
            'system_prompt': '''Sei un esperto analista di documenti. Il tuo compito è:
1. Analizzare documenti in modo approfondito
2. Estrarre informazioni chiave
3. Fornire riassunti strutturati
4. Identificare pattern e trends
5. Suggerire azioni basate sui dati

Rispondi sempre in modo professionale e dettagliato.''',
            'model': 'gpt-4',
            'temperature': 0.3,
            'max_tokens': 2000,
            'active': True,
            'created_at': '2024-10-26 14:30:00'
        }
    ]

    return {
        'documents': demo_documents,
        'chat_history': demo_chat_history,
        'chatbot_configs': demo_chatbot_configs
    }

def initialize_demo_session():
    """Inizializza la sessione con dati demo"""
    if 'demo_loaded' not in st.session_state:
        demo_data = load_demo_data()
        
        # Carica documenti demo
        if 'uploaded_documents' not in st.session_state:
            st.session_state.uploaded_documents = demo_data['documents']
        
        # Carica chat history demo
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = demo_data['chat_history']
        
        # Carica configurazioni chatbot demo
        if 'chatbot_configs' not in st.session_state:
            st.session_state.chatbot_configs = demo_data['chatbot_configs']
        
        # Imposta flag demo caricato
        st.session_state.demo_loaded = True
        
        return True
    return False

# Funzioni helper per demo
def get_demo_document_analysis(doc_name):
    """Ritorna analisi demo per un documento specifico"""
    demo_data = load_demo_data()
    for doc in demo_data['documents']:
        if doc['name'] == doc_name:
            return doc['analysis']
    return None

def add_demo_chat_message(session_id, role, content):
    """Aggiunge messaggio demo alla chat history"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    message = {
        'role': role,
        'content': content,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Trova sessione esistente o crea nuova
    session_found = False
    for session in st.session_state.chat_history:
        if session['session_id'] == session_id:
            session['messages'].append(message)
            session_found = True
            break
    
    if not session_found:
        new_session = {
            'session_id': session_id,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'messages': [message]
        }
        st.session_state.chat_history.append(new_session)

def simulate_ai_response(user_input, config_name="Assistente Generale"):
    """Simula risposta AI per demo"""
    # Risposte predefinite per demo
    demo_responses = {
        "ciao": "Ciao! Sono il tuo assistente AI. Come posso aiutarti oggi?",
        "come stai": "Sto bene, grazie! Sono qui e pronto ad assisterti. Di cosa hai bisogno?",
        "analisi documento": "Perfetto! Posso analizzare documenti PDF, DOCX e TXT. Carica un file e ti fornirò un'analisi dettagliata.",
        "aiuto": "Posso aiutarti con: 📄 Analisi documenti, 💬 Conversazioni intelligenti, 📊 Estrazione dati, 🔍 Ricerche mirate. Cosa ti interessa?",
        "funzionalità": "Le mie principali funzionalità includono: analisi documenti, chatbot intelligente, estrazione informazioni, riassunti automatici e molto altro!"
    }
    
    # Cerca risposta predefinita
    user_lower = user_input.lower()
    for key, response in demo_responses.items():
        if key in user_lower:
            return response
    
    # Risposta generica
    return f"Ho ricevuto la tua domanda: '{user_input}'. In modalità demo, posso fornire risposte simulate. Per funzionalità complete, configura le API keys nelle impostazioni!"

# Utility per reset demo
def reset_demo_data():
    """Reset dei dati demo"""
    keys_to_remove = ['demo_loaded', 'uploaded_documents', 'chat_history', 'chatbot_configs']
    for key in keys_to_remove:
        if key in st.session_state:
            del st.session_state[key]

# Export demo configuration
def export_demo_config():
    """Esporta configurazione demo"""
    demo_data = load_demo_data()
    return json.dumps(demo_data, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    # Test delle funzioni demo
    print("🧪 Testing Demo Data Generator...")
    
    # Test caricamento dati
    data = load_demo_data()
    print(f"✅ Caricati {len(data['documents'])} documenti demo")
    print(f"✅ Caricate {len(data['chat_history'])} sessioni chat demo") 
    print(f"✅ Caricate {len(data['chatbot_configs'])} configurazioni chatbot demo")
    
    # Test analisi documento
    analysis = get_demo_document_analysis('Relazione_Trimestrale_Q3_2024.pdf')
    if analysis:
        print(f"✅ Analisi documento trovata: {analysis['summary'][:50]}...")
    
    # Test risposta AI
    response = simulate_ai_response("Ciao come stai?")
    print(f"✅ Risposta AI simulata: {response}")
    
    print("🎉 Demo Data Generator test completato!")