tasksList = []

def add_task():
    print("\n# ADD A NEW TASK #")
    taskTitle = input("Title: ").strip()
    taskStatus = input("Status: ").strip()
    
# TODO: colocar status pre-definido como pending
    
    # Create a dictionary for the new task
    task = {
        "title": taskTitle,
        "status": taskStatus
    }
    
    # Add it to the list
    tasksList.append(task)
    print(f"Task '{taskTitle}' ({taskStatus}) added successfully!")
    
def view_tasks():
    print("\n# TASKS LIST #")
    if not tasksList:
        print("No tasks yet.")
        return
    else:
        for i, task in enumerate(tasksList, start=1):
            title = task.get("title", "<no title>")
            status = task.get("status", "<no status>")
            print(f"{i}. {title} ({status})")

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
