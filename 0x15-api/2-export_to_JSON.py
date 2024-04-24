#!/usr/bin/python3
"""
Python Module
"""

import json
import requests
import sys


def GetEmployee_Info(id):
    """
    Defines the function export data in JSON format,

    Argumrnts:
        id (int): The employee ID.
    """

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    employee_response = requests.get(url)
    response_to_json = employee_response.json()
    employee_name = response_to_json("name")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos_response = requests.get(url)
    todos_to_json = todos_response.json()

    todo_list = []

    for to_do in todos_to_json:
        todo_to_dict = {}
        todo_to_dict["task"] = to_do.get("title")
        todo_to_dict["completed"] = to_do.get("completed")
        todo_to_dict["username"] = employee_name
        todo_list.append(todo_to_dict)

    todos_response = {"{}".format(id): todo_list}

    filename = "{}.json".format(id)
    with open(filename, "w") as json_file:
        json.dump(todos_response, json_file)


if __name__ == "__main__":
    GetEmployee_Info(sys.argv[1])
