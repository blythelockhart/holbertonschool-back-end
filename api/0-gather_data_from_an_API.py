#!/usr/bin/python3
""" Returns information about a given employee's TODO list progress. """
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = int(sys.argv[1])
    emp = requests.get(url + "users/{}".format(emp_id)).json()
    todo = requests.get(url + "todos", params={"userId": emp_id}).json()
    done = [task for task in todo if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(emp.get("name"),
                                                          len(done),
                                                          len(todo)))
    for task in done:
        print("\t {}".format(task.get("title")))
