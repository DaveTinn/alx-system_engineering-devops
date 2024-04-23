#!/usr/bin/python3
"""
A Python script to export data in CSV format.
"""

import requests
import sys


def export_data(id):
    """
    Function to export data in CSV format

    Arguments:
        id (int): the employee ID.
    """

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    employee_response = requests.get(url)
    response_to_json = employee_response.json()
    employee_name = response_to_json["name"]

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos_response = requests.get(url)
    todos_to_json = todos_response.json()
    total_tasks = len(todos_to_json)

    num_of_task_completed = 0
    todo_list = ""

    filename = "{}.csv".format(id)

    with open(filename, "a") as fn:
        for todo in todos_to_json:
            completed_tasks = todo.get("completed")
            task_title = todo.get("title")
            csv_data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                        id, employee_name, completed_tasks, task_title)
            fn.write(csv_data)


if __name__ == "__main__":
    export_data(sys.argv[1])
