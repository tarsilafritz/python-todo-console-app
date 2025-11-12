# 📝 To-Do List (Python Console App)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Type-CLI-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A simple **to-do list application** built with Python, running entirely in the terminal.  
You can **add, view, update, and remove tasks**, with each task having a **priority** and **status**.  
All tasks are automatically saved to a local JSON file for persistence between runs.

---

## 🎯 Learning Goals
Through this project, I aimed to:
- Practice Python syntax and basic structure  
- Reinforce understanding of **variables**, **data types**, and **type conversion**  
- Work with **loops** and **conditional statements**  
- Handle **user input** and prevent program crashes with **error handling**
- Apply **modularization** by separating logic into multiple Python files
- Learn how to **save and load data** using JSON files for persistence

---

## 🧩 Features
- ➕ Add new tasks with title, priority, and status  
- 👀 View all current tasks  
- 🔄 Update task status (`pending`, `in progress`, `done`)  
- ❌ Remove tasks  
- 💾 Data automatically saved and loaded from `tasks.json`  
- 🧩 Simple modular structure:
  - `main.py` — runs the main program loop  
  - `menu.py` — shows the menu options  
  - `options.py` — handles user actions  
  - `storage.py` — saves and loads tasks safely  

---

## 🧠 How It Works
The program follows a modular and interactive flow:
1. **Program Start**
    - When you run `main.py`, the program loads all existing tasks from the `tasks.json` file using `storage.py`.
    - If no file exists yet, an empty task list is created automatically.
2. **Menu Display**
    - The `menu.py` module shows a simple text menu with numbered options.
    - The user selects what they want to do (add, view, update, remove, or exit).
3. **Handling Actions**
    - The selected option is sent to `options.py`, which executes the appropriate function.
    - Example:
      - Option `1` → asks for task details and adds it
      - Option `2` → displays all stored tasks neatly
      - Option `3` → lets you update a task’s status
      - Option `4` → removes a task by its index
4. **Program Exit**
    - When you choose to exit (`0`), the app automatically saves the most recent version of your tasks before closing.
Each task is stored as a Python dictionary like this:
```python
{
  "title": "Study Python",
  "priority": "high",
  "status": "pending"
}
```
All these dictionaries are stored in a list (`tasksList`) and saved as a JSON array in `tasks.json`.
---

## 🗂️ Project Structure
```bash
python-todo-console/
├── main.py        # Runs the main program loop
├── menu.py        # Displays the menu
├── options.py     # Handles user actions
├── storage.py     # Saves and loads tasks
└── tasks.json     # Stores your tasks (auto-generated)
```

---

## 🚀 How to Run

### 1. Clone or download this repository
```bash
git clone https://github.com/tarsilafritz/python-todo-console.git
cd python-todo-console
```
### 2. Run the script
```bash
python main.py
```
### 3. Choose an option:
```markdown
# MENU #
1. Add a task
2. View all tasks
3. Update task status
4. Remove a task
0. Exit
```
---

## 🧑‍💻 Example JSON Output
After adding a few tasks, your `tasks.json` file might look like this:
```json
[
    {
        "title": "Study Python",
        "status": "in progress",
        "priority": "high"
    },
    {
        "title": "Clean the room",
        "status": "done",
        "priority": "low"
    }
]

```

---

## 💡 Future Improvements (Ideas)
- [ ] Add task due dates
- [ ] Sort/filter tasks by priority or status
- [ ] Add an option to edit task titles
- [ ] Implement colored output for better readability

---

## 🐍 Requirements
- Python 3.8 or newer
  </br>*No external libraries needed (uses only built-in Python modules).*

---

> 💬 *"One task at a time — keep coding!"*

[![Made by Tarsila Fritz](https://img.shields.io/badge/Made_by-Tarsila_Fritz-blueviolet?logo=github&logoColor=white)](https://github.com/tarsilafritz)
