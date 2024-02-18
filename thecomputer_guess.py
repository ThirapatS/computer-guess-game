import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low <= high:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high [h], too low [l], or correct [c]? ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay {guess} is correct!")

getReady = ''
while getReady != "y":
    print("The computer will try to guess what number do you think")
    getReady = input("Are you ready? ready[y] not now[n]")
    if getReady == "y":
        highN = int(input("What the highest number ex. you what number 55 maybe the highest number should be 100 :"))
        computer_guess(highN)
    else:
        continue
