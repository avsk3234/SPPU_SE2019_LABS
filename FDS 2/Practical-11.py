import os 

def add_student_info(file_name):
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    division = input("Enter Division: ")
    address = input("Enter Address: ")

    with open(file_name, 'a') as file:
        file.write(f"{roll_number},{name},{division},{address}\n")
   
    print("Student information added successfully.")

def delete_student_info(file_name):
    roll_number = input("Enter Roll Number of the student to delete: ")

    found = False
    temp_file = "temp.txt"
    with open(file_name, 'r') as file, open(temp_file, 'w') as temp:
        for line in file:
            record = line.strip().split(',')
            if record[0] == roll_number:
                found = True
            else:
                temp.write(line)

    if found:
        print("Student information deleted successfully.")
        # Rename temp file to the original file
        os.replace(temp_file, file_name)
    else:
        print("Student record not found.")
        # Remove temp file
        os.remove(temp_file)

def display_student_info(file_name):
    roll_number = input("Enter Roll Number of the student to display: ")

    with open(file_name, 'r') as file:
        found = False
        for line in file:
            record = line.strip().split(',')
            if record[0] == roll_number:
                print("Roll Number:", record[0])
                print("Name:", record[1])
                print("Division:", record[2])
                print("Address:", record[3])
                found = True
                break
       
        if not found:
            print("Student record not found.")

def main():
    file_name = "student_info.txt"

    while True:
        print("\n********** Student Information System **********")
        print("1. Add Student Information")
        print("2. Delete Student Information")
        print("3. Display Student Information")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student_info(file_name)
        elif choice == '2':
            delete_student_info(file_name)
        elif choice == '3':
            display_student_info(file_name)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()