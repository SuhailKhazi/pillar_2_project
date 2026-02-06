import subprocess
import json

def classify_message(message: str):
    """
    Sends the message to local Mistral via Ollama and expects strict JSON output.
    Works on Windows.
    """

    prompt = f"""
You are an internal operations assistant. 
Classify the following message into JSON with the following schema:

{{
  "type": "policy_question" or "task",
  "domain": "expenses, procurement, general",
  "priority": "low, medium, high"
}}

Message:
\"\"\"{message}\"\"\"

Only output valid JSON. Do not add extra text.
"""

    try:
        # Run Ollama and send prompt via stdin
        result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        capture_output=True,
        text=True,
        shell=True,
        encoding="utf-8"   # <--- ADD THIS
        )

        print("result: ",result)

        output = result.stdout.strip()

        print("output: ",output)

        # Try to parse JSON
        classification = json.loads(output)
        print("got classification here")
        print("classification: ",classification)

    except json.JSONDecodeError:
        print("in except 1")
        # fallback if model output is malformed
        classification = {
            "type": "task",
            "domain": "general",
            "risk": "low"
        }
    except Exception as e:
        print("in except 2")
        classification = {
            "type": "task",
            "domain": "general",
            "risk": "low"
        }

    return classification
