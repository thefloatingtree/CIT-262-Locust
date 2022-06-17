# setup locust tests


from locust import HttpUser, task


class UserBehavior(HttpUser):

    @task
    def index(self):
        self.client.get("/")

    @task
    def index(self):
        self.client.get("/api/ping")
    
    @task
    def login(self):
        self.client.post("/api/login", json={"username": "thefloatingtree@gmail.com", "password": "oatmeal"})
