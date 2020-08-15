import tkinter as tk
from tkinter import messagebox as msg

main = tk.Tk()
main.title('Calculator')
#main.iconbitmap('ICON_PATH')
main.geometry('265x240')
main.resizable(0,0)


# FUNCTIONS
def close():
    if msg.askyesno(title='Exit', message='Are You Sure To Exit?'):
        main.destroy()
    else:
        pass

main.protocol("WM_DELETE_WINDOW", close)

def key(k):
    if nums.get() == 'Invalid Input':
        nums.set('')
    
    pre = nums.get()
    nums.set(pre + str(k))

def clrscr():
    nums.set('')

def calc():
    if nums.get() == '':
        pass
    elif nums.get()[-1] in ['+', '-', '*', '/']:
        pass
    else:
        try:
            nums.set(eval(nums.get()))
        except:
            nums.set('Invalid Input')

def back():
    nums.set(nums.get()[:-1])

# FRAMES
frame1 = tk.Frame(master=main)
frame2 = tk.Frame(master=main)
frame3 = tk.Frame(master=main)

# DISPLAY
nums = tk.StringVar()
display = tk.Entry(master=frame1,font=(10), textvariable=nums)
display.config(state=tk.DISABLED)
display.pack(pady=10, padx=10, fill=tk.X, ipady=5, expand=True)

B_PADX = 2
B_PADY = 2

# BUTTONS
btn7 = tk.Button(master=frame2, text='7', width=5, height=2, command=lambda: key(7)).grid(row=0, column=0, padx=B_PADX, pady=B_PADY)
btn8 = tk.Button(master=frame2, text='8', width=5, height=2, command=lambda: key(8)).grid(row=0, column=1, padx=B_PADX, pady=B_PADY)
btn9 = tk.Button(master=frame2, text='9', width=5, height=2, command=lambda: key(9)).grid(row=0, column=2, padx=B_PADX, pady=B_PADY)

btn4 = tk.Button(master=frame2, text='4', width=5, height=2, command=lambda: key(4)).grid(row=1, column=0, padx=B_PADX, pady=B_PADY)
btn5 = tk.Button(master=frame2, text='5', width=5, height=2, command=lambda: key(5)).grid(row=1, column=1, padx=B_PADX, pady=B_PADY)
btn6 = tk.Button(master=frame2, text='6', width=5, height=2, command=lambda: key(6)).grid(row=1, column=2, padx=B_PADX, pady=B_PADY)

btn1 = tk.Button(master=frame2, text='1', width=5, height=2, command=lambda: key(1)).grid(row=2, column=0, padx=B_PADX, pady=B_PADY)
btn2 = tk.Button(master=frame2, text='2', width=5, height=2, command=lambda: key(2)).grid(row=2, column=1, padx=B_PADX, pady=B_PADY)
btn3 = tk.Button(master=frame2, text='3', width=5, height=2, command=lambda: key(3)).grid(row=2, column=2, padx=B_PADX, pady=B_PADY)

btn0 = tk.Button(master=frame3, text='0', width=12, height=2, command=lambda: key(0)).grid(row=0, column=0, padx=B_PADX, pady=B_PADY)
btnd = tk.Button(master=frame3, text='.', width=5, height=2, command=lambda: key('.')).grid(row=0, column=1, padx=B_PADX, pady=B_PADY)

btn_div = tk.Button(master=frame2, text='/', width=5, height=2, command=lambda: key('/')).grid(row=1, column=3, padx=B_PADX, pady=B_PADY)
btn_mul = tk.Button(master=frame2, text='*', width=5, height=2, command=lambda: key('*')).grid(row=1, column=4, padx=B_PADX, pady=B_PADY)
btn_sub = tk.Button(master=frame2, text='-', width=5, height=2, command=lambda: key('-')).grid(row=2, column=3, padx=B_PADX, pady=B_PADY)
btn_add = tk.Button(master=frame2, text='+', width=5, height=2, command=lambda: key('+')).grid(row=2, column=4, padx=B_PADX, pady=B_PADY)

btn_clr = tk.Button(master=frame2, text='<-', width=5, height=2, command=back).grid(row=0, column=3, padx=B_PADX, pady=B_PADY)
btn_clr = tk.Button(master=frame2, text='CLR', width=5, height=2, command=clrscr).grid(row=0, column=4, padx=B_PADX, pady=B_PADY)
btn_eql = tk.Button(master=frame3, text='=', width=12, height=2, command=calc).grid(row=0, column=2, padx=B_PADX, pady=B_PADY)

# PACK FRAMES
frame1.pack(fill=tk.X, side=tk.TOP)
frame2.pack(fill=tk.X, padx=10)
frame3.pack(fill=tk.X, padx=10)

main.mainloop()
