#if, else and elif statements in Python
# Python এ if, else এবং elif স্টেটমেন্ট ব্যবহার করে শর্তাধীন কার্যক্রম করা হয়।

#  এখন আমরা দেখবো কিভাবে if, else এবং elif স্টেটমেন্ট ব্যবহার করে GPA নির্নয় করবো।

# আমাদের কি কি লাগবে ? ১/ ইউজার থেকে নাম্বার ইনপুট নিতে হবে। ২/ ইনপুট নাম্বার থেকে GPA নির্নয় করতে হবে।
# ৩/ GPA এর উপর ভিত্তি করে গ্রেড নির্নয় করতে হবে। ৪/ গ্রেড প্রিন্ট করতে হবে।

marks = float(input("Enter your marks:"))
if marks >=80:
    print("your GPA is A+")
elif marks >=70:
    print("your GPA is A")
elif marks>=60:
    print("your Gpa is A-")
elif marks>=50:
    print("your Gpa is B")
elif marks>=40:
    print("your Gpa is C")
elif marks>= 33:
    print("your Gpa is D")
else:
    print("your Gpa is F")  
