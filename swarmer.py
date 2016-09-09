from locust import HttpLocust, TaskSet
from sitemapSwarmer import SitemapSwarmer
from startpageSwarmer import StartpageSwarmer


class SwarmerTasks(TaskSet):
    tasks = {
        SitemapSwarmer: 10,
        StartpageSwarmer: 5,
    }


class Swarmer(HttpLocust):
    task_set = SwarmerTasks
    host = "localhost"
    min_wait = 5 * 1000
    max_wait = 20 * 1000
