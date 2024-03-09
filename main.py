import random

start_money = 1300

def main():
    money = start_money
    for n in range(1337):
        print(f"Balance {money}")
        print("enter the bid")
        bet = int(input("- "))
        if money >= bet:
            rand = random.randint(1,2)
            print("1- eagle \n2- tails")
            stav = int(input("- "))
            if rand == stav:
                money -= bet
                money += bet * 3
                print("win")
            if rand != stav:
                money -= bet
                print("lose")
        else:
            print("Not enough money")
        if money == 0:
            print("enter the promo code (drop)")
            prom = input("- ")
            if prom == "drop":
                money += 4000


main()
