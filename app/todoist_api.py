import requests

TODOIST_API_TOKEN = "397f71edcad37aeebd93024505841ae6f2ed005b"


PRIORITY_MAP = {
    "low": 1,
    "medium": 2,
    "high": 4
}

def create_todoist_task(content, priority="low", extra_notes=None):
    url = "https://api.todoist.com/rest/v2/tasks"
    headers = {
        "Authorization": f"Bearer {TODOIST_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "content": content,
        "priority": PRIORITY_MAP.get(priority, 1)
    }
    # if TODOIST_PROJECT_ID:
    #     data["project_id"] = TODOIST_PROJECT_ID
    if extra_notes:
        data["description"] = extra_notes

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        print("Todoist task creation failed:", response.status_code, response.text)
        return None
