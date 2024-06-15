import tkinter as tk
from tkinter import ttk

check = {'meat': 1, 'milk': 2, 'cheese': 3, 'eggs': 4, 'carrot': 5, 'potato': 6, 'apple': 7, 'banana': 8, 'cherry': 9,
         'orange': 10}
chip = {'meat': 0, 'milk': 0, 'cheese': 0, 'eggs': 0, 'carrot': 0, 'potato': 0, 'apple': 0, 'banana': 0, 'cherry': 0,
        'orange': 0}


def add_clicked(i):
    """добавление в корзину"""
    chip[add_btn[i]['text']] = int(chip.get(add_btn[i]['text'])) + 1
    suml.configure(text=int(suml['text']) + int(check.get(add_btn[i]['text'])))
    choose_list.insert(0, add_btn[i]['text'])


def dell_clicked():
    """удаление из корзины"""
    if choose_list.curselection():
        value = choose_list.curselection()
        i = int(value[0])
        chip[choose_list.get(i)] = int(chip.get(choose_list.get(i))) - 1
        suml.configure(text=int(suml['text']) - int(check.get(choose_list.get(i))))
        choose_list.delete(i)


def pay_clicked():
    """создание чека и очистка старой корзины"""
    cash_receipt.delete(0, tk.END)
    for i in chip:
        if chip.get(i):
            cash_receipt.insert(tk.END,
                                f'{i}:{''.join(['_' for i in range(0, 15 - len(i))])}x{chip.get(i)}__{check.get(i)}$')
            chip[i] = 0
    cash_receipt.insert(tk.END, '====================')
    cash_receipt.insert(tk.END, f'final price:====={suml['text']}$')
    choose_list.delete(0, tk.END)
    suml['text'] = 0


window = tk.Tk()
window.title('market')
window.geometry('600x250')
window.resizable(width=False, height=False)

frame = [tk.Frame(window) for i in range(0, 4)]
frame[0].place(relwidth=0.16, relheight=1)
frame[1].place(relx=0.16, relwidth=0.16, relheight=1)
frame[2].place(relx=0.35, relwidth=0.16, relheight=1)
frame[3].place(relx=0.55, relwidth=0.4, relheight=1)

goods = ['meat', 'milk', 'cheese', 'eggs', 'carrot', 'potato', 'apple', 'banana', 'cherry', 'orange']
add_btn = [ttk.Button(frame[0], text=goods[i], command=lambda x=i: add_clicked(x)) for i in range(0, 10)]
btn_del = ttk.Button(frame[1], text='put away', command=dell_clicked)
btn_pay = ttk.Button(frame[2], text='pay', command=pay_clicked)
choose_list = tk.Listbox(frame[1])
cash_receipt = tk.Listbox(frame[3])
suml = tk.Label(frame[2], text='0')

for i in range(0, 10):
    add_btn[i].pack()

choose_list.pack(fill='both', expand=True)
btn_del.pack()

tk.Label(frame[2], text="summ").pack(fill=tk.X, pady=[100, 0])
suml.pack(fill=tk.X)
btn_pay.pack(fill=tk.X)

cash_receipt.pack(fill='both', expand=True)

window.mainloop()
