#calculating future age of user in 2050 from 2023
age_now = int(input("How old are you? "))
print(age_now)
currentyear = 2023
futureyear = 2050

years = futureyear - currentyear 
age = age_now + years

print(f"In 2050, you will be {age} years old.")