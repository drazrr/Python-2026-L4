def extract_even(l):
    even_list = []
    for x in l: 
        if x % 2 == 0: 
            even_list += [x]
    return even_list 
#list(input("Enter a list of ...").split(" "))