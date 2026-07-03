blackls = ["iamspam@gmail.com","tomcruise@gmail.com","ethanhunt@gmail.com","hehe@gmail.com","idkhow@gmail.com","whyyy@yahoo.com"]
mail = input("Enter sender email: ")
f = False
for recieve in blackls:
    if recieve == email:
        f = True
        break
if f:
    print("Spam Email")
else:
    print("Safe Email")
