from input import input_student, input_course, input_mark
from output import output_list_student,output_list_course,output_list_mark

def main():
    list_std = []
    list_course = []
    list_marks = []
    while True:
        print("\n" + "="*35)
        print("    System Data University    ")
        print("="*35)
        print("1. Enter list of student ")
        print("2. Enter list of course ")
        print("3. Enter mark for student ")
        print("4. Display data ")
        print("0. Exit")
        print("="*35)
        choice = input("Choose function (0-4): ")
        if choice == '1':
            list_std = input_student()
        elif choice == '2':
            list_course = input_course()
        elif choice == '3':
            new_marks = input_mark(list_std, list_course)
            if new_marks:
                list_marks.extend(new_marks)
        elif choice == '4':
            print("\n--- Choose Type of Data to show---")
            print("A. Show list of course")
            print("B. Show list of student")
            print("C. Show list of mark")
            sub_choice = input("Your Choose (A/B/C): ").upper()
            
            if sub_choice == 'A':
                output_list_course(list_course)
            elif sub_choice == 'B':
                output_list_student(list_std)
            elif sub_choice == 'C':
                output_list_mark(list_marks,list_course)
            else:
                print("Error")
        elif choice == '0':
            print("\nGood Bye ")
            break
        else:
            print("\nError, Please enter again")
if __name__ == "__main__":
    main()