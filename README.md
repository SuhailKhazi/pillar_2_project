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
      ↓
[Task Monitor Endpoint]
      ↓
[Cron Job / Scheduler]
      ↓
[Reminder / Escalation]
```
