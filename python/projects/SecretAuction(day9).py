import auctionlogo
print(auctionlogo.logo)
dic={}

def again():
    name=input("What is your name? ")
    bid=int(input("What's your bid? ₹"))
    dic[name]=bid
while True:
    again()
    another=input("Are there other bidders yes or no? ").lower()
    if another=="no":
        break
winner=max(dic,key=dic.get)
print(f"{winner} won the bid with bid amount{winner[0]}")