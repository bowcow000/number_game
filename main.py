import random

attempt = 3
wins = 0

while attempt > 0:
    randoms = random.randint(1, 10)
    asd = int(input("Угадайте число: "))
    attempt -= 1
    if asd == randoms:
        print(f"Вы угадали число {randoms}")
        print("="*30,"|")
        wins += 1
    else:
        print(f"Вы не угадали число {randoms}")
        print("="*30,"|")
    if wins == 3:
        print("Вы угадали все числа!!!")
    elif attempt == 0:
        print("Ваши попытки исчерпаны")
        print("Игра завершается")