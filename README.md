# fastapi-math-examples

[![Build Status](https://travis-ci.com/coding-excercises/fastapi-math-examples.svg?branch=main)](https://travis-ci.com/coding-excercises/fastapi-math-examples) [![DeepSource](https://deepsource.io/gh/coding-excercises/fastapi-math-examples.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/coding-excercises/fastapi-math-examples/?ref=repository-badge) [![Coverage Status](https://coveralls.io/repos/github/coding-excercises/fastapi-math-examples/badge.svg?branch=main)](https://coveralls.io/github/coding-excercises/fastapi-math-examples?branch=main) ![Website](https://img.shields.io/website?down_color=red&down_message=down&up_color=green&up_message=up&url=https%3A%2F%2Ffastapi-math-examples.herokuapp.com%2Fdocs)


## Steps to setup the engineering pipeline and tools

All the below services are free at the time of creating this repo.

1. Create a Github repo.
2. Clone the repo to create a local copy.
3. Based on the programming language, select the unit test framework. In case of Python, pytest and hupothesis are recommended.
4. Create accounts in Travis-CI.com, Coveralls.io, Deepsource.io, Cron-Job.org, Blazemeter.com and Datadog.com
5. Link the Github repo with Travis-Ci. On every commit to master branch, the Travis-CI build job will be triggered.
6. Link the Github repo to Deepsource.io and configure the Deepsource DSN in Travis-CI so that analysis of the code can be done.
7. Link the Github repo to Coveralls.io and configure the Coveralls.io token in Travis-CI so that the code coverage is pushed to Coveralls.
8. Link the Github repo to the applicaiton in Heroku and in the deployment section, set the "Wait for CI to pass before deploy" option. This will ensure that only after a successful build in Travis-CI, will the application be deployed to Heroku.
9. In addition, in Heroku, add the following build packs in the same order - datadog and python. This ensures that the required dependencies are installed.
10. Ensure that the following environment variables are set in Heroku - DD_AGENT_MAJOR_VERSION = 7, DD_API_KEY = [Datadog API Key], DD_LOG_LEVEL = ERROR, DD_PYTHON_VERSION = 3, DD_SITE = [datadoghq.eu or datadoghq.com].
11. In Cron-Job.org, setup a job to call the Heroku application (preferably a "health" endpoint) every 15 minutes. This ensures that the heroku application will not go to "sleep" due to inactivity.
12. Create a performance test script in Blazemeter to load test the Heroku application.
