import math

students = []
courses = []
marks = {} 

def input_students():
    try:
        n = int(input("Number of students: "))
        for i in range(n):
            print(f"Student {i + 1}")
            sid = input("  ID: ")
            name = input("  Name: ")
            dob = input("  DoB: ")
            students.append({"id": sid, "name": name, "dob": dob})
    except ValueError:
        print("Invalid input! Please enter a number.")

def input_courses():
    try:
        n = int(input("Number of courses: "))
        for i in range(n):
            print(f"Course {i + 1}")
            cid = input("  ID: ")
            name = input("  Name: ")
            courses.append({"id": cid, "name": name})
    except ValueError:
        print("Invalid input! Please enter a number.")

def list_students():
    print("\n--- List of Students ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def list_courses():
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def input_marks():
    if not courses:
        print("Please input courses first!")
        return
    list_courses()
    cid = input("Choose a course ID to enter marks: ")
    
    # Kiểm tra xem ID môn học có tồn tại không
    course_exists = False
    for c in courses:
        if c['id'] == cid:
            course_exists = True
            break
    
    if not course_exists:
        print("Course ID not found!")
        return

    if cid not in marks:
        marks[cid] = {}

    print(f"Entering marks for course: {cid}")
    for s in students:
        try:
            score = float(input(f"  Mark for {s['name']} (ID: {s['id']}): "))
            marks[cid][s['id']] = score
        except ValueError:
            print("  Invalid score! Skipping this student.")

def show_marks():
    list_courses()
    cid = input("Choose a course ID to show marks: ")
    if cid not in marks:
        print("No marks recorded for this course yet.")
        return

    print(f"\n--- Marks for Course {cid} ---")
    for s in students:
        if s['id'] in marks[cid]:
            print(f"{s['name']}: {marks[cid][s['id']]}")
        else:
            print(f"{s['name']}: No mark")

def main():
    while True:
        print("\n--- STUDENT MARK MANAGEMENT ---")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == "1": input_students()
        elif choice == "2": input_courses()
        elif choice == "3": input_marks()
        elif choice == "4": list_students()
        elif choice == "5": list_courses()
        elif choice == "6": show_marks()
        elif choice == "0": break
        else: print("Wrong choice, try again.")

if __name__ == "__main__":
    main()