question_one = int(input('Enter your monthly income:'))
question_two = int(input('Enter your total monthly expenses: '))

MonthlySavings = question_one - question_two
ProjectedSavings = MonthlySavings * 12 + (MonthlySavings * 12 * 0.05)
print("Your monthly savings are ", MonthlySavings )
print("Projected savings after one year, with interest, is:",ProjectedSavings )