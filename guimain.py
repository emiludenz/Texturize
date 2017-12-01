import tkinter as tk
import moviecut
import timeformatter

def main():
    root = tk.Tk()
    num = 5.6
    w = tk.Label(root, textvariable=str(num))

    con_button = tk.Button(root, text="Convert", command=timeformatter.format_time(num), )

    w.pack()
    con_button.pack()
    root.mainloop()


if __name__ == "__main__":
    main()