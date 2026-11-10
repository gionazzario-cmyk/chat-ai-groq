# 🤖 Chat AI con Groq

Un'app di chat AI che funziona online gratuitamente usando i modelli Llama
ospitati da Groq.

## 🚀 Cosa fa questa app?

- **Chat intelligente** con Llama 3 (70 miliardi di parametri)
- **Funziona online gratis** su Streamlit Cloud
- **Carica file .txt** per farli analizzare dall'IA
- **Scegli la velocità** di risposta (lenta/normale/veloce)
- **Memoria della conversazione** - l'IA ricorda cosa hai detto prima

## 📋 Cosa ti serve (molto facile!)

1. **Account GitHub** (gratis se non ce l'hai)
2. **Account Streamlit** (gratis, si crea con GitHub)

## 🔑 Ottenere la Chiave API di Groq (GRATIS!)

Segui questi passaggi:

1. Vai su [https://console.groq.com/](https://console.groq.com/)
2. Clicca su "Sign up" e registrati con la tua email
3. Dopo il login, clicca su "API Keys" nel menu a sinistra
4. Clicca su "Create API Key"
5. Dai un nome alla chiave (es. "mia chat app")
6. **COPIA LA CHIAVE** (è importante, non puoi rivederla!)

La chiave sarà simile a: `gsk_abc123def456...`

## 🛠️ Come mettere l'app online

### Passaggio 1: Carica su GitHub

1. Vai su [github.com](https://github.com) e fai login
2. Clicca sul "+" verde in alto a destra e scegli "New repository"
3. Dai un nome al progetto (es. `chat-ai-app`)
4. Spunta "Add a README file"
5. Clicca "Create repository"
6. Clicca su "uploading an existing file" e carica tutti i tuoi file:
   - `app.py`
   - `requirements.txt`
   - `README.md`

### Passaggio 2: Attiva su Streamlit Cloud

1. Vai su [share.streamlit.io](https://share.streamlit.io)
2. Fai login con il tuo account GitHub
3. Clicca su "New app"
4. Scegli il repository che hai appena creato
5. Lascia il file principale come `app.py`
6. Clicca "Deploy!"

### Passaggio 3: Aggiungi la Chiave API

1. Nella tua app su Streamlit Cloud, vai su "Settings" (⚙️)
2. Clicca su "Secrets"
3. Incolla questo codice:

```toml
GROQ_API_KEY = "gsk_QUI_LA_TUA_CHIAVE_API"
```

4. Sostituisci `gsk_QUI_LA_TUA_CHIAVE_API` con la tua chiave API vera
5. Clicca "Save" e poi "Rerun" l'app

## 🎮 Come usare l'app

Una volta online, potrai:

1. **Scrivere messaggi** come in WhatsApp con l'IA
2. **Caricare file .txt** per farli analizzare
3. **Scegliere il modello**:
   - `llama3-70b-8192` - Il più potente (consigliato!)
   - `llama3-8b-8192` - Più veloce ma meno intelligente
   - `mixtral-8x7b-32768` - Buon compromesso
4. **Scegliere la velocità**:
   - **Lenta** - Risposte molto precise
   - **Normale** - Equilibrata (consigliata)
   - **Veloce** - Risposte rapide ma più creative

## 💡 Consigli per un 14enne

- **Sii gentile** con l'IA, risponde meglio!
- **Fai domande specifiche** per avere risposte migliori
- **Puoi chiedere qualsiasi cosa**: aiuto per i compiti, spiegazioni, idee creative
- **L'app è gratis** ma ha un limite di messaggi al giorno (abbastanza per usi normali)

## 🚨 Attenzione

- **Non condividere mai** la tua chiave API con altri!
- **Non inserire dati personali** importanti nella chat
- L'IA può sbagliare, verifica sempre le informazioni importanti

## 🆘 Hai problemi?

Se qualcosa non funziona:

1. **Controlla la chiave API** - è corretta?
2. **Aspetta qualche minuto** dopo aver salvato i secrets
3. **Ricarica la pagina** dell'app
4. **Controlla di aver caricato tutti i file** su GitHub

## 🎉 Fatto!

Ora hai una tua app di AI online gratuita! Puoi condividerla con i tuoi amici e usarla quando vuoi.

---

## Note su marchi e modelli

Questo progetto è una demo didattica e **non è affiliato** ad Anthropic, a Claude
né a Groq. I nomi citati appartengono ai rispettivi proprietari.

I modelli Groq citati in questa guida (`llama3-70b-8192`, `llama3-8b-8192`,
`mixtral-8x7b-32768`) cambiano nel tempo: se uno non è più disponibile, aggiorna
l'elenco in `app.py` con i modelli attualmente attivi su
[console.groq.com](https://console.groq.com/).

## Licenza

Rilasciato con licenza MIT — vedere il file [LICENSE](LICENSE).

---

**Creato con ❤️ per ragazzi curiosi come te!**
