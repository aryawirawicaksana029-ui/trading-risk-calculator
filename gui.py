import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Trading Risk Calculator")
window.geometry("450x650")
window.configure(bg="#1a1a2e")  # background gelap

# Warna tema
BG = "#1a1a2e"
CARD = "#16213e"
ACCENT = "#0f3460"
GREEN = "#00b4d8"
WHITE = "#ffffff"
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

# Card Input
card = tk.Frame(window, bg=CARD, padx=20, pady=15)
card.pack(padx=20, fill="x")

# Input fields
label(card, "Modal (USDT):").pack(anchor="w")
input_modal = entry(card)
input_modal.pack(fill="x", pady=3)

label(card, "Risk %:").pack(anchor="w", pady=(8,0))
input_risk = entry(card)
input_risk.pack(fill="x", pady=3)

label(card, "Posisi:").pack(anchor="w", pady=(8,0))
posisi_var = tk.StringVar(value="LONG")
frame_posisi = tk.Frame(card, bg=CARD)
frame_posisi.pack(anchor="w")
tk.Radiobutton(frame_posisi, text="LONG", variable=posisi_var, value="LONG",
               bg=CARD, fg=GREEN, selectcolor=ACCENT, font=("Arial", 10)).pack(side="left")
tk.Radiobutton(frame_posisi, text="SHORT", variable=posisi_var, value="SHORT",
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

def hitung_risiko(modal, resiko_persen, entry_price, titik_sl, posisi, leverage, rr):
    risk_amount = modal * (resiko_persen / 100)
    if posisi == "LONG":
        jarak_sl = entry_price - titik_sl
        take_profit = entry_price + (jarak_sl * rr)
    elif posisi == "SHORT":
        jarak_sl = titik_sl - entry_price
        take_profit = entry_price - (jarak_sl * rr)
    position_size = round(risk_amount / jarak_sl, 2)
    position_size_leverage = round(position_size * leverage, 2)
    return risk_amount, jarak_sl, position_size, position_size_leverage, take_profit

def hitung():
    try:
        modal = float(input_modal.get())
        risk = float(input_risk.get())
        posisi = posisi_var.get()
        leverage = int(input_leverage.get())
        rr = int(input_rr.get())
        entry_price = float(input_entry.get())
        sl = float(input_sl.get())

        risk_amount, jarak_sl, position_size, position_size_leverage, take_profit = hitung_risiko(
            modal, risk, entry_price, sl, posisi, leverage, rr
        )

        hasil_label.config(text=
            f"  Risk Amount   : ${risk_amount}\n"
            f"  Take Profit   : {take_profit}\n"
            f"  Jarak SL      : {jarak_sl}\n"
            f"  Size Tanpa LV : {position_size}\n"
            f"  Size + LV     : {position_size_leverage}"
        )
    except:
        messagebox.showerror("Error", "Input tidak valid! Pastikan semua terisi dengan benar.")

# Tombol Hitung
tk.Button(window, text="⚡ HITUNG RISIKO", command=hitung,
          bg=GREEN, fg="#1a1a2e", font=("Arial", 12, "bold"),
          relief="flat", padx=20, pady=8).pack(pady=15)

from datetime import datetime

def simpan():
    try:
        with open("history_trading.txt", "a", encoding="utf-8") as file:
            file.write(f"\nTanggal: {datetime.now()}\n")
            file.write(hasil_label.cget("text"))
            file.write("\n" + "="*40 + "\n")
        messagebox.showinfo("Sukses", "Hasil berhasil disimpan!")
    except:
        messagebox.showerror("Error", "Hitung dulu sebelum menyimpan!")

tk.Button(window, text="💾 SIMPAN HASIL", command=simpan,
          bg=YELLOW, fg="#1a1a2e", font=("Arial", 12, "bold"),
          relief="flat", padx=20, pady=8).pack(pady=5)

# Card Hasil
card_hasil = tk.Frame(window, bg=CARD, padx=20, pady=15)
card_hasil.pack(padx=20, fill="x")

tk.Label(card_hasil, text="📊 HASIL PERHITUNGAN", 
         bg=CARD, fg=YELLOW, font=("Arial", 11, "bold")).pack(anchor="w")

hasil_label = tk.Label(card_hasil, text="Isi form di atas dan klik HITUNG RISIKO",
                        bg=CARD, fg=WHITE, font=("Courier", 10), justify="left")
hasil_label.pack(anchor="w", pady=8)

window.mainloop()