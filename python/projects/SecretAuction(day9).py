import auctionlogo
print(auctionlogo.logo)
bid={}
def find_max():
    winner=max(bid,key=bid.get)
    print(f"{winner} is the winner")

con=True
while con:
    name=input("Enter name: ")
    amnt=int(input("Enter bid amount ₹"))
    bid[name]=amnt
    con=input("Any other bidder yes or no ").lower()
    if con=="no":
        con=False
        find_max()
    elif con =="yes":
        print("\n"*100)
    else:
        print("invalid")