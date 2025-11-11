import time

tasksList = []

def add_task():
    time.sleep(2)
    print("\n# ADD A NEW TASK #")
    taskTitle = input("Title: ").strip()
    taskPriority = input("Priority (high / medium / low): ").strip().lower()
    valid_priorities = ["high", "medium", "low"]
    
    if taskPriority not in valid_priorities:
        print("Invalid priority. Defaulting to 'medium'.")
        taskPriority = "medium"
    
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
 
def mark_task_done():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to mark done: "))
        tasksList[task_num - 1]["status"] = "done"
        time.sleep(2)
        print("\nTask updated successfully!\n")
    except (ValueError, IndexError):
        print("Invalid number.")
#TODO: add ENUM: in progress, done
        
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
