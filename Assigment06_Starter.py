# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# David Grunloh,5.12.2021,Modified code to complete assignment 6
# David Grunloh,5.12.2021,Added code to functions in processor class
# David Grunloh,5.13.2021,Added code to functions in IO Class
# David Grunloh,5.13.2021,Altered main to utilize functions
# David Grunloh,5.14.2021,Modified code to help with user experience
# David Grunloh,5.14.2021,Modified code to better document functions
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strStatus = ""  # Captures the status of an processing functions
# objFile = None   # An object that represents a file
# dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
# strTask = ""  # Captures the user task data
# strPriority = ""  # Captures the user priority data



# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """Adds data to the list

        :param task: (string) with the task
        :param priority: (string) with the priority
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = {"Task": task, "Priority": priority}
        list_of_rows.append(row)
        print("Current Data in table:")
        # for dicRow in lstTable:
        #     print(dicRow)
        print("*******************************************")
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """Removes data from list

        :param task: (string) with the task
        :param list_of_rows: (list) of dictionary rows
        :return: list_of_rows: (list) of dictionary rows
        """
        item_removed = False  # Creating a boolean Flag
        row_number = 0
        for row in list_of_rows:
            task, priority = dict(row).values()
            if task == strKeyToRemove:
                del list_of_rows[row_number]
                item_removed = True
            row_number += 1
            # end if
        # end for loop
        # Step 5b - Update user on the status
        if (item_removed == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """Writes list data to the file

        :param file_name: (string) with name of file:
        :param list_of_rows: list_of_rows: (list) of dictionary rows
        :return: list_of_rows: list_of_rows: (list) of dictionary rows
        """
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """Allows user to input a new task and priority

        :return: task: (string) with the task
        :return: priority: (string) with the priority
        """
        task = str(input("What is the task? - ")).strip()
        priority = str(input("What is the priority? [high|low] - ")).strip()
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """Allows user to input a task to remove

        :return: task: (string) with the task
        """
        task = input("Which TASK would you like removed? - ")
        return task

# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        # Complete
        # IO.input_press_to_continue(strStatus) # Removed for usability
        data = IO.input_new_task_and_priority()
        Processor.add_data_to_list(task=data[0], priority=data[1], list_of_rows=lstTable)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here
        # Complete
        # IO.input_press_to_continue(strStatus)
        strKeyToRemove = IO.input_task_to_remove()
        Processor.remove_data_from_list(task=strKeyToRemove, list_of_rows=lstTable)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here!
            # Complete
            # IO.input_press_to_continue(strStatus) # Removed for usability
            Processor.write_data_to_file(file_name=strFileName, list_of_rows=lstTable)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # TODO: Add Code Here!
            # Complete
            # IO.input_press_to_continue(strStatus) # Removed for usability
            Processor.read_data_from_file(strFileName, lstTable)  # read file data
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        IO.input_press_to_continue(strStatus)
        break   # and Exit
