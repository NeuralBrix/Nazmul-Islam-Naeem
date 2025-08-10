# এখন আমরা দেখবো কিভাবে ইউজার থেকে ইনপুট নিতে হয়।
# Python এ ইনপুট নেওয়ার জন্য input() ফাংশন ব্যবহার করা হয়।   
a = input ("Enter your name : ") # এখানে "a" ভেরিয়েবল হিসাবে রাখা হয়েছে। 
print("Your input is : ",a) # এখানে ইউজার যে ইনপুট দিয়েছে তা প্রিন্ট করা হয়েছে। 

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
addition = a + b# এখানে দুইটি ভেরিয়েবল যোগ করা হয়েছে।
subtraction = a - b # এখানে দুইটি ভেরিয়েবল বিয়োগ করা হয়েছে।
division = a / b # এখানে দুইটি ভেরিয়েবল ভাগ করা হয়েছে।
multiplication = a * b # এখানে দুইটি ভেরিয়েবল গুন করা হয়েছে।

print("Addition is : ", addition) # এখানে যোগফল প্রিন্ট করা হয়েছে।
print("Subtraction is : ", subtraction) # এখানে বিয়োগফল প্রিন্ট করা হয়েছে।
print("Division is : ", division) # এখানে ভাগফল প্রিন্ট করা হয়েছে।
print("Multiplication is : ", multiplication) # এখানে গুনফল প্রিন্ট করা হয়েছে।
