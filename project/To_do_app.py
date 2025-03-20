# Python To Do App 
tasks=[]
tasks_done=[]
# writing in file function 
def writing_in_file():
    with open("To_do.txt","w") as file:
        file.write ("Task To Do \n")
        for item in tasks:
            file.write(f"- {item}\n")
        file.write("Completed Task ")
        for item in tasks_done:
            file.write(f"\n-{item}\n")
# to do list function 
def to_do_list():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1.Add Task")
        print("2.Remove Task")
        print("3.Show Task")
        print("4.Quit")
        print("5.View Completed Task")
        print("6.Mark task as completed")
        print("=====================")
        choose=input("choose one option\n")


        if choose=="1":
            print("Entering the Task....")
            task=input("Enter Task:")
            tasks.append(task)
            writing_in_file()  # Save tasks after modification
        elif choose=="2":
            print("Removing the Task:")
            task=input("Enter the task you want to remove:")
            if task in tasks:
                tasks.remove(task)
                writing_in_file()  # Save tasks after modification
            else:
                print("Task not found\n")
        elif choose=="3":
            print("list of Added Task:")
            if len(tasks)==0:
                print("You Haven't Added Any Task")
            else:
                for task in tasks:
                    print(" - " + task)
            
        elif choose=="4":
            print("Exiting ...")
            writing_in_file()  # Save tasks after modification
            exit()
            
        elif choose=="5":
            print("Tasks which are Done!")
            if len(tasks_done)==0:
                print("You haven't Complete Single Task")
            for task_done in tasks_done:
                print(task_done)
        elif choose=="6":
            print("Adding the completed Task ")
            done=input("Enter the completed Task:")
            tasks_done.append(done)
            tasks.remove(done)
            writing_in_file()  # Save tasks after modification
        else:
            print("Error 404!")
        




to_do_list()
writing_in_file()


        
            


    

