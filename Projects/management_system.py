students=[]

def add_student():
    name=input("Enter the name of student:")
    age=int(input("Enter the age of student:"))
    major=input("Enter major of student:")
    mark=int(input("Enter Mark of student:"))

    student={"name":name,"age":age,"major":major,"mark":mark}
    students.append(student)
    print(f"Successfully added {name}")

def show_student():
    if not students:
        print("no student has been added.")
        return
    print("List of students")
    for i,student in enumerate(students, start=1):
        print(f"{i}, name {student['name']}  age{student['age']}  major{student['major']} mark {student['mark']} ")



def search_student():
    name=input("Enter your name:")
    found=False
    for student in students:
        if student["name"].lower()==name.lower():
            print(f"student found{student}")
            found=True
            break
    if not found:
        print("no student has been found.")



def update_student():
    name=input("Enter your name:")
    for student in students:
        if student["name"].lower()==name.lower():
            student["age"]=int(input("Enter new age:"))
            student["major"]=(input("Enter new major:"))
            student["mark"]=(input("Enter new mark:"))
            print("it is updated.")
            return
        

def delete_student():
    name=input("Enter your name:")
    for student in students:
        if student["name"].lower()==name.lower():
            students.remove(student)
            print("it is deleted.")
            return


def main():
    while True:
        print("management system of students.")
        print("adding 1️⃣")
        print("showing 2️⃣")
        print("searching 3️⃣")
        print("updating 4️⃣")
        print("deleting 5️⃣")
        print("exit 6️⃣")

        choice=input("Choose:")
        if choice=="1":
            add_student()
        elif choice=="2":
            show_student()
        elif choice=="3":
            search_student()
        elif choice=="4":
            update_student()
        elif choice=="5":
            delete_student()
        elif choice=="6":
            print("program is closed")
            break
        else:
            print("The number you entered is wrong")

main()






