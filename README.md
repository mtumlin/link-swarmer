# link-swarmer
loadtesting based on [locust.io](www.locust.io) utilizing [pyquery](https://pypi.python.org/pypi/pyquery) to parse sitemap.xml for links to visit


##Setup
* `pip install -r requirements.txt`
* `locust -f swarmer.py`
* Browse to the web ui and start a swarm