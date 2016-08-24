from locust import HttpLocust, TaskSet
from sitemapSwarmer import SitemapSwarmer


class SwarmerTasks(TaskSet):
    tasks = {
        SitemapSwarmer: 10,
    }


class Swarmer(HttpLocust):
    task_set = SwarmerTasks
    host = "localhost"
    min_wait = 20 * 1000
    max_wait = 600 * 1000
