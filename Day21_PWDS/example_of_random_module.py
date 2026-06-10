import random

# Roll a dice
print(random.randint(1, 6))

# Toss a coin
print(random.choice(["Head", "Tail"]))

# Generate a 6-digit OTP
otp = random.randint(100000, 999999)
print("OTP:", otp)

# Pick a random winner
participants = ["Ram", "Shyam", "Hari", "Sita"]
print("Winner:", random.choice(participants))

# Shuffle cards
cards = list(range(1, 53))
random.shuffle(cards)
print(cards)