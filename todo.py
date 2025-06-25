import os
def add():
    add_element=input("Enter the task you want to add: ")
    f=open("To-do.txt","a")
    f.write('{}\n'.format(add_element))
    print("Updated!")
    f.close()

def remove():
    remove_element=input("Enter the task you want to remove:" )
    f=open("To-do.txt","r")
    tasks=f.readlines()
    tasks=[task.strip() for task in tasks if task.strip() != remove_element]
    f.close()
    f=open("To-do.txt","w")
    for task in tasks:
        f.write(task+"\n")   
    f.close() 
    print("Successfully removed!")
def view():
    print("****TO-DO LIST****")
    try:
        f=open("To-do.txt","r")
        content=f.read().strip()
        if content:
            print(content)
        else:
            print("No task yet!")
        f.close()
    except FileNotFoundError:
        print("No such file!")
        

while True:  
    print("What do you want to do?")
    print("1.Add task\n2.Remove task\n3.View tasks\n4.Exit\n")
    choice=int(input("Press (1-4)"))
    match choice:
        case 1:
            add()
        case 2:
            remove()
        case 3:
            view()
        case 4:
            break
        case _:
            print("Incorrect input")
