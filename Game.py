import ContestantFunctions as c
import random
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry('1500x900')
window.title("MTV's Are You The One?")
window.configure(background = 'white')

greeting = tk.Label(text = "MTV's Are You The One? Simulator",
                    font = ("Arial Bold", 25), bg = 'white')
greeting.pack()

contestants = c.create_contestants()
contestants = c.similarities(contestants)
contestants = c.create_traits(contestants)
for i in range(len(contestants)):
    c1 = contestants[i]
    qualities = c1[3]
    keys = c1[1]
    contestantlabel = tk.Label(window, text = "Name: " + c1[0] + "        Qualities: " + qualities[0] + ", " + qualities[1] +
                               ", " + qualities[2] + ", " + qualities[3] + ", " + qualities[4] + ", " + qualities[5] + "                              Looking For: " + keys[0] + ", " + keys[1] + ", " + keys[2], bg = 'white')
    contestantlabel.pack(side = TOP, anchor = "w")

matches = c.create_matches(contestants)
print(matches)
alternate_matches = c.alternate_match_list(matches)

def get_matches():
    match1 = [c1.get(), c2.get()]
    match2 = [c3.get(), c4.get()]
    match3 = [c5.get(), c6.get()]
    match4 = [c7.get(), c8.get()]
    match5 = [c9.get(), c10.get()]
    match6 = [c11.get(), c12.get()]
    match7 = [c13.get(), c14.get()]
    match8 = [c15.get(), c16.get()]
    user_matches = [match1, match2, match3,
                    match4, match5, match6, match7, match8]
    user_matches = c.user_guesses(contestants, user_matches)
    return user_matches

def check():
    num_correct = c.num_correct(get_matches(), matches, alternate_matches)
    correct_label = tk.Label(
        window, text="Number of Correct Matches: " + str(num_correct), bg='white')
    correct_label.pack(side = TOP)
    if num_correct == 8:
        correct_label = tk.Label(window, text = 'Number of Correct Matches: 8 YOU WON!', bg = 'white')
    truth_booth_couple = c.truth_booth_couple(get_matches())
    couple_name1 = truth_booth_couple[0]
    couple_name2 = truth_booth_couple[1]
    couple_label = tk.Label(window, text="Couple Sent to Truth Booth: " +
                            couple_name1[0] + ' and ' + couple_name2[0], bg ='white')
    couple_label.pack(side = TOP)
    perfect = c.truth_booth(truth_booth_couple, matches, alternate_matches)
    perfect_label = tk.Label(
        window, text='Is This Couple Perfect? ' + str(perfect), bg = 'white')
    perfect_label.pack(side = TOP)

c1 = tk.StringVar()
c1entry = tk.Entry(window, textvariable = c1, width = 10)
c1entry.pack(side = LEFT)
c2 = tk.StringVar()
c2entry = tk.Entry(window, textvariable = c2, width = 10)
c2entry.pack(side = LEFT)
c3 = tk.StringVar()
c3entry = tk.Entry(window, textvariable=c3, width=10)
c3entry.pack(side = LEFT)
c4 = tk.StringVar()
c4entry = tk.Entry(window, textvariable=c4, width=10)
c4entry.pack(side = LEFT)
c5 = tk.StringVar()
c5entry = tk.Entry(window, textvariable=c5, width=10)
c5entry.pack(side = LEFT)
c6 = tk.StringVar()
c6entry = tk.Entry(window, textvariable=c6, width=10)
c6entry.pack(side = LEFT)
c7 = tk.StringVar()
c7entry = tk.Entry(window, textvariable=c7, width=10)
c7entry.pack(side = LEFT)
c8 = tk.StringVar()
c8entry = tk.Entry(window, textvariable=c8, width=10)
c8entry.pack(side = LEFT)
c9 = tk.StringVar()
c9entry = tk.Entry(window, textvariable=c9, width=10)
c9entry.pack(side = LEFT)
c10 = tk.StringVar()
c10entry = tk.Entry(window, textvariable=c10, width=10)
c10entry.pack(side = LEFT)
c11 = tk.StringVar()
c11entry = tk.Entry(window, textvariable=c11, width=10)
c11entry.pack(side = LEFT)
c12 = tk.StringVar()
c12entry = tk.Entry(window, textvariable=c12, width=10)
c12entry.pack(side = LEFT)
c13 = tk.StringVar()
c13entry = tk.Entry(window, textvariable=c13, width=10)
c13entry.pack(side =LEFT)
c14 = tk.StringVar()
c14entry = tk.Entry(window, textvariable=c14, width=10)
c14entry.pack(side = LEFT)
c15 = tk.StringVar()
c15entry = tk.Entry(window, textvariable=c15, width=10)
c15entry.pack(side = LEFT)
c16 = tk.StringVar()
c16entry = tk.Entry(window, textvariable=c16, width=10)
c16entry.pack(side = LEFT)

submit = tk.Button(window, text="Submit", command=get_matches)
submit.pack(side=LEFT, anchor='w')

checkbutton = tk.Button(window, text = 'Check', command = check)
checkbutton.pack(side = LEFT, anchor = 'w')

window.mainloop()
