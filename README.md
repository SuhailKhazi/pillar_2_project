Ops AI – Task Automation MVP

Description:
An AI-powered operations assistant that converts unstructured messages into actionable tasks and tracks their completion in Todoist.

Features

Accepts free-text operational requests

Classifies messages as task or policy question

Creates tasks in Todoist automatically

Checks task completion status via API

Traceable logs with timestamps

Tech Stack

Python 3.12

Flask

Open-source LLM: Mistral via Ollama

Todoist REST API

FAISS vector database for SOP retrieval

Python logging module for traceability

API Endpoints
1. POST /intake

Create a task from a message.

Request Example

{
  "message": "Arrange laptop for new employee"
}


Response Example

{
  "status": "success",
  "task": {
    "content": "Arrange laptop",
    "priority": "high",
    "added_at": "2026-02-06T04:42:55"
  }
}

2. GET /tasks/status

Retrieve all tasks and their completion status.

Response Example

{
  "tasks": [
    {
      "content": "Arrange laptop",
      "added_at": "2026-02-06T04:42:55",
      "due": "2026-02-07",
      "completed": false
    }
  ]
}

Setup

Clone the repo:

git clone https://github.com/yourusername/ops-ai.git
cd ops-ai


Install dependencies:

pip install -r requirements.txt


Set environment variables:

TODOIST_API_KEY=your_todoist_key
TODOIST_PROJECT_ID=your_project_id


Run Flask app:

python app.py

Notes

Designed as an MVP; can be extended with notifications, cron-based reminders, and more advanced RAG features.

Logs all operations for traceability.
