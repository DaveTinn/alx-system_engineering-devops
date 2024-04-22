#!/usr/bin/python3
"""
A Python script for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def get_employee_info(id):
    """
    Function to get information about a to-do list progress

    Arguments:
        id (int): the employee ID.
    """
    employee = {}

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    employee_response = requests.get(url)
    response_to_json = employee_response.json()
    employee_name = response_to_json.get("name")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos_response = requests.get(url)
    todos_to_json = todos_response.json()

    employee["name"] = employee_name
    employee["todos"] = todos_to_json

    return employee


def show_employee_info(info):
    if not info:
        print("Employee not found")
        return

    employee_name = info.get("name")
    tasks_completed = [todo for todo in info["todos"] if todo["completed"]]
    all_tasks = len(info["todos"])
    num_of_tasks_completed = len(tasks_completed)

    print("Employee {} is done with tasks({}/{}):".format(
           employee_name, num_of_tasks_completed, all_tasks))
    for todo in tasks_completed:
        print("\t{}".format(todo["title"]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py [id]")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_info = get_employee_info(employee_id)
    show_employee_info(employee_info)
