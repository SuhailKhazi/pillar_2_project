from classifier import classify_message
from rag import query_sop, generate_natural_response
from todoist_api import create_todoist_task
from logger import log_event

def handle_intake(message: str):
    # 1. Log message received
    log_event("intake_received", {"message": message})

    # 2. Classify message
    classification = classify_message(message)
    log_event("classification_done", {"message": message, "classification": classification})

    response_text = None

    # 3a. Policy question → RAG + summary

    if classification["type"] == "policy_question":
        sop_chunks = query_sop(message, top_k=3)  # top 3 chunks
        response_text = generate_natural_response(message, sop_chunks)
        log_event("policy_response_generated", {
            "message": message,
            "sop_response": response_text
        })
    

    # 3b. Task → Todoist
    elif classification["type"] == "task":
        sop_chunks = query_sop(message)
        sop_tip = " ".join(sop_chunks[:1])  # brief tip

        todoist_response = create_todoist_task(
            content=message,
            priority=classification.get("priority", "low"),
            extra_notes=sop_tip
        )
        if todoist_response:
            response_text = f"Task created in Todoist: {todoist_response.get('id')}"
            log_event("task_created", {
                "message": message,
                "todoist_id": todoist_response.get('id'),
                "priority": classification.get("priority", "low"),
                "sop_tip": sop_tip
            })
        else:
            response_text = "Task creation failed."
            log_event("task_creation_failed", {"message": message, "priority": classification.get("priority", "low")})

    return {
        "status": "ok",
        "message": message,
        "classification": classification,
        "sop_response": response_text
    }
