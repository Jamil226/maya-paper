# Maya - Hospital Receptionist

Maya is an intelligent hospital receptionist agent capable of handling general inquiries, checking doctor availability, and booking appointments. It uses a graph-based agent architecture to orchestrate interactions between a local LLM, a vector database for knowledge retrieval, and a SQL database for transactional operations.

## Tech Stack

- **Language:** Python
- **Frameworks:** LangChain, LangGraph
- **UI:** Streamlit
- **LLM & Embeddings:** Ollama (Llama 3.1)
- **Databases:**
  - SQLite (Relational data for doctors, patients, appointments)
  - ChromaDB (Vector store for general hospital knowledge)

## Features

- **Conversation History:** Remembers context within a session using memory capability.
- **Tool Usage:** Dynamically chooses tools to look up information (RAG/SQL) or perform actions (booking).
- **Hybrid Data Access:** Combines unstructured data search (vector DB) with structured data queries (SQL DB).
- **Local LLM Execution:** Runs completely locally using Ollama.

## Project Structure

### Core Application

- **`main.py`**: The Streamlit web application. Manages the chat interface, session state, and invokes the Maya agent.
- **`console_app.py`**: A simple console-based script to test the agent's functionality without the web UI.

### Agent Logic

- **`maya_agent.py`**: Implements the agent using LangGraph (`StateGraph`). Defines the chatbot node, tool routing, and memory persistence.
- **`tools.py`**: Defines access to:
  - `ask_hospital_info`: RAG tool (ChromaDB) for general questions.
  - `ask_database`: SQL agent tool (SQLite) for structured data (doctors, schedules).
  - `book_appointment`: Transactional tool to create appointments.
- **`llms.py`**: Configures `ChatOllama` and `OllamaEmbeddings` (Llama 3.1).

### Data Management

- **`rag_info.py`**: Ingests data from `knowledge_base.json` into the local ChromaDB vector store.
- **`db_handler.py`**: Initializes the SQLite database and defines table schemas (`doctors`, `patients`, `appointments`).
- **`setup.py`**: Scripts to set up the environment/database.
- **Data Files**:
  - `knowledge_base.json`: Source text for RAG.
  - `doctors_info.json`, `pseudo_patients_info.json`: Initial seed data for the database.
  - `update_doctors.py`, `update_patients.py`: Scripts to populate the database.

## Setup & Running

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Install Ollama**
   Ensure you have [Ollama](https://ollama.com/) installed and the llama3.1 model pulled:

   ```bash
   ollama pull llama3.1
   ```

3. **Initialize Databases**
   Run the setup scripts to prepare the SQLite and ChromaDB data:

   ```bash
   python setup.py
   python rag_info.py
   # Populate SQLite data if needed
   python update_doctors.py
   python update_patients.py
   ```

4. **Run the Application**
   Start the Streamlit interface:
   ```bash
   streamlit run main.py
   ```
