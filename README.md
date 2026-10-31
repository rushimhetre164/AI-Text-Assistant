# AI Text Assistant

A Python-based AI Text Assistant powered by a locally running Ollama LLM.

## Features
- Text Summarization
- Concept Explanation
- Question and Answer
- Interactive command-line menu
- API integration using Python Requests
- Exception handling and input validation

## Technologies Used
- Python
- Ollama
- Qwen 3.5 (4B)
- REST API
- Requests Library

## Setup

1. Install Python.
2. Install Ollama: https://ollama.com/
3. Download the model:

```bash
ollama pull qwen3.5:4b
```

4. Install the dependency:

```bash
pip install requests
```

5. Run the application:

```bash
python main.py
```

## Note
Ollama must be running locally before starting the application.
