import options
import menu
from storage import load_tasks, save_tasks

load_tasks()

while True:       
    menu.show_menu()    
    try:
        userChoice = int(input("Inform the option you want to choose: "))
    except ValueError:
        print("Please, enter a valid number (0, 1, 2).")
        continue
    
    if userChoice == 1:
        options.add_task()
    elif userChoice == 2:
        options.view_tasks()
    elif userChoice == 3:
        options.update_status()
    elif userChoice == 4:
        options.remove_task()
    elif userChoice == 0:
        print("Saving tasks and exiting program...")
        save_tasks()
        break
    else:
        print("Invalid option, please choose again.")


    
