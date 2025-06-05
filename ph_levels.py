# Write code below 💖
"""
An else clause can be optionally added to an if statement.

If the condition evaluates to True, code in the if part is executed.
If the condition evaluates to False, code in the else part is executed.

# Elif
One or more elif statements (short for "else if") can be optionally
added in between the if and else to provide additional condition(s)
to check. Sometimes two is simply not enough.
"""
import random
grade = random.randint(0,100)

if grade > 90:
    print('A')
elif grade> 80:
    print('B')
elif grade >70:
    print('C')
elif grade >60:
    print('D')
else:
    print('F 😂')

print('Your Grade es ' + str(grade))