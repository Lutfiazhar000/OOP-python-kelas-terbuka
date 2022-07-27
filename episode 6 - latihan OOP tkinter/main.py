import tkinter

main_window = tkinter.Tk()

label = tkinter.Label(main_window, text = "label") 
label2 = tkinter.Label(main_window, text = "label2")

tombol = tkinter.Button(main_window, text = "tombol")
tombol2 = tkinter.Button(main_window, text = "tombol2") # .Label dan .Button adalah class

# method positioning
label.pack() # .pack adalah method
label2.pack()
tombol.pack()
tombol2.pack()

# method menampilakan GUI
main_window.mainloop()