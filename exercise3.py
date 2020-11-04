from tkinter import *

root = Tk()


def get_val():
    global foodservice_value
    if foodservice_value.get() == '1':
        foodservice_value = "Yes"
    else:
        foodservice_value = 'No'

    print(f"""name = {name_value.get()}
phone number = {phone_value.get()}
gender = {gender_value.get()}
email address = {email_value.get()}
payment_method = {payment_method_value.get()}
foodservice = {foodservice_value}""")

    with open('recorces.txt', 'a') as f:
        f.write(f"""\nName = {name_value.get()}
Phone number = {phone_value.get()}
Gender = {gender_value.get()}
Email address = {email_value.get()}
Payment_method = {payment_method_value.get()}
Foodservice = {foodservice_value}\n""")


root.title("Pranav Travels")
root.geometry('450x344')
root.maxsize(450, 344)
root.maxsize(450, 344)
Label(root, text="Welcome to Pranav Travels", font="comicsans-bold 15 bold", pady=15).grid(row=0, column=3)
name = Label(root, text="Name")
phone = Label(root, text="Phone Number")
gender = Label(root, text="Gender")
email = Label(root, text="Email Address")
payment_method = Label(root, text="Payment Method")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
email.grid(row=4, column=2)
payment_method.grid(row=5, column=2)

name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
email_value = StringVar()
payment_method_value = StringVar()
foodservice_value = IntVar()

name_entry = Entry(root, textvariable=name_value)
phone_entry = Entry(root, textvariable=phone_value)
gender_entry = Entry(root, textvariable=gender_value)
email_entry = Entry(root, textvariable=email_value)
payment_method_entry = Entry(root, textvariable=payment_method_value)

name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
email_entry.grid(row=4, column=3)
payment_method_entry.grid(row=5, column=3)

# Checkbox and packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable=foodservice_value)
foodservice.grid(row=6, column=3)

# Button
Button(text="Submit to Pranav Travels", command=get_val).grid(row=7, column=3)

root.mainloop()
