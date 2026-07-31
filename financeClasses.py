# stores basic information, income and expenses
class Transaction:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def getTransactionInfo(self):
        return self.description + ": $" + format(self.amount, ".2f")

# money user recieves/earns monthly
class Income(Transaction):
    def __init__(self, description, amount):
        super().__init__(description, amount)

    def getIncomeInfo(self):
        return "Income - " + self.getTransactionInfo()

# money user spends
class Expense(Transaction):
    def __init__(self, description, amount, category):
        super().__init__(description, amount)
        self.category = category

    def getExpenseInfo(self):
        return (
            "Expense - "
            + self.description
            + " | Category: "
            + self.category
            + " | Amount: $"
            + format(self.amount, ".2f")
        )

# stores budget, saving goal, income, and expenses input by user
class BudgetTracker:
    def __init__(self):
        self.monthlyBudget = 0.0
        self.savingsGoal = 0.0
        self.incomeList = []
        self.expenseList = []

    def setBudget(self, monthlyBudget):
        self.monthlyBudget = monthlyBudget

    def setSavingsGoal(self, savingsGoal):
        self.savingsGoal = savingsGoal

    def addIncome(self, income):
        self.incomeList.append(income)

    def addExpense(self, expense):
        self.expenseList.append(expense)

    def calculateTotalIncome(self):
        totalIncome = 0.0

        for income in self.incomeList:
            totalIncome += income.amount

        return totalIncome

    def calculateTotalExpenses(self):
        totalExpenses = 0.0

        for expense in self.expenseList:
            totalExpenses += expense.amount

        return totalExpenses

    def calculateBalance(self):
        totalIncome = self.calculateTotalIncome()
        totalExpenses = self.calculateTotalExpenses()

        return totalIncome - totalExpenses

    def calculateBudgetRemaining(self):
        totalExpenses = self.calculateTotalExpenses()

        return self.monthlyBudget - totalExpenses

    def calculateMoneyAfterSavings(self):
        remainingBalance = self.calculateBalance()

        return remainingBalance - self.savingsGoal

    def getBudgetStatus(self):
        totalExpenses = self.calculateTotalExpenses()

        if totalExpenses <= self.monthlyBudget:
            return "Within Budget"
        else:
            return "Over Budget"

    def getSavingsStatus(self):
        remainingBalance = self.calculateBalance()

        if remainingBalance >= self.savingsGoal:
            return "Savings Goal Can Be Reached"
        else:
            return "Savings Goal Cannot Be Reached"
