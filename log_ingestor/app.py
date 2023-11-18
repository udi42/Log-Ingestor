from flask import Flask, request

app = Flask(__name__)

logs = []  # In-memory storage for simplicity, consider using a database in a real scenario

@app.route('/ingest', methods=['POST'])
def ingest_logs():
    # Retrieve JSON data from the incoming POST request
    data = request.get_json()

    # Validate that the required fields are present
    required_fields = ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit']
    for field in required_fields:
        if field not in data:
            # Return an error response if any required field is missing
            return f'Error: Missing required field - {field}', 400

    # Append the received log data to the in-memory logs list
    logs.append(data)

    # Return a success response after ingesting the logs
    return 'Logs ingested successfully'

if __name__ == '__main__':
    # Run the Flask app on port 3000
    app.run(port=3000)
