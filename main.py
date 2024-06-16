from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import webbrowser
import os
from tkinter import ttk

root = Tk()
root.minsize("650","650")
root.maxsize("650","650")

label_file_name = Label(root, text="File Name")
label_file_name.place(relx = 0.28,rely=0.03,anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

elements=["sanitation"]
selectedval = StringVar()
dropdown=ttk.Combobox(root,state="readonly",values=elements,textvariable=selectedval)
dropdown.place(relx=0.7,rely=0.03,anchor=CENTER)

my_text = Text(root, height=35, width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name = ""
code =  ""

def woah():
    global elements
    elements=selectedval.get()
    if elements == "sanitation":
        my_text.delete(1.0, END)
        cool=open('test2.txt', 'r')
        content=cool.read()
        my_text.insert(1.0,content)
    

def openfile():
        global name
        my_text.delete(1.0, END)
        input_file_name.delete(0, END)
        text_file = filedialog.askopenfilename(title=" Open File", filetypes = (("html files", "*.html"),))
        print(text_file)
        name = os.path.basename(text_file)
        formated_name = name.split('.')[0]
        input_file_name.insert(END, formated_name)
        root.title(formated_name)
        text_file = open(name, 'r')
        paragraph=text_file.read()
        my_text.insert(END, paragraph)
        text_file.close()
    
def save(): 
    global input_file_name
    if input_file_name =="":
        input_file_name = "index"
    else:    
        input_name = input_file_name.get()
        file = open(input_name+".html", "w")
        data =  my_text.get("1.0",  END)
        print(data)
        file.write(data)
        input_file_name.delete(0, END)
        my_text.delete(1.0, END)
        messagebox.showinfo("Update", "Success")
    
    
def exitfile():
    webbrowser.open(name)
    root.destroy()
    

    
open_button= Button(root, text="OpenFile",command=openfile )
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button= Button(root, text="SaveFile",command=save )
save_button.place(relx=0.10,rely=0.03,anchor=CENTER)
exit_button= Button(root,text="Exit File",command=exitfile )
exit_button.place(relx=0.15,rely=0.03,anchor=CENTER)
BtnAi = Button(root,text="Create!",foreground="green",background="#ffcc66",font=(25),command=woah)
BtnAi.place(relx=0.7,rely=0.08,anchor=CENTER )

root.mainloop() 