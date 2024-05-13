from pathlib import Path
import sqlite3

OUTPUT_PATH = Path(__file__).parent.parent
DATA_PATH = OUTPUT_PATH / "data"
DB_PATH = DATA_PATH / "transactions.db"

def initialize_db(table: str, balance: float) -> None:
    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Create the table if it doesn't exist, with columns id, name, amount, date, and balance
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table}
                (id INTEGER PRIMARY KEY, name TEXT, amount REAL, date TEXT, balance REAL)''')

    # Insert a new row into the table with the provided name, amount, date, and balance
    c.execute(f"INSERT INTO {table} (name, amount, date, balance) VALUES (?, ?, ?, ?)", (None, None, None, balance))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the connection
    c.close()
    conn.close()


def add_transaction(table: str, name: str, amount: float, date: str) -> None:
    """
    Add a transaction to the database.

    Parameters:
    - name (str): The name of the transaction.
    - amount (float): The amount of the transaction.
    - date (str): The date and time of the transaction in the format 'YYYY-MM-DD HH:MM:SS'.

    Returns:
    - None
    """
    if amount == 0:
        return
    
    # Extract last knowkn balance and convert it to float
    last_balance_raw: list[tuple] = collect_balance(table)
    last_balance: float = last_balance_raw[0]

    # Update the balance adding the transaction amount
    new_balance = last_balance + amount

    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Insert a new row into the table with the provided name, amount and date
    c.execute(f"INSERT INTO {table} (name, amount, date, balance) VALUES (?, ?, ?, ?)", (name, f"{amount:.2f}", date, f"{new_balance:.2f}"))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the connection
    c.close()
    conn.close()
#add_transaction("transactions_history", "Spesa", 138.76, "06/05/2024 16:34:45")


def edit_transaction_attribute(table: str, attribute: str, primary_key: str, new_value: str) -> None:
    """
    Edit a specific attribute in a table using the primary key.

    Parameters:
    - table (str): The name of the table where the attribute is located.
    - attribute (str): The name of the attribute to edit.
    - new_value (str): The new value to assign to the attribute.
    - primary_key (str): The value of the primary key to identify the row to edit.

    Returns:
    - None
    """
    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)
    print(f"Connection to DB estabilished")

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Execute the SQL query to update the attribute using the primary key with parameters (new_value)
    c.execute(f"UPDATE {table} SET {attribute} = ? WHERE rowid = ?", (new_value, primary_key))
    print(f"Executin query: UPDATE {table} SET {attribute} = ? WHERE rowid = ?", (new_value, primary_key))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the connection
    c.close()
    conn.close()


def delete_transaction(table: str, primary_key: str) -> None:
    """
    Delete a row from a table in the SQLite database based on its primary key value.

    Parameters:
    - table (str): The name of the table from which to delete the row.
    - primary_key (str): The value of the primary key of the row to delete.

    Returns:
    - None
    """
    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Execute the SQL query to delete the row using the primary key
    c.execute(f"DELETE FROM {table} WHERE rowid = ?", (primary_key,))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the connection
    c.close()
    conn.close()
'''
for x in range(1, 10):
    delete_transaction("transactions_history", x)
'''


def collect_income_total(table: str) -> list[tuple]:
    """
    Collects the total income from transactions in the specified table.

    Parameters:
    - table (str): The name of the table containing the transactions.

    Returns:
    - list[tuple]: A list of tuples containing the income amounts.
    """
    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Build the SQL query and execute it to select all income transactions
    c.execute(f"SELECT amount FROM {table} WHERE amount > 0")
    
    # Fetch the results
    data = c.fetchall()
    
    # Close the connection
    conn.close()
    
    return data
# db_data_raw: list[tuple] = collect_income_total(table="transactions_history")
# db_data = [int(value[0]) for value in db_data_raw]
# print(db_data)


def collect_expense_total(table: str) -> list[tuple]:
    """
    Collects the total expenses from transactions in the specified table.

    Parameters:
    - table (str): The name of the table containing the transactions.

    Returns:
    - list[tuple]: A list of tuples containing the expense amounts.
    """
    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Build the SQL query and execute it to select all expense transactions
    c.execute(f"SELECT amount FROM {table} WHERE amount < 0")
    
    # Fetch the results
    data = c.fetchall()
    
    # Close the connection
    conn.close()
    
    return data
# db_data_raw: list[tuple] = collect_expense_total(table="transactions_history")
# db_data = [int(value[0]) for value in db_data_raw]
# print(db_data)


def collect_balance(table: str) -> list[tuple]:
    """
    Collects the balance of the last transaction.

    Parameters:
    - table (str): The name of the table containing the transactions.

    Returns:
    - list[tuple]: A list of tuples containing the balance.
    """
    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Build the SQL query and execute it to select all expense transactions
    c.execute(f"SELECT balance FROM {table} ORDER BY id DESC LIMIT 1")
    
    # Fetch the results
    data = c.fetchone()
    
    # Close the connection
    conn.close()
    
    return data


def count_item(table: str) -> int:
    """
    Count how many rows are in the database.

    Parameters:
    - table (str): The name of the table containing the transactions.

    Returns:
    - rows (int): The number of rows in the database.
    """
    # Connect to the SQLite database using the provided DB_PATH
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor object to execute SQLite statements
    c = conn.cursor()

    # Build the SQL query and execute it to select all expense transactions
    c.execute(f"SELECT COUNT(*) FROM {table};")
    
    # Fetch the results
    rows =  c.fetchone()[0]
    
    # Close the connection
    conn.close()
    
    return rows