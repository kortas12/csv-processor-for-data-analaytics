# packages importing
from source import processData
from tkinter import ttk, filedialog, Tk, messagebox

# welcome, Page
welcome = {"window": Tk()}
welcome["window"].title("Data processor")
welcome["window"].configure(border=8)
welcome["window"].resizable(False, False)

welcome["message"] = ttk.Label(welcome["window"],
                               text="                     welcome to\n                   data processor                       \n")
welcome["message"].grid(row=0, column=0)

welcome["button"] = ttk.Button(welcome["window"], text="start")
welcome["button"].grid(row=1, column=0)


# work page
pathIn = ""
pathOut = ""
def getWork():
    welcome["window"].destroy()

    home = {"window": Tk()}
    home["window"].title("Data processor")
    home["window"].configure(border=8)
    home["window"].resizable(False, False)

    home["pathIn"] = [ttk.Label(home["window"], text="load from"), ttk.Combobox(home["window"], state="readonly"), ttk.Button(home["window"], text="Browse")]
    home["pathIn"][0].grid(row=0, column=0)
    home["pathIn"][1].grid(row=0, column=1)
    home["pathIn"][2].grid(row=0, column=2)

    home["pathOut"] = [ttk.Label(home["window"], text="save as"), ttk.Combobox(home["window"], state="readonly"), ttk.Button(home["window"], text="Browse")]
    home["pathOut"][0].grid(row=1, column=0)
    home["pathOut"][1].grid(row=1, column=1)
    home["pathOut"][2].grid(row=1, column=2)

    home["workButton"] = ttk.Button(home["window"], text="play", state="disabled")
    home["workButton"].grid(row=2, column=1)

    def inBrowse():
        global pathIn
        pathIn = filedialog.askopenfilename(title="data processor", filetypes=[("csv file", "csv")])
        if len(pathIn) > 0:
            home["pathIn"][1].set(pathIn)

    def outBrowse():
        global pathOut
        pathOut = filedialog.asksaveasfilename(title="data processor", filetypes=[("csv file", "csv")])
        if len(pathOut) > 0:
            home["pathOut"][1].set(pathOut)

    def work():
        processData(pathOut, pathIn)

        messagebox.showinfo(title="data processor", message=f"operation done successfully\ncheck {home["pathOut"][1].get()} to see the result")

    home["pathIn"][2].configure(command=inBrowse)
    home["pathOut"][2].configure(command=outBrowse)
    home["workButton"].configure(command=work)

    while True:
        if not pathIn == "":
            if not pathOut == "":
                home["workButton"].state(["!disabled"])

        home["window"].update()


welcome["button"].config(command=getWork)
welcome["window"].mainloop()
