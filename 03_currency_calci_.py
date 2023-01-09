




with open('currencycalci.txt', 'r') as f:
    lines = f.readlines()

currencyDict = {}
try:
    
    for line in lines :
        parsed = line.split("\t")
        currencyDict[parsed[0]] = parsed[1]

    print (currencyDict)
except:
    print ("please do something good!!")
amount = int(input("Enter amount:\n"))
print = ("Enter which currency you want to select out off these: \n")
[print (item) for item in currencyDict.keys()]
currency = input("please enter one of the values: \n")
print (f"{amount} USD = {amount * float(currencyDict [currency])} {currency}")
