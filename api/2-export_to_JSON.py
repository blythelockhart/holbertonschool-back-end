#!/usr/bin/python3
""" Returns information about a given employee's TODO list progress. """
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = int(sys.argv[1])
    emp = requests.get(url + "users/{}".format(emp_id)).json()
    todo = requests.get(url + "todos", params={"userId": emp_id}).json()
    data = {str(emp_id): [{"task": task.get("title"),
                           "completed": task.get("completed"),
                           "username": emp.get("username")}
                           for task in todo]}
    new_file = "{}.json".format(emp_id)

    with open(new_file, mode="w") as filename:
        json.dump(data, filename)
