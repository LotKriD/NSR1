from tkinter import *
from tkinter import messagebox
from RPN import *

def clicked():
    try:
        res = solve(txt.get())
        lblRes.configure(text = "Решение: {}".format(res))
    except ZeroDivisionError:
        messagebox.showerror('Ошибка', 'Деление на ноль')
    except:
        messagebox.showerror('Ошибка', 'Неверный ввод')

window = Tk()
window.title("Калькулятор")
window.geometry('480x240')

lbl = Label(window, text = "Пример: ")
lbl.grid(column = 0, row = 0)

txt = Entry(window, width = 50)
txt.grid(column = 1, row = 0)
txt.focus()

lblRes = Label(window, text = "Решение: ")
lblRes.grid(column = 0, row = 1)

btn = Button(window, text = "Решение", command = clicked, height = 10, width = 50)
btn.grid(column = 1, row = 2)
window.mainloop()