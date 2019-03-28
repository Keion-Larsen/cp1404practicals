"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def score_insert():
    global score
    score = float(input("Enter score: "))


score_insert()

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
