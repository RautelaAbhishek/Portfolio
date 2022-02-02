print ("Welcome to the Tip Calculator")
total = float(input("What was the total bill? $"))
percentage = int(input("What percentage would you like to tip? "))
ppl = int(input("How many people are splitting the bill? "))
tpp = ( total * (1 + percentage/100) )/ppl
print(f"Each person should should pay ${tpp:.2f}.")