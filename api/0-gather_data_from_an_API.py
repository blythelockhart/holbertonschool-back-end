#!/usr/bin/bash/python3
import sys
import requests

def get_todo_progress(employee_id):
    # API endpoint
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        # Make a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            todo_list = response.json()

            # Get employee name
            employee_name = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()['name']

            # Calculate the number of completed tasks and total tasks
            completed_tasks = [task for task in todo_list if task['completed']]
            num_completed_tasks = len(completed_tasks)
            total_tasks = len(todo_list)

            # Display the result in the required format
            print(f'Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):')
            
            # Display titles of completed tasks
            for task in completed_tasks:
                print(f'\t{task["title"]}')

        else:
            # Display an error message if the request was not successful
            print(f'Error: Unable to fetch data for employee {employee_id}. Status code: {response.status_code}')

    except requests.RequestException as e:
        # Display an error message if an exception occurs
        print(f'Error: {e}')

if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print('Usage: python3 script_name.py employee_id')
        sys.exit(1)

    # Get the employee ID from the command-line arguments
    employee_id = int(sys.argv[1])

    # Call the function with the provided employee ID
    get_todo_progress(employee_id)

