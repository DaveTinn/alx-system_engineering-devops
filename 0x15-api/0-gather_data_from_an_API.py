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

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    employee_response = requests.get(url)
    response_to_json = employee_response.json()
    employee_name = response_to_json.get("name")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos_response = requests.get(url)
    todos_to_json = todos_response.json()
    total_tasks = len(todos_to_json)

    num_of_tasks_completed = 0
    todo_list = ""

    for todo in todos_to_json:
        if todo.get("completed") is True:
            num_of_tasks_completed += 1
            todo_list += "\t " + todo.get("title") + "\n"
    print("Employee {} is done with tasks({}/{}):".format(
           employee_name, num_of_tasks_completed, total_tasks))

    print(todo_list[:-1])


if __name__ == "__main__":
    get_employee_info(sys.argv[1])
