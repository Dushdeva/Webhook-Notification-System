from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_listener():
    """
    Endpoint to receive webhook notifications about completed tasks
    """
    try:
        # Get the JSON data from the request (important)
        data = request.json
        
        # Log the received data main
        logger.info("Received webhook notification:")
        logger.info(f"Task ID: {data.get('task_id')}")
        logger.info(f"Task Name: {data.get('task_name')}")
        logger.info(f"Status: {data.get('status')}")
        logger.info(f"Completed At: {data.get('completed_at')}")
        logger.info(f"Additional Data: {data.get('additional_data', {})}")
        
        # Returned a success response (I hope works properly)
        return jsonify({
            "status": "success",
            "message": "Webhook received successfully",
            "received_data": data
        }), 200
        
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

if __name__ == '__main__':
    # Run the Flask app on port 5000 (default) follow instructions as per given do not stray from the path boy
    app.run(host='0.0.0.0', port=5000, debug=True)
