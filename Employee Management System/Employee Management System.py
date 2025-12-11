import pickle
import os


class Employee:

    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def __str__(self):
        return f"Name: {self.name}\nID Number: {self.id_number}\nDepartment: {self.department}\nJob Title: {self.job_title}"


def load_employees(filename='employees.dat'):
    if os.path.exists(filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except:
            print("Error loading file. Starting with empty dictionary.")
            return {}
    return {}


def save_employees(employees, filename='employees.dat'):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(employees, file)
        print("Employee data saved successfully.")
    except:
        print("Error saving employee data.")


def display_menu():
    print("\n" + "=" * 40)
    print("Employee Management System")
    print("=" * 40)
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee")
    print("4. Delete an employee")
    print("5. Display all employees")
    print("6. Quit")
    print("=" * 40)


def lookup_employee(employees):
    try:
        id_num = int(input("Enter employee ID number: "))
        if id_num in employees:
            print("\n" + "-" * 40)
            print(employees[id_num])
            print("-" * 40)
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid ID number. Please enter a number.")


def add_employee(employees):
    try:
        id_num = int(input("Enter employee ID number: "))
        if id_num in employees:
            print("An employee with this ID already exists.")
            return

        name = input("Enter employee name: ")
        department = input("Enter department: ")
        job_title = input("Enter job title: ")

        employees[id_num] = Employee(name, id_num, department, job_title)
        print("Employee added successfully.")
    except ValueError:
        print("Invalid ID number. Please enter a number.")


def change_employee(employees):
    try:
        id_num = int(input("Enter employee ID number: "))
        if id_num not in employees:
            print("Employee not found.")
            return

        print("\nCurrent employee information:")
        print(employees[id_num])
        print("\nEnter new information (press Enter to keep current value):")

        name = input(f"Enter new name [{employees[id_num].name}]: ")
        department = input(f"Enter new department [{employees[id_num].department}]: ")
        job_title = input(f"Enter new job title [{employees[id_num].job_title}]: ")

        if name:
            employees[id_num].name = name
        if department:
            employees[id_num].department = department
        if job_title:
            employees[id_num].job_title = job_title

        print("Employee information updated successfully.")
    except ValueError:
        print("Invalid ID number. Please enter a number.")


def delete_employee(employees):
    try:
        id_num = int(input("Enter employee ID number to delete: "))
        if id_num in employees:
            print("\nEmployee to be deleted:")
            print(employees[id_num])
            confirm = input("\nAre you sure you want to delete this employee? (yes/no): ")
            if confirm.lower() == 'yes':
                del employees[id_num]
                print("Employee deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid ID number. Please enter a number.")


def display_all_employees(employees):
    if not employees:
        print("\nNo employees in the system.")
        return

    print("\n" + "=" * 40)
    print(f"Total Employees: {len(employees)}")
    print("=" * 40)
    for emp in employees.values():
        print(emp)
        print("-" * 40)


def main():
    employees = load_employees()

    # Add initial employees if dictionary is empty
    if not employees:
        print("Starting with sample employees...")
        employees[47800] = Employee("Susan Meyers", 47800, "Accounting", "Vice President")
        employees[39120] = Employee("Mark Jones", 39120, "IT", "Programmer")
        employees[81744] = Employee("Joy Rogers", 81744, "Manufacturing", "Engineer")

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            lookup_employee(employees)
        elif choice == '2':
            add_employee(employees)
        elif choice == '3':
            change_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            display_all_employees(employees)
        elif choice == '6':
            save_employees(employees)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()