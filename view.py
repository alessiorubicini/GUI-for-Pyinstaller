from tkinter import *
from tkinter import messagebox
import webbrowser
#import controller as c


# Interfaccia grafica
class View(object):

    def __init__(self):
        global win

        win = Tk()

    # Metodo costruttore
    def window(self, c):
        global win
        
        # Creazione finestra
        #win = Tk()
        win.title("Pyinstaller GUI - Version 2.0")
        win.resizable(False, False)
        win.config(bg="white")

        rect1 = Frame(win, bg="firebrick3", height=100, width=660, borderwidth=6, relief=GROOVE)
        rect1.grid(row=0, column=0, columnspan=5, pady=10)
        title = Label(win, text='PyInstaller GUI - Version 2.0\nDeveloped by Alessio Rubicini', bg='firebrick3', fg='white', font='Arial-Rounded 17 bold')
        title.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        
        rect2 = Frame(win, bg="firebrick3", height=250, width=660, borderwidth=6, relief=GROOVE)
        rect2.grid(row=1, column=0, rowspan=3, columnspan=5, padx=10)
        info_text = Label(win, text='To use this software you must have installed\nthe Pyinstaller module on your computer', bg='firebrick3', fg='white', font='Arial-Rounded 11')
        info_text.grid(row=1, column=0, columnspan=5, padx=20, pady=(30, 10))
        install = Button(win, text="Download and Install", width=20, height=1,  font='Arial 15')
        install.grid(row=2, column=0, columnspan=5, pady=10)
        info = Button(win, text="Info about Pyinstaller", width=20, height=1, command=lambda: webbrowser.open_new("https://www.pyinstaller.org/"), font='Arial 15')
        info.grid(row=3, column=0, columnspan=5,pady=10)


        selectPy = Button(win, text="Select .py file", bg='black', fg='white', font='Arial-Rounded 15')
        selectPy.config(command = c.askFilePy)
        selectPy.grid(row=4, column=0, pady=15, padx=10, rowspan=2)

        selectExtraFiles = Button(win, text="Select extra files", bg='black', fg='white', font='Arial-Rounded 15')
        selectExtraFiles.config(command = c.askExtraFiles)
        selectExtraFiles.grid(row=4, column=1, pady=15, padx=10, rowspan=2)

        # Radiobuttons for export option
        radiobuttons_app = StringVar(value='--onefile')
        onefile_option = Radiobutton(win, text="Single file", variable=radiobuttons_app, value='--onefile', font='Arial 14')
        onefile_option.config(bg='white', fg='black', activeforeground='black', activebackground='white', selectcolor='white', highlightthickness=0)
        onefile_option.grid(row=4, column=2, padx=5, pady=15)
        onedir_option = Radiobutton(win, text="Directory", variable=radiobuttons_app, value='--onedir', font='Arial 14')
        onedir_option.config(bg='white', fg='black', activeforeground='black', activebackground='white', selectcolor='white', highlightthickness=0)
        onedir_option.grid(row=5, column=2, padx=5, pady=15)

        selectDirectory = Button(win, text="Select\noutput directory", bg='black', fg='white', font='Arial-Rounded 13')
        selectDirectory.config(command = c.askOutputDirectory)
        selectDirectory.grid(row=6, column=0, pady=15, padx=10, rowspan=2)

        selectIcon = Button(win, text="Select icon", bg='black', fg='white', font='Arial-Rounded 15')
        selectIcon.config(command = c.askExecutableIcon)
        selectIcon.grid(row=6, column=1, pady=15, padx=10, rowspan=2)

        mode_app = StringVar(value='--windowed')
        onefile_option = Radiobutton(win, text="Console (--console)", variable=mode_app, value='--console', font='Arial 14')
        onefile_option.config(bg='white', fg='black', activeforeground='black', activebackground='white', selectcolor='white', highlightthickness=0)
        onefile_option.grid(row=6, column=2, padx=5, pady=15)
        onedir_option = Radiobutton(win, text="Windowed (--windowed)", variable=mode_app, value='--windowed', font='Arial 14')
        onedir_option.config(bg='white', fg='black', activeforeground='black', activebackground='white', selectcolor='white', highlightthickness=0)
        onedir_option.grid(row=7, column=2, padx=5, pady=15)

        convertFile = Button(win, text="CONVERT", bg="dark olive green", fg="white", font='Arial-Rounded 23')
        convertFile.config(command = lambda : c.convertiFile(radiobuttons_app, mode_app))
        convertFile.grid(row=8, column=0, columnspan=5, pady=20, padx=20)

        win.mainloop()

    # Message error for input variables not specified from the user
    def notDeclared(self, var):
        messagebox.showerror("Error", "{} not specified".format(var))
    

    # Message error for empty path from the user
    def pathError(self, var):
        messagebox.showerror("Error", "You didn't specify any {}".format(var))
    

    # Message error for file conversion
    def conversionError(self):
        messagebox.showerror('Error', 'An error has occurred during the conversion')

    