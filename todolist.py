# Importing necessary libraries
import sys

# Defining the Task class to hold each task's data
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.description}"

# Defining the ToDoList class to manage the list of tasks
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task added: '{description}'")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\n--- To-Do List ---")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self, index, new_description):
        try:
            self.tasks[index - 1].description = new_description
            print(f"Task {index} updated to: '{new_description}'")
        except IndexError:
            print("Invalid task number.")

    def mark_task_completed(self, index):
        try:
            self.tasks[index - 1].mark_completed()
            print(f"Task {index} marked as completed.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, index):
        try:
            task = self.tasks.pop(index - 1)
            print(f"Task '{task.description}' deleted.")
        except IndexError:
            print("Invalid task number.")

# Defining the main function to interact with the user
def main():
    to_do_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            description = input("Enter the task description: ")
            to_do_list.add_task(description)

        elif choice == '2':
            to_do_list.view_tasks()

        elif choice == '3':
            to_do_list.view_tasks()
            try:
                task_num = int(input("Enter the task number to update: "))
                new_description = input("Enter the new task description: ")
                to_do_list.update_task(task_num, new_description)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == '4':
            to_do_list.view_tasks()
            try:
                task_num = int(input("Enter the task number to mark as completed: "))
                to_do_list.mark_task_completed(task_num)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == '5':
            to_do_list.view_tasks()
            try:
                task_num = int(input("Enter the task number to delete: "))
                to_do_list.delete_task(task_num)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == '6':
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from the menu.")

# Run the program
if __name__ == "__main__":
    main()
