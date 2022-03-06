from random import *
from threading import local
from tkinter import *
from tkinter import messagebox

from numpy import append

click = 0
click_chance = 0

# generation of random chance number

def generate_chance_number():
    global click_chance
    click_chance += 1
    random_num = ["1", "2", "3",
                  "4", "5", "6",
                  "7", "8", "9",
                  "10"]
    chance_number = choice(random_num)

    numc_entry.delete(0, END)
    numc_entry.insert(0, chance_number)
    with open("chance_number.txt", "a+") as file:
        for chance_numbers in chance_number:
            file.write(str(chance_numbers))
        file.write("\n")
        file.close()

    chance_number = str(chance_number)

    if click_chance == 1:
        switch2()
        message = messagebox.askyesno(
            title="Info message", message="Votre chiffre chance :\n " + chance_number + " !")
        if message == True:
            message

# generation of random email
def generate_norm_num():
    global click
    click += 1
    list_ran_num = {"Your First Number": [], "Your Second Number": [],
                    "Your Third Number": [], "Your Four Number": [],
                    "Your Five Number": []
                    }
    random_num = ["1", "2", "3",
                  "4", "5", "6",
                  "7", "8", "9",
                  "10", "11", "12",
                  "13", "14", "15",
                  "16", "17", "18",
                  "19", "20", "21",
                  "22", "23", "24",
                  "25", "26", "27",
                  "28", "29", "30",
                  "31", "32", "33",
                  "34", "35", "36",
                  "37", "38", "39",
                  "40", "41", "42",
                  "43", "44", "45",
                  "46", "47", "48",
                  "49"]
    ran_num1 = choice(random_num)
    ran_num2 = choice(random_num)
    ran_num3 = choice(random_num)
    ran_num4 = choice(random_num)
    ran_num5 = choice(random_num)

    ran_num = (ran_num1, ran_num2, ran_num3, ran_num4, ran_num5)

    list_ran_num["Your First Number"].append(ran_num1)
    list_ran_num["Your Second Number"].append(ran_num2)
    list_ran_num["Your Third Number"].append(ran_num3)
    list_ran_num["Your Four Number"].append(ran_num4)
    list_ran_num["Your Five Number"].append(ran_num5)

    num_entry.delete(0, END)
    num_entry.insert(0, ran_num)
    with open("norm_num.txt", "a+") as file:
        for ran_nums in ran_num:
            file.write(ran_nums)
            file.write(" , ")
        file.write("\n")
        file.close()

    list_ran_nums = str(list_ran_num)
    if click == 1:
        switch()
        message = messagebox.askyesno(
            title="Info message", message="Vos 5 chiffres :\n " + list_ran_nums + " !")
        if message == True:
            message

def switch():
    if num_bttn["state"] == NORMAL:
        num_bttn["state"] = DISABLED
    else:
        num_bttn["state"] = NORMAL

def switch2():
    if numc_bttn["state"] == NORMAL:
        numc_bttn["state"] = DISABLED
    else:
        numc_bttn["state"] = NORMAL

def restart():
    num_bttn["state"] = NORMAL
    numc_bttn["state"] = NORMAL
    num_entry.delete(0, END)
    num_entry.insert(0, "")
    numc_entry.delete(0, END)
    numc_entry.insert(0, "")

root = Tk()
root.title("Loto Number generator")
root.geometry("900x300")
root.config(bg="lightblue")

label1 = Label(root, text="normal number", font="Poppins 20",
               bg="lightblue", fg="#151515")
label1.grid(row=0, column=0, pady=25)

label2 = Label(root, text="chance number", font="Poppins 20",
               bg="lightblue", fg="#151515")
label2.grid(row=0, column=3, pady=25)

numc_entry = Entry(root, font="Poppins 18", fg="#151515", width=2)
numc_entry.grid(row=1, column=3,  pady=10)

num_entry = Entry(root, font="Poppins 18", fg="#151515", width=16)
num_entry.grid(row=1, column=0,  pady=10)

num_bttn = Button(root, text="Generate 5 normal number",
                  font="Poppins 18", fg="#151515", command=generate_norm_num)
num_bttn.grid(row=2, column=0,  pady=10)

numc_bttn = Button(root, text="Generate chance number", font="Poppins 18",
                   fg="#151515", command=generate_chance_number)
numc_bttn.grid(row=2, column=3,  pady=10)

label_cre = Label(root, text="Created by Exarven", font="Poppins 18 ")
label_cre.grid(row=4, column=2, pady=10)

quit = Button(root, text="QUIT", font="Poppins 18 ", command=quit)
quit.grid(row=3, column=1)

restarte = Button(root, text="Restart", font="Poppins 18 ",
                  command=restart).grid(row=3, column=2)
root.mainloop()
