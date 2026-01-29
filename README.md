# 🏥 Maya - Agentic Hospital Receptionist

Maya is an intelligent agent designed to handle hospital receptionist duties. Powered by **Llama 3.1** and a graph-based agent architecture (**LangGraph**), Maya orchestrates interactions between a local LLM, a generic knowledge base, and a structured hospital database to help patients efficiently.

## ✨ Key Features

- **Conversational Booking**: engage in natural dialogue to book appointments.
- **RAG-Powered Knowledge**: Answers general questions (visiting hours, locations) using vector search over hospital documents.
- **SQL Integration**: Queries real-time doctor availability and patient records.
- **Stateful Memory**: Remembers context across the conversation.
- **Privacy-First**: Runs entirely locally using Ollama.

## 🛠️ Tech Stack

- **Agent Framework**: LangChain & LangGraph
- **LLM**: Ollama (Llama 3.1)
- **Vector Store**: ChromaDB
- **Database**: SQLite
- **Interface**: Streamlit (Web) & Python Console

## 📂 Project Structure

```bash
├── main.py                # Streamlit web application entry point
├── console_app.py         # Terminal-based chat interface for testing
├── maya_agent.py          # Core agent logic, graph definition, and state management
├── tools.py               # Tool definitions (RAG, SQL, Booking)
├── llms.py                # LLM and Embedding configuration
├── db_handler.py          # Database schema and initialization logic
├── rag_info.py            # Script to ingest knowledge base into ChromaDB
├── setup.py               # Utility to initialize the SQLite database
├── update_doctors.py      # Seed script for doctor data
├── update_patients.py     # Seed script for patient data
├── hospital.db            # Local SQLite database (generated)
├── chroma_db/             # Local Vector store (generated)
└── requirements.txt       # Project dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) installed and running.

### 1. Installation

Clone the repository and install Python dependencies:

```bash
pip install -r requirements.txt
```

Pull the required LLM model:

```bash
ollama pull llama3.1
```

### 2. Database Setup

Initialize the structured database and the vector store:

```bash
# Initialize SQLite DB schema
python setup.py

# Ingest Knowledge Base into ChromaDB (RAG)
python rag_info.py
```

Populate the database with sample data:

```bash
python update_doctors.py
python update_patients.py
```

### 3. Running the Agent

**Option A: Web Assistant (Recommended)**
Launch the Streamlit interface:

```bash
streamlit run main.py
```

**Option B: Console Mode**
Run a quick test in the terminal:

```bash
python console_app.py
```

## 💡 Capabilities

Maya is equipped with specific tools to handle different requests:

| Intent                    | Tool Used           | Description                               |
| ------------------------- | ------------------- | ----------------------------------------- |
| "Where is cardiology?"    | `ask_hospital_info` | Retrieves static info from ChromaDB.      |
| "Is Dr. Smith available?" | `ask_database`      | SQL query to `hospital.db` for schedules. |
| "Book an appointment."    | `book_appointment`  | Transactional write to the database.      |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
