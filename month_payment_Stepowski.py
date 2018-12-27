#Title and imports

print ("Monthly Payment")
import locale as lc
from decimal import Decimal
print ()
print("DATA ENTRY")



def get_month_payment(loan_amount, yearly_interest_rate, years):
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months =  12 * years
    month_payment = Decimal("0.00")
    for i in range(months):
        month_payment +=  loan_amount
        monthly_interest = month_payment * monthly_interest_rate
        month_payment += monthly_interest
    month_payment = loan_amount * monthly_interest_rate / (1 -1 / (1 + monthly_interest_rate) ** months)
    month_payment = month_payment.quantize(Decimal("1.00"))
    return month_payment
    

def main():
    choice = "y"    
    while choice.lower() == "y":

        #This part converts the integers to the correct values
         while True:
            try:
                loan_amount = Decimal(input("Enter loan amount: "))
                yearly_interest_rate = Decimal(input("Enter yearly interest rate: "))
                years = int(input("Enter the amount of years "))
                month_payment = get_month_payment(loan_amount, yearly_interest_rate, years)
            except ValueError:
                 print ("Invalid integer. Please try again")
            else:
                break



         #Format and display results
         result = lc.setlocale(lc.LC_ALL, "")
         if result == "C":
             lc.setlocale(lc.LC_ALL, "en_US")
         line = "{:20} {:>10}"
         print ()
         print ("FORMATTED RESULTS ")
         print (line.format("Loan amount: ",
        	 lc.currency(loan_amount, grouping=True)))
         print (line.format("Interest rate:", yearly_interest_rate))
         print (line.format("Years: ", years))
         print (line.format("Monthly Payment:",
             lc.currency(month_payment, grouping=True)), "\n")


         choice = input("Continue? y/n: ")
         print ()

if __name__ == "__main__":
 	main()
         


   
