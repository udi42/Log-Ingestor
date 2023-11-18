from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(['elasticsearch_host:9200'])  # Replace with your Elasticsearch host

@app.route('/')
def index():
    # Render the index.html template when accessing the root endpoint
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_logs():
    # Retrieve the user's search query from the form
    query = request.form.get('query')

    # Implement Elasticsearch query based on the user's input
    # Example: es.search(index='logs', q=query)
    
    # For simplicity, using a dummy list instead of a real Elasticsearch index
    dummy_logs = [
        {"level": "error", "message": "Failed to connect to DB", "resourceId": "server-1234", "timestamp": "2023-09-15T08:00:00Z", "traceId": "abc-xyz-123", "spanId": "span-456", "commit": "5e5342f", "metadata": {"parentResourceId": "server-0987"}},
        {"level": "info", "message": "Connection established", "resourceId": "server-5678", "timestamp": "2023-09-15T09:00:00Z", "traceId": "def-uvw-456", "spanId": "span-789", "commit": "6a7b8cd", "metadata": {"parentResourceId": "server-0123"}}
    ]
    
    # Search for logs that match the user's query
    search_results = [
        log for log in dummy_logs 
        if query.lower() in log["message"].lower() 
        or query.lower() in log["level"].lower() 
        or query.lower() in log["resourceId"].lower() 
        or query.lower() in log["timestamp"].lower()
    ]

    # Render the search_results.html template with the search results
    return render_template('search_results.html', results=search_results)

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(port=5000)
