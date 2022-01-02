import os
import csvreading
import tkinter as tk
from tkinter import filedialog

def createStatsWindow():
    canvas1.pack_forget()
    stats = tk.Canvas(root, width = 400, height = 300)
    stats.pack()

    # Title Text
    nametext = tk.Label(root, text="CSV Contents")
    stats.create_window(200, 80, window=nametext)

    # Average Points
    points = tk.Label(root, text="Average Points: " + str(round(csvreading.average_points(100), 2)))
    stats.create_window(200, 100, window=points)

    # Average Matches
    matches = tk.Label(root, text="Average Matches: " + str(round(csvreading.average_matches(100), 2)))
    stats.create_window(200, 120, window=matches)

    # Average Wins
    wins = tk.Label(root, text="Average Wins: " + str(round(csvreading.average_wins(100), 2)))
    stats.create_window(200, 140, window=wins)

    # Average Kills
    kills = tk.Label(root, text="Average Kills: " + str(round(csvreading.average_kills(100), 2)))
    stats.create_window(200, 160, window=kills)

    # Average Placement
    placement = tk.Label(root, text="Average Placement: " + str(round(csvreading.average_place(100), 2)))
    stats.create_window(200, 180, window=placement)

    #Go Back Button
    goback = tk.Button(text='Go Back', command=lambda:[mainWindow(), stats.destroy()])
    stats.create_window(40, 280, window=goback)

# Re-shows the main menu and hides the stats menu
def mainWindow():
    canvas1.pack()

# Prompts the user to select a csv file
def uploadAction():
    filename = filedialog.askopenfilename()
    file_extension = os.path.splitext(str(filename))
    if file_extension[1] != ".csv":
        uploadAction()
    else:
        createStatsWindow()

# Creation of main window with title
root = tk.Tk()
root.title("FortniteDataTracking")

# Makes windows 400x300
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

# Creates the label and button on screen
entrytext = tk.Label(root, text="Upload a csv file...")
canvas1.create_window(200, 140, window=entrytext)

filebutton = tk.Button(text='Open', command=uploadAction)
canvas1.create_window(200, 160, window=filebutton)

# Disables window resizing and opens the window
root.resizable(False, False)
root.mainloop()