#!/usr/bin/python3
""" Returns information about a given employee's TODO list progress. """
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    emp = requests.get(url + "users/{}".f(sys.arg[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.arg[1]}).json()
    for task in todo:
        if task.get("completed"):
            done.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".f(emp.get("name"),
                                                     len(done), len(todo)))
    for i in done:
        print("\t {}".f(i))
