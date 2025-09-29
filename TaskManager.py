tasks = [ ]
print(input("Day Started please plan your day! "))
n =  int(input("Enter the no of task for the day? "))
for i in range(n):
    task = input("Enter task? ")
    tasks.append(task)
completed_task = []
incompleted_task = []  
print(input("End of the day reviewed task! "))
for i in tasks:
    status = input(f"Did you completed the {i} task (Yes or No)?")
    if status.lower() == "Yes":
        completed_task.append(i)   
    else:
        incompleted_task.append(i)    
print(f"Completed Tasks are {completed_task}")
print(f"Incompleted Tasks are {incompleted_task}")

