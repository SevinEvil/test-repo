def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Fehler: Division durch 0!"
    return a / b

def main():
    while True:
        print("\nWähle die Operation:")
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")
        print("5. Beenden")

        choice = input("Deine Wahl: ")

        if choice == "5":
            print("Taschenrechner beendet.")
            break

        num1 = float(input("Erste Zahl: "))
        num2 = float(input("Zweite Zahl: "))

        if choice == "1":
            print("Ergebnis:", add(num1, num2))
        elif choice == "2":
            print("Ergebnis:", subtract(num1, num2))
        elif choice == "3":
            print("Ergebnis:", multiply(num1, num2))
        elif choice == "4":
            print("Ergebnis:", divide(num1, num2))
        else:
            print("Ungültige Auswahl!")

if __name__ == "__main__":
    main()
