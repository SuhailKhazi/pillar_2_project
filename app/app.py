from flask import Flask, request, jsonify
from intake import handle_intake
from todoist_check import get_todoist_tasks

import requests
from datetime import datetime

TODOIST_API_TOKEN = "397f71edcad37aeebd93024505841ae6f2ed005b"

app = Flask(__name__)

@app.route("/check_tasks", methods=["GET"])
def check_tasks():
    tasks = get_todoist_tasks()

    results = []

    for task in tasks["results"]:
        if task["project_id"] == "6fwVcMmWJXVPvWrP":

            results.append({
                "task_id": task.get("id"),
                "content": task.get("content"),
                "status": "completed" if task.get("completed_at") else "incomplete",
                "added_at": task.get("added_at"),
                "due_date": task.get("due"),
                "completed_at": task.get("completed_at"),
                "priority": task.get("priority")
            })

    return {
        "total_tasks": len(results),
        "tasks": results
    }
    # print("tasks: ",tasks)
    # incomplete = [t for t in tasks]  # since API v1 only returns active tasks
    # return jsonify({
    #     "incomplete_count": len(incomplete),
    #     "tasks": incomplete
    # })

    # for key, value in tasks.iteritems() :
    #     print(key)
    
    # print(type(tasks))
    # for idx, task in enumerate(tasks, start=1):
    #     print(task)
    #     for key, value in task.iteritems() :
    #         print(key)
    #     content = task.get("content")
    #     completed = task.get("checked", False)
    #     priority = task.get("priority")
    #     due = task.get("due")

    #     due_date = due.get("date") if due else "No due date"
    #     status = "✅ Completed" if completed else "⏳ Incomplete"

    #     print(f"{idx}. {content}")
    #     print(f"   Status   : {status}")
    #     print(f"   Due Date : {due_date}")
    #     print(f"   Priority : {priority}")

    #     if not completed:
    #         print("   ⚠️ Action needed: task is still incomplete")

    #     print("-" * 40)

@app.route("/intake", methods=["POST"])
def intake():
    data = request.get_json()
    result = handle_intake(data["message"])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
