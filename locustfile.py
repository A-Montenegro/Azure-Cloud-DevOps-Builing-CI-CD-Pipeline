from locust import HttpUser, between, task

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_predict_endpoint(self):
        headers = {'Content-Type': 'application/json'}
        data = '{"CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98}}'
        self.client.post("/predict", headers=headers, data=data)

