from datetime import datetime

def save_result(balance, risk_percent, position, entry, stop_loss, risk_amount, sl_distance, leverage, position_size, position_size_leverage, rr, take_profit):
    now = datetime.now()
    with open("trading_history.txt", "a", encoding="utf-8") as file:
        file.write(f"\nDate: {now}\n")
        file.write("╔═════════════════════════════════════╗\n")
        file.write("║     RISK MANAGEMENT CALCULATOR      ║\n")
        file.write("╠═════════════════════════════════════╣\n")
        file.write(f"║  Position     : {f'{position}'.ljust(20)}║\n")
        file.write(f"║  Balance      : {f'${balance}'.ljust(20)}║\n")
        file.write(f"║  Risk %       : {f'{risk_percent}%'.ljust(20)}║\n")
        file.write(f"║  Entry        : {f'{entry}'.ljust(20)}║\n")
        file.write(f"║  Stop Loss    : {f'{stop_loss}'.ljust(20)}║\n")
        file.write(f"║  Take Profit  : {f'{take_profit}'.ljust(20)}║\n")
        file.write(f"║  RR Ratio     : {f'1:{rr}'.ljust(20)}║\n")
        file.write("╠═════════════════════════════════════╣\n")
        file.write(f"║  Risk Amount  : {f'${risk_amount}'.ljust(20)}║\n")
        file.write(f"║  SL Distance  : {f'{sl_distance}'.ljust(20)}║\n")
        file.write(f"║  Leverage     : {f'{leverage}x'.ljust(20)}║\n")
        file.write(f"║  Size (No LV) : {f'{position_size}'.ljust(20)}║\n")
        file.write(f"║  Size (LV)    : {f'{position_size_leverage}'.ljust(20)}║\n")
        file.write("╚═════════════════════════════════════╝\n")

def input_balance():
    while True:
        try:
            balance = float(input("Enter account balance (USDT): "))
            if balance < 100 or balance > 1000000000:
                print("Minimum balance is $100 USDT.")
            else:
                return balance
        except:
            print("Invalid input! Please enter a number.")

def input_risk_percent():
    while True:
        try:
            risk_percent = float(input("Enter risk percentage (%): "))
            if risk_percent < 1 or risk_percent > 100:
                print("Risk must be between 1% and 100%.")
            else:
                return risk_percent
        except:
            print("Invalid input! Please enter a number.")

def input_entry():
    while True:
        try:
            entry = float(input("Enter entry price: "))
            if entry <= 0 or entry > 99999999999:
                print("Invalid entry price! Please enter a valid number.")
            else:
                return entry
        except:
            print("Invalid input! Please enter a number.")

def input_leverage():
    while True:
        try:
            leverage = int(input("Enter leverage (1-150x): "))
            if leverage < 1 or leverage > 150:
                print("Leverage must be between 1x and 150x.")
            else:
                return leverage
        except:
            print("Invalid input! Please enter a number.")

def input_position():
    while True:
        print("Select trading position:")
        print("1. LONG")
        print("2. SHORT")
        choice = input("Enter choice (1/2): ")
        if choice == "1":
            return "LONG"
        elif choice == "2":
            return "SHORT"
        else:
            print("Invalid choice! Please enter 1 or 2.")

def input_stop_loss(entry, position):
    while True:
        try:
            stop_loss = float(input("Enter stop loss price: "))
            if position == "LONG":
                if stop_loss <= 0 or stop_loss >= entry:
                    print("LONG: Stop loss must be below entry price!")
                else:
                    return stop_loss
            elif position == "SHORT":
                if stop_loss <= entry:
                    print("SHORT: Stop loss must be above entry price!")
                else:
                    return stop_loss
        except:
            print("Invalid input! Please enter a number.")

def input_rr():
    while True:
        try:
            rr = int(input("Enter Risk Reward Ratio (1-100): "))
            if rr < 1 or rr > 100:
                print("RR Ratio must be between 1 and 100.")
            else:
                return rr
        except:
            print("Invalid input! Please enter a number.")

def calculate_risk(balance, risk_percent, entry, stop_loss, position, leverage, rr):
    risk_amount = balance * (risk_percent / 100)
    if position == "LONG":
        sl_distance = entry - stop_loss
        take_profit = entry + (sl_distance * rr)
    elif position == "SHORT":
        sl_distance = stop_loss - entry
        take_profit = entry - (sl_distance * rr)
    position_size = round(risk_amount / sl_distance, 2)
    position_size_leverage = round(position_size * leverage, 2)
    return risk_amount, sl_distance, position_size, position_size_leverage, take_profit

def display_result(balance, risk_percent, position, entry, stop_loss, risk_amount, sl_distance, leverage, position_size, position_size_leverage, rr, take_profit):
    print("╔═════════════════════════════════════╗")
    print("║     RISK MANAGEMENT CALCULATOR      ║")
    print("╠═════════════════════════════════════╣")
    print(f"║  Position     : {f'{position}'.ljust(20)}║")
    print(f"║  Balance      : {f'${balance}'.ljust(20)}║")
    print(f"║  Risk %       : {f'{risk_percent}%'.ljust(20)}║")
    print(f"║  Entry        : {f'{entry}'.ljust(20)}║")
    print(f"║  Stop Loss    : {f'{stop_loss}'.ljust(20)}║")
    print(f"║  Take Profit  : {f'{take_profit}'.ljust(20)}║")
    print(f"║  RR Ratio     : {f'1:{rr}'.ljust(20)}║")
    print("╠═════════════════════════════════════╣")
    print(f"║  Risk Amount  : {f'${risk_amount}'.ljust(20)}║")
    print(f"║  SL Distance  : {f'{sl_distance}'.ljust(20)}║")
    print(f"║  Leverage     : {f'{leverage}x'.ljust(20)}║")
    print(f"║  Size (No LV) : {f'{position_size}'.ljust(20)}║")
    print(f"║  Size (LV)    : {f'{position_size_leverage}'.ljust(20)}║")
    print("╚═════════════════════════════════════╝")

def main():
    while True:
        balance = input_balance()
        risk_percent = input_risk_percent()
        position = input_position()
        leverage = input_leverage()
        rr = input_rr()
        entry = input_entry()
        stop_loss = input_stop_loss(entry, position)

        risk_amount, sl_distance, position_size, position_size_leverage, take_profit = calculate_risk(
            balance, risk_percent, entry, stop_loss, position, leverage, rr
        )

        display_result(balance, risk_percent, position, entry, stop_loss,
                       risk_amount, sl_distance, leverage,
                       position_size, position_size_leverage, rr, take_profit)

        save = input("\nSave result? (y/n): ")
        if save.lower() == "y":
            save_result(balance, risk_percent, position, entry, stop_loss,
                        risk_amount, sl_distance, leverage,
                        position_size, position_size_leverage, rr, take_profit)
            print("Result saved to trading_history.txt!")
        else:
            print("Result not saved.")

        again = input("Calculate again? (y/n): ")
        if again.lower() == "n":
            print("Goodbye! Stay focused and consistent! 👋")
            break

if __name__ == "__main__":
    main()