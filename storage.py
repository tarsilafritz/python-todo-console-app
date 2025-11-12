import json
import os
import tempfile

DATA_FILE = "tasks.json"
tasksList = []

def save_tasks():
    """Write taskList to disk safely"""
    global tasksList
    dir_name = os.path.dirname(os.path.abspath(DATA_FILE)) or "."
    fd, tmp_path = tempfile.mkstemp(dir=dir_name)
    
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as tmp_file:
            json.dump(tasksList, tmp_file, indent=4, ensure_ascii=False)
        os.replace(tmp_path, DATA_FILE)
    except Exception as e:
        try:
            os.remove(tmp_path)
        except Exception:
            pass
        print(f"Error saving tasks: {e}")

def load_tasks():
    """Load taskList from the disk"""
    global tasksList
    
    if not os.path.exists(DATA_FILE):
        tasksList = []
        return
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            tasksList = json.load(file)
        # print("\nTasks loaded successfully!\n")
    except json.JSONDecodeError:
        print("Error: tasks.json file is corrupted or not valid JSON.")
        tasksList = []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        tasksList = []        