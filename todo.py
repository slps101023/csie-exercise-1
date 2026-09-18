tasks = []

def add_task(name):
    if name in tasks:
        print(f"Task '{name}' already exists, skipping.")
        return
    tasks.append(name)

def show_tasks():
    print(f"=== Todo List ({len(tasks)} items) ===")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def delete_task(index):
    tasks.pop(index - 1)

def main():
    add_task("Learn Git")
    add_task("Learn Git")
    show_tasks()
    delete_task(1)
    show_tasks()

if __name__ == "__main__":
    main()
