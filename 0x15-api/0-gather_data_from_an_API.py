#!/usr/bin/pyhton3
"""API for todo lists of employees"""


import requests
import sys


def get_employee_info(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    response.raise_for_status()
    return response.json().get('name')


def get_completed_tasks(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}/todos"

    response = requests.get(url)
    response.raise_for_status()
    tasks = response.json()

    done_tasks = [task for task in tasks if task.get('completed')]
    return tasks, done_tasks


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        employee_name = get_employee_info(employee_id)
        tasks, done_tasks = get_completed_tasks(employee_id)

        total_tasks = len(tasks)
        done_task_count = len(done_tasks)

        print(f"Employee {employee_name} is done with tasks "
              f"({done_task_count}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t{task.get('title')}")

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
