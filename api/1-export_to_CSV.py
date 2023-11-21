#!/usr/bin/python3
""" Returns information about a given employee's TODO list progress. """
import csv
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = int(sys.argv[1])
    emp = requests.get(url + "users/{}".format(emp_id)).json()
    todo = requests.get(url + "todos", params={"userId": emp_id}).json()
    new_file = "{}.csv".format(emp_id)
    with open(new_file, mode="w", newline='') as filename:
        fieldnames = ['USER_ID',
                      'USERNAME',
                      'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(filename, fieldnames=fieldnames)

        for task in todo:
            writer.writerow({
                'USER_ID': task.get("userId"),
                'USERNAME': emp.get("username"),
                'TASK_COMPLETED_STATUS': str(task.get("completed")),
                'TASK_TITLE': task.get("title")})
