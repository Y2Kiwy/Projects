from pathlib import Path

# Define all usefull path for the code
PROJECT_DIR = Path(__file__).parent.parent.parent            # Project directory path
ASSETS_DIR = PROJECT_DIR / "build" / "assets" / "frame0"     # Assets directory path
DB_PATH = PROJECT_DIR / "build" / "data" / "transactions.db" # Database path

from dbf import *

# Check if the database exists to initialize it if not
if not DB_PATH.exists():
    initialize_db("transactions_history", "balance_history", 0)

from functions import *

# Handles submission of transaction amounts and updates global variables and canvas display accordingly
def submit_transaction() -> None:

    # Get values from texboxes and normalize it
    txn_data: tuple = normalize_textbox_values(name_textbox.get(), amount_textbox.get(), date_textbox.get())

    # Extract transaction value
    txn_name: str = txn_data[0]
    txn_amount: float = txn_data[1]
    txn_date: datetime = txn_data[2]

    if txn_name and txn_amount and txn_date:
        print(f"New transaction registered: {txn_name}, {txn_amount:,.2f}, {txn_date}")

    # Collect income and expense total and the last known balance
    income_total: float = collect_income_total("transactions_history")
    balance_last: float = collect_balance("balance_history")
    expense_total: float = collect_expense_total("transactions_history")

    # Check if 'txn_amount' is not empty
    if txn_amount:

        # Check if 'txn_amount' is income
        if txn_amount > 0:
            # Recalculate the income total
            income_total += txn_amount
            # Update the displayed income on the canvas
            canvas.itemconfig(tagOrId=income, text=f"{income_total:,.2f}€")

        # Check if 'txn_amount' is expense
        elif txn_amount < 0:
            # Recalculate the expense total
            expense_total += txn_amount
            # Update the displayed income on the canvas
            canvas.itemconfig(tagOrId=expense, text=f"{expense_total:,.2f}€")

        # Update the balance label by adding income and subtracting expenses
        update_balance = balance_last + txn_amount

        # Update the displayed balance on the canvas
        canvas.itemconfig(tagOrId=balance, text=f"{update_balance:,.2f}€")

        # Add the new transaction to the database
        add_transaction("transactions_history", "balance_history", txn_name, txn_amount, txn_date)

    # Update all the shown texts
    update_texts()

def update_texts() -> None:
    income_total: float = collect_income_total("transactions_history")
    canvas.itemconfig(tagOrId=income, text=f"{income_total:,.2f}€")

    balance_last: float = collect_balance("balance_history")
    canvas.itemconfig(tagOrId=balance, text=f"{balance_last:,.2f}€")

    expense_total: float = collect_expense_total("transactions_history")
    canvas.itemconfig(tagOrId=expense, text=f"{expense_total:,.2f}€")



from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Start of main GUI -----------------------------------------------------------

# Create new tkinter graphic window
window = Tk()

# Set window size 
window.geometry("640x480")

# Set window background color
window.configure(bg = "#FFFFFF")



# Create new canva over the tkinter window
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(
    x = 0,
    y = 0
)

# Blu rectangle on the top screen
canvas.create_rectangle(
    0.0,
    0.0,
    640.0,
    96.0,
    fill="#00317B",
    outline=""
)

# Title of the app in the top-left corner
canvas.create_text(
    24.0,
    29.0,
    anchor="nw",
    text="Balance Tracker",
    fill="#FFFFFF",
    font=("Ubuntu", 32 * -1, "bold")
)



# 'income' background rectangle
income_bg_rect_obj = PhotoImage(
    file=asset_path_build("income_bg_rect.png"))
income_bg_rect_canvas = canvas.create_image(
    176.0,
    160.0,
    image=income_bg_rect_obj
)

# 'balance' background rectangle
balance_bg_rect_obj = PhotoImage(
    file=asset_path_build("balance_bg_rect.png"))
balance_bg_rect_canvas = canvas.create_image(
    320.0,
    240.0,
    image=balance_bg_rect_obj
)

# 'expenses' background rectangle
expense_bg_rect_obj = PhotoImage(
    file=asset_path_build("expense_bg_rect.png"))
expense_bg_rect_canvas = canvas.create_image(
    464.0,
    160.0,
    image=expense_bg_rect_obj
)

# Logo of the app in the top-right corner
logo_obj = PhotoImage(
    file=asset_path_build("logo.png"))
logo_canvas = canvas.create_image(
    590.0,
    48.0,
    image=logo_obj
)



# 'income' title text
canvas.create_text(
    72.0,
    137.0,
    anchor="nw",
    text="Income",
    fill="#604500",
    font=("Ubuntu", 12 * -1, "bold")
)

# 'balance' title text
canvas.create_text(
    72.0,
    217.0,
    anchor="nw",
    text="Balance",
    fill="#0A4B00",
    font=("Ubuntu", 12 * -1, "bold")
)

# 'expenses' title text
canvas.create_text(
    360.0,
    137.0,
    anchor="nw",
    text="Expenses",
    fill="#660000",
    font=("Ubuntu", 12 * -1, "bold")
)

# 'income' value text
income_total: float = collect_income_total("transactions_history")
income = canvas.create_text(
    72.0,
    152.0,
    anchor="nw",
    text=f"{income_total:,.2f}€",
    fill="#4F4500",
    font=("Ubuntu", 24 * -1, "bold")
)

# 'balance' value text
balance_last: float = collect_balance("balance_history")
balance = canvas.create_text(
    72.0,
    232.0,
    anchor="nw",
    text=f"{balance_last:,.2f}€",
    fill="#0A4B00",
    font=("Ubuntu", 24 * -1, "bold")
)

# 'expenses' value text
expense_total: float = collect_expense_total("transactions_history")
expense = canvas.create_text(
    360.0,
    152.0,
    anchor="nw",
    text=f"{expense_total:,.2f}€",
    fill="#660000",
    font=("Ubuntu", 24 * -1, "bold")
)

# 'add transaction' title text
canvas.create_text(
    250.0,
    310.0,
    anchor="nw",
    text="Add Transaction\n",
    fill="#00317B",
    font=("Ubuntu", 16 * -1, "bold")
)

# 'name' title text
canvas.create_text(
    72.0,
    334.0,
    anchor="nw",
    text="Name\n",
    fill="#6682AD",
    font=("Ubuntu", 12 * -1, "bold")
)

# 'amount' title text
canvas.create_text(
    344.0,
    334.0,
    anchor="nw",
    text="Amount (€)\n",
    fill="#6682AD",
    font=("Ubuntu", 12 * -1, "bold")
)

# 'date' title text
canvas.create_text(
    488.0,
    335.0,
    anchor="nw",
    text="Date\n",
    fill="#6682AD",
    font=("Ubuntu", 12 * -1, "bold")
)



# Function to handle placeholders behaviour on click
def on_entry_click(event, textbox, placeholder):
    if textbox.get() == placeholder:
        textbox.delete(0, "end")
        textbox.config(fg='black')


# Function to handle placeholders behaviour on click release
def on_focus_out(event, textbox, placeholder):
    if not textbox.get():
        textbox.insert(0, placeholder)
        textbox.config(fg='#848484')



# 'name' background rectangle, textbox and placeholder
name_placeholder: str = "e.g. -> Shopping"  # Placeholder text
name_bg_rect_obj = PhotoImage(
    file=asset_path_build("name_bg_rect.png"))
name_bg_rect_canvas = canvas.create_image(
    176.0,
    368.0,
    image=name_bg_rect_obj
)
name_textbox = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
name_textbox.place(
    x=64.0,
    y=352.0,
    width=224.0,
    height=30.0
)
name_textbox.insert( # Insert placeholder text
    0, 
    name_placeholder
)
name_textbox.config(  # Set placeholder text color to grey
    fg='#848484'
)
name_textbox.bind( # Bind event handler for focus in
    '<FocusIn>',
    lambda event: on_entry_click(event, name_textbox, name_placeholder)
)
name_textbox.bind(  # Bind event handler for focus out
    '<FocusOut>', 
    lambda event: on_focus_out(event, name_textbox, name_placeholder)
)



# 'amount' background rectangle, textbox and placeholder
amount_placeholder: str = "e.g. -> -18.06"  # Placeholder text
amount_bg_rect_obj = PhotoImage(
    file=asset_path_build("amount_bg_rect.png"))
amount_bg_rect_canvas = canvas.create_image(
    384.0,
    368.0,
    image=amount_bg_rect_obj
)
amount_textbox = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
amount_textbox.place(
    x=336.0,
    y=352.0,
    width=96.0,
    height=30.0
)
amount_textbox.insert(  # Insert placeholder text
    0, 
    amount_placeholder
)
amount_textbox.config(  # Set text color to grey
    fg='#848484'
)
amount_textbox.bind(  # Bind event handler for focus in
    '<FocusIn>', 
    lambda event: on_entry_click(event, amount_textbox, amount_placeholder)
)
amount_textbox.bind(  # Bind event handler for focus out
    '<FocusOut>', 
    lambda event: on_focus_out(event, amount_textbox, amount_placeholder)
)



# 'date' background rectangle, textbox and placeholder
date_placeholder: str = "e.g. -> 2024-01-01"  # Placeholder text
date_bg_rect_obj = PhotoImage(
    file=asset_path_build("date_bg_rect.png"))
date_bg_rect_canvas = canvas.create_image(
    528.0,
    368.0,
    image=date_bg_rect_obj
)
date_textbox = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
date_textbox.place(
    x=480.0,
    y=352.0,
    width=96.0,
    height=30.0
)
date_textbox.insert(  # Insert placeholder text
    0, 
    date_placeholder
)
date_textbox.config(  # Set text color to grey
    fg='#848484'
)
date_textbox.bind(  # Bind event handler for focus in
    '<FocusIn>', 
    lambda event: on_entry_click(event, date_textbox, date_placeholder)
)
date_textbox.bind(  # Bind event handler for focus out
    '<FocusOut>', 
    lambda event: on_focus_out(event, date_textbox, date_placeholder)
)



# 'submit' background rectangle, button
submit_bg_rect_obj = PhotoImage(
    file=asset_path_build("submit_button.png"))
submit_button = Button(
    image=submit_bg_rect_obj,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: submit_transaction(),
    relief="flat"
)
submit_button.place(
    x=48.0,
    y=400.0,
    width=544.0,
    height=48.0
)

# 'settings' background rectangle, button
settings_bg_rect_obj = PhotoImage(
    file=asset_path_build("settings_button.png"))
settings_button = Button(
    image=settings_bg_rect_obj,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: toggle_settings_panel(),
    relief="flat"
)
settings_button.place(
    x=616.0,
    y=456.0,
    width=16.0,
    height=16.0
)



# Start of settings GUI -------------------------------------------------------

# Handle settings panel hide/show
def toggle_settings_panel():

    if settings_canvas.winfo_ismapped():
        settings_canvas.place_forget()                                        # Make the 'settings_canva' window disappear
        home_button.place_forget()                                            # Make the 'home_button' disappear
        print("Settings panel hidden")

    else:
        settings_canvas.place(x = 0, y = 0)                                   # Make the 'settings_canva' window appear
        home_button.place(x=616.0, y=456.0, width=16.0, height=16.0)          # Make the 'home_button' appear
        print("Settings panel shown")

# Create new canva over main canva
settings_canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)



# Blu rectangle on the top screen
settings_canvas.create_rectangle(
    0.0,
    0.0,
    640.0,
    96.0,
    fill="#00317B",
    outline=""
)

# Title of the app in the top-left corner
settings_canvas.create_text(
    24.0,
    29.0,
    anchor="nw",
    text="Balance Tracker",
    fill="#FFFFFF",
    font=("Ubuntu", 32 * -1, "bold")
)

# Logo of the app in the top-right corner
settings_logo_obj = PhotoImage(
    file=asset_path_build("logo.png"))
settings_logo_canvas = settings_canvas.create_image(
    590.0,
    48.0,
    image=settings_logo_obj
)



# Coming Soon
settings_canvas.create_text(
    192.0,
    192.0,
    anchor="nw",
    text="Coming Soon",
    fill="#000000",
    font=("Ubuntu", 41 * -1, "bold")
)



# 'home' background rectangle, button
home_bg_rect_obj = PhotoImage(
    file=asset_path_build("home_button.png"))
home_button = Button(
    image=home_bg_rect_obj,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: toggle_settings_panel(),
    relief="flat"
)
home_button.place(
    x=616.0,
    y=456.0,
    width=16.0,
    height=16.0
)

home_button.place_forget() # Prevent 'home_button' from appear when 'settings_canva' is not active

# End of settings GUI ---------------------------------------------------------



# Deactivate window resize
window.resizable(False, False) 

# Start the mainloop of the window
window.mainloop() 

# End of main GUI -------------------------------------------------------------