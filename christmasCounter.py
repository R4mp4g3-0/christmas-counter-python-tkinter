from tkinter import *
from tkinter import messagebox
from datetime import datetime


newYear = datetime.now().year + 1
newYear = datetime(newYear, 1, 1,  0, 0, 0)



def myApp():
    labels = [l_Year, l_Month, l_Day, l_Hour, l_Minute, l_Second]

    global newYear
    now = datetime.now()
    remaining_time = newYear - now

    rMonth = int(remaining_time.days / 30)
    rYear = int(rMonth / 12)
    rSecond = remaining_time.seconds % 60
    rMinute = int(remaining_time.seconds / 60) % 60
    rHour = int(remaining_time.seconds / 60) // 60
    resultList = [rYear, rMonth, remaining_time.days, rHour, rMinute, rSecond]

    for i in range(6):
        labels[i].config(text=resultList[i])

    if sum(resultList)==0:
        messagebox.showinfo("Progran", "Yeni Yıl Hayırlı olsun")
        return 0

    root.after(1000, myApp)





root = Tk()
root.geometry("570x300+400+150")
root.title("Yılbaşı sayacı")
root.config(bg="gray")
root.minsize("570", "270")


# Define a Frame
myFrame = Frame(root, bg="gray")
myFrame.pack(anchor="center", pady=(100, 0))

# Define a Font
myFont = ("Gigi Normal", 40, "bold")


labelColors = {"bg": 'white', "fg": 'gray'}

# Define an Labels
l_Year = Label(myFrame, text="Year", bg=labelColors["bg"], fg=labelColors["fg"], font=myFont)
l_Year.grid(row=0, column=0, padx=20)

l_Month = Label(myFrame, text="Month", bg=labelColors["bg"], fg=labelColors["fg"], font=myFont)
l_Month.grid(row=0, column=1, padx=20)

l_Day = Label(myFrame, text="Day", bg=labelColors["bg"], fg=labelColors["fg"], font=myFont)
l_Day.grid(row=0, column=2, padx=20)

Label(myFrame, text=":", bg=labelColors["fg"], fg=labelColors["bg"], font=myFont).grid(row=0, column=3, padx=3)

l_Hour = Label(myFrame, text="Hour", bg=labelColors["bg"], fg=labelColors["fg"], font=myFont)
l_Hour.grid(row=0, column=4, padx=20)

l_Minute = Label(myFrame, text="Minute", bg=labelColors["bg"], fg=labelColors["fg"], font=myFont)
l_Minute.grid(row=0, column=5, padx=20)

l_Second = Label(myFrame, text="Second", bg=labelColors["bg"], fg=labelColors["fg"], font=myFont)
l_Second.grid(row=0, column=6, padx=20)

myApp()



root.mainloop()