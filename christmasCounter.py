"""
Turkish: Bu Program yanlızca yılbaşına bir gün kala kullanılabilir.
English: This Program can only be used one day before Christmas.



"""



from tkinter import *
from tkinter import messagebox
from datetime import datetime


newYear = datetime.now().year + 1
newYear = datetime(newYear, 1, 1,  0, 0, 0)



def myApp():
    labels = [l_Hour, l_Minute, l_Second]

    global newYear
    now = datetime.now()
    remaining_time = newYear - now

    rMonth = int(remaining_time.days / 30)
    rYear = int(rMonth / 12)
    rSecond = remaining_time.seconds % 60
    rMinute = int(remaining_time.seconds / 60) % 60
    rHour = int(remaining_time.seconds / 60) // 60
    resultList = [rHour, rMinute, rSecond]

    for i in range(len(labels)):
        labels[i].config(text=resultList[i])
    
    
    if sum((rYear, rMonth, remaining_time.days)) !=0:
        m = messagebox.showinfo("Progran", f"Bu Program yanlızca\nYıl başına 1 gün Kala{datetime.now().year}/12/31\nGünü Kullanılabilir\n")
        if m == "ok":
            __import__("time").sleep(5)
            quit()
    elif sum(resultList)==0:
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
myFrame.pack(anchor="center", pady=(70, 0))

# Define the Fonts
myFont = ("Gigi Normal", 40, "bold")
textFont = ("Gigi Normal", 20,"italic")

labelColors = {"bg": 'white', "fg": 'gray'}

# Define an Labels
l_HourText = Label(myFrame, text="Hour", bg=labelColors["bg"], fg=labelColors["fg"], font=textFont)
l_HourText.grid(row=0, column=0, padx=20, pady=20)

l_MinuteText = Label(myFrame, text="Minute", bg=labelColors["bg"], fg=labelColors["fg"], font=textFont)
l_MinuteText.grid(row=0, column=1, padx=20, pady=20)

l_SecondText= Label(myFrame, text="Second", bg=labelColors["bg"], fg=labelColors["fg"], font=textFont)
l_SecondText.grid(row=0, column=2, padx=20, pady=20)





l_Hour = Label(myFrame, text="Hour", bg=labelColors["bg"], fg=labelColors["fg"], font=myFont)
l_Hour.grid(row=1, column=0, padx=20)

l_Minute = Label(myFrame, text="Minute", bg=labelColors["bg"], fg=labelColors["fg"], font=myFont)
l_Minute.grid(row=1, column=1, padx=20)

l_Second = Label(myFrame, text="Second", bg=labelColors["bg"], fg=labelColors["fg"], font=myFont)
l_Second.grid(row=1, column=2, padx=20)

myApp()



root.mainloop()
