from fastapi.testclient import TestClient
from main import app  # assuming your FastAPI app is defined in a file called main.py
import json
from pprint import pprint

client = TestClient(app)

def test_calculate_reward():
    # Define test payloads for multiple contest IDs
    test_payloads = [
        {"contest_id": 1, "percentage": 0.6},
        {"contest_id": 2, "completion_time": 8}
    ]

    # Initialize an empty list to store response data
    response_data = []

    # Iterate over each test payload
    for payload in test_payloads:
        response = client.post("/calculate_reward/", json=payload)
        assert response.status_code == 200
        
        data = response.json()
        response_data.append(data)

    # Dump all response data to a JSON file
    with open("C:/Users/DELL/Documents/VS/INTERNSHIPS/GENAI/FASTAPI/test_output.json", "w") as file:
        json.dump(response_data, file)
        print("Data dumped.")
    
    pprint(response_data)

test_calculate_reward()
