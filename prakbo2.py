import tkinter

main_window = tkinter.Tk()

tombol1 = tkinter.Button(main_window, text = "match")
tombol2 = tkinter.Button(main_window, text = "pukul")

#method positioning
tombol1.pack()
tombol2.pack()


#method menampilkan GUI
main_window.mainloop()


