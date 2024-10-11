import random
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
reset = Fore.RESET

card_info_db = {
    "461046": {
        "brand": "Visa",
        "type": "Debit",
        "level": "Visa Classic",
        "bank": "Jpmorgan Chase Bank N.A.",
        "country": "United States of America",
        "currency": "USD",
        "issuer_contact": "Unavailable"
    },
    "541234": {
        "brand": "Mastercard",
        "type": "Credit",
        "level": "Mastercard Standard",
        "bank": "Bank of America",
        "country": "United States of America",
        "currency": "USD",
        "issuer_contact": "Unavailable"
    },
    "371449": {
        "brand": "American Express",
        "type": "Credit",
        "level": "American Express Gold",
        "bank": "American Express Bank, FSB",
        "country": "United States of America",
        "currency": "USD",
        "issuer_contact": "Unavailable"
    },
    "601100": {
        "brand": "Discover",
        "type": "Credit",
        "level": "Discover Card",
        "bank": "Discover Bank",
        "country": "United States of America",
        "currency": "USD",
        "issuer_contact": "Unavailable"
    },
    "353011": {
        "brand": "JCB",
        "type": "Credit",
        "level": "JCB Card",
        "bank": "JCB International",
        "country": "Japan",
        "currency": "JPY",
        "issuer_contact": "Unavailable"
    },
    "450028": {
        "brand": "Visa",
        "type": "Credit",
        "level": "Visa Signature",
        "bank": "Wells Fargo Bank",
        "country": "United States of America",
        "currency": "USD",
        "issuer_contact": "Unavailable"
    },
    "545454": {
        "brand": "Mastercard",
        "type": "Debit",
        "level": "Mastercard World",
        "bank": "Citibank",
        "country": "United States of America",
        "currency": "USD",
        "issuer_contact": "Unavailable"
    },
    "375193": {
        "brand": "American Express",
        "type": "Credit",
        "level": "American Express Platinum",
        "bank": "American Express Bank, FSB",
        "country": "United States of America",
        "currency": "USD",
        "issuer_contact": "Unavailable"
    },
    "601151": {
        "brand": "Discover",
        "type": "Credit",
        "level": "Discover It",
        "bank": "Discover Bank",
        "country": "United States of America",
        "currency": "USD",
        "issuer_contact": "Unavailable"
    },
}

def check_bin(bin_number):
    return card_info_db.get(bin_number)

def generate_card_numbers(bin_number):
    numbers = [f"{bin_number}{''.join([str(random.randint(0, 9)) for _ in range(10)])}|{random.randint(1, 12):02}|{random.randint(2024, 2029)}|{random.randint(100, 999)}"
               for _ in range(10)]
    save_generated_cards(numbers)
    return numbers

def save_generated_cards(numbers):
    if not os.path.exists('data'):
        os.makedirs('data')
    
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("data/generated_cards.txt", "a") as f:
        f.write(f"{date_str}|{len(numbers)} cards generated\n")
        for number in numbers:
            f.write(f"{number}\n")

def display_menu():
    print(f"{cyan}--- Menu ---{reset}")
    print(f"{blue}1. Check a BIN/IIN{reset}")
    print(f"{green}2. Generate card numbers{reset}")
    print(f"{red}3. Exit{reset}")

def main():
    while True:
        display_menu()

        choice = input(f"{cyan}Choose an option (1-3): {reset}")

        if choice == '1':
            bin_number = input(f"{cyan}Enter the BIN/IIN to check (e.g., 461046): {reset}")
            info = check_bin(bin_number)
            if info:
                print(f"{green}💳 BIN/IIN: {bin_number} 🇺🇸")
                print(f"{green}💳 Card Brand: {info['brand']}")
                print(f"{green}💳 Card Type: {info['type']}")
                print(f"{green}💳 Card Level: {info['level']}")
                print(f"{green}🏦 Bank Name: {info['bank']}")
                print(f"{green}🌐 Country: {info['country']} - 💲{info['currency']}")
                print(f"{green}☃️ Issuer's Contact: {info['issuer_contact']}")
            else:
                print(f"{red}Information not found for this BIN/IIN.{reset}")

        elif choice == '2':
            bin_number = input(f"{cyan}Enter the BIN/IIN to generate numbers (e.g., 461046): {reset}")
            numbers = generate_card_numbers(bin_number)
            print(f"{blue}Generated card numbers:")
            for number in numbers:
                print(f"{blue}{number}")

        elif choice == '3':
            print(f"{yellow}Goodbye!{reset}")
            break

        else:
            print(f"{red}Invalid option, please try again.{reset}")

if __name__ == "__main__":
    main()
