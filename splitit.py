from collections import defaultdict

def reconcile_expenses(transactions):
    balances = defaultdict(int)

    for transaction in transactions:
        payer, recipients, amount = transaction.split('/')
        recipients_list = recipients.split(',')

        amount_per_person = int(amount) // len(recipients_list)

        for recipient in recipients_list:
            balances[recipient] += amount_per_person

        balances[payer] -= int(amount)

    return balances

def reconcile_loans(transactions):
    balances = defaultdict(int)

    for transaction in transactions:
        lender, borrower, transaction_type, amount = transaction.split('/')
        
        if transaction_type == 'L':
            balances[borrower] += int(amount)
        else:
            interest = int(amount) * 0.12 // 52  # Assuming 52 weeks in a year
            principal_plus_interest = int(amount) + interest
            balances[lender] -= principal_plus_interest
            balances[borrower] += principal_plus_interest

    return balances

def reconcile_and_print(balances):
    sorted_balances = sorted(balances.items(), key=lambda x: x[0])

    for person, balance in sorted_balances:
        if balance != 0:
            print(f"{person}/{sorted_balances[0][0]}/{abs(balance)}")

def main():
    N = int(input())
    transactions = [input() for _ in range(N)]

    expense_transactions = [transaction for transaction in transactions if '/' in transaction[1]]
    loan_transactions = [transaction for transaction in transactions if '/' in transaction[2]]

    expense_balances = reconcile_expenses(expense_transactions)
    loan_balances = reconcile_loans(loan_transactions)

    final_balances = defaultdict(int)

    for person in set(expense_balances.keys()) | set(loan_balances.keys()):
        final_balances[person] = expense_balances[person] + loan_balances[person]

    reconcile_and_print(final_balances)

if __name__ == "__main__":
    main()
