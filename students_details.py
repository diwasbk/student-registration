from tkinter import *
import sqlite3

root = Tk()
root.title("Student Details")

# Labels Bar
line_label = Label(root, text="__________________________________________________________________________________________________________________________________________________________________________________________", font=("Arial", 16, "bold"), fg="green")
line_label.place(y=25)

# Labels
name_label = Label(root, text="Name  ", font=("Arial", 12, "bold"), fg="blue")
name_label.grid(row=1, column=1, padx=40, pady=20)

dob_label = Label(root, text="DOB  ", font=("Arial", 12, "bold"), fg="blue")
dob_label.grid(row=1, column=2, padx=20, pady=20)

gender_label = Label(root, text="Gender ", font=("Arial", 12, "bold"), fg="blue")
gender_label.grid(row=1, column=3, padx=10, pady=20)

address_label = Label(root, text="Address", font=("Arial", 12, "bold"), fg="blue")
address_label.grid(row=1, column=4, padx=10, pady=20)

phone_number_label = Label(root, text="Phone Number", font=("Arial", 12, "bold"), fg="blue")
phone_number_label.grid(row=1, column=5, padx=10, pady=20)

email_label = Label(root, text="Email", font=("Arial", 12, "bold"), fg="blue")
email_label.grid(row=1, column=6, padx=20, pady=20)

previous_college_label = Label(root, text="Previous College", font=("Arial", 12, "bold"), fg="blue")
previous_college_label.grid(row=1, column=7, padx=10, pady=20)

year_label = Label(root, text="Year", font=("Arial", 12, "bold"), fg="blue")
year_label.grid(row=1, column=8, padx=15, pady=20)

stream_label = Label(root, text="Stream", font=("Arial", 12, "bold"), fg="blue")
stream_label.grid(row=1, column=9, padx=20, pady=20)

grade_label = Label(root, text="Grade", font=("Arial", 12, "bold"), fg="blue")
grade_label.grid(row=1, column=10, padx=10, pady=20)

applied_course_label = Label(root, text="Applied Course", font=("Arial", 12, "bold"), fg="blue")
applied_course_label.grid(row=1, column=11, padx=10, pady=20)

# Establishing database
conn = sqlite3.connect('Student Registration.db')
cursor = conn.cursor()

# Fetch data from the database
cursor.execute("SELECT * FROM students")
details = cursor.fetchall()

# Display details in the GUI
num = 2
for i in details:
    for j in range(len(i)):
        label = Label(root, text=i[j], font=("Arial", 10, "bold"))
        label.grid(row=num, column=j+1, padx=2, pady=5)
    num += 1

# Commit and close connection
conn.commit()
conn.close()

root.mainloop()