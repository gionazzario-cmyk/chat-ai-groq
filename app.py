"""
App di Chat AI - similar to Claude
Creato con Streamlit e Groq per funzionare online gratuitamente

Caratteristiche:
- Interfaccia chat pulita con sidebar per impostazioni
- Usa Groq API per modelli gratuiti e velocissimi (Llama 3 70B)
- Memoria della conversazione corrente
- Possibilità di caricare file .txt da analizzare
- Pronta per Streamlit Cloud
"""

# ============================================================================
# IMPORTAZIONI
# ============================================================================

import streamlit as st
from groq import Groq
import os

# ============================================================================
# CONFIGURAZIONE DELLA PAGINA
# ============================================================================

# Configurazione Streamlit
st.set_page_config(
    page_title="Chat AI - Assistente Online",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# FUNZIONI UTILITY
# ============================================================================

def init_session_state():
    """
    Inizializza lo stato della sessione per la memoria della chat.
    Utilizza st.session_state per conservare i messaggi tra le interazioni.
    Limitiamo la cronologia per non superare i limiti di Groq API.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "model" not in st.session_state:
        st.session_state.model = "llama3-70b-8192"
    
    if "file_content" not in st.session_state:
        st.session_state.file_content = None
    
    if "speed" not in st.session_state:
        st.session_state.speed = "normale"


def init_groq_client():
    """
    Inizializza il client Groq usando la chiave API da st.secrets.
    La chiave API deve essere configurata in Streamlit Cloud.
    """
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        return Groq(api_key=api_key)
    except KeyError:
        st.error("⚠️ Chiave API di Groq non trovata! Leggi il README per configurarla.")
        return None
    except Exception as e:
        st.error(f"Errore nel connettersi a Groq: {e}")
        return None


def generate_response(client, model: str, messages: list, speed: str) -> str:
    """
    Genera una risposta utilizzando Groq API.
    
    Args:
        client: Client Groq inizializzato
        model: Nome del modello da utilizzare
        messages: Lista di messaggi nel formato richiesto da Groq
        speed: Velocità di risposta (lenta, normale, veloce)
        
    Returns:
        Risposta del modello AI
    """
    try:
        # Impostazioni temperatura in base alla velocità
        temp_settings = {
            "lenta": 0.3,      # Più preciso e lento
            "normale": 0.7,    # Bilanciato
            "veloce": 1.0      # Più creativo e veloce
        }
        
        temperature = temp_settings.get(speed, 0.7)
        
        # Converte i messaggi per Groq
        groq_messages = []
        for msg in messages:
            if msg["role"] == "system":
                groq_messages.append({"role": "system", "content": msg["content"]})
            elif msg["role"] == "user":
                groq_messages.append({"role": "user", "content": msg["content"]})
            elif msg["role"] == "assistant":
                groq_messages.append({"role": "assistant", "content": msg["content"]})
        
        response = client.chat.completions.create(
            model=model,
            messages=groq_messages,
            temperature=temperature,
            max_tokens=1024
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Errore nella generazione della risposta: {e}"


def read_text_file(uploaded_file):
    """
    Legge il contenuto di un file di testo caricato.
    
    Args:
        uploaded_file: File caricato dall'utente
        
    Returns:
        Contenuto del file come stringa
    """
    try:
        return uploaded_file.getvalue().decode("utf-8")
    except Exception as e:
        st.error(f"Errore nella lettura del file: {e}")
        return None


# ============================================================================
# INTERFACCIA UTENTE - SIDEBAR
# ============================================================================

def render_sidebar():
    """
    Renderizza la barra laterale con le impostazioni.
    """
    st.sidebar.title("⚙️ Impostazioni")
    
    # Inizializza il client Groq
    client = init_groq_client()
    if not client:
        st.sidebar.error("⚠️ App non funzionante senza chiave API di Groq")
        return None
    
    # Selezione del modello
    available_models = [
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mixtral-8x7b-32768"
    ]
    
    selected_model = st.sidebar.selectbox(
        "Seleziona Modello",
        options=available_models,
        index=0,
        help="Llama 3 70B è il più potente, simile a Claude"
    )
    
    # Aggiorna il modello nella sessione
    st.session_state.model = selected_model
    
    # Selettore velocità
    speed_options = ["lenta", "normale", "veloce"]
    selected_speed = st.sidebar.selectbox(
        "Velocità Risposta",
        options=speed_options,
        index=1,
        help="Lenta = più preciso, Veloce = più creativo"
    )
    st.session_state.speed = selected_speed
    
    st.sidebar.divider()
    
    # Informazioni sul modello
    st.sidebar.subheader("ℹ️ Info Modello")
    st.sidebar.info(f"Modello attivo: **{selected_model}**")
    st.sidebar.info(f"Velocità: **{selected_speed}**")
    
    st.sidebar.divider()
    
    # Pulizia della chat
    if st.sidebar.button("🗑️ Pulisci Chat", type="primary"):
        st.session_state.messages = []
        st.session_state.file_content = None
        st.rerun()
    
    st.sidebar.divider()
    
    # Istruzioni
    st.sidebar.subheader("📋 Istruzioni")
    st.sidebar.markdown("""
    1. Configura la chiave API di Groq (vedi README)
    2. Seleziona un modello dalla lista sopra
    3. Scegli la velocità di risposta
    4. Scrivi un messaggio nella chat
    5. (Opzionale) Carica un file .txt da analizzare
    
    **Nota:** L'app funziona online gratuitamente su Streamlit Cloud!
    """)
    
    return client


# ============================================================================
# INTERFACCIA UTENTE - AREA PRINCIPALE
# ============================================================================

def render_chat(client):
    """
    Renderizza l'interfaccia della chat con la cronologia dei messaggi.
    """
    st.title("💬 Chat AI - Assistente Online")
    
    # Mostra i messaggi precedenti
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input dell'utente
    if prompt := st.chat_input("Scrivi il tuo messaggio..."):
        # Aggiungi il messaggio dell'utente alla cronologia
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Mostra il messaggio dell'utente
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Prepara i messaggi per Groq
        groq_messages = []
        
        # Aggiungi il contenuto del file come contesto iniziale
        if st.session_state.file_content:
            context_prompt = f"Ecco il contenuto di un file che devi analizzare:\n\n{st.session_state.file_content}\n\nOra rispondi alla domanda dell'utente."
            groq_messages.append({"role": "system", "content": context_prompt})
        
        # Aggiungi la cronologia dei messaggi (limitata per efficienza)
        # Massimo 20 messaggi per non superare i limiti API
        recent_messages = st.session_state.messages[-20:]
        for msg in recent_messages:
            groq_messages.append({"role": msg["role"], "content": msg["content"]})
        
        # Genera la risposta
        with st.chat_message("assistant"):
            with st.spinner("🤔 Sto pensando..."):
                response = generate_response(client, st.session_state.model, groq_messages, st.session_state.speed)
                st.markdown(response)
        
        # Aggiungi la risposta alla cronologia
        st.session_state.messages.append({"role": "assistant", "content": response})


def render_file_uploader():
    """
    Renderizza il selettore per caricare file .txt
    """
    st.sidebar.subheader("📁 Carica File")
    
    uploaded_file = st.sidebar.file_uploader(
        "Seleziona un file .txt da analizzare",
        type=["txt"],
        help="Carica un file di testo che l'IA leggerà e commenterà"
    )
    
    if uploaded_file is not None:
        # Leggi il contenuto del file
        content = read_text_file(uploaded_file)
        
        if content:
            st.session_state.file_content = content
            st.sidebar.success(f"✅ File caricato: {uploaded_file.name}")
            st.sidebar.markdown("---")
            st.sidebar.subheader("📄 Contenuto del File")
            # Mostra un'anteprima del file (primi 1000 caratteri)
            preview = content[:1000] + "..." if len(content) > 1000 else content
            st.sidebar.text_area("Anteprima", preview, height=150, disabled=True)
            
            # Opzione per rimuovere il file
            if st.sidebar.button("❌ Rimuovi File"):
                st.session_state.file_content = None
                st.rerun()
    
    elif st.session_state.file_content is not None:
        st.sidebar.info("📄 File già caricato dalla sessione precedente")


# ============================================================================
# PUNTO DI INGRESSO
# ============================================================================

def main():
    """
    Funzione principale dell'applicazione.
    """
    # Inizializza lo stato della sessione
    init_session_state()
    
    # Renderizza la sidebar e ottieni il client
    client = render_sidebar()
    render_file_uploader()
    
    # Renderizza l'area di chat solo se il client è disponibile
    if client:
        render_chat(client)
    else:
        st.error("⚠️ L'app non può funzionare senza la configurazione di Groq. Leggi il README.md per istruzioni.")


if __name__ == "__main__":
    main()