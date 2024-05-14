from pathlib import Path

# Define all usefull path for the code
PROJECT_DIR = Path(__file__).parent.parent.parent            # Project directory path
ASSETS_DIR = PROJECT_DIR / "build" / "assets" / "frame0"     # Assets directory path
DBF_PATH = PROJECT_DIR / "build" / "data"                    # Database functions lib directory
DB_PATH = PROJECT_DIR / "build" / "data" / "transactions.db" # Database path

import sys
sys.path.append(str(DBF_PATH))
from dbf import *

from tkinter import *

from datetime import datetime

def normalize_textbox_values(txn_name: str, txn_amount: str, txn_date: str) -> tuple[str, float, datetime]:
    """
    Normalizes the values of transaction amount, and date and check for hidden codes in transaction name.

    Args:
    - txn_name (str): The name of the transaction.
    - txn_amount (str): The amount of the transaction.
    - txn_date (str): The date and time of the transaction.

    Returns:
    - str, float, datetime: The three values normalized
    """
    # Define the placeholder for the texboxes
    name_placeholder: str = "e.g. -> Shopping"
    amount_placeholder: str = "e.g. -> -18.06"
    date_placeholder: str = "e.g. -> 2024-01-01"

    # Initialize a list for valid transaction data
    txn_valid_data: list[str] = [None, None, None]

    # Check if 'txn_name' value is not the placeholder
    if txn_name != name_placeholder:
        # Check for hidden code in 'txn_name'
        if txn_name != "":
            print("'txn_name correctly recovered")
            hidden_code_handler(txn_name)
            txn_valid_data[0] = txn_name

    # Check if 'txn_amount' value is not the placeholder
    if txn_amount != amount_placeholder:
        # Normalize 'txn_amount' to float if not empty
        if txn_amount != "":
            print("'txn_amount correctly recovered")
            txn_amount: float = float(txn_amount.replace(",", "."))
            txn_valid_data[1] = txn_amount

    # Check if 'txn_date' value is not the placeholder
    if txn_date != date_placeholder:
        # Normalize 'txn_date' to datetime if not empty
        if txn_date != "":
            try:
                print("'txn_date correctly recovered")
                txn_date: datetime = datetime.strptime(txn_date, "%Y-%m-%d %H:%M")
                txn_valid_data[2] = txn_date

            except ValueError:
                print("'txn_date is not with '%Y-%m-%d %H:%M' format trying '%Y-%m-%d'")
                txn_date: datetime = datetime.strptime(txn_date, "%Y-%m-%d").date()
                txn_valid_data[2] = txn_date

    # Return a tuple with the valid transaction data
    return tuple(txn_valid_data)



# Build assets path
def asset_path_build(path: str) -> Path:
    return ASSETS_DIR / Path(path)


# Function to handle hidden code in a string
def hidden_code_handler(code_str: str) -> None:
    # Define special identifiers for specific actions
    # balance_id: str = "!balance:"
    # delete_id: str = "!delete:"
    # edit_id: str = "!edit:"
    # pdf_id: str = "!pdf:"
    # bug_id: str = "!bug:"

    hidden_codes: dict = {
        "!balance:": balance_hidden_code,
        "!edit:": None,
        "!delete:": None,
        "!pdf:": pdf_hidden_code,
        "!bug:": bug_hidden_code
    }

    for code, function in hidden_codes.items():
        if code in code_str:
            print(f"Detected hidden code: '{code}' calling '{function}'...")
            function(code_str)
            break


# Function to handle hidden code related to balance
def balance_hidden_code(code_str: str) -> None:
    # Count the number of rows in the transactions table in the database
    db_rows: int = count_item("balance_history")
    print(f"Checking if the database is empty...")

    # If there is only one row in the database
    if db_rows == 1:
        # Extract the new balance from the code string
        new_balance: float = float(code_str.split(":")[1].replace(",", "."))
        # Edit the 'balance' attribute of the first transaction in the database
        edit_transaction_attribute("balance_history", "balance", 1, new_balance)
        edit_transaction_attribute("transactions_history", "amount", 1, new_balance)
        print(f"Attribute 'balance' edited correctly to {new_balance}")
    else:
        # If the database is not empty, print a message indicating failure
        print(f"The database is not empty ({db_rows} rows found) or do not exist, failed to edit 'balance'")

import sqlite3
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

# Function to handle hidden code related to generate a pdf copy of database transactions
def pdf_hidden_code(code_str: str) -> None:
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Execute a query to select data from the table
    cursor.execute("SELECT * FROM transactions_history LIMIT -1 OFFSET 1;")
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Create the PDF document
    pdf_path = "transactions_history.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    data = []

    # Add the table header
    header = ["id", "name", "amount", "balance"]
    data.append(header)

    # Add the data rows to the table
    for row in rows:
        data.append(row)

    # Create the table in the PDF document
    table = Table(data)
    table.setStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    # Add the table to the document
    doc.build([table])

    print("PDF file successfully created:", pdf_path)


# Function to handle hidden code related to bugs_report report
def bug_hidden_code(code_str) -> None:

    # Extract the bug description from the code string
    bug_description: str = code_str.split(":")[1]

    # Get current datetime
    bug_date_raw = datetime.now()

    # Format current datetime in '%Y-%M-%d %H:%M'
    bug_date = bug_date_raw.strftime('%Y-%M-%d %H:%M')

    # Add bug data into the 'bugs_report' table of database
    add_bug(bug_description, bug_date)