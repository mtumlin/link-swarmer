# link-swarmer
load testing based on [locust.io](www.locust.io), containting a number of diffrent types of tests including; [pyquery](https://pypi.python.org/pypi/pyquery) to parse sitemap.xml for links to visit. The diffrent test cases are splitt up into diffrent files to be more flexible to choose what type of tests you want to run.


##Setup
* `pip install -r requirements.txt`
* `locust -f swarmer.py`
* Browse to the web ui and start a swarm
