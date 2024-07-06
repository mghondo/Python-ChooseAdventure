from Art import gavel_art

def get_player_info(player_number):
    name = input(f"Player {player_number}, what's your name? ")
    while True:
        try:
            bid = float(input(f"{name}, what's your bid? $"))
            if bid < 0:
                print("What's your deal, you want money back? Come on bro.")
            else:
                return name, bid
        except ValueError:
            print("Please enter a valid number.")

def find_winner(bids):
    return max(bids, key=bids.get)

def silent_auction():
    print(gavel_art)  # Print the gavel art at the start of the auction
    print("Welcome to the Silent Auction!")
    print("------------------------------")
    
    bids = {}
    
    for i in range(1, 4):  # For 3 players
        name, bid = get_player_info(i)
        bids[name] = bid
    
    print("\nAll bids:")
    for name, bid in bids.items():
        print(f"{name}: ${bid:.2f}")
    
    winner = find_winner(bids)
    winning_bid = bids[winner]
    
    print("\n" + gavel_art)  # Print the gavel art again before announcing the winner
    print(f"The winner is {winner} with a bid of ${winning_bid:.2f}!")

if __name__ == "__main__":
    silent_auction()
