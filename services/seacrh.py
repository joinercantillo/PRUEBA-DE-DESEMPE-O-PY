def search(studentlist):
    import os
    import csv
    # this comand seacrh any student by the id
    print("\n=== SEARCH STUDENT ===")
    id = input("Enter the Student ID to search: ")
    found_students = [c for c in studentlist if c['Student ID'].lower() == id.lower()]
    #if student not found in the he list show this message:
    if found_students:
        print("\nStudent not found")
        for student in found_students:
            print(f"  Student ID: {student['Student ID']}, Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}, State: {student['State']}")
    else:
        print(f"No Students found with the ID '{id}'.")
    
    return studentlist