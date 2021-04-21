======================
SelectStar_SV_Solution
======================


.. image:: https://img.shields.io/pypi/v/selectstar_sv_solution.svg
        :target: https://pypi.python.org/pypi/selectstar_sv_solution

.. image:: https://img.shields.io/travis/sugix/SelectStar_SV_Solution.svg
        :target: https://travis-ci.org/sugix/SelectStar_SV_Solution

.. image:: https://readthedocs.org/projects/selectstar-sv-solution/badge/?version=latest
        :target: https://selectstar-sv-solution.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/sugix/SelectStar_SV_Solution/shield.svg
     :target: https://pyup.io/repos/github/sugix/SelectStar_SV_Solution/
     :alt: Updates



Solution submitted by SugiV for Select Star TLM take home exercise


* Free software: Apache Software License 2.0

* Documentation: https://selectstar-sv-solution.readthedocs.io.

Features
--------

* The input file has underscore as special character to serialize the shortest prefixes.
* The solution contains bruteforce grouping and another way of grouping using affinity propogation and distance.
* The solution only works for underscore as delimited for now.
* APIs are exposed using fastapi. (Code comments are yet to be added)
* Frontend is simple Vue app to show the grouping done via bruteforce approach.

Pre-Req

* Checkout the project and enter the project directory.
* Install poetry using curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
* poetry install --no-root --no-dev
* Activate poetry virtual environment in all your terminal where you will run your backend server and serve frontend resources.
* source $(poetry env info --path)/bin/activate - to activate poetry virtual env.

Usage

* Run command uvicorn src.app.main:app --reload from the root. The above will start the backend.
* You can visit 127.0.0.1:8000/docs after application startup finishes and interactively try. On start-up, the app will process input file.
* You can issue a POST request so that affinity propogation based grouping will run async.
* Issue a GET request to / (Intelligent Grouping Status) to know the count of dictionary. If the count is not zero then the above said affinity based grouping has finished.
* Issue a GET request to /intelligent_group to see how the names are grouped.

* Open a new terminal for the same project folder.
* cd into frontend folder
* Install latest node and install yarn globally.
* Type yarn install
* Type yarn dev
* You can hit http://localhost:3001/ to view the frontend VUE app calling the GET api of bruteforce grouping.


