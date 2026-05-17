import requests
import json
from datetime import datetime
import logging

#basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_webhook(task_data):
    """
    Sends a webhook notification about a completed task
    """
    webhook_url = "http://localhost:5000/webhook"

    try:
        response = requests.post(
            webhook_url,
            json=task_data,
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code == 200:
            logger.info("Webhook sent successfully!")
            logger.info(f"Response: {response.json()}")
        else:
            logger.error(f"Webhook failed with status code {response.status_code}")
            logger.error(f"Response: {response.text}")

    except Exception as e:
        logger.error(f"Error sending webhook: {str(e)}")

def simulate_task_completion():
    """
    Creates fake task data to simulate completion
    """
    task_data = {
        "task_id": "task_2",
        "task_name": "Internship project",
        "status": "completed",
        "completed_at": datetime.now().isoformat(),
        "additional_data": {
            "assignee": "Mr. Prashant Kumar",
            "priority": "Very High",
            "estimated_time": "3 hours",
            "actual_time": "9 hours"
        }
    }
    return task_data

if __name__ == '__main__':
    completed_task = simulate_task_completion()

    logger.info("Sending webhook with the task data:")
    logger.info(json.dumps(completed_task, indent=2))

    send_webhook(completed_task)
