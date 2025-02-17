
def bid_winner(bid_details):
    winner = {}
    highest_bidder_amount = 0
    for bid in bid_details:
        if highest_bidder_amount < bid_details[bid]:
            highest_bidder_amount = bid_details[bid]
            winner = {bid: bid_details[bid]}
    print(f"Bid winner is {list(winner)[0]} with a bid amount {winner.get(list(winner)[0])}")

bidding = True
bidder_details = {}
while bidding:
    bidder_name = input("Enter bidder name :")
    bidding_amount = int(input("Enter bidding amount"))
    bidder_details[bidder_name] = bidding_amount
    next_bidder = input("Are there any more bidder. Type 'Yes' or 'No':").lower()

    if next_bidder == 'no':
        bidding = False

print(f"Bid Details: {bidder_details}")
bid_winner(bidder_details)
