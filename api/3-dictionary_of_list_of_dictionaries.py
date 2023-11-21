#!/usr/bin/python3
""" Returns information about a given employee's TODO list progress. """
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    emps = requests.get(url + "users/").json()
    todo = requests.get(url + "todos").json()
    data = {}
    for emp in emps:
        emp_todo = [task for task in todo if task.get("userId") == emp.get("id")]
        emp_todo = [{"username": emp.get("username"),
                     "task": task.get("title"),
                     "completed": task.get("completed")}
                    for task in emp_todo]
        data[str(emp.get("id"))] = emp_todo
    new_file = "todo_all_employees.json"

    with open(new_file, mode="w") as filename:
        json.dump(data, filename)
