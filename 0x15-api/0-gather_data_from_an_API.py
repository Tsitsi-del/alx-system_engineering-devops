#!/usr/bin/python3
"""Rest API for todo lists of employees"""

import sys
import requests


if __name__ == "__main__":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get("name")

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    tasks_done = []

    for t in tasks:
        if t.get('completed'):
            tasks_done.append(t)
            done += 1

    print("Employee {} is done with tasks({}/ {}):"
          .formart(employeeName, done, len(tasks)))

    for t in tasks_done:
        print("\t {}".format(t.get('title")))
