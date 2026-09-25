colors = ["Blue","Yellow","Red","Pink"]
a = input("What is your favorite color ? ")
found = False 
index = -1
for i in range(0,len(colors)):
    if colors[i].lower() == a.lower():
            found = True 
            index = i
            break
    
if found:
      print("found")
else:
      print("sorry")
            
