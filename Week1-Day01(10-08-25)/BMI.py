#  আজ আমরা BMI (বডি মাস ইনডেক্স) হিসাব করব।
#  BMI হিসাবের সূত্র: BMI = ওজন (কেজি) / (উচ্চতা (মিটার) * উচ্চতা (মিটার))

weight = float(input(" Enter your weight in kg:"))
hight = float(input("enter your hight in meter:"))

bmi = weight / (hight * hight)
print("your bmi is : ",bmi)
print(f"your BMI is : {bmi:.2f}")
