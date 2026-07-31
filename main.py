import tkinter as tk
from tkinter import messagebox

from financeClasses import Income, Expense, BudgetTracker
from financeTools import buildSummary, saveSummary

#creates budget tracker object
budgetTracker = BudgetTracker()

#validates and stores user budget info
def updateBudgetInformation():
    userName = nameEntry.get().strip()

    if userName == "":
        messagebox.showerror("Input Error", "Enter your name.")
        return False

    try:
        monthlyBudget = float(budgetEntry.get())
        savingsGoal = float(savingsEntry.get())

        if monthlyBudget < 0 or savingsGoal < 0:
            messagebox.showerror(
                "Input Error",
                "Budget and savings goal cannot be negative."
            )
            return False

        budgetTracker.setBudget(monthlyBudget)
        budgetTracker.setSavingsGoal(savingsGoal)

        return True

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Enter valid numbers for the budget and savings goal."
        )
        return False

#adds valid income input
def addIncome():
    incomeDescription = incomeDescriptionEntry.get().strip()
    incomeAmountText = incomeAmountEntry.get().strip()

    if incomeDescription == "":
        messagebox.showerror(
            "Input Error",
            "Enter an income description."
        )
        return

    try:
        incomeAmount = float(incomeAmountText)

        if incomeAmount <= 0:
            messagebox.showerror(
                "Input Error",
                "Income amount must be greater than zero."
            )
            return

        income = Income(incomeDescription, incomeAmount)
        budgetTracker.addIncome(income)

        displayText.insert(
            tk.END,
            income.getIncomeInfo() + "\n"
        )

        incomeDescriptionEntry.delete(0, tk.END)
        incomeAmountEntry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Enter a valid number for the income amount."
        )

#adds valuid expsense input
def addExpense():
    expenseDescription = expenseDescriptionEntry.get().strip()
    expenseCategory = expenseCategoryEntry.get().strip()
    expenseAmountText = expenseAmountEntry.get().strip()

    if expenseDescription == "" or expenseCategory == "":
        messagebox.showerror(
            "Input Error",
            "Enter an expense description and category."
        )
        return

    try:
        expenseAmount = float(expenseAmountText)

        if expenseAmount <= 0:
            messagebox.showerror(
                "Input Error",
                "Expense amount must be greater than zero."
            )
            return

        expense = Expense(
            expenseDescription,
            expenseAmount,
            expenseCategory
        )

        budgetTracker.addExpense(expense)

        displayText.insert(
            tk.END,
            expense.getExpenseInfo() + "\n"
        )

        expenseDescriptionEntry.delete(0, tk.END)
        expenseCategoryEntry.delete(0, tk.END)
        expenseAmountEntry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Enter a valid number for the expense amount."
        )

#display completed finanicla summary
def viewSummary():
    if updateBudgetInformation() == False:
        return

    userName = nameEntry.get().strip()
    summary = buildSummary(userName, budgetTracker)

    displayText.delete("1.0", tk.END)
    displayText.insert(tk.END, summary)

def saveCurrentSummary():
    if updateBudgetInformation() == False:
        return

    if (
        len(budgetTracker.incomeList) == 0
        and len(budgetTracker.expenseList) == 0
    ):
        messagebox.showerror(
            "No Transactions",
            "Enter at least one income or expense transaction."
        )
        return

    userName = nameEntry.get().strip()
    summary = buildSummary(userName, budgetTracker)

    fileSaved = saveSummary(
        "financeSummary.txt",
        summary
    )

    if fileSaved:
        messagebox.showinfo(
            "Summary Saved",
            "The summary was saved as financeSummary.txt."
        )
    else:
        messagebox.showerror(
            "File Error",
            "The summary could not be saved."
        )

def clearEntries():
    incomeDescriptionEntry.delete(0, tk.END)
    incomeAmountEntry.delete(0, tk.END)
    expenseDescriptionEntry.delete(0, tk.END)
    expenseCategoryEntry.delete(0, tk.END)
    expenseAmountEntry.delete(0, tk.END)

    messagebox.showinfo(
        "Entries Cleared",
        "The transaction entry boxes were cleared."
    )

def exitProgram():
    exitChoice = messagebox.askyesno(
        "Exit Program",
        "Are you sure you want to exit?"
    )

    if exitChoice:
        mainWindow.destroy()

#creates the Tkinter window and interface
mainWindow = tk.Tk()
mainWindow.title("Monthly Personal Finance Tracker")
mainWindow.geometry("700x720")
mainWindow.resizable(False, False)

titleLabel = tk.Label(
    mainWindow,
    text="Monthly Personal Finance Tracker",
    font=("Arial", 18, "bold")
)
titleLabel.pack(pady=15)

userFrame = tk.LabelFrame(
    mainWindow,
    text="User Information",
    padx=10,
    pady=10
)
userFrame.pack(fill="x", padx=20, pady=5)

nameLabel = tk.Label(
    userFrame,
    text="Name:"
)
nameLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)

nameEntry = tk.Entry(
    userFrame,
    width=30
)
nameEntry.grid(row=0, column=1, padx=5, pady=5)

budgetLabel = tk.Label(
    userFrame,
    text="Monthly Budget:"
)
budgetLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)

budgetEntry = tk.Entry(
    userFrame,
    width=30
)
budgetEntry.grid(row=1, column=1, padx=5, pady=5)

savingsLabel = tk.Label(
    userFrame,
    text="Savings Goal:"
)
savingsLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)

savingsEntry = tk.Entry(
    userFrame,
    width=30
)
savingsEntry.grid(row=2, column=1, padx=5, pady=5)

incomeFrame = tk.LabelFrame(
    mainWindow,
    text="Income",
    padx=10,
    pady=10
)
incomeFrame.pack(fill="x", padx=20, pady=5)

incomeDescriptionLabel = tk.Label(
    incomeFrame,
    text="Description:"
)
incomeDescriptionLabel.grid(
    row=0,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

incomeDescriptionEntry = tk.Entry(
    incomeFrame,
    width=30
)
incomeDescriptionEntry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

incomeAmountLabel = tk.Label(
    incomeFrame,
    text="Amount:"
)
incomeAmountLabel.grid(
    row=1,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

incomeAmountEntry = tk.Entry(
    incomeFrame,
    width=30
)
incomeAmountEntry.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)

addIncomeButton = tk.Button(
    incomeFrame,
    text="Add Income",
    width=18,
    command=addIncome
)
addIncomeButton.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=8
)

expenseFrame = tk.LabelFrame(
    mainWindow,
    text="Expense",
    padx=10,
    pady=10
)
expenseFrame.pack(fill="x", padx=20, pady=5)

expenseDescriptionLabel = tk.Label(
    expenseFrame,
    text="Description:"
)
expenseDescriptionLabel.grid(
    row=0,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

expenseDescriptionEntry = tk.Entry(
    expenseFrame,
    width=30
)
expenseDescriptionEntry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

expenseCategoryLabel = tk.Label(
    expenseFrame,
    text="Category:"
)
expenseCategoryLabel.grid(
    row=1,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

expenseCategoryEntry = tk.Entry(
    expenseFrame,
    width=30
)
expenseCategoryEntry.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)

expenseAmountLabel = tk.Label(
    expenseFrame,
    text="Amount:"
)
expenseAmountLabel.grid(
    row=2,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

expenseAmountEntry = tk.Entry(
    expenseFrame,
    width=30
)
expenseAmountEntry.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)

addExpenseButton = tk.Button(
    expenseFrame,
    text="Add Expense",
    width=18,
    command=addExpense
)
addExpenseButton.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=8
)

buttonFrame = tk.Frame(mainWindow)
buttonFrame.pack(pady=10)

viewSummaryButton = tk.Button(
    buttonFrame,
    text="View Summary",
    width=15,
    command=viewSummary
)
viewSummaryButton.grid(row=0, column=0, padx=5)

saveSummaryButton = tk.Button(
    buttonFrame,
    text="Save Summary",
    width=15,
    command=saveCurrentSummary
)
saveSummaryButton.grid(row=0, column=1, padx=5)

clearButton = tk.Button(
    buttonFrame,
    text="Clear Entries",
    width=15,
    command=clearEntries
)
clearButton.grid(row=0, column=2, padx=5)

exitButton = tk.Button(
    buttonFrame,
    text="Exit",
    width=15,
    command=exitProgram
)
exitButton.grid(row=0, column=3, padx=5)

displayText = tk.Text(
    mainWindow,
    width=78,
    height=14
)
displayText.pack(padx=20, pady=10)

mainWindow.protocol(
    "WM_DELETE_WINDOW",
    exitProgram
)

mainWindow.mainloop()
