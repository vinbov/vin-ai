"""
🚀 Vin-AI - Intelligent Assistant Interface
Un'interfaccia web semplice per usare AI avanzate senza scrivere codice.
"""

import streamlit as st
import json
import os
from typing import Dict, Any, Optional
import tempfile
from datetime import datetime

# Importa dati demo
try:
    from demo_data import initialize_demo_session, load_demo_data
    DEMO_MODE = True
except ImportError:
    DEMO_MODE = False
    def initialize_demo_session():
        return False

# Configurazione pagina
st.set_page_config(
    page_title="Vin-AI - Intelligent Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizzato
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .demo-banner {
        background-color: #e8f4fd;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 10px;
        margin: 10px 0;
    }
    .success-banner {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session():
    """Inizializza la sessione Streamlit"""
    # Stato delle pagine
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Chat'
    
    # Configurazioni AI
    if 'ai_settings' not in st.session_state:
        st.session_state.ai_settings = {
            'provider': 'demo',
            'api_key': '',
            'model': 'gpt-4',
            'temperature': 0.7,
            'max_tokens': 1500
        }
    
    # Documenti caricati
    if 'uploaded_documents' not in st.session_state:
        st.session_state.uploaded_documents = []
    
    # Chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def show_header():
    """Mostra header dell'applicazione"""
    st.markdown("""
    <div class="main-header">
        <h1>🚀 Vin-AI - Intelligent Assistant</h1>
        <p>Interfaccia user-friendly per AI avanzate</p>
    </div>
    """, unsafe_allow_html=True)

def show_sidebar():
    """Mostra sidebar con navigazione"""
    with st.sidebar:
        st.title("🧭 Navigazione")
        
        # Menu principale
        pages = ['Chat AI', 'Analisi Documenti', 'Impostazioni', 'Info']
        
        for page in pages:
            if st.button(f"📍 {page}", key=f"nav_{page}", use_container_width=True):
                st.session_state.current_page = page
                st.rerun()
        
        st.divider()
        
        # Stato demo
        if DEMO_MODE:
            st.markdown("""
            <div class="demo-banner">
                <strong>🧪 Modalità Demo</strong><br>
                Dati di esempio caricati per testing
            </div>
            """, unsafe_allow_html=True)
        
        # Info quick
        st.markdown("### 📊 Quick Stats")
        st.metric("Documenti", len(st.session_state.uploaded_documents))
        st.metric("Chat Sessioni", len(st.session_state.chat_history))

def show_chat_page():
    """Pagina chat AI"""
    st.title("💬 Chat AI")
    
    # Selezione configurazione
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("**Chatta con l'AI** - Fai domande, chiedi analisi o cerca informazioni")
    
    with col2:
        if st.button("🔄 Nuova Chat"):
            st.session_state.current_chat = []
            st.rerun()
    
    # Area chat
    if 'current_chat' not in st.session_state:
        st.session_state.current_chat = []
    
    # Mostra messaggi esistenti
    for message in st.session_state.current_chat:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Input utente
    if prompt := st.chat_input("Scrivi il tuo messaggio..."):
        # Aggiungi messaggio utente
        st.session_state.current_chat.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.write(prompt)
        
        # Simula risposta AI (demo)
        if DEMO_MODE:
            from demo_data import simulate_ai_response
            response = simulate_ai_response(prompt)
        else:
            response = "⚙️ Configura le API keys nelle impostazioni per utilizzare l'AI."
        
        # Aggiungi risposta AI
        st.session_state.current_chat.append({"role": "assistant", "content": response})
        
        with st.chat_message("assistant"):
            st.write(response)
        
        st.rerun()

def show_documents_page():
    """Pagina analisi documenti"""
    st.title("📄 Analisi Documenti")
    
    # Upload documenti
    st.markdown("### 📤 Carica Documenti")
    uploaded_files = st.file_uploader(
        "Scegli file da analizzare",
        type=['pdf', 'docx', 'txt', 'md'],
        accept_multiple_files=True
    )
    
    if uploaded_files:
        for file in uploaded_files:
            if file not in [doc['file'] for doc in st.session_state.uploaded_documents if 'file' in doc]:
                # Simula analisi
                doc_info = {
                    'name': file.name,
                    'type': file.type,
                    'size': file.size,
                    'status': 'Caricato',
                    'file': file,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                st.session_state.uploaded_documents.append(doc_info)
        st.success(f"✅ {len(uploaded_files)} file caricati!")
    
    # Lista documenti
    st.markdown("### 📚 Documenti Caricati")
    
    if st.session_state.uploaded_documents:
        for i, doc in enumerate(st.session_state.uploaded_documents):
            with st.expander(f"📄 {doc['name']} ({doc.get('status', 'Unknown')})"):
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    st.write(f"**Tipo:** {doc.get('type', 'N/A')}")
                    st.write(f"**Dimensione:** {doc.get('size', 0)} bytes")
                    st.write(f"**Caricato:** {doc.get('timestamp', 'N/A')}")
                
                with col2:
                    if st.button(f"🔍 Analizza", key=f"analyze_{i}"):
                        st.info("Analisi simulata in modalità demo")
                
                with col3:
                    if st.button(f"🗑️ Rimuovi", key=f"remove_{i}"):
                        st.session_state.uploaded_documents.pop(i)
                        st.rerun()
    else:
        st.info("📝 Nessun documento caricato. Usa il form sopra per iniziare!")

def show_settings_page():
    """Pagina impostazioni"""
    st.title("⚙️ Impostazioni")
    
    # Configurazione AI
    st.markdown("### 🤖 Configurazione AI Provider")
    
    provider = st.selectbox(
        "Provider AI",
        options=['demo', 'openai', 'google', 'anthropic', 'mistral'],
        index=0,
        help="Scegli il provider AI da utilizzare"
    )
    
    if provider != 'demo':
        api_key = st.text_input(
            "API Key",
            type="password",
            placeholder="Inserisci la tua API key",
            help="La chiave API per accedere al servizio"
        )
        
        model = st.selectbox(
            "Modello",
            options=['gpt-4', 'gpt-3.5-turbo', 'claude-3', 'gemini-pro']
        )
        
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=2.0,
            value=0.7,
            step=0.1,
            help="Controlla la creatività delle risposte"
        )
        
        max_tokens = st.number_input(
            "Max Tokens",
            min_value=100,
            max_value=4000,
            value=1500,
            help="Lunghezza massima delle risposte"
        )
        
        if st.button("💾 Salva Configurazione"):
            st.session_state.ai_settings = {
                'provider': provider,
                'api_key': api_key,
                'model': model,
                'temperature': temperature,
                'max_tokens': max_tokens
            }
            st.success("✅ Configurazione salvata!")
    
    else:
        st.info("🧪 Modalità demo attiva - nessuna configurazione richiesta")
    
    # Gestione dati
    st.markdown("### 🗂️ Gestione Dati")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🗑️ Cancella Chat"):
            st.session_state.chat_history = []
            st.session_state.current_chat = []
            st.success("Chat cancellate!")
    
    with col2:
        if st.button("🗑️ Cancella Documenti"):
            st.session_state.uploaded_documents = []
            st.success("Documenti cancellati!")

def show_info_page():
    """Pagina informazioni"""
    st.title("ℹ️ Informazioni")
    
    st.markdown("""
    ## 🚀 Vin-AI - Intelligent Assistant
    
    **Versione:** 1.0.0  
    **Rilascio:** Ottobre 2025
    
    ### 🎯 Caratteristiche Principali
    
    - **💬 Chat AI Intelligente**: Conversazioni naturali con AI avanzate
    - **📄 Analisi Documenti**: Upload e analisi automatica di PDF, DOCX, TXT
    - **🔧 Multi-Provider**: Supporto OpenAI, Google, Anthropic, Mistral
    - **🎨 Interface User-Friendly**: Nessuna programmazione richiesta
    - **📊 Analytics**: Monitoraggio conversazioni e utilizzo
    
    ### 🛠️ Tecnologie Utilizzate
    
    - **Frontend**: Streamlit
    - **Linguaggio**: Python 3.8+
    - **AI Integration**: API multiple providers
    - **Document Processing**: PyPDF2, python-docx
    - **UI Components**: Plotly, pandas
    
    ### 📄 Licenza
    
    Questo progetto è rilasciato sotto licenza MIT.
    
    ### 🤝 Supporto
    
    Per assistenza o segnalazioni:
    - 🐛 [Issues GitHub](https://github.com/vinbov/vin-ai/issues)
    - 📧 Contatta il team di sviluppo
    
    ---
    
    **Creato con 🚀 per democratizzare l'accesso all'AI**
    """)

def main():
    """Funzione principale dell'applicazione"""
    # Inizializza sessione
    initialize_session()
    
    # Carica dati demo se disponibili
    if DEMO_MODE:
        initialize_demo_session()
    
    # Mostra header
    show_header()
    
    # Mostra sidebar
    show_sidebar()
    
    # Routing pagine
    current_page = st.session_state.current_page
    
    if current_page == 'Chat AI':
        show_chat_page()
    elif current_page == 'Analisi Documenti':
        show_documents_page()
    elif current_page == 'Impostazioni':
        show_settings_page()
    elif current_page == 'Info':
        show_info_page()
    else:
        show_chat_page()  # Default

if __name__ == "__main__":
    main()