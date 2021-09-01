tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted(list):
    uncompleted_tasks = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks

def completed(list):
    completed_tasks = []
    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks

def descriptions(list): 
    descriptions = []
    for task in list:
        descriptions.append(task["description"])
    return descriptions

def filter_by_time(list, time):
    timed = []
    for task in list:
        if task["time_taken"] >= time:
            timed.append(task)
    return timed

def search_by_description(list, description):
    described = []
    for task in list:
        if task["description"] == description:
            return task
    return "Not Found"

def mark_as_completed(description, list):
    for task in list:
        if task["description"] == description:
            task["completed"] = True

def add_task(list, description, time):
    list.append({
        "description": description,
        "completed": False,
        "time_taken": time
    })

def print_menu():
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

def display_menu():
    print_menu()

    command = input("What would you like to do? ").lower()

    while command != "q":

        if command == "1":
            print(tasks)
            command = input("What next? ").lower()
        if command == "2":
            print(uncompleted(tasks))
            command = input("What next? ").lower()
        if command == "3":
            print(completed(tasks))
            command = input("What next? ").lower()
        if command == "4":
            description = input("Which task would you like to mark as complete? ")
            mark_as_completed(description, tasks)
            print(description + " marked as completed.")
            command = input("What next? ").lower()
        if command == "5":
            time = input("What time span in minutes would you like to use as a filter? ")
            print(filter_by_time(tasks, int(time)))
            command = input("What next? ").lower()
        if command == "6":
            description = input("What task are you looking for? ")
            print(search_by_description(tasks, description))
            command = input("What next? ").lower()
        if command == "7":
            description = input("What task would you like to add? ")
            time = input("How long (in minutes) will this task take? ")
            add_task(tasks, description, time)
            print("Task added to list.")
            command = input("What next? ").lower()
        if command == "m":
            print_menu()
            command = input("What would you like to do? ").lower()

    print("Goodbye!")
    return

        

display_menu()


