import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bidder = 0
    for bidder in bidding_dictionary:
        bidding_amount = bidding_dictionary[bidder]
        if bidding_amount > highest_bidder:
            highest_bidder = bidder
            winner = bidder
    print(f"The  winner is {winner} and highest_bidder is {highest_bidder}")


bids = {}

should_continue = True
while should_continue:
    name = input("What is your name? ")
    price = int(input("How much would you like to bet?:$ "))
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bidders == 'no':
        should_continue = False
        find_highest_bidder(bids)
    elif other_bidders == 'yes':
        print("\n" * 40)