#welcome message
import json
print("STUDENT STUDY PLANNER")
inp=0
def addtask(l):
    d={}
    print("Add a task selected")
    taskname=input("Enter task name: ")
    subject=input("Enter subject: ")
    deadline=input("Enter deadline: ")
    d["task_name"]=taskname
    d["subject"]=subject
    d["deadline"]=deadline
    d["status"]="Pending"
    l.append(d)  
def viewtask(l):
        print("View all tasks selected")
        if(len(l)==0):
            print("No tasks found.")
        else:
            for task in l:
                print("Taskname:",task["task_name"],", Subject:",task["subject"],", Deadline:",task["deadline"],", Status:",task["status"]) 
def save_and_exit(l):
    print("Exiting Student Study Planner...")
    with open("studyplanner.json",'w') as f:
        json.dump(l,f,indent=4) 
def markcompleted(l):
    if(len(l)==0):
        print("No tasks found.")
    else:
        for task in l:
            print(l.index(task)+1,"Taskname:",task["task_name"],", Subject:",task["subject"],", Deadline:",task["deadline"],", Status:",task["status"]) 
        x=int(input("Enter the task number which you have completed: ")) 
        if(x not in range(1,len(l)+1)):
            print("Enter Valid Number.")
        else:
            l[x-1]["status"]="Completed" 
def deltask(l):
    if(len(l)==0):
        print("No tasks found.")   
    else:
        for task in l:
            print(l.index(task)+1,"Taskname:",task["task_name"],", Subject:",task["subject"],", Deadline:",task["deadline"],", Status:",task["status"]) 
        x=int(input("Enter the task number which you want to delete: ")) 
        if(x not in range(1,len(l)+1)):
            print("Enter Valid Number.")
        else:
            confirm=input("Do you confirm (yes or no):")
            if(confirm.lower()=="yes"):
                l.pop(x-1)
            elif(confirm.lower()=="no"):
                return
            else:
                print("Please enter only yes or no.")   
def searchtask(l):
    subj=input("Enter Subject Name: ")
    flag=False
    for task in l:
        if(task['subject'].lower()==subj.lower()):
            print("task_name: ",task['task_name']," deadline: ",task['deadline']," status: ",task['status'])
            flag=True
    if(flag!=True):
        print("No Matching Tasks Found.")
def filtertask(l):
    stat=input("Do you want to see Pending Tasks or Completed tasks (Enter 'completed' or 'pending'): ")
    flag=False
    for task in l:
        if(task['status'].lower()==stat.lower()):
            print("task_name: ",task['task_name']," subject: ",task['subject']," deadline: ",task['deadline'])
            flag=True
    if(flag!=True):
        print("No Matching Tasks Found.")
try:
    with open("studyplanner.json") as f:
        l=json.load(f)
except(FileNotFoundError, json.JSONDecodeError):
    l=[]
if(len(l)!=0):
    for i in l:
        print(i)
while(inp!=3):
    print("MENU:\n(1)Add a task\n(2)View all tasks\n(3)Exit\n(4)Mark a task as completed\n(5)Delete a task\n(6)Search tasks by subject\n(7)Filter tasks by status")
    inp=int(input("Enter 1, 2, 3, 4, 5, 6 or 7 : "))
    if(inp==1):
        addtask(l)
    elif(inp==2):
        viewtask(l)
    elif(inp==3):
        save_and_exit(l)
    elif(inp==4):
        markcompleted(l)
    elif(inp==5):
        deltask(l)
    elif(inp==6):
        searchtask(l)
    elif(inp==7):
        filtertask(l)
    else:
        print("Invalid choice. Try again.")