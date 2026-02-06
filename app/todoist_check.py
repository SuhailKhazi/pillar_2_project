import requests

TODOIST_API_TOKEN = "397f71edcad37aeebd93024505841ae6f2ed005b"

def get_todoist_tasks():
    url = "https://api.todoist.com/api/v1/tasks"
    headers = {
        "Authorization": f"Bearer {TODOIST_API_TOKEN}",
        "project_id": "6fwVcMmWJXVPvWrP"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch tasks:", response.status_code, response.text)
        return []

    tasks = response.json()
    return tasks

def check_incomplete_tasks():
    tasks = get_todoist_tasks()
    if not tasks:
        print("No tasks retrieved (or error).")
        return

    # All tasks returned by this endpoint are “active” (incomplete) by definition,
    # since completed tasks are not part of the active list in API v1.
    print(f"Total active tasks: {len(tasks)}")

    if len(tasks) == 0:
        print("✔ No incomplete tasks!")
    else:
        print("⚠ Incomplete tasks found:")
        for t in tasks:
            # Example printout; adjust format as you like
            print(f"- {t.get('content')} (ID: {t.get('id')}) Due: {t.get('due')}")
