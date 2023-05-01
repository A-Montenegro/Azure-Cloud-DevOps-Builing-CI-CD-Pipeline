from locust import HttpUser, task, between, HttpLocust, TaskSet
import json

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    
    @task(1)
    def test_predict(self):
        headers = {'Content-Type': 'application/json'}
        data = {
            "CHAS": {
                "0": 0
            },
            "RM": {
                "0": 6.575
            },
            "TAX": {
                "0": 296.0
            },
            "PTRATIO": {
                "0": 15.3
            },
            "B": {
                "0": 396.9
            },
            "LSTAT": {
                "0": 4.98
            }
        }
        response = self.client.post("/predict", data=json.dumps(data), headers=headers, name="predict")
        expected_response = {"prediction": [20.353731771344123]}
        response_json = response.json()

