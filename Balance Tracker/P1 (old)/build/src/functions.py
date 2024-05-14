from pathlib import Path

import sys

OUTPUT_PATH = Path(__file__).parent.parent
DBF_PATH = OUTPUT_PATH / "data"
DB_PATH = DBF_PATH / "transactions.db"

sys.path.append(str(DBF_PATH))
from dbf import *

# Define special identifiers for specific actions
balance_id: str = "!balance:"
delete_id: str = "!delete:"
edit_id: str = "!edit:"
pdf_id: str = "!pdf:"

# Function to handle hidden code in a string
def hidden_code_handler(code_str: str) -> None:
    # Check if the string contains the balance_id
    if balance_id in code_str:
        # If so, call the balance_hidden_code function
        print(f"Label 'name' contains '!balance:' hidden code, calling 'balance_hidden_code()'...")
        balance_hidden_code(code_str)
    elif pdf_id in code_str:
        # If so, call the generate_pdf_from_db function
        print(f"Label 'name' contains '!pdf:' hidden code, calling 'generate_pdf_from_db()'...")
        generate_pdf_from_db()

# Function to handle hidden code related to balance
def balance_hidden_code(code_str: str) -> None:
    # Count the number of rows in the transactions table in the database
    db_rows: int = count_item("transactions_history")
    print(f"Checking if the database is empty...")

    # If there is only one row in the database
    if db_rows == 1:
        # Extract the new balance from the code string
        new_balance: int = int(code_str.split(":")[1])
        # Edit the 'balance' attribute of the first transaction in the database
        edit_transaction_attribute("transactions_history", "balance", 1, new_balance)
        print(f"Attribute 'balance' edited correctly to {new_balance}")
    else:
        # If the database is not empty, print a message indicating failure
        print(f"The database is not empty, failed to edit 'balance'")


import sqlite3
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

# Generate a PDF file with all the database transactions
def generate_pdf_from_db() -> None:
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Execute a query to select data from the table
    cursor.execute("SELECT * FROM transactions_history;")
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
