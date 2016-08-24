import random
from locust import TaskSet, task
from pyquery import PyQuery


class SitemapSwarmer(TaskSet):
    def on_start(self):
        request = self.client.get("/sitemap.xml")
        pq = PyQuery(request.content, parser='html')
        self.sitemap_links = []
        for loc in pq.find('loc'):
            self.sitemap_links.append(PyQuery(loc).text())

    @task(10)
    def load_page(self):
        url = random.choice(self.sitemap_links)
        self.client.get(url)
