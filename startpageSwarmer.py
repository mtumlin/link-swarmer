from locust import TaskSet, task


class StartpageSwarmer(TaskSet):

    @task(10)
    def load_page(self):
        self.client.get("/")
