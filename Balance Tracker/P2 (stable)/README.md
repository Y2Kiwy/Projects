# Balance Tracker v2.0.0
This Tkinter Desktop application can manually keep track of your transactions.

# Usage:
When starting the app for the first time you shuld set your current balance (0 by default),
to do that you have to use a specific code inserted in the 'Name' texbox: *!balance:x* where 'x' is the money amount.

Once the balance amount is setted the app is ready and you can use it. To register a new transaction you need to give it a name, amount and date:
    - name: The name you want to call the transaction
    - amount: Negative numbers to register a new expense and positive numbers to register an income
    - date: The date when the transaction has be done, use OLDY this two formats: YYYY-MM-DD or YYYY-MM-DD HH:MM

# Secrete codes
There are three working secret code that have to be writed in the 'name' texbox and they are:
    - *!balance:x* Where x is the money amount you want to set balance **USE THIS CODE ONLY IF DB DO NOT EXIST (first time using the app)**
    - *!pdf:* That can generate a pdf file with all the transactions regitered
    - *!bug:x* Where x is the bug description, you can report bugs through this code






**TO DO**
1 - Create pdf in a more accesible location
2 - Exclude first db row of 'transactions_history' table when creating pdf
3 - Fix cannot use colon for decimals when settings new balance

4 - Make possible to choose location where to create the file