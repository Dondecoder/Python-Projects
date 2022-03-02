import sys
import tkinter as tk
from PIL import ImageTk, Image
from calendar import monthrange
from tkinter import messagebox

root = tk.Tk()
# title of your app
root.title("EBudget")
root.iconbitmap("C:/Users/patri/Desktop/Patrik_ python_projects/Budget/budget_app_icon.ico.ico")
root.configure(bg="SeaGreen1")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.state('zoomed')




label1 = tk.Label(root, text='Monthly Budget', font=('Times', 25, "underline", "bold"), anchor="center", bg="SeaGreen1"
                                                                                                        ,fg="midnight "
                                                                                                            "blue")
label1.grid(row=1, column=1, columnspan=2)
label1.grid_rowconfigure(1, weight=1)
label1.grid_columnconfigure(1, weight=1)

# Budget Questions
User_name = tk.Label(root, justify="left", text="Please input your name: ", font=('Times', 13, "bold"), bg="SeaGreen1",
                     fg="midnight blue")
User_name.grid(row=2, column=1, padx=10, pady=10)
User_name.place(x=35, y=50)

Month = tk.Label(root, justify="left", text="Please input the month this budget is for? Ex: For March enter: 03 ",
                 font=('Times', 13,
                       "bold"), bg="SeaGreen1", fg="midnight blue")
Month.grid(row=4, column=1, padx=10, pady=10, columnspan=1)
Month.place(x=35, y=95)

Year = tk.Label(root, justify="left", text="Please input the year this budget is for? Ex: 2011", font=('Times', 13,
                                                                                                       "bold"),bg="SeaGreen1", fg="midnight blue")
Year.grid(row=6, column=1, padx=10, pady=10)
Year.place(x=35, y=140)

monthly_goal = tk.Label(root, justify="left", text="How much money would you like to save per month? Ex: 400 ",
                        font=('Times', 13, "bold"), bg="SeaGreen1", fg="midnight blue")
monthly_goal.grid(row=8, column=1, padx=10, pady=10)
monthly_goal.place(x=35, y=185)

monthly_check = tk.Label(root, justify="left", text="How much do you make monthly after taxes? ",
                         font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_check.grid(row=10, column=1, padx=10, pady=10)
monthly_check.place(x=35, y=228)

monthly_rent = tk.Label(root, justify="left", text="How much is your monthly rent/mortgage? ",
                        font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_rent.grid(row=12, column=1, padx=10, pady=10)
monthly_rent.place(x=35, y=270)

monthly_utilities = tk.Label(root, justify="left", text="How much do you pay in utilities per month? ",
                             font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_utilities.grid(row=14, column=1, padx=10, pady=10)
monthly_utilities.place(x=35, y=310)

monthly_cable = tk.Label(root, justify="left", text="How much do you spend on cable per month? ",
                         font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_cable.grid(row=16, column=1, padx=10, pady=10)
monthly_cable.place(x=35, y=352)

monthly_phone = tk.Label(root, justify="left", text="How much do you spend on your phone bill per month? ",
                         font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_phone.grid(row=18, column=1, padx=10, pady=10)
monthly_phone.place(x=35, y=393)

monthly_food = tk.Label(root, justify="left", text="How much do you spend on food per month? ",
                        font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_food.grid(row=20, column=1, padx=10, pady=10)
monthly_food.place(x=35, y=433)

monthly_travel = tk.Label(root, justify="left", text="How much do you spend on travel per month? "
                                                     "Ex: Buses, Trains, "
                                                     "Flights, "
                                                     "Gas, "
                                                     "etc:  ", font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_travel.grid(row=22, column=1, padx=10, pady=10)
monthly_travel.place(x=35, y=473)

monthly_wardrobe = tk.Label(root, justify="left", text="How much do you spend on clothes per month? ",
                            font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_wardrobe.grid(row=24, column=1, padx=10, pady=10)
monthly_wardrobe.place(x=35, y=513)

monthly_subscription = tk.Label(root, justify="left", text="How much do you spend monthly on subscriptions and "
                                                           "memberships? ", font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_subscription.grid(row=26, column=1, padx=10, pady=10)
monthly_subscription.place(x=35, y=553)
#
monthly_car_note = tk.Label(root, justify="left", text="How much do you pay monthly on your car note? ",
                            font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_car_note.grid(row=28, column=1, padx=10, pady=10)
monthly_car_note.place(x=35, y=594)

monthly_car_insurance = tk.Label(root, justify="left", text="How much do you spend monthly on car insurance? ",
                                 font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_car_insurance.grid(row=30, column=1, padx=10, pady=10)
monthly_car_insurance.place(x=35, y=634)

monthly_child_care = tk.Label(root, justify="left", text="How much do you spend monthly on child care? ",
                              font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_child_care.grid(row=32, column=1, padx=10, pady=10)
monthly_child_care.place(x=35, y=675)

monthly_insurance = tk.Label(root, justify="left", text="How much do you spend on monthly on insurance? Ex: Health, "
                                                        "Life, "
                                                        "Dental, "
                                                        "Vision, etc.", font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_insurance.grid(row=0, column=2, padx=10, pady=10)
monthly_insurance.place(x=855, y=50)

monthly_entertainment = tk.Label(root, justify="left", text="How much do you spend monthly on entertainment? Ex "
                                                            "Dining, Movies, "
                                                            "Shows, etc",
                                 font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_entertainment.grid(row=2, column=2, padx=10, pady=10)
monthly_entertainment.place(x=855, y=92)

monthly_miscellaneous = tk.Label(root, justify="left", text="How much do you spend on miscellaneous expenses per "
                                                            "month? ", font=('Times', 13, "bold"),bg="SeaGreen1", fg="midnight blue")
monthly_miscellaneous.grid(row=4, column=2, padx=10, pady=10)
monthly_miscellaneous.place(x=855, y=135)

# Entry Boxes for answers
User_name_entry = tk.Entry(root, font=('Arial', 12, "bold"))
User_name_entry.grid(row=3, column=1, columnspan=1)
User_name_entry.configure(width=71,bg="snow", fg="midnight blue", highlightbackground="SeaGreen1")
User_name_entry.place(x=35, y=75)

Month_entry = tk.Entry(root, font=('Arial', 12, "bold"))
Month_entry.grid(row=5, column=1, columnspan=1)
Month_entry.configure(width=71)
Month_entry.place(x=35, y=120)

Year_entry = tk.Entry(root, font=('Arial', 12, "bold"))
Year_entry.grid(row=7, column=1, columnspan=1)
Year_entry.configure(width=71)
Year_entry.place(x=35, y=165)

monthly_goal_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_goal_entry.grid(row=9, column=1, columnspan=1)
monthly_goal_entry.configure(width=71)
monthly_goal_entry.place(x=35, y=208)

monthly_check_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_check_entry.grid(row=11, column=1, columnspan=1)
monthly_check_entry.configure(width=71)
monthly_check_entry.place(x=35, y=250)

monthly_rent_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_rent_entry.grid(row=13, column=1, columnspan=1)
monthly_rent_entry.configure(width=71)
monthly_rent_entry.place(x=35, y=292)

monthly_utilities_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_utilities_entry.configure(width=71)
monthly_utilities_entry.grid(row=15, column=1, columnspan=1)
monthly_utilities_entry.place(x=35, y=332)

monthly_cable_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_cable_entry.configure(width=71)
monthly_cable_entry.grid(row=17, column=1, columnspan=1)
monthly_cable_entry.place(x=35, y=373)

monthly_phone_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_phone_entry.configure(width=71)
monthly_phone_entry.grid(row=19, column=1, columnspan=1)
monthly_phone_entry.place(x=35, y=414)

monthly_food_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_food_entry.configure(width=71)
monthly_food_entry.grid(row=21, column=1, columnspan=1)
monthly_food_entry.place(x=35, y=454)

monthly_travel_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_travel_entry.configure(width=71)
monthly_travel_entry.grid(row=23, column=1, columnspan=1)
monthly_travel_entry.place(x=35, y=494)

monthly_wardrobe_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_wardrobe_entry.configure(width=71)
monthly_wardrobe_entry.grid(row=25, column=1, columnspan=1)
monthly_wardrobe_entry.place(x=35, y=535)

monthly_subscription_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_subscription_entry.configure(width=71)
monthly_subscription_entry.grid(row=27, column=1, columnspan=1)
monthly_subscription_entry.place(x=35, y=576)

monthly_car_note_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_car_note_entry.configure(width=71)
monthly_car_note_entry.grid(row=29, column=1, columnspan=1)
monthly_car_note_entry.place(x=35, y=615)

monthly_car_insurance_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_car_insurance_entry.configure(width=71)
monthly_car_insurance_entry.grid(row=31, column=1, columnspan=1)
monthly_car_insurance_entry.place(x=35, y=655)

monthly_child_care_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_child_care_entry.configure(width=71)
monthly_child_care_entry.grid(row=33, column=1, columnspan=1)
monthly_child_care_entry.place(x=35, y=696)

monthly_insurance_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_insurance_entry.configure(width=71)
monthly_insurance_entry.grid(row=1, column=2, columnspan=2)
monthly_insurance_entry.place(x=855, y=72)

monthly_entertainment_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_entertainment_entry.configure(width=71)
monthly_entertainment_entry.grid(row=3, column=2, columnspan=2)
monthly_entertainment_entry.place(x=855, y=115)

monthly_miscellaneous_entry = tk.Entry(root, font=('Arial', 12, "bold"))
monthly_miscellaneous_entry.configure(width=71)
monthly_miscellaneous_entry.grid(row=5, column=2, columnspan=2)
monthly_miscellaneous_entry.place(x=855, y=160)

def calculate():

    global month_amount, year_amount, monthly_goal_amount, monthly_check_amount, monthly_rent_amount, monthly_utilities_amount \
        , monthly_cable_amount, monthly_phone_amount,monthly_food_amount, monthly_travel_amount, monthly_wardrobe_amount \
        , monthly_subscription_amount, monthly_car_note_amount, monthly_car_insurance_amount, monthly_entertainment_amount \
        , monthly_miscellaneous_amount, discretionary_amount



    month_amount = int(Month_entry.get())
    year_amount = int(Year_entry.get())
    monthly_goal_amount = int(monthly_goal_entry.get())
    monthly_check_amount = int(monthly_check_entry.get())
    monthly_rent_amount = int(monthly_rent_entry.get())
    monthly_utilities_amount = int(monthly_utilities_entry.get())
    monthly_cable_amount = int(monthly_cable_entry.get())
    monthly_phone_amount = int(monthly_phone_entry.get())
    monthly_food_amount = int(monthly_food_entry.get())
    monthly_travel_amount = int(monthly_travel_entry.get())
    monthly_wardrobe_amount = int(monthly_wardrobe_entry.get())
    monthly_subscription_amount = int(monthly_subscription_entry.get())
    monthly_car_note_amount = int(monthly_car_note_entry.get())
    monthly_car_insurance_amount = int(monthly_car_insurance_entry.get())
    monthly_child_care_amount = int(monthly_child_care_entry.get())
    monthly_insurance_amount = int(monthly_insurance_entry.get())
    monthly_entertainment_amount = int(monthly_entertainment_entry.get())
    monthly_miscellaneous_amount = int(monthly_miscellaneous_entry.get())

    discretionary_amount = int(
        monthly_check_amount - monthly_rent_amount - monthly_utilities_amount - monthly_cable_amount \
        - monthly_phone_amount - monthly_food_amount - monthly_travel_amount \
        - monthly_wardrobe_amount - monthly_subscription_amount - monthly_car_note_amount \
        - monthly_car_insurance_amount - monthly_child_care_amount - monthly_insurance_amount \
        - monthly_entertainment_amount - monthly_miscellaneous_amount)

    if discretionary_amount == monthly_goal_amount:
        on_par_label = tk.Label(root,
                                text=f"{User_name_entry.get()} your leftover amount is ${str(discretionary_amount)} and "
                                     f"your monthly savings goal is ${monthly_goal_entry.get()}. You're on par with "
                                     f"your savings goal "
                                     f"let's see if you can cut down more expenses.",
                                font=('Times', 13, "bold"), wraplength=600, justify="left", bg="SeaGreen1", fg="midnight blue")
        on_par_label.place(x=900, y=260)

    elif discretionary_amount < monthly_goal_amount:
        lower_amt_label = tk.Label(root,
                                   text=f"{User_name_entry.get()} let's look again at your budget and find a more "
                                        f"realistic number that you "
                                        f"can save. Currently your leftover amount of ${discretionary_amount} is a "
                                        f"lower than "
                                        f"your monthly savings goal of ${monthly_goal_amount}.",
                                   font=('Times', 13, "bold"), wraplength=600, justify="left", bg="SeaGreen1", fg="midnight blue")
        lower_amt_label.place(x=900, y=260)

    else:
        higher_amt_label = tk.Label(root, text=f"{User_name_entry.get()} you should easily be able to make your "
                                               f"savings goal. Your leftover amount of" \
                                               f" ${discretionary_amount} is more than your monthly savings goal of ${monthly_goal_amount}.",
                                    font=('Times', 13, "bold"), wraplength=600, justify="left", bg="SeaGreen1", fg="midnight blue")
        higher_amt_label.place(x=900, y=260)


def weekly_amt():
    days_in_month = int(monthrange(month=month_amount, year=year_amount)[1])

    daily_savings = int(int(monthly_goal_entry.get()) / days_in_month)

    weekly_savings = daily_savings * 7

    weekly_amt_message_box = messagebox.askyesno(title="Weekly Savings amount",
                                                 message="Would you like to know how much "
                                                         "you need to "
                                                         "save weekly to reach your "
                                                         "savings goal")

    if weekly_amt_message_box == "Yes" or "yes":
        if discretionary_amount >= monthly_goal_amount:
            weekly_amt_label_yes = tk.Label(root, text=f"{User_name_entry.get()} you need to save ${weekly_savings} "
                                                       f"weekly in order to reach your savings goal.",
                                            font=('Times', 13, "bold"), wraplength=600, justify="left", bg="SeaGreen1", fg="midnight blue")
            weekly_amt_label_yes.place(x=900, y=400)
    else:
        weekly_amt_label_no = tk.Label(root, text=f"{User_name_entry.get()} it looks like your leftover amount of "
                                                  f"${discretionary_amount} is lower than your monthly goal of "
                                                  f"${monthly_goal_amount}. Take some time and revisit your expenses "
                                                  f"so we can reach a more realistic goal.", font=('Times', 13, "bold"),
                                       wraplength=600, justify="left", bg="SeaGreen1", fg="midnight blue")
        weekly_amt_label_no.place(x=900, y=400)
        sys.exit()


Calculate_button = tk.Button(text="Calculate", command= calculate, bg="#118C4F", fg="snow",
                             font=("Times", 22, 'bold'))
Calculate_button.place(x=1100, y=195)

Weekly_amt_button = tk.Button(text="Weekly Savings Amount", command=weekly_amt, bg="goldenrod", fg="snow",
                              font=('Times', 22, "bold"))
Weekly_amt_button.place(x=1015, y=330)

root.mainloop()


