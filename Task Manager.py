import json
from datetime import datetime

class TaskList:
    def __init__(self):
        self.TaskList = []
        self.load_TaskList()

    def addq(self, v):
        self.TaskList.append(v)
        self.save_TaskList()

    def delq(self, v):
        self.TaskList.remove(v)
        self.save_TaskList()

    def searchq(self, v):
        return v in self.TaskList

    def isempty(self):
        return self.TaskList == []

    def __str__(self):
        return str(self.TaskList)

    def save_TaskList(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.TaskList, f)

    def load_TaskList(self):
        try:
            with open('tasks.json', 'r') as f:
                self.TaskList = json.load(f)
        except FileNotFoundError:
            self.TaskList = []

class task_manager:
    def __init__(self):    
        self.q = TaskList()
        
    def add_task(self,s):
        if self.q.searchq(s):
            self.log_activity(f'Create {s} : unsuccessful')
            raise Exception(f'{s} : already exists')            
        
        else:
            self.q.addq(s)
            self.log_activity(f'Create {s} : successful')

    def del_task(self,s):
        if self.q.searchq(s):
            self.q.delq(s)
            self.log_activity(f'Delete {s} : successful')

        else:
            self.log_activity(f'Delete {s} : unsuccessful')
            raise Exception(f'{s} : does not exist thus deletion not possible')

    def search_task(self, s):
        if self.q.searchq(s):
            self.log_activity(f'Search {s} : successful')
        else:
            self.log_activity(f'Search {s} : unsuccessful')
            raise Exception(f'{s} : does not exists')

    def log_activity(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'[{timestamp}] {message}'
        
        try:
            with open('audit_log', 'a') as f:
                f.write(log_message + '\n')
        except FileNotFoundError:
            with open('audit_log', 'w') as f:
                f.write("Task Management Activity Log\n\n")
                f.write(log_message + '\n')
    
    def print_tasks(self):
        if self.q.isempty():
            print('No tasks left')
        else:
            print(self.q)
    
class Solution:
    t = task_manager()
    try:
        choice = int(input('Welcome to Task Manager!\nPress 1 to add a task\nPress 2 to delete a task\nPress 3 to search for a task\nPress 4 to view all tasks\nPress 5 to exit\nEnter choice: '))
        while choice != 5:
            try:
                if choice == 1:
                    s = input('Enter task you want to add: ')
                    t.add_task(s)
                    print('Task added to TaskList')

                elif choice == 2:
                    s = input('Enter the task you want to delete: ')
                    t.del_task(s)
                    print('Task deleted from TaskList')
                
                elif choice == 3:
                    s = input('Enter the task you want to search for: ')
                    t.search_task(s)
                    print('Task is present in TaskList')  

                elif choice == 4:
                    print('Following tasks are left: ')
                    t.print_tasks()

            except Exception as e:
                        print(e) 
                
            choice = int(input('\n\nPress 1 to add a task\nPress 2 to delete a task\nPress 3 to search for a task\nPress 4 to view all tasks\nPress 5 to exit\nEnter choice: '))

        print('Thank you for using Task Manager')

    except:
        print('Wrong choice, program terminated')