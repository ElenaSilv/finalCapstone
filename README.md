# Capstone Project - Task Manager
This is the final project in the HyperionDev SE bootcamp (Nov 2023 cohort).
## Description
This programme allows a team to list and manage their tasks.

It makes use of Loops, Lists, Dictionaries and Functions. 
## How to Use
### Table of Contents
Login section

Menu:
* R - Registering a user
* A - Adding a task
* VA - View all tasks
* VM - View my task
* GR - Generate reports
* DS - Display statistics
* E - Exit

The first thing you will be asked to do is to enter your username and password.
You can use 'admin' and 'password' for the first login. 
![Image of login section](https://raw.githubusercontent.com/ElenaSilv/finalCapstone/main/login%20section.JPG)

Once inside the programme, you will be able to choose what to do next by inputing one or two letters:
![image of main menu](https://raw.githubusercontent.com/ElenaSilv/finalCapstone/main/menu.JPG)

By choosing **R** you will be asked to input a new username and a new password. The new user will be added to user.txt   
  
By choosing **A** you will be asked to input:
* The name of the user assigned to the task
* The title of the task
* The task description
* The task due date
The tasks will be added to tasks.txt      
  
By choosing **VA** you will be able to see you the tasks added to tasks.txt
  
By choosing **VM** the programme will list all the tasks assigned to the logged in user. You will then be able to choose a task and:
* Mark it as complete
* Edit the user it's assigned to
* Edit its due date
    
By choosing **GR** the programme will generate two different reports:     
* A **Task overview report** (task_overview.txt) listing:
  * The total number of tasks
  * The number of complete tasks
  * The number of incomplete
  * The number of overdue tasks
  * The percentage of incomplet tasks
  * The percentage of overdue tasks
* A **User overview report** (user_overview.txt) listing:
  * The total number of users registered
  * The percentage of tasks assigned to them
  * The percentage of tasks completed by them
  * The percentage of their incomplete tasks
  * The percentage of their overdue tasks

**DS** can only be accessed by the admin and displays the statistics by accessing the generated reports. If the reports have not been generated yet, the programme will create them.      

By choosing **E** you will exit the programme.   

## Credits
Project created by HyperionDev and modified by me, Elena Silvestri Cecinelli. 
