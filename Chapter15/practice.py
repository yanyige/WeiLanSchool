# F = float(input("请输入华氏温度值："))
# C = (5 / 9) * (F - 32)
# print("对应的摄氏温度为：", format(C, ".2f"))
import tkinter as tk
import tkinter.messagebox
win = tk.Tk()
win.geometry("250x140")
win.title("no compose window")


var_F = tk.DoubleVar()
var_F.set(0)
var_C = tk.DoubleVar()
var_C.set(0)

# 2 label
labF = tk.Label(win, text="华氏温度:", width=80)
labC = tk.Label(win, text="摄氏温度:", width=80)

# 2 entry
entF = tk.Entry(win, width=100, textvariable=var_F)
entC = tk.Entry(win, width=100, textvariable=var_C)


def F2C():
    f = float(entF.get())
    c = float((5 / 9) * (f - 32))
    tk.messagebox.showinfo(title="F2C", message=c)


def C2F():
    c = float(entC.get())
    f = float((9 / 5 * c) + 32)
    return tk.messagebox.showinfo(title="C2F", message=f)


# 4 button
butF2C = tk.Button(win, text="F2C", command=F2C)
butC2F = tk.Button(win, text="C2F", command=C2F)

labF.place(x=20, y=10, width=80, height=20)
labC.place(x=20, y=40, width=80, height=20)
entF.place(x=120, y=10, width=80, height=20)
entC.place(x=120, y=40, width=80, height=20)
labF.place(x=20, y=10, width=80, height=20)
butF2C.place(x=30, y=80, width=50, height=20)
butC2F.place(x=100, y=80, width=50, height=20)

win.mainloop()
