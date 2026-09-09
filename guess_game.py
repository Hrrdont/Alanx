import random
secret = random.randint(1, 100)
a = 0   # 随机生成 1~100 的整数

while True:        # 无限循环，直到遇到 break
    a += 1
    guess = int(input("Guess the number (1-100): "))   # 输入文字并转成整数
    if guess < secret:
        print("Too low! Try again.")   
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
        break          # 跳出循环

print(f"You guessed {a} times.")