question_one = int(input('Enter your monthly income:'))
question_two = int(input('Enter your total monthly expenses: '))

Monthly_Savings = question_one - question_two
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print("Your monthly savings are ", Monthly_Savings )
print("Projected savings after one year, with interest, is:",Projected_Savings )