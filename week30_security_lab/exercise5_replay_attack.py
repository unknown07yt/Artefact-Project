
# Part 1: Original Needham-Schroeder Session
print("=== Part 1: Original Needham-Schroeder Session ===\n")

# Server generates session key
K_AB = "SESSIONKEY123"

# Ticket for Bob
message3 = "Ticket_for_Bob_encrypted_with_KBS"

print("Alice -> Server: Request session with Bob")
print("Server -> Alice: Sends session key K_AB")
print("Alice -> Bob: Sends Message 3 (ticket)")
print("Message 3:", message3)

# Bob challenge
Nb = 100
print("Bob challenge:", Nb)
print("Alice responds:", Nb - 1)
print("Authentication Successful\n")


# Part 2: Attacker Records Old Session

print("=== Part 2: Attacker Records Old Session ===\n")

# Attacker records old session key and ticket
recorded_KAB = K_AB
recorded_message3 = message3

print("Attacker recorded session key:", recorded_KAB)
print("Attacker recorded message3:", recorded_message3, "\n")


# Part 3: Replay Attack (Successful)

print("=== Part 3: Replay Attack Begins ===\n")

# Attacker replays old Message 3 to Bob
print("Attacker -> Bob: Replays old Message 3")
print("Bob believes Alice wants to start a new session")

# Bob sends new challenge
Nb_attack = 700
print("Bob sends challenge Nb:", Nb_attack)

# Attacker knows old session key and can respond correctly
response = Nb_attack - 1
print("Attacker responds:", response)

# Bob verifies response
print("\nBob verifies response")
print("Authentication Successful")
print("\nReplay attack SUCCESSFUL: Bob believes attacker is Alice")