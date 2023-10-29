def take_input():
    num_tasks = int(input("Enter the number of tasks: "))
    tasks = []

    for i in range(num_tasks):
        task_name = input(f"Enter the name of task {i + 1}: ")
        time_taken = float(input(f"Enter time taken for task in minutes {task_name}: "))
        urgency_level = int(input(f"Enter urgency level (1-10) for task {task_name}: "))
        tasks.append((task_name, time_taken, urgency_level))
    
    return tasks

def custom_sort(task):
    # Sort first by urgency level (in descending order) and then by time taken (in ascending order)
    return (-task[2], task[1])

def schedule_tasks(tasks):
    tasks.sort(key=custom_sort)

    print("Scheduled tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Task: {task[0]}, Time taken: {task[1]}, Urgency level: {task[2]}")

if __name__ == "__main__":
    tasks = take_input()
    schedule_tasks(tasks)