#Day1 [16/7/2018]
#A Few Things to Try
#1. Hours in a year. How many hours are in a year?
print(24*365)
print(24*366)
# If that year is a normal year with 365 days, there are 8760 hours in a year.
# If that year is a leap year with 366 days, there are 8784 hours in a year.

#2.Minutes in a decade. How many minutes are in a decade?
print(60*24*365*10)
# there are 5256000 minutes in a decade.

#3.Your age in seconds. How many seconds old are you?
print(20*60*60*24*365)
#I am 630720000 seconds old.

#4.Andreea Visanoiu: I'm 486180000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
print(486180000/60/60/24/365)
#Andreea is 15 years old.

#Here are some tougher questions:
#5.How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
#integer n = 1;
#assump the system increasw +1 per millisecond
#calculate the maximum
maximum = (2 ** 31 - 1)
print(maximum)
time_run_out = maximum/100/60/60/24
print(time_run_out)
print(int(time_run_out))
#So, it takes around 248 days for a 32-bit system to timeout, if it has a bug with integer overflow 

#6.How about a 64-bit system?
maximum = (2 ** 63 - 1)
print(maximum)
time_run_out = maximum/100/60/60/24
print(time_run_out)
print(int(time_run_out))
#So, it takes around 1067519911673 days for a 64-bit system to timeout, if it has a bug with integer overflow 

#7.Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday)
import datetime
Year = int(input(" Please enter the year you were born "))
Month = int(input(" Please enter the number of the month you were born.  For example 10 = October "))
Day = int(input(" Please enter the day you were born "))
Time = int(input(" Please enter the time you were born in integer. For example 1200 = noon"))
DOB = datetime.datetime(Year,Month,Day,Time)
Age = (datetime.datetime.now() - DOB)
Hours_of_birth = (Age.days*24*365)
Minutes_of_birth = (Age.days*60*24*365)
Seconds_of_birth = (Age.days*60*60*24*365)
print("You are " + str(Age.days) + " days old, " + str(Hours_of_birth) + " hours, " + str(Minutes_of_birth) + " minutes, "+ str(Seconds_of_birth) + " seconds. " )
convertdays = int(Age.days)
AgeYears = convertdays/365
print("Or you are " + str(AgeYears) + " years old to be more precise!")

#Day2 [17/7/2018]
#No Homework 

#Day3 [18/7/2018]
#1.Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.
first_name = str(input(" Please tell me your first name. "))
last_name = str(input(" Please tell me your last name. "))
print("Hello, " + first_name + (" ") + last_name + " ! ")

#2.Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)

#3. Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
#WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
#Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
#Table of Contents

#Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13

#Day4 [19/7/2018]

#Day5 [20/7/2018]
