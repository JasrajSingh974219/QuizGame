import time

true = ["T", "t", "True", "true"]
false = ["F", "f", "False", "false"]
correct = 0

name = input ("what is your name?")

print("\nOK, " + name +", let's get started. remember, the following answers are only true of false")

print ("\n paris is the capital of france.")
choice = input(">>>")
if choice in true:
    correct += 1
else:
    correct += 0

print ("\n england is an island.")
choice = input(">>>")
if choice in true:
    correct += 1
else:
    correct += 0

print ("\n northern ireland isn't part of great britian.")
choice = input(">>>")
if choice in true:
    correct += 1
else:
    correct += 0

print ("\n andorra is between france and spain.")
choice = input(">>>")
if choice in true:
    correct += 1
else:
    correct += 0

print ("\n iran use to be part of the persian empire.")
choice = input(">>>")
if choice in true:
    correct += 1
else:
    correct += 0

print ("\n turkmenistan ins't a real country.")
choice = input(">>>")
if choice in true:
    correct += 1
else:
    correct += 0

print("\nyou're finished," + name +". you got", correct, "out of 6 correct.")