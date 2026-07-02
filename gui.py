import tkinter as tk
from tkinter import messagebox
from datetime import datetime

window = tk.Tk()
window.title("Trading Risk Calculator")
window.geometry("450x650")
window.configure(bg="#1a1a2e")

# Color theme
BG     = "#1a1a2e"
CARD   = "#16213e"
ACCENT = "#0f3460"
GREEN  = "#00b4d8"
WHITE  = "#ffffff"
YELLOW = "#ffd60a"

def label(parent, text, color=WHITE):
    return tk.Label(parent, text=text, bg=CARD, fg=color, font=("Arial", 10))

def entry(parent):
    e = tk.Entry(parent, bg=ACCENT, fg=WHITE, insertbackground=WHITE,
                 font=("Arial", 11), relief="flat", width=25)
    return e

# Header
tk.Label(window, text="📈 TRADING RISK CALCULATOR",
         bg=BG, fg=GREEN, font=("Arial", 14, "bold")).pack(pady=15)

# Input Card
card = tk.Frame(window, bg=CARD, padx=20, pady=15)
card.pack(padx=20, fill="x")

label(card, "Balance (USDT):").pack(anchor="w")
input_balance = entry(card)
input_balance.pack(fill="x", pady=3)

label(card, "Risk %:").pack(anchor="w", pady=(8,0))
input_risk = entry(card)
input_risk.pack(fill="x", pady=3)

label(card, "Position:").pack(anchor="w", pady=(8,0))
position_var = tk.StringVar(value="LONG")
frame_position = tk.Frame(card, bg=CARD)
frame_position.pack(anchor="w")
tk.Radiobutton(frame_position, text="LONG", variable=position_var, value="LONG",
               bg=CARD, fg=GREEN, selectcolor=ACCENT, font=("Arial", 10)).pack(side="left")
tk.Radiobutton(frame_position, text="SHORT", variable=position_var, value="SHORT",
               bg=CARD, fg="#ff6b6b", selectcolor=ACCENT, font=("Arial", 10)).pack(side="left", padx=10)

label(card, "Leverage (1-150x):").pack(anchor="w", pady=(8,0))
input_leverage = entry(card)
input_leverage.pack(fill="x", pady=3)

label(card, "Risk Reward Ratio:").pack(anchor="w", pady=(8,0))
input_rr = entry(card)
input_rr.pack(fill="x", pady=3)

label(card, "Entry Price:").pack(anchor="w", pady=(8,0))
input_entry = entry(card)
input_entry.pack(fill="x", pady=3)

label(card, "Stop Loss:").pack(anchor="w", pady=(8,0))
input_sl = entry(card)
input_sl.pack(fill="x", pady=3)

def calculate_risk(balance, risk_percent, entry_price, stop_loss, position, leverage, rr):
    risk_amount = balance * (risk_percent / 100)
    if position == "LONG":
        sl_distance = entry_price - stop_loss
        take_profit = entry_price + (sl_distance * rr)
    elif position == "SHORT":
        sl_distance = stop_loss - entry_price
        take_profit = entry_price - (sl_distance * rr)
    position_size = round(risk_amount / sl_distance, 2)
    position_size_leverage = round(position_size * leverage, 2)
    return risk_amount, sl_distance, position_size, position_size_leverage, take_profit

def calculate():
    try:
        balance    = float(input_balance.get())
        risk       = float(input_risk.get())
        position   = position_var.get()
        leverage   = int(input_leverage.get())
        rr         = int(input_rr.get())
        entry_price = float(input_entry.get())
        sl         = float(input_sl.get())

        risk_amount, sl_distance, position_size, position_size_leverage, take_profit = calculate_risk(
            balance, risk, entry_price, sl, position, leverage, rr
        )

        result_label.config(text=
            f"  Risk Amount   : ${risk_amount}\n"
            f"  Take Profit   : {take_profit}\n"
            f"  SL Distance   : {sl_distance}\n"
            f"  Size (No LV)  : {position_size}\n"
            f"  Size (LV)     : {position_size_leverage}"
        )
    except:
        messagebox.showerror("Error", "Invalid input! Please fill all fields correctly.")

# Calculate Button
tk.Button(window, text="⚡ CALCULATE RISK", command=calculate,
          bg=GREEN, fg="#1a1a2e", font=("Arial", 12, "bold"),
          relief="flat", padx=20, pady=8).pack(pady=15)

def save():
    try:
        with open("trading_history.txt", "a", encoding="utf-8") as file:
            file.write(f"\nDate: {datetime.now()}\n")
            file.write(result_label.cget("text"))
            file.write("\n" + "="*40 + "\n")
        messagebox.showinfo("Success", "Result saved successfully!")
    except:
        messagebox.showerror("Error", "Please calculate first before saving!")

# Save Button
tk.Button(window, text="💾 SAVE RESULT", command=save,
          bg=YELLOW, fg="#1a1a2e", font=("Arial", 12, "bold"),
          relief="flat", padx=20, pady=8).pack(pady=5)

# Result Card
card_result = tk.Frame(window, bg=CARD, padx=20, pady=15)
card_result.pack(padx=20, fill="x")

tk.Label(card_result, text="📊 CALCULATION RESULT",
         bg=CARD, fg=YELLOW, font=("Arial", 11, "bold")).pack(anchor="w")

result_label = tk.Label(card_result, text="Fill the form above and click CALCULATE RISK",
                         bg=CARD, fg=WHITE, font=("Courier", 10), justify="left")
result_label.pack(anchor="w", pady=8)

window.mainloop()