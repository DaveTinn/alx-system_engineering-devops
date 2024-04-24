#!/usr/bin/python3
"""
A Python script to export data in CSV format.
"""

import csv
import requests
import sys


def GetEmployee_Info(id):
    """
    Function to import data in CSV format

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

    with open(filename, "a") as csv_file:
        for to_do in todos_to_json:
            completed_tasks = to_do.get("completed")
            task_title = to_do.get("title")
            csv_data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                        id, employee_name, completed_tasks, task_title)
            csv_file.write(csv_data)


if __name__ == "__main__":
    GetEmployee_Info(sys.argv[1])
