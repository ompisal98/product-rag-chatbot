# Product RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** based product customer service chatbot that answers user questions using information retrieved from a product knowledge base.

The project combines document retrieval with a Groq-powered language model to provide context-aware answers about products.

## Features

* Load product information from CSV documents.
* Build a searchable knowledge base using embeddings.
* Retrieve relevant product information for each question.
* Generate answers using a Groq LLM.
* Interactive command-line chatbot.
* Supports questions such as:

  * "What is the battery life?"
  * "How do I connect Bluetooth?"
  * "What are the product features?"
* Uses environment variables to keep API keys secure.

## Project Structure

```text
product-rag-chatbot/
│
├── chatbot.py          # Main chatbot application
├── .env                # API keys (not committed to Git)
├── .gitignore          # Files excluded from Git
├── pyproject.toml      # Project dependencies and configuration
├── uv.lock             # Locked dependency versions
├── data/               # Product knowledge base / CSV files
│   └── *.csv
│
└── README.md
```

> The exact folder structure may vary depending on your implementation.

## Technologies Used

* **Python** — Programming language
* **RAG** — Retrieval-Augmented Generation
* **Embeddings** — Convert documents into numerical vectors for semantic search
* **Groq API** — LLM inference
* **OpenAI-compatible chat completions API** — Used through the Groq Python SDK
* **python-dotenv** — Load environment variables from `.env`
* **uv** — Python project and dependency management

## How It Works

```text
User Question
      │
      ▼
Document Retrieval
      │
      ▼
Relevant Product Context
      │
      ▼
Prompt + Retrieved Context
      │
      ▼
Groq LLM
      │
      ▼
Generated Answer
```

The chatbot retrieves relevant information from the product knowledge base before generating a response. This helps the model answer questions using the available product data rather than relying only on general knowledge.

## Prerequisites

Make sure you have:

* Python 3.10 or later
* [uv](https://docs.astral.sh/uv/) installed
* A Groq API key

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd product-rag-chatbot
```

### 2. Install dependencies

If the project already contains a `pyproject.toml`:

```bash
uv sync
```

If you need to add the required packages:

```bash
uv add groq python-dotenv
```

> Add any other dependencies required by your existing RAG implementation.

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

Replace `your_actual_groq_api_key` with your real API key.

**Do not share your API key or commit the `.env` file to GitHub.**

### 4. Add product data

Place your product CSV files in the folder expected by your `chatbot.py` implementation.

For example:

```text
data/
├── product1.csv
├── product2.csv
└── product3.csv
```

The CSV files should contain the product information that the chatbot needs to answer questions.

## Running the Chatbot

Run the application using:

```bash
uv run chatbot.py
```

Example:

```text
Loaded 35 documents
Knowledge base ready!

Product Customer Service Chatbot
Type 'exit' to stop.

You: what is the battery life?
Assistant: ...
```

To stop the chatbot:

```text
You: exit
```

## Model Configuration

The chatbot uses a Groq-supported model. In the current implementation, the model is configured as:

```python
model="openai/gpt-oss-20b"
```

This model was selected because it is available for the configured Groq API key.

To use another model, replace the model ID with one available to your account.

## Environment Variables

| Variable       | Description                         |
| -------------- | ----------------------------------- |
| `GROQ_API_KEY` | API key used to access the Groq API |


## Security

Add the following to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

Never commit API keys, tokens, or other secrets to the repository.

## Future Improvements

* Add a web interface using Streamlit or FastAPI.
* Support multiple product categories.
* Add conversation history.
* Improve retrieval accuracy with better chunking.
* Add source citations to answers.
* Add error handling for API failures.
* Add automated tests.
* Support multilingual product queries.

## License

This project is for educational and development purposes.

Add your preferred license here, such as MIT, if you plan to distribute the project.

## Author

**Om Rajaram Pisal**

---

*Built as a Product RAG Chatbot project using Python, embeddings, and Groq LLM inference.*
