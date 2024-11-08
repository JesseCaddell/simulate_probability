import random
import matplotlib.pyplot as plt
from collections import Counter


#### TASK 1: SIMULATE COIN TOSS

def simulate_coin_toss(n=100):
    results = [random.choice(["Heads", "Tails"]) for _ in range(n)]
    counts = Counter(results)

    # print the counts
    print("Coin toss results:", counts)

    # plot the results
    plt.bar(counts.keys(), counts.values(), color=['blue','green'])
    plt.title("Coin toss simulation for 100 tosses")
    plt.xlabel("Outcome")
    plt.ylabel("Frequency")
    plt.show()

simulate_coin_toss()

### TASK 2: ROLLING DIE

def simulate_die_rolls(n=60):
    results = [random.randint(1, 6) for _ in range(n)]
    counts = Counter(results)

    # print the counts
    print("Die rolls results:", counts)

    # plot the results
    plt.bar(counts.keys(), counts.values(), color=['purple'])
    plt.title("Die roll simulation for 60 rolls")
    plt.xlabel("Die")
    plt.ylabel("Frequency")
    plt.show()

simulate_die_rolls()

### TASK 3: DRAWING CARDS

def simulate_card_draws(n=20):
    deck = ["Red"] * 26 + ["Black"] * 26
    results = [random.choice(deck) for _ in range(n)]
    counts = Counter(results)

    # Print the counts
    print("Card draw results:", counts)

    # Plot the results
    plt.bar(counts.keys(), counts.values(), color=['red', 'black'])
    plt.title("Card draw sim for 20 draws")
    plt.xlabel("Card Color")
    plt.ylabel("Frequency")
    plt.show()

simulate_card_draws()

## TASK 4: PROBABILITY OF COMPOUND EVENTS

def simulate_two_coin_flips(n=50):
    both_heads = 0
    one_head = 0

    for _ in range(n):
        flip1 = random.choice(["Heads", "Tails"])
        flip2 = random.choice(["Heads", "Tails"])

        if flip1 == "Heads" and flip2 == "Heads":
            both_heads += 1
        if flip1 == "Heads" or flip2 == "Heads":
            one_head += 1

    # Print results
    print(f"Both Heads: {both_heads}")
    print(f"At least one head: {one_head}")

    # Plot the results
    plt.bar(["Both Heads", "At Least One Head"], [both_heads, one_head], color=['purple', 'orange'])
    plt.title("Two coin flip sim for 50 flips")
    plt.xlabel("Event")
    plt.ylabel("Frequency")
    plt.show()

simulate_two_coin_flips()