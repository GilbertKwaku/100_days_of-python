# LOVE CALCULATOR
print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is your partner's name?\n")

# Converted names to lower case
lower_casename1 = (name1.lower())
lower_casename2 = (name2.lower())

# Count characters in your name
your_t = (lower_casename1.count("t"))
your_r = (lower_casename1.count("r"))
your_u = (lower_casename1.count("u"))
your_e = (lower_casename1.count("e"))
your_l = (lower_casename1.count("l"))
your_o = (lower_casename1.count("o"))
your_v = (lower_casename1.count("v"))


# Count characters in Partner's name
their_t = (lower_casename2.count("t"))
their_r = (lower_casename2.count("r"))
their_u = (lower_casename2.count("u"))
their_e = (lower_casename2.count("e"))
their_l = (lower_casename2.count("l"))
their_o = (lower_casename2.count("o"))
their_v = (lower_casename2.count("v"))


# Displaying to the user number of times the letters in 'TRUELOVE' occur in YOUR name
print("NUMBER OF 'TRUELOVE' CHARACTERS PRESENT IN YOUR NAME:\n=======================================================")
print(f"T occurs : {your_t} times")
print(f"R occurs : {your_r} times")
print(f"U occurs : {your_u} times")
print(f"E occurs : {your_e} times")
print(f"L occurs : {your_l} times")
print(f"O occurs : {your_o} times")
print(f"V occurs : {your_v} times")
print(f"E occurs : {your_e} times")

# Total for YOUR name:
your_total = your_t + your_r + your_u + your_e + your_l + your_o  + your_v + your_e
print(f"Your total is {your_total}")
# print(type(total))

# Displaying to the user number of times the letters in 'TRUELOVE' occur in PARTNER'S name
print("NUMBER OF 'TRUELOVE' CHARACTERS PRESENT IN PARTNER'S NAME:\n=======================================================")
print(f"T occurs : {their_t} times")
print(f"R occurs : {their_r} times")
print(f"U occurs : {their_u} times")
print(f"E occurs : {their_e} times")
print(f"L occurs : {their_l} times")
print(f"O occurs : {their_o} times")
print(f"V occurs : {their_v} times")
print(f"E occurs : {their_e} times")

# Score for PARTNER'S name :
their_total = their_t + their_r + their_u + their_e + their_l + their_o  + their_v + their_e
print(f"Partner's total is {their_total}")

# Display the total score of  counted 'TRUELOVE' characters in both names
love_score  = str(your_total) + str(their_total)
final_score = int(love_score)
# print(f"Your love score is: {love_score}")


# conditions
if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score} and you go together like coke and mentos")
elif final_score > 40 and final_score > 50:
    print(f"Your score is {final_score}, you are alright together")
else:
    print(f"Your score is {final_score} you should break up immediately")
