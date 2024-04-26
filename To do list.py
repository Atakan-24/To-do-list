class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Aufgabe hinzugefügt:", task)

    def edit_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            print("Aufgabe bearbeitet:", new_task)
        else:
            print("Ungültiger Index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted_task = self.tasks.pop(index)
            print("Aufgabe gelöscht:", deleted_task)
        else:
            print("Ungültiger Index.")

    def display_tasks(self):
        if self.tasks:
            print("ToDo-Liste:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
        else:
            print("Keine Aufgaben in der Liste.")

def main():
    todo_list = TodoList()

    while True:
        print("\n--- ToDo-Liste ---")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgabe bearbeiten")
        print("3. Aufgabe löschen")
        print("4. Aufgaben anzeigen")
        print("5. Beenden")

        choice = input("Bitte wählen Sie eine Option (1-5): ")

        if choice == '1':
            task = input("Neue Aufgabe eingeben: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Index der Aufgabe zum Bearbeiten eingeben: "))
            new_task = input("Neue Aufgabe eingeben: ")
            todo_list.edit_task(index - 1, new_task)
        elif choice == '3':
            index = int(input("Index der zu löschenden Aufgabe eingeben: "))
            todo_list.delete_task(index - 1)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie 1-5.")

if __name__ == "__main__":
    main()
