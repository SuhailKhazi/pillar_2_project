# 🧠 Ops AI — Task Intelligence & Workflow Automation

An AI-powered operations assistant that converts unstructured messages into structured tasks, routes them to Todoist, and continuously monitors task completion for reminders and escalation.

This project demonstrates how AI can reduce operational overhead by automating task intake, tracking, and hygiene — without requiring users to change how they communicate.

---

## 🚀 Problem Statement

Operations and admin teams receive requests via chat, email, or forms in free text:

> “Please arrange laptop and access for the new employee joining next week”

These messages are:
- Unstructured  
- Easy to miss  
- Hard to track  
- Often forgotten until it’s too late  

---

## 🧩 Solution Overview

**Workflow:**

1. User sends a free-text message  
2. AI determines whether the message is actionable  
3. Actionable messages are converted into structured tasks  
4. Tasks are created in Todoist  
5. A scheduled job checks task status  
6. Incomplete or overdue tasks are flagged for notification  

---

## 🏗️ Architecture

```text
[User Message]
      ↓
[AI Classifier]
      ↓
[Task Extraction]
      ↓
[Todoist API]



---

## 🔑 Key Features

- Natural language → task detection  
- Automatic task creation in Todoist  
- Task metadata tracking (due date, created date, completion)  
- REST endpoint for querying task status  
- Cron-ready task monitoring  
- Centralized logging with timestamps and traceability  

---

## 🛠️ Tech Stack

- Python  
- Flask  
- OpenAI API  
- Todoist REST API  
- Python `logging`  
- JSON-based REST endpoints  

---

## 📡 API Endpoints

### POST `/intake`

Accepts free-text input and creates a task if actionable.

**Request**
```json
{
  "message": "Arrange assets for new employee joining Monday"
}
GET /tasks/status

Returns tasks with metadata and completion status.

Response

{
  "tasks": [
    {
      "content": "Arrange laptop for new employee",
      "added_at": "2026-02-05T09:12:00Z",
      "due": "2026-02-07",
      "completed": false
    }
  ]
}


This endpoint is intended to be executed periodically using a cron job.

⏱️ Task Monitoring

A scheduled job can:

Query task status

Identify incomplete or overdue tasks

Trigger notifications (email, Slack, WhatsApp, etc.)

Notification mechanisms are intentionally modular.

🧠 Design Decisions

Simple and explainable AI logic

Minimal UI, focus on workflow automation

Clear extension points for future features

Built for demo clarity and real-world relevance

🔮 Future Enhancements

SLA-based escalation

Manager dashboards

Slack / WhatsApp notifications

Policy-aware workflows using RAG

Priority prediction and auto-escalation

🔐 Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_key
TODOIST_API_KEY=your_todoist_key
TODOIST_PROJECT_ID=your_project_id

📦 Installation & Run
pip install -r requirements.txt
python app.py

📄 License

This project is for demonstration and educational purposes.


---

### ✅ This version:
- Uses proper Markdown headings  
- Has valid code blocks  
- Renders cleanly on GitHub  
- Is demo-ready and recruiter-friendly  

If you want next:
- 🎥 **Demo video script**
- 🧠 **“Explain to non-technical interviewer” version**
- 🧾 **Resume bullets derived from this project**
- 📊 **Architecture diagram (image)**

Say the word and we’ll polish it to perfection 🔥
      ↓
[Task Monitor Endpoint]
      ↓
[Cron Job / Scheduler]
      ↓
[Reminder / Escalation]
