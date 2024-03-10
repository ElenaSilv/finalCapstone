# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#========importing libraries========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)



#========defining functions========

# 1. Add a new user to user.txt
def reg_user(): 
    '''Add a new user to the user.txt file'''

        # - Request input (new username)
    new_username = input("New Username: ")
    while new_username in username_password.keys():
        print("Username already exists. Please enter a different username.")
        new_username = input("New username: ")
        if new_username not in username_password.keys():
            break
        # - Request input (password)
    new_password = input("New Password: ")   

        # - Request input ( password confirmation)
    confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        # - If they are the same, add them to the user.txt file,
        # - Otherwise you present a relevant message.
    if new_password == confirm_password:
        print("New user added")
        username_password[new_username] = new_password
            
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
            
    else:
        print("Passwords do no match")


# 2. Add a new task to task.txt
def add_task():
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
    '''

    # Request input (user assigned to task) 
    task_username = input("Name of person assigned to task: ")
    while task_username not in username_password.keys():
        task_username = input("User does not exist. Please enter a valid username: ")
        if task_username in username_password.keys():
            break

    # Request input (task title)
    task_title = input("Title of Task: ")
    task_title = task_title.capitalize()

    # Request input (task description)
    task_description = input("Description of Task: ")

    # Request input (task due date)
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")


# 3. View all tasks listed in task.txt
def view_all():
    ''' Reads the task from task.txt file and prints to the console in the 
            format of Output 2 presented in the task pdf (i.e. includes spacing
            and labelling) 
    '''
    
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


# 4. Show all tasks assigned to a user
def view_mine():
    ''' Reads the task from task.txt file and prints to the console in the 
            format of Output 2 presented in the task pdf (i.e. includes spacing
            and labelling)
    '''
    
    while True:
        print("\n\nYour Tasks: ")
        for index, t in enumerate(task_list, 0):
            if t['username'] == curr_user:
                print(f"{index}. Task: {t["title"]}")

        print("-1. Return to Main Menu")

        task_choice = input("Enter the number of the task you want to select, or -1 to return to the main menu.")
        if task_choice == "-1":
            break
        
        try:
            task_index = int(task_choice) - 1
            selected_task = task_list[task_index]

            print("\nSelected Task:")
            print(f"Title: {selected_task['title']}")
            print(f"Assigned to: {selected_task['username']}")
            print(f"Due date: {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Description: {selected_task['description']}")
            print(f"Completed: {'Yes' if selected_task['completed'] else 'No'}")

            if not selected_task['completed']:
                action = input("\nEnter 'C' to mark the task as complete, 'E' to edit the task, or any other key to cancel: " ).upper() 
                if action == "C":
                    selected_task['completed'] == True
                    print("The task has been marked as complete.")
                elif action == "E":
                    new_username = input("Enter a new username or press Enter to keep the same: ")
                    if new_username:
                        selected_task['username'] = new_username

                    new_due_date = input("Enter a new due date (YYYY-MM-DD) or press Enter to keep the same:")
                    if new_due_date:
                        try:
                            selected_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                        except ValueError:
                            print("Invalid date format. Task due date remains unchanged.")
                    print("The task has been edited.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")



            # disp_str = f"Task: \t\t {t['title']}\n"
            # disp_str += f"Assigned to: \t {t['username']}\n"
            # disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            # disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            # disp_str += f"Task Description: \n {t['description']}\n"
            # print(disp_str)


# 5. Generate reports 
def gen_reports():
    # Task overview report
    today = date.today()
    total_tasks = len(task_list)
    completed_tasks = sum(task['completed'] for task in task_list)
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum((task['due_date'].date() < today and not task['completed']) for task in task_list)
    
    if total_tasks > 0:
        incomplete_tasks_percentage = (uncompleted_tasks / total_tasks) * 100
        overdue_task_percentage = (overdue_tasks / total_tasks) * 100
    else: 
        incomplete_tasks_percentage = 0
        overdue_task_percentage = 0

    with open("task_overview.txt", 'w') as file:
        file.write("Task Overview Report\n\n")
        file.write(f"Number of tasks generated and tracked: {total_tasks}\n")
        file.write(f"Total number of complete tasks: {completed_tasks}\n")
        file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        file.write(f"Total number of overdue tasks: {overdue_tasks}\n")
        file.write(f"Percentage of incomplete tasks: {incomplete_tasks_percentage}%\n")
        file.write(f"Percentage of tasks overdue: {overdue_task_percentage}%\n")
    
    with open("user_overview.txt", 'w') as file:
        file.write("User Overview Report\n\n")
        file.write(f"Total number of users registered with task_manager: {len(username_password)}\n")
        file.write(f"Total number of tasks generated and tracked using task_manager: {total_tasks}\n\n")
        for user in username_password:
            user_tasks = [task for task in task_list if task['username']==user]
            num_user_tasks = len(user_tasks)
            num_completed_tasks = sum(task['completed'] for task in user_tasks)
            if num_user_tasks > 0:
                tasks_assigned_percentage = (num_user_tasks / total_tasks) *100
                task_completed_percentage = (num_completed_tasks / num_user_tasks) *100
                task_uncompleted_percentage = ((num_user_tasks - num_completed_tasks) / num_user_tasks) *100
                task_overdue_percentage = (sum((task['due_date'].date() < today and not task['completed']) for task in user_tasks) / num_user_tasks)*100
            else:
                tasks_assigned_percentage = 0
                task_completed_percentage = 0
                task_uncompleted_percentage = 0
                task_overdue_percentage = 0
        

            file.write(f"User: {user}\n")
            file.write(f"Percentage of tasks assigned to {user}: {tasks_assigned_percentage}%\n")
            file.write(f"Percentage of tasks assigned and completed: {task_completed_percentage}%\n")
            file.write(f"Percentage of tasks assigned and not completed: {task_uncompleted_percentage}%\n")
            file.write(f"Percentage of tasks assigned and overdue: {task_overdue_percentage}%\n\n")

    # Printing the reports after generating them
    print("Task Overview Report:")
    with open("task_overview.txt", 'r') as task_file:
        print(task_file.read())

    print("\nUser Overview Report:")
    with open("user_overview.txt", 'r') as user_file:
        print(user_file.read())    


#====Login Section====
        '''This code reads usernames and password from the user.txt file to 
                allow a user to login.
        '''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports 
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
    
    elif menu == 'vm':
        view_mine()             
    
    elif menu == 'gr':
        gen_reports()

    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")