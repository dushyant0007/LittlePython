from turtle import clear

import logo

nextBitter = True

bids = {}
print(logo.logo)

while nextBitter:
    name = input(" Enter Your Name \n ")
    bit = int(input(" Enter Your Bid \n $"))
    bids[name] = bit
    isNext = input(" Is There any other bitter \n type 'y' for yes 'n' for no ")
    if isNext == 'y':
        nextBitter = True

    else:
        nextBitter = False

nameOfWinner = ''
highestBid = 0
for bidder in bids:

    bidder_amount = bids[bidder]

    if bidder_amount > highestBid:
        highestBid = bidder_amount
        nameOfWinner = bidder

print(f" The winner is {nameOfWinner} bid {highestBid}")
