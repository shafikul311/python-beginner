age = int(input('Enter your age '))

limit_age = 18

ticket_price = 10 if int(age) < limit_age else 20
print("$",ticket_price) 