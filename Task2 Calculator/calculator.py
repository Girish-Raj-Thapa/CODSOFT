from tkinter import *

# Function to handle button clicks
def click(event):
    global scvalue  # Accessing the global variable scvalue
    text = event.widget.cget("text")  # Getting the text from the clicked button
    # If equals button is clicked
    if text == "=":
        # If the current value in the screen is a digit, set it as the result
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        # If it's an expression, evaluate it and set the result
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)  # Set the value in the screen
        screen.update()  # Update the screen
    # If AC button is clicked, reset the screen to 0
    elif text == "AC":
        scvalue.set("0")  # Set the value in the screen to 0
        screen.update()  # Update the screen
    else:
        # If the screen shows 0, replace it with the clicked number/operator
        if scvalue.get() == "0":
            scvalue.set("")
        # Append the clicked number/operator to the screen
        scvalue.set(scvalue.get() + text)
        screen.update()  # Update the screen

# Create main window
root = Tk()
root.geometry("485x540")  # Setting the size of the window
root.title("Calculator App")  # Setting the title of the window
root.configure(bg="black")  # Setting the background color of the window
root.wm_iconbitmap("1.ico")  # Setting the window icon

# StringVar to hold the value displayed on the screen
scvalue = StringVar()
scvalue.set("0")  # Initializing the value to 0

# Entry widget to display the input/output
screen = Entry(root, textvar=scvalue, font="Helvetica 30 bold", bg="#FFCD3A", justify="right")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)  # Packing the screen widget

# Frame for the first row of buttons
f = Frame(root, bg="black")

# Creating and placing buttons for the first row
b = Button(f, text="AC", padx=30, pady=20, font="Helvetica 20 bold", bg="#FFCD3A")
b.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)  # Binding click event to the AC button

b = Button(f, text="**", padx=30, pady=20, font="Helvetica 20 bold", bg="#FFCD3A")
b.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=30, pady=20, font="Helvetica 20 bold", bg="#FFCD3A")
b.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=30, pady=20, font="Helvetica 20 bold", bg="#FF9500")
b.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

f.pack()  # Packing the frame containing the buttons

# Frame for the second row of buttons
f = Frame(root, bg="black")

# Creating and placing buttons for the second row
b = Button(f, text="7", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=30, pady=20, font="Helvetica 20 bold", bg="#FF9500")
b.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

f.pack()  # Packing the frame containing the buttons

# Frame for the third row of buttons
f = Frame(root, bg="black")

# Creating and placing buttons for the third row
b = Button(f, text="4", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=30, pady=20, font="Helvetica 20 bold", bg="#FF9500")
b.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

f.pack()  # Packing the frame containing the buttons

# Frame for the fourth row of buttons
f = Frame(root, bg="black")

# Creating and placing buttons for the fourth row
b = Button(f, text="1", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=30, pady=20, font="Helvetica 20 bold", bg="#FF9500")
b.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

f.pack()  # Packing the frame containing the buttons

# Frame for the fifth row of buttons
f = Frame(root, bg="black")

# Creating and placing buttons for the fifth row
b = Button(f, text="0", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=30, pady=20, font="Helvetica 20 bold", bg="#323232")
b.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=30, pady=20, font="Helvetica 20 bold", bg="#FF9500")
b.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
b.bind("<Button-1>", click)

f.pack()  # Packing the frame containing the buttons

root.mainloop()  # Run the GUI application
