# setup locust tests
from locust import HttpUser, task


class UserBehavior(HttpUser):

    @task
    def index(self):
        self.client.get("/")
    
    @task
    def login(self):
        self.client.post("/login", json={ "userName": "thefloatingtree@gmail.com", "password": "696969Aa@7" })
