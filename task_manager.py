# This program hepls a small business manage tasks assigned to members of the team. It does the following: 
#1. uses data stored in user.txt to validate and login users
#2. Allows only admins to register new users and see total number of users as well as total number of tasks
#3. uses data stored in tasks.txt to know tasks asigned to different users
#4. Allows all users to create tasks which is stored in tasks.txt
# Instructions were provided to aid in the execution of this program and I left the instructions to serve as part of documentation. 
 
#=====importing libraries===========

from datetime import date, datetime

#===== function I created =========
#This function ensures the right date format is entered by user and prevents a ValueError from wrong date format input

def check_date(due_date):
    due_date_list = due_date.split('-')
    str_date=''.join(due_date_list)
    is_date_formatted = False
        
    while (str_date.isnumeric() and is_date_formatted)  is False :
        
        if str_date.isnumeric() is True:

            try:
                due_date_obj = datetime.strptime(due_date, "%d-%m-%Y")   #this line converts the string into a date object. I used dd-mm-yyyy, because it is easy for users to type in this format
                due_date_formatted = due_date_obj.strftime("%d %b %Y")   #this line formats the date object into the format requested in the capstone project
                is_date_formatted = True
                
            except ValueError as ve:
                print(f'You entered the wrong date format.')
                due_date = input('Please enter the due date of the task in the right date format eg 30-12-2023: ')
                due_date_list = due_date.split('-')
                str_date=''.join(due_date_list)

        else:
            
            due_date = input('Please enter the due date correctly eg 30-12-2023: ')
            input_date_list = due_date.split('-')
            str_date =''.join(input_date_list)
    
    return due_date_formatted


#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
username_input = input('Please enter your username: ').strip(' ').lower()
password_input = input('Please enter your password: ')
f = open('user.txt', 'r+') # Opens the file
data = f.readlines()
username = ""
password = ""


while (username_input == username or password_input == password) is False:
    for line in data:
        data_line = line.split(', ')        
        username = data_line[0]
        
        password = data_line[-1].strip('\n')
        
       

        if (username_input == username and password_input == password):
            break

    else:
            
        print('Password or Username is incorrect')
        username_input = input('Please enter your username: ')
        password_input = input('Please enter your password: ')

f.close()


while True:

#-----------------------------This section creates a menu for the user who is admin ---------------------------------------#
    if username_input == 'admin':
        
        #presenting the menu to the user          
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    d  - Display statistics
    e - Exit
    : ''').lower()

    
        if menu == 'r':
            pass
            '''In this block you will write code to add a new user to the user.txt file
            - You can follow the following steps:
                - Request input of a new username
                - Request input of a new password
                - Request input of password confirmation.
                - Check if the new password and confirmed password are the same.
                - If they are the same, add them to the user.txt file,
                - Otherwise you present a relevant message.'''
        
# to prevent duplicate registration of the same user, I modified this block to check if entered username already exists.             
                                  
            f = open('user.txt', 'r+')
            data_users = f.readlines()

            list_of_usernames = []
            
            for line in data_users:
                words = line.split(', ')
                list_of_usernames.append(words[0])

            f.close()

            reg_user = input('Please enter a user\'s username: ').strip(' ').lower()

        #The while loop below prevents duplicate registration of the same username    
            while reg_user in list_of_usernames:
                reg_user = input('Username already exists. Please register the new user with a different username: ').strip(' ').lower()

            else:
                reg_password = input('Please enter user\'s password: ')
                f = open('user.txt', 'a+') 
            
                f.write('\n'+ reg_user +', '+ reg_password)
                
                print('User registered! Good job!\n')

            f.close()
        

        elif menu == 'a':
            pass
            '''In this block you will put code that will allow a user to add a new task to task.txt file
            - You can follow these steps:
                - Prompt a user for the following: 
                    - A username of the person whom the task is assigned to,
                    - A title of a task,
                    - A description of the task and 
                    - the due date of the task.
                - Then get the current date.
                - Add the data to the file task.txt and
                - You must remember to include the 'No' to indicate if the task is complete.'''
            
            username_entered = input('Please enter the username of the person the task is assigned to: ').strip(' ').lower()

            # I added the requirement stated below to make the program more robust: 
            # requirement>> if username_enter exists in the user.txt file, proceed. Otherwise display an error message and return to main menu
            
            f = open('user.txt', 'r+') 

            data = f.readlines()

            list_of_names = []

            for line in data:
                a = line.split(',')
                list_of_names.append(a[0])

            f.close()

            if username_entered in list_of_names:                

                title_task = input('Please enter the title of the task: ')

                desc_task = input('Please enter the description of the task: ')

                due_date = input('Please enter the due date of the task in format dd-mm-yyyy eg 30-12-2023: ')

                due_date_correct = check_date(due_date) #this line calls the check_date() function I created to validate and format the date entered by user
                
                current_date = date.today()
                
                current_date_formatted = current_date.strftime("%d %b %Y")

                is_task_completed = 'No'

                f = open('tasks.txt', 'a+') 
                
                f.write(f'{username_entered}, {title_task}, {desc_task}, {current_date_formatted}, {due_date_correct}, {is_task_completed}\n')
                
                print('You have added a Task successfully. Good job!\n')

            else:
                print('Username entered does not exist in the user.txt file. Please try again with a correct username\n')

            f.close()

        elif menu == 'va':
            pass
            '''In this block you will put code so that the program will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
                - Read a line from the file.
                - Split that line where there is comma and space.
                - Then print the results in the format shown in the Output 2 
                - It is much easier to read a file using a for loop.'''
            # For admin,  I added a task_counter that displays the total number of tasks after displaying the details of the tasks
            # This is because admin already has privileges to access display statistics

            f = open('tasks.txt', 'r+') 
            
            data_tasks = f.readlines()

            task_counter = 0

            for line in data_tasks:

                details = line.split(', ')
            
                print('Task: \t\t\t'+ str(details[1])+'\nAssigned To: \t\t'+str(details[0])+
                        '\nDate Assigned: \t\t'+str(details[3])+ '\nDue Date: \t\t'+ str(details[4])+
                        '\nTask Complete?: \t'+str(details[5]).strip("\n")+'\nTask Description: \n' + str(details[2]) + '\n')
                
                task_counter += 1
            
            print(f'A total of {task_counter} tasks are in the task manager. The details are displayed above. \n')
                
            f.close()
    
        elif menu == 'vm':
            pass
            '''In this block you will put code the that will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
                - Read a line from the file
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same as the username you have
                read from the file.
                - If they are the same print it in the format of Output 2 in the task PDF'''
            # I added count, to display the total number of tasks assigned to the logged in user

            f = open('tasks.txt', 'r+') 

            data_tasks = f.readlines()

            count = 0

            for line in data_tasks:

                details = line.split(', ')

                if str(details[0]).lower() == username_input:
                    print('Task: \t\t\t'+ str(details[1])+'\nAssigned To: \t\t'+str(details[0])+
                        '\nDate Assigned: \t\t'+str(details[3])+ '\nDue Date: \t\t'+ str(details[4])+
                        '\nTask Complete?: \t'+str(details[5]).strip("\n")+'\nTask Description: \n' + str(details[2]) + '\n')
                    
                    count += 1
            
            print(f'You have a total of {count} tasks and the details of each task is shown above\n')
                    
                
            f.close()

        elif menu =='d':
            pass
            
            '''display statics When this menu option is selected, the total number of tasks and the total number of users should be
            displayed in a user-friendly manner.

            '''
            total_number_of_tasks=0

            total_number_of_users = 0

            f = open('user.txt', 'r+') 

            data_user = f.readlines()

            
            for line in data_user:
                total_number_of_users += 1     

            print(f'Total number of users in Task Manager is: {total_number_of_users}')

            f.close()

            f = open('tasks.txt', 'r+') 

            data_tasks = f.readlines()

            for line in data_tasks:
                total_number_of_tasks += 1 

            print(f'Total number of tasks in Task Manager is: {total_number_of_tasks}\n')

            f.close()




        elif menu == 'e':
            print('Goodbye!!!')
            exit()       


        else:
            print("You have made a wrong choice, Please Try again. \n")



#--------------This section creates a menu for users that are NOT admin ---------------------------------------#
    else:
        menu = input('''Select one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()
        

        if menu == 'a':
            pass
            '''In this block you will put code that will allow a user to add a new task to task.txt file
            - You can follow these steps:
                - Prompt a user for the following: 
                    - A username of the person whom the task is assigned to,
                    - A title of a task,
                    - A description of the task and 
                    - the due date of the task.
                - Then get the current date.
                - Add the data to the file task.txt and
                - You must remember to include the 'No' to indicate if the task is complete.'''
            
            username_enter = input('Please enter the username of the person the task is assigned to: ').strip(' ').lower()

            #I added this requirement: if username_enter exists in the user.txt file, proceed. Otherwise display an error message and return to main menu
            
            f = open('user.txt', 'r+') 

            data = f.readlines()

            list_of_names = []

            for line in data:
                a = line.split(',')
                list_of_names.append(a[0])

            f.close()

            if username_enter in list_of_names:                

                title_task = input('Please enter the title of the task: ')

                desc_task = input('Please enter the description of the task: ')

                due_date = input('Please enter the due date of the task in format dd-mm-yyyy eg 30-12-2023: ')

                due_date_correct = check_date(due_date) #this line calls the check_date() function I created to validate and format the date entered by user
                
                current_date = date.today()
                
                current_date_formatted = current_date.strftime("%d %b %Y")

                is_task_completed = 'No'

                f = open('tasks.txt', 'a+') 
                
                f.write(f'{username_enter}, {title_task}, {desc_task}, {current_date_formatted}, {due_date_correct}, {is_task_completed}\n')
                
                print('You have added a Task successfully. Good job!\n')

            else:
                print('Username entered does not exist in the user.txt file. PLease try again with a correct username\n')

            f.close()

        elif menu == 'va':
            pass
            '''In this block you will put code so that the program will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
                - Read a line from the file.
                - Split that line where there is comma and space.
                - Then print the results in the format shown in the Output 2 
                - It is much easier to read a file using a for loop.'''
            f = open('tasks.txt', 'r+') 

            data_tasks = f.readlines()

            for line in data_tasks:
                details = line.split(', ')
            
                print('Task: \t\t\t'+ str(details[1])+'\nAssigned To: \t\t'+str(details[0])+
                        '\nDate Assigned: \t\t'+str(details[3])+ '\nDue Date: \t\t'+ str(details[4])+
                        '\nTask Complete?: \t'+str(details[5]).strip("\n")+'\nTask Description: \n' + str(details[2]) + '\n')
                
            f.close()
    
        elif menu == 'vm':
            pass
            '''In this block you will put code the that will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
                - Read a line from the file
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same as the username you have
                read from the file.
                - If they are the same print it in the format of Output 2 in the task PDF'''
            f = open('tasks.txt', 'r+') 

            data_tasks = f.readlines()

            count = 0

            for line in data_tasks:
                details = line.split(', ')
                

                if str(details[0]).lower() == username_input:

                    print('Task: \t\t\t'+ str(details[1])+'\nAssigned To: \t\t'+str(details[0])+
                        '\nDate Assigned: \t\t'+str(details[3])+ '\nDue Date: \t\t'+ str(details[4])+
                        '\nTask Complete?: \t'+str(details[5]).strip("\n")+'\nTask Description: \n' + str(details[2]) + '\n')
                    
                    count +=1
            
            
            
            if count == 0:
                print('\nNo Tasks have been assigned to you yet. \n')

            else:
                print(f'You have a total of {count} tasks and the details of each task is shown above.\n')

                
            
            f.close()


        elif menu == 'e':
            print('Goodbye!!!')
            exit()


        else:
            print("You have made a wrong choice, Please Try again. \n")
