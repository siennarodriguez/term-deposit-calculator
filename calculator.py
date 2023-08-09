"""Simple Term Deposit Calculator that takes the following inputs:
1. Start deposit amount (e.g. $10,000)
2. Interest rate (e.g. 1.10%)
3. Investment term (e.g. 3 years)
4. Interest paid (Monthly, Quarterly, Annually, At Maturity)

Result output is the final balance (e.g. $10,330 on the above inputs, interest paid At Maturity)

Author: Sienna Rodriguez
Created: 09/08/2023
"""

def validate_input(prompt):
    """
    Repeatedly asks user for input until they enter a valid input amount (positive integer)

    :param amount: input needed to calculate compound interest, int
                   (start_deposit_amount, investment_term)
    :return: the user's amount, int
    """
    while True:
        try:
            amount = int(input(prompt))
            try:
                assert amount > 0
                break
            except AssertionError:
                print(f"Invalid input - you entered {amount}. Amount must be greater than zero. Please try again...")
        except ValueError:
            print("Invalid input - amount must be an integer greater than zero. Please try again...")
    return amount

def validate_interest_rate(prompt):
    """
    Repeatedly asks user for input until they enter a valid input amount (positive float)

    :param amount: input needed to calculate compound interest, positive float (interest_rate)
    :return: the user's amount, positive flota
    """
    while True:
        try:
            amount = float(input(prompt))
            try:
                assert amount > 0
                break
            except AssertionError:
                print(f"Invalid input - you entered {amount}. Amount must be greater than zero. Please try again...")
        except ValueError:
            print("Invalid input - amount must be a percentage value. Please try again...")
    return amount

def validate_interest_frequency(prompt, valid_inputs):
    """
    Repeatedly asks user for input until they an input within a set of valid inputs 

    :param prompt: prompt message to display to the user, string
    :param valid_inputs: list of valid inputs user can select from, list
    :return: frequency of interest paid, int
    """
    while True:
        try:
            freq = int(input(prompt))
            try: 
                assert freq in valid_inputs
                break
            except AssertionError:
                print("\nInvalid input - please select from the list of options...")
        except ValueError:
            print("\nInvalid input - please select from the list of options...")
    
    return freq

def main():
    """
    Calculates the final balance for a term deposit using the start deposit amount,
    interest rate, investment term and frequency of interest paid 

    :return: final balance of the term deposit based on user inputs
    """
    start_deposit_amount = validate_input("Please enter the start deposit amount (e.g. 10000): ")
    interest_rate = validate_interest_rate("Please enter the interest rate (e.g. 1.1): ")
    investment_term = validate_input("Please enter the investment term in years (e.g. 3): ")
    interest_frequency = validate_interest_frequency("Please select the frequency of interest paid:\n1) Monthly\n2) Quarterly\n3) Annually\n4) At Maturity\n", [1,2,3,4])
    
    if interest_frequency == 1:
        frequency_str = "Monthly"
        compound_interest = round(start_deposit_amount * (1 + interest_rate/1200) ** (investment_term * 12))
    elif interest_frequency == 2:
        frequency_str = "Quarterly"
        compound_interest = round(start_deposit_amount * (1 + interest_rate/400) ** (investment_term * 4))
    elif interest_frequency == 3:
        frequency_str = "Annually"
        compound_interest = round(start_deposit_amount * (1 + interest_rate/100) ** investment_term)
    elif interest_frequency == 4:
        frequency_str = "At Maturity"
        compound_interest = round(start_deposit_amount + start_deposit_amount * (interest_rate/100) * investment_term)
    
    return f"Based on the following inputs...\nStart deposit amount: ${start_deposit_amount}\nInterest rate: {interest_rate}\nInvestment term: {investment_term} years\nInterest paid: {frequency_str}\nYour final balace = ${compound_interest}"

if __name__ == "__main__":
    print(main())
