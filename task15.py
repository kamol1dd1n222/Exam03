tasks = list()
class TodoList:
    
    def add_task(self,task:str):
        self.task = task
        tasks.append(self.task)
        
    def show_tasks(self):
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
            
todo = TodoList()
todo.add_task('Coding')
todo.add_task("Create database")
todo.show_tasks()
