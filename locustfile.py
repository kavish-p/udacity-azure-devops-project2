from locust import HttpUser, task

class PredictionModelUser(HttpUser):
  @task
  def predict(self):
    post_data = {
      "CHAS":{"0":0},
      "RM":{"0":6.575},
      "TAX":{"0":296.0},
      "PTRATIO":{"0":15.3},
      "B":{"0":396.9},
      "LSTAT":{"0":4.98}
    }
    self.client.post("predict",json=post_data)