import tkinter as tk

''' COLORS VARIABLES '''

gray = '#D0D5CE'
black = '#131919'
blue = '#3C5759'
blue_active = '#35454C'
dark_gray = '#959D90'
dgray_active = '#7C847A'
white = '#EFECE9'

error_info = 'Error! Please, use only numbers'

''' ROOT AND FRAMES '''

root = tk.Tk()
root.title('Loan Calculator')
root.config(bg='#D0D5CE', padx=20, pady=20)

for i in range(0, 6):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

''' FUNCTIONS '''


def compute_payment():
    try:
        air = float(annual_int_var.get())/100
        nyv = int(number_years_var.get())
        la = float(loan_amount_var.get())

        total_pay = float(la * (1 + air) ** nyv)
        month_pay = float(total_pay / (nyv * 12))

        total_pay_var.set(format(total_pay, '10.2f'))
        month_pay_var.set(format(month_pay, '10.2f'))
        error_info_var.set('')

    except Exception as e:
        error_info_var.set(format(error_info, ''))


def clear_all():
    annual_int_var.set('')
    number_years_var.set('')
    loan_amount_var.set('')
    total_pay_var.set('')
    month_pay_var.set('')
    error_info_var.set('')


''' INPUTS '''

tk.Label(root,
         font='Helvetica 12 bold',
         text='Annual Interest Rate (%)',
         bg=gray,
         fg=black
         ).grid(row=0, column=0, sticky='w', padx=20)

tk.Label(root,
         font='Helvetica 12 bold',
         text='Number of Years',
         bg=gray,
         fg=black
         ).grid(row=1, column=0, sticky='w', padx=20)

tk.Label(root,
         font='Helvetica 12 bold',
         text='Loan Amount',
         bg=gray,
         fg=black
         ).grid(row=2, column=0, sticky='w', padx=20)

annual_int_var = tk.StringVar()
tk.Entry(root,
         font='Helvetica 12 bold',
         textvariable=annual_int_var,
         justify=tk.RIGHT,
         fg=black
         ).grid(row=0, column=1, sticky='nsew', pady=3, padx=20)

number_years_var = tk.StringVar()
tk.Entry(root,
         font='Helvetica 12 bold',
         textvariable=number_years_var,
         justify=tk.RIGHT,
         fg=black
         ).grid(row=1, column=1, sticky='nsew', pady=3, padx=20)

loan_amount_var = tk.StringVar()
tk.Entry(root,
         font='Helvetica 12 bold',
         textvariable=loan_amount_var,
         justify=tk.RIGHT,
         fg=black
         ).grid(row=2, column=1, sticky='nsew', pady=3, padx=20)

''' RESULTS '''

tk.Label(root,
         font='Helvetica 12 bold',
         text='Monthly Payment',
         bg=gray,
         fg=black
         ).grid(row=3, column=0, sticky='w', padx=20)

tk.Label(root,
         font='Helvetica 12 bold',
         text='Total Payment',
         bg=gray,
         fg=black
         ).grid(row=4, column=0, sticky='w', padx=20)

month_pay_var = tk.StringVar()
month_pay_lb = tk.Label(root,
                        font='Helvetica 12 bold',
                        textvariable=month_pay_var,
                        bg=gray,
                        fg=black
                        ).grid(row=3, column=1, pady=3, padx=20, sticky='e')

total_pay_var = tk.StringVar()
total_pay_lb = tk.Label(root,
                        font='Helvetica 12 bold',
                        textvariable=total_pay_var,
                        bg=gray,
                        fg=black
                        ).grid(row=4, column=1, pady=3, padx=20, sticky='e')


''' ERROR LABEL '''

error_info_var = tk.StringVar()
error_info_lab = tk.Label(root,
                          textvariable=error_info_var,
                          font='Helvetica 12 bold',
                          bg=gray,
                          fg=black
                          ).grid(row=5, columnspan=2, sticky='nsew')


''' BUTTONS '''

button_compute = tk.Button(root,
                           font='Helvetica 12 bold',
                           text='Compute Payment',
                           command=compute_payment,
                           fg=white,
                           bg=blue,
                           activebackground=blue_active,
                           activeforeground=white
                           ).grid(row=6, column=0, sticky='ew', pady=20, padx=20)

button_clear = tk.Button(root,
                         font='Helvetica 12 bold',
                         text='Clear',
                         command=clear_all,
                         fg=black,
                         bg=dark_gray,
                         activebackground=dgray_active
                         ).grid(row=6, column=1, sticky='ew', pady=20, padx=20)

root.mainloop()