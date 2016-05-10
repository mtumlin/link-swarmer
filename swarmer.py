import random
from locust import HttpLocust, TaskSet, task
from pyquery import PyQuery


class SwarmerTasks(TaskSet):
    def on_start(self):
        request = self.client.get("/sitemap.xml")
        pq = PyQuery(request.content, parser='html')
        self.sitemap_links = []
        for loc in pq.find('loc'):
            self.sitemap_links.append(PyQuery(loc).text())

    @task(10)
    def load_page(self):
        url = random.choice(self.sitemap_links)
        request = self.client.get(url)


class Swarmer(HttpLocust):
    task_set = SwarmerTasks
    host = "localhost"
    min_wait = 20 * 1000
    max_wait = 600 * 1000
