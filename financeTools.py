def formatMoney(amount):
    return "$" + format(amount, ".2f")

#creates completed finanical summary
def buildSummary(userName, budgetTracker):
    totalIncome = budgetTracker.calculateTotalIncome()
    totalExpenses = budgetTracker.calculateTotalExpenses()
    remainingBalance = budgetTracker.calculateBalance()
    budgetRemaining = budgetTracker.calculateBudgetRemaining()
    moneyAfterSavings = budgetTracker.calculateMoneyAfterSavings()

    summary = "Monthly Personal Finance Summary\n"
    summary += "Name: " + userName + "\n"
    summary += "Monthly Budget: " + formatMoney(budgetTracker.monthlyBudget) + "\n"
    summary += "Savings Goal: " + formatMoney(budgetTracker.savingsGoal) + "\n\n"
    summary += "Income Transactions\n"

    if len(budgetTracker.incomeList) == 0:
        summary += "No income transactions entered.\n"
    else:
        for income in budgetTracker.incomeList:
            summary += income.getIncomeInfo() + "\n"

    summary += "\nExpense Transactions\n"

    if len(budgetTracker.expenseList) == 0:
        summary += "No expense transactions entered.\n"
    else:
        for expense in budgetTracker.expenseList:
            summary += expense.getExpenseInfo() + "\n"

    summary += "\nFinancial Totals\n"
    summary += "Total Income: " + formatMoney(totalIncome) + "\n"
    summary += "Total Expenses: " + formatMoney(totalExpenses) + "\n"
    summary += "Remaining Balance: " + formatMoney(remainingBalance) + "\n"
    summary += "Budget Remaining: " + formatMoney(budgetRemaining) + "\n"
    summary += "Money After Savings: " + formatMoney(moneyAfterSavings) + "\n"
    summary += "Budget Status: " + budgetTracker.getBudgetStatus() + "\n"
    summary += "Savings Status: " + budgetTracker.getSavingsStatus() + "\n"

    return summary

# saves and inputs summary of financial info to text file
def saveSummary(fileName, summary):
    try:
        outputFile = open(fileName, "w")
        outputFile.write(summary)
        outputFile.close()
        return True
    except OSError:
        return False
