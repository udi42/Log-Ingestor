# Log Ingestor And Query Implementation

## Installation
1. Clone the repository using **git clone.** Navigate to the project directory  and install the dependencies using **pip.** We need **Flask and elasticsearch.**
>pip install -r log_ingestor/requirements.txt
>
>pip install -r query_interface/requirements.txt

## Log Ingestor
1. Navigate to the log_ingestor directory i.e **cd log_ingestor** 
2. Run the Python file in one cmd.
>python app.py
3. Now, insert the log using a tool like **curl or Postman** 

- If it is cmd.
```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "level": "error",
    "message": "Failed to connect to DB",
    "resourceId": "server-1234",
    "timestamp": "2023-09-15T08:00:00Z",
    "traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
        "parentResourceId": "server-0987"
    }
}' http://localhost:3000/ingest
```

- If it is powershell.
```powershell
$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    "level" = "error"
    "message" = "Failed to connect to DB"
    "resourceId" = "server-1234"
    "timestamp" = "2023-09-15T08:00:00Z"
    "traceId" = "abc-xyz-123"
    "spanId" = "span-456"
    "commit" = "5e5342f"
    "metadata" = @{
        "parentResourceId" = "server-0987"
    }
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:3000/ingest -Method Post -Headers $headers -Body $body
```

## Query Ingestor
1. Navigate to the log_ingestor directory i.e **cd query_ingestor**
2. Run the Python file in another cmd.
>python app.py

3. The query interface will be accessible at http://localhost:5000.

## Perform Searches
- Enter search queries in the provided input field. For eg: in search box type **Failed to connect**
- Click the "Search" button to execute the search.
