from tkinter import *
import tkinter.messagebox

def slider(value):
    r = red_Scale.get()
    g = green_Scale.get()
    b = blue_Scale.get()
    rgb = f"rgb({r}, {g}, {b})"
    codeColor = "#%02x%02x%02x" % (r, g, b)
    colorLab.config(bg=codeColor)
    rgb_entry.delete(0, END)
    rgb_entry.insert(0, rgb)

def onClick():
    tkinter.messagebox.showinfo("Copy to clipboard", f"Your color code {rgb_entry.get()} has successfully copied")
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(rgb_entry.get())
    clip.destroy()

root = Tk()

root.title("RGB Color Picker")
root.geometry("420x424")
root.maxsize(420, 424)
root.minsize(420, 424)

colorLab = Label(root, height=10, width=50, bg="black", bd=1, relief=SUNKEN)
colorLab.pack(pady=5, padx=5)

frame = Frame(root, bd=1, relief=GROOVE)
frame.pack(pady=5)

red_lab = Label(frame, fg="red", font=("ubuntu", 12, "bold"), text="Red")
red_lab.grid(row=0, column=0)
red_Scale = Scale(frame, from_=0, to_=255, length=220, orient=HORIZONTAL, fg="red", command=slider)
red_Scale.grid(row=0, column=1)

green_lab = Label(frame, fg="green", font=("ubuntu", 12, "bold"), text="Green")
green_lab.grid(row=1, column=0)
green_Scale = Scale(frame, from_=0, to_=255, length=220, orient=HORIZONTAL, fg="green", command=slider)
green_Scale.grid(row=1, column=1)

blue_lab = Label(frame, fg="blue", font=("ubuntu", 12, "bold"), text="Blue")
blue_lab.grid(row=2, column=0)
blue_Scale = Scale(frame, from_=0, to_=255, length=220, orient=HORIZONTAL, fg="blue", command=slider)
blue_Scale.grid(row=2, column=1)

frame2 = Frame(root, bd=1, relief=None)
frame2.pack(pady=5)

rgb_lab = Label(frame2, font=("ubuntu", 12, "bold"), fg="purple", text="RGB CODE :")
rgb_lab.grid(row=2, column=0)

rgb_entry = Entry(frame2, width=15, font=("ubuntu", 12), fg="darkorange", borderwidth=0)
rgb_entry.grid(row=2, column=1, padx=5)
rgb_entry.insert(END, "")

copy = Button(frame2, font=("ubuntu", 12, "bold"), bg="black", fg="LavenderBlush", text="Copy", command=onClick, relief=SUNKEN)
copy.grid(row=3, columnspan=3, pady=7)

statusvar = StringVar()
statusvar.set("Developed by- Kunwar Pratap")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, font="ubuntu 11 bold", bg="teal", fg="GhostWhite", padx=10)
sbar.pack(side=BOTTOM, fill=X)

root.mainloop()