tasks = [10, 11, 12, 13, 14, 15]

def load_balancer(all_tasks):
    for task_id in all_tasks:
        server_number = task_id % 3
        
        if server_number == 0:
            print(f"{task_id} - server A")
        elif server_number == 1:
            print(f"{task_id} - server B")
        else:
            print(f"{task_id} - server C")
load_balancer(tasks)