def remove_dollar_sign(s):
    return s.replace("$","")
s = input("What is ur choosen word ?")
new_s = remove_dollar_sign(s)
print(new_s)