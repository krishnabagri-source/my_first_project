def game():
    import random
    '''
    ROCK = 1
    SCISSOR = 0
    PAPER = -1
    '''
    computer = random.choice([-1,0,1])
    a = input("Enter your choice (r for Rock, p for Paper, s for Scissors):").strip().upper()
    dic = {"R":1, "S":0, "P":-1}
    if a not in dic:
        print("Invalid input. Please enter r, p, or s.")
        return
    revdic = {1:"rock" , 0:"scissor", -1:"paper"}
    b = dic[a]
    print(f"you choose {revdic[b]}\ncomputer choose {revdic[computer]}")
    if(b == computer):
        print("its a draw")
    else:
        if(computer == -1 and b == 0):
            print("you win")
        elif(computer == -1 and b == 1):
            print("you lose")
        elif(computer == 0 and b ==-1):
            print("you lose")
        elif(computer == 0 and b == 1):
            print("you win")
        elif(computer == 1 and b == 0):
            print("you lose")
        elif(computer == 1 and b == -1):
            print("you win")
for _ in range(7):
    game()
