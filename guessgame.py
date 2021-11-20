import random

def main():
    num1 = random.randint(0,9)
    print("you have 3 guesses to find the number ")
    i = 3
    while i >0 :
        print("please guess a number")
        guess = int(input())
        if(guess == num1):
            print("you have guessed correctly")
            print(f"your score is ",i)
            print("would you like to play again : y/n (y stands for yes , n stands for no)")
            r=input()
            if (r=='y'):
                main()
        else:
            print("you have gussed incorrectly ")
            print(f"you have", i-1, "chances")
            i = i-1

    if(i==0):
     print("you have lost the game")
     print(f"the correct number is ", num1)
     print("would you like to play again : y/n (y stands for yes , n stands for no)")
     s=input()
     if (s=='y'):
         main()

if __name__ == '__main__':
    main()
