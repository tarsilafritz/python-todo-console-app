import time

tasksList = []

def add_task():
    time.sleep(2)
    print("\n# ADD A NEW TASK #")
    taskTitle = input("Title: ").strip()
    taskPriority = input("Priority (high / medium / low): ").strip().lower()
    taskStatus = input("Status (pending / in progress / done): ").strip().lower()    
    
    valid_priorities = ["high", "medium", "low"]
    valid_statuses = ["peding", "in progress", "done"]

    if taskPriority not in valid_priorities:
        print("Invalid priority. Defaulting to 'medium'.")
        taskPriority = "medium"

    if taskStatus not in valid_statuses:
        print("Invalid status. Defaulting to 'pending'.")
        taskStatus = "pending"
    
    # Create a dictionary for the new task
    task = {
        "title": taskTitle,
        "status": taskStatus,
        "priority": taskPriority
    }
    
    # Add it to the list
    tasksList.append(task)
    time.sleep(2)
    print(f"\nTask '{taskTitle}' - {taskPriority} ({taskStatus}) added successfully!")
 
def update_status():
    time.sleep(2)
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to update status: "))
        valid_statuses = ["peding", "in progress", "done"]
        new_status = input("Enter new status (pending / in progress / done): ").strip().lower()
        
        if new_status not in valid_statuses:
            print("Invalid status. No changes made.")
            return
        
        tasksList[task_num - 1]["status"] = new_status
        time.sleep(1)
        print(f"\nTask '{tasksList[task_num - 1]['title']}' updated to '{new_status} successfully!\n")
    except (ValueError, IndexError):
        print("Invalid number.")
        
def view_tasks():
    print("\n# TASKS LIST #")
    if not tasksList:
        print("No tasks yet.")
        return
    else:
        for i, task in enumerate(tasksList, start=1):
            title = task.get("title", "<no title>")
            priority = task.get("priority", "<no priority>")
            status = task.get("status", "<no status>")
            print(f"{i}. {title} - {priority} ({status})")

def remove_task():
    print("\n# DELETE TASK#")
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        removed = tasksList.pop(task_num - 1)
        print(f"Removed task '{removed['title']}'")
    except (ValueError, IndexError):
        print("Invalid task number.")
  
#def save_tasks():

#def load_tasks():
