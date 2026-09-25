#IMPORTANT:

# COMPOUND INTREST CALCULATOR 


#Principle = float(input("Enter the principle amount: "))
#Rate = float(input("Enter the rate of interest: "))
#Time = float(input("Enter the time in years: "))

#Compound_interest = Principle * (pow((1 + Rate / 100), Time)) - Principle

#print(f"Compound Interest: {Compound_interest:.2f}")

Principal = 0
Rate = 0
Time = 0 

while Principal <= 0:
    Principal = float(input("Enter the principal amount: "))
    if Principal <= 0:
        print("Principal cannot be less than or equal to zero")

while Rate <= 0:
    Rate = float(input("Enter the rate of interest: "))
    if Rate <= 0:
        print("Rate cannot be less than or equal to zero")

while Time <= 0:
    Time = float(input("Enter the time in years: "))
    if Time <= 0:
        print("Time cannot be less than or equal to zero")

total_amount = Principal * (pow((1 + Rate / 100), Time))
print (f" Balance fter {Time}year : ${total_amount:}")
