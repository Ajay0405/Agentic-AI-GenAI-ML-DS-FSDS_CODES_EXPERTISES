import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("200x100")


# Funcation  to print "Hello , World!" in the consol
def say_hello():
    print("Hello , World!")
    print("wel come to python world!")
    
#Create button that triggers the say_hello funcation   
hello_button = tk.Button(root, text="Click Me", command=say_hello)
hello_button.pack(pady=20) # Pack the button into the window

# Start The Tkinter even loop
root.mainloop()
    


  

