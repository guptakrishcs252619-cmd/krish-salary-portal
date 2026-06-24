from tkinter import *

employees = []



def add_employee():
    emp_id = id_entry.get()
    name = name_entry.get()
    salary = salary_entry.get()

    if emp_id == "" or name == "" or salary == "":
        status_label.config(text="Please fill all fields!")
        return

    employee = {
        "ID": emp_id,
        "Name": name,
        "Salary": salary
    }

    employees.append(employee)
    display_employees()

    status_label.config(text="Employee Added Successfully!")

   
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    salary_entry.delete(0, END)


    id_entry.focus()


def update_employee():
    emp_id = id_entry.get()

    for emp in employees:
        if emp["ID"] == emp_id:
            emp["Name"] = name_entry.get()
            emp["Salary"] = salary_entry.get()

            display_employees()
            status_label.config(text="Employee Updated Successfully!")

            id_entry.delete(0, END)
            name_entry.delete(0, END)
            salary_entry.delete(0, END)
            id_entry.focus()
            return

    status_label.config(text="Employee Not Found!")


def delete_employee():
    emp_id = id_entry.get()

    for emp in employees:
        if emp["ID"] == emp_id:
            employees.remove(emp)
            display_employees()
            status_label.config(text="Employee Deleted Successfully!")

            id_entry.delete(0, END)
            name_entry.delete(0, END)
            salary_entry.delete(0, END)
            id_entry.focus()
            return

    status_label.config(text="Employee Not Found!")


def display_employees():
    text_area.delete(1.0, END)

    if len(employees) == 0:
        text_area.insert(END, "No Employee Records Found!")
    else:
        for emp in employees:
            text_area.insert(
                END,
                f"👨‍💼 Employee ID : {emp['ID']}\n"
                f"📝 Name         : {emp['Name']}\n"
                f"💰 Salary       : ₹{emp['Salary']}\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            )

root = Tk()
root.title("Employee ADT System")
root.geometry("550x550")
root.configure(bg="#1E1E2F")

Label(root,
      text="EMPLOYEE MANAGEMENT SYSTEM",
      font=("Arial", 18, "bold"),
      bg="#1E1E2F",
      fg="cyan").pack(pady=10)

frame = Frame(root, bg="#2E2E4D", padx=20, pady=20)
frame.pack(pady=10)

Label(frame, text="Employee ID",
      font=("Arial", 12, "bold"),
      bg="#2E2E4D",
      fg="white").grid(row=0, column=0, padx=10, pady=10)

id_entry = Entry(frame, font=("Arial", 12), width=25)
id_entry.grid(row=0, column=1)

Label(frame, text="Employee Name",
      font=("Arial", 12, "bold"),
      bg="#2E2E4D",
      fg="white").grid(row=1, column=0, padx=10, pady=10)

name_entry = Entry(frame, font=("Arial", 12), width=25)
name_entry.grid(row=1, column=1)


Label(frame, text="Salary",
      font=("Arial", 12, "bold"),
      bg="#2E2E4D",
      fg="white").grid(row=2, column=0, padx=10, pady=10)

salary_entry = Entry(frame, font=("Arial", 12), width=25)
salary_entry.grid(row=2, column=1)


id_entry.bind("<Return>", lambda event: name_entry.focus())
name_entry.bind("<Return>", lambda event: salary_entry.focus())
salary_entry.bind("<Return>", lambda event: add_employee())

Button(frame, text="➕ Add",
       command=add_employee,
       bg="green",
       fg="white",
       font=("Arial", 11, "bold"),
       width=12).grid(row=3, column=0, pady=15)

Button(frame, text="✏ Update",
       command=update_employee,
       bg="orange",
       fg="white",
       font=("Arial", 11, "bold"),
       width=12).grid(row=3, column=1)

Button(frame, text="❌ Delete",
       command=delete_employee,
       bg="red",
       fg="white",
       font=("Arial", 11, "bold"),
       width=12).grid(row=4, column=0, columnspan=2, pady=10)


status_label = Label(root,
                     text="Enter Employee Details",
                     font=("Arial", 11, "bold"),
                     bg="#1E1E2F",
                     fg="yellow")

status_label.pack()


text_area = Text(root,
                 width=55,
                 height=12,
                 font=("Consolas", 11),
                 bg="black",
                 fg="lime")

text_area.pack(pady=15)


id_entry.focus()

root.mainloop()
