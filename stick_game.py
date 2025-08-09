import time

sticks = 10
player = 1

def display_sticks(count):
    print("Sticks: " + "| " * count)
    print(f"({count} remaining)\n")

print("🎮 Welcome to the Stick Game!")
print("Rule: Take 1 to 3 sticks. The player who takes the last stick loses.\n")
time.sleep(1)

while sticks > 0:
    display_sticks(sticks)
    try:
        taken = int(input(f"Player {player}, how many sticks will you take? (1-3): "))
        if taken < 1 or taken > 3 or taken > sticks:
            print("❌ Invalid move! Try again.\n")
            continue
    except ValueError:
        print("❌ Please enter a valid number!\n")
        continue

    sticks -= taken
    time.sleep(0.5)

    if sticks == 0:
        print(f"\n💥 Player {player} took the last stick!")
        print(f"🏆 Player {3 - player} wins! 🎉")
        break

    player = 2 if player == 1 else 1
    print("-" * 30)
    time.sleep(0.5)
