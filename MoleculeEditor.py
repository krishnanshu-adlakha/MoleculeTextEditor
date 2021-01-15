from guizero import *
from tkinter import filedialog

def save_as():
    global open_file_name
    global text
    save_as_file = filedialog.asksaveasfilename(title="Save As",defaultextension=".*",filetypes=(("Text files","*.txt"),("HTML files","*.html"),("Python files","*.py"),("All files","*.*")))
    open_file_name = save_as_file
    if save_as_file:
        file = open(save_as_file,"w")
        file.write(text.value)
        app.title = save_as_file + " - Molecule"
        file.close()
def save():
    global open_file_name
    global text
    if open_file_name and app.title != "Untitled - Molecule":
        file = open(open_file_name,"w")
        file.write(text.value)
        app.info("File saved","Your file was saved successfully!")
    else:
        save_as()

def open_file():
    global text
    global open_file_name
    save_changes = app.yesno("Save file","Do you want to save any changes made to this file?")
    if save_changes:
        save()
    file_open = filedialog.askopenfilename(title="Open file",filetypes=(("Text files","*.txt"),("HTML files","*.html"),("Python files","*.py"),("All files","*.*")))
    try:
        if file_open:
            file = open(file_open,"r")
            open_file_name = file_open
            app.title = file_open + " - Molecule"
            file_contents = file.read()
            text.value = file_contents
            file.close()
    except:
        app.error("File error","Cannot open files of selected type.")

def new():
    global text
    save_changes = app.yesno("Save file","Do you want to save any changes made to this file?")
    if save_changes:
        save()
    text.value = ""
    app.title = "Untitled - Molecule"

def info():
    app.info("Info","Molecule Text Editor v1.0\nCreated by Dragon Rider Tech")

def help():
    app.info("Help","Molecule is an amzing text editor with all the features you need and more.\n\nHere are some tips:\n\nYou can use the mouse wheel to scroll up and down.\n\nYou can go to Settings -> Font settings to change the style and colour of your text.\n\nCtrl + C to copy\n\nCtrl + V to paste\n\nTo exit the application, just click Exit on the menu.")

def change_colour(colour):
    global text
    text.text_color = colour

def change_font(font):
    global text
    text.font = font

def change_size(size):
    global text
    text.text_size = size

def settings():
    global text
    window = Window(app,title="Molecule - Font Settings")
    title = Text(window,text="Font Settings",size=20,font="Arial")
    slider = Slider(window,1,50,command=change_size)
    colour = Combo(window,command=change_colour,selected=text.text_color,options=["black","white","red","green","blue","orange","turquoise","light green","cyan","yellow"])
    font = Combo(window,command=change_font,selected=text.font,options=["Arial","Verdana","Courier","Courier New","Calbiri","Times New Roman","Comic Sans MS","Impact"])

#Create app with menu bar and textbox
app = App(title="Molecule",width=1000,height=500)
open_file_name = False
menubar = MenuBar(app,
                  toplevel=["File", "Settings","Exit"],
                  options=[
                      [ ["Save As", save_as], ["Save", save],["Open",open_file],["New",new]],
                      [ ["Font settings",settings],["Info",info],["Help",help] ],
                      [ ["Exit",exit] ]
                  ])
text = TextBox(app,multiline=True,width="fill",height="fill")
app.display()
