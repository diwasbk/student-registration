from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Registration System")
root.geometry("430x610")
root.resizable(0, 0)
root.config(bg="blue")

# Creating Database
conn = sqlite3.connect('Student Registration.db')
cursor = conn.cursor()
cursor.execute('''
          CREATE TABLE IF NOT EXISTS students (
               Name TEXT,
               DOB TEXT,
               Gender TEXT,
               Address TEXT,
               Phone_Number TEXT PRIMARY KEY,
               Email TEXT,
               Previous_College TEXT,
               Year INT,
               Stream TEXT,
               Grade TEXT,
               Applied_Course TEXT
          )
          ''')
conn.commit()
conn.close()

def retrieve():
    import students_details

def submit():
    # Validating the inputs
    if (name_entry.get() == "" or dob_entry.get() == "" or gender_combobox.get() == "Select Gender" or address_entry.get() == "" or email_entry.get() == "" or school_entry.get() == "" or year_combobox.get() == "Select Year" or stream_combobox.get()=="Select Stream" or grade_combobox.get() == "Select Grade" or course_combobox.get() == "Select Course"):
        messagebox.showerror("Incomplete Information", "Please complete all the fields")
    elif not email_entry.get().endswith("@gmail.com"):
        messagebox.showerror("Error", "Invalid gmail account")
    elif not phone_entry.get().isdigit() or len(phone_entry.get()) != 10:
        messagebox.showerror("Error", "Invalid phone number")
    else:
        result = messagebox.askquestion("Confirmation", "Are you sure you want submit?")
        if result == "yes":
            # Insert into table
            conn = sqlite3.connect('Student Registration.db')
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO students (Name, DOB, Gender, Address, Phone_Number, Email, "Previous_College", Year, Stream, Grade, "Applied_Course") 
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
               (name_entry.get().upper(), dob_entry.get(), gender_combobox.get(), address_entry.get().upper(), phone_entry.get(), email_entry.get().lower(), 
                school_entry.get().upper(), year_combobox.get(), stream_combobox.get(), grade_combobox.get(), course_combobox.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful!")
            
def clear():
    result = messagebox.askquestion("Confirmation", "Are you sure you want to clear all fields?")
    if result == "yes":
        # Clear entry fields
        name_entry.delete(0, END)
        dob_entry.delete(0, END)
        address_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        school_entry.delete(0, END)
        # Set combo boxes to default text
        gender_combobox.set("Select Gender")
        year_combobox.set("Select Year")
        stream_combobox.set("Select Stream")
        grade_combobox.set("Select Grade")
        course_combobox.set("Select Course")

# Title Label
title_label = Label(root, text="Registration System", font="Arial 22 bold", fg="white",  bg="blue")
title_label.place(x=60, y=20)

# Name Label and Entry
name_label = Label(root, text="Name:", font="Arial 10 bold", fg="white",  bg="blue")
name_label.place(x=25, y=90)
name_entry = Entry(root, width=30)
name_entry.place(x=180, y=90)

# Date of Birth Label and Entry
dob_label = Label(root, text="Date of Birth:", font="Arial 10 bold", fg="white",  bg="blue")
dob_label.place(x=25, y=130)
dob_entry = DateEntry(root, width=27)
dob_entry.place(x=180, y=130)

# Gender Label and Options
gender_label = Label(root, text="Gender:", font="Arial 10 bold", fg="white",  bg="blue")
gender_label.place(x=25, y=170)
gender_combobox = ttk.Combobox(root, values=["Male", "Female", "Others"], width=27, state="readonly")
gender_combobox.place(x=180, y=170)
gender_combobox.set("Select Gender")

# Address Label and Entry
address_label = Label(root, text="Address:", font="Arial 10 bold", fg="white",  bg="blue")
address_label.place(x=25, y=210)
address_entry = Entry(root, width=30)
address_entry.place(x=180, y=210)

# Phone Number Label and Entry
phone_label = Label(root, text="Phone Number:", font="Arial 10 bold", fg="white",  bg="blue")
phone_label.place(x=25, y=250)
phone_entry = Entry(root, width=30)
phone_entry.place(x=180, y=250)

# Email Address Label and Entry
email_label = Label(root, text="Email Address:", font="Arial 10 bold", fg="white",  bg="blue")
email_label.place(x=25, y=290)
email_entry = Entry(root, width=30)
email_entry.place(x=180, y=290)

# Previous School Name Label and Entry
school_label = Label(root, text="Previous School:", font="Arial 10 bold", fg="white",  bg="blue")
school_label.place(x=25, y=330)
school_entry = Entry(root, width=30)
school_entry.place(x=180, y=330)

# Year of Passing Label and Entry
year_label = Label(root, text="Year of Passing:", font="Arial 10 bold", fg="white",  bg="blue")
year_label.place(x=25, y=370)
year_combobox = ttk.Combobox(root, values=["2020", "2021", "2022", "2023", "2024"], width=27, state="readonly")
year_combobox .place(x=180, y=370)
year_combobox.set("Select Year")

# Stream Label and Combobox
stream_label = Label(root, text="Stream:", font="Arial 10 bold", fg="white", bg="blue")
stream_label.place(x=25, y=410)
stream_combobox = ttk.Combobox(root, values=["Science", "Management", "Law"], width=27, state="readonly")
stream_combobox.place(x=180, y=410)
stream_combobox.set("Select Stream")

# Grades Label and Entry
grades_label = Label(root, text="Grades/Marks:", font="Arial 10 bold",fg="white",  bg="blue")
grades_label.place(x=25, y=450)
grade_combobox = ttk.Combobox(root, values=["A+", "A", "B+", "B", "C+", "C"], width=27, state="readonly")
grade_combobox.place(x=180, y=450)
grade_combobox.set("Select Grade")

# Course Applying For Label and Entry
course_label = Label(root, text="Course Applying For:", font="Arial 10 bold",fg="white",  bg="blue")
course_label.place(x=25, y=490)
course_combobox = ttk.Combobox(root, values=["B.Sc. Computing", "B.Sc. Ethical Hacking", "B.Sc. Computing with AI"], width=27, state="readonly")
course_combobox.place(x=180, y=490)
course_combobox.set("Select Course")

# Retrieve Button
retrieve_button = Button(root, text="Retrieve", font="Arial 10 bold", bg="green", fg="white", width=15, cursor="hand2", command=retrieve)
retrieve_button.place(x=25, y=550)

# Clear Button
clear_button = Button(root, text="Clear", font="Arial 10 bold", bg="red", fg="white", width=15, cursor="hand2", command=clear)
clear_button.place(x=155, y=550)

# Submit Button
submit_button = Button(root, text="Submit", font="Arial 10 bold", bg="green", fg="white", width=15, cursor="hand2",  command=submit)
submit_button.place(x=275, y=550)
root.mainloop()