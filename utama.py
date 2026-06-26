from datetime import datetime

def simpan_hasil(modal, resiko_persen, posisi, entry, titik_sl, risk_amount, jarak_sl, hasil_leverage, position_size, position_size_leverage, rr, take_profit):
    sekarang = datetime.now()
    with open("history_trading.txt", "a", encoding="utf-8") as file:
        file.write(f"\nTanggal: {sekarang}\n")
        file.write("╔═════════════════════════════════════╗\n")
        file.write("║     RISK MANAGEMENT CALCULATOR      ║\n")
        file.write("╠═════════════════════════════════════╣\n")
        file.write(f"║  Posisi       : {f'{posisi}'.ljust(20)}║\n")
        file.write(f"║  Modal        : {f'${modal}'.ljust(20)}║\n")
        file.write(f"║  Risk %       : {f'{resiko_persen}%'.ljust(20)}║\n")
        file.write(f"║  Entry        : {f'{entry}'.ljust(20)}║\n")
        file.write(f"║  Stop Loss    : {f'{titik_sl}'.ljust(20)}║\n")
        file.write(f"║  Take Profit  : {f'{take_profit}'.ljust(20)}║\n")
        file.write(f"║  RR Ratio     : {f'1:{rr}'.ljust(20)}║\n")
        file.write("╠═════════════════════════════════════╣\n")
        file.write(f"║  Risk Amount  : {f'${risk_amount}'.ljust(20)}║\n")
        file.write(f"║  Jarak SL     : {f'{jarak_sl}'.ljust(20)}║\n")
        file.write(f"║  Leverage     : {f'{hasil_leverage}x'.ljust(20)}║\n")
        file.write(f"║  Size Tanpa LV: {f'{position_size}'.ljust(20)}║\n")
        file.write(f"║  Size + LV    : {f'{position_size_leverage}'.ljust(20)}║\n")
        file.write("╚═════════════════════════════════════╝\n")

def input_modal():
    while True:
        try:
            modal = float(input("Masukkan modal (USDT): "))
            if modal < 100 or modal > 1000000000:
                print("Waduh minimal 100 USDT kurang dari itu tidak bisa")
            else:
                return modal
        except:
            print("USDT tidak valid, masukan USDT (angka)")
    
def input_risk_percent():
    while True:
        try:
            resiko_persen = float(input("Masukkan risk percent (%): "))
            if resiko_persen < 1 or resiko_persen > 100:
                print("Waduh Minimal 1%, Maksimal 100%")
            else: 
                return resiko_persen
        except:
            print("Resiko tidak valid, masukan persen (angka)")

def input_entry():
    while True:
        try:
            entry = float(input("Masukkan mau Entry dimana: "))
            if entry <= 0 or entry > 99999999999:
                print("Waduh Entry-mu tidak valid, masukan ulang")
            else: 
                return entry
        except:
            print("Waduh Entry-mu tidak valid, masukan ulang")

def input_leverage():
    while True:
        try:
            leverage = int(input("Masukan leverage (1-150x): "))
            if leverage < 1 or leverage > 150:
                print("Minimal 1, Maksimal 150. Okai? Masukan ulang")
            else:
                return leverage
        except:
            print("Tidak valid, masukan jumlah leverage-nya")      

def input_posisi():
    while True:
        print("Pilih posisi trading:")
        print("1. LONG")
        print("2. SHORT")
        pilihan = input("Masukan pilihan (1/2): ")
        if pilihan == "1":
            return "LONG"
        elif pilihan == "2":
            return "SHORT"
        else:
            print("Pilihan tidak valid, masukan 1 atau 2!")

def input_sl(entry, posisi):  # ← tambah posisi sebagai argumen
    while True:
        try:
            titik_sl = float(input("Masukkan mau SL-nya dimana: "))
            if posisi == "LONG":
                if titik_sl <= 0 or titik_sl >= entry:
                    print("LONG: Stoploss harus dibawah entry!")
                else:
                    return titik_sl
            elif posisi == "SHORT":
                if titik_sl <= entry:
                    print("SHORT: Stoploss harus diatas entry!")
                else:
                    return titik_sl
        except:
            print("Stoploss tidak valid, masukan angka!")

def input_rr():
    while True:
        try:
            rr = int(input("Masukan Risk Reward Ratio (1-100): "))
            if rr < 1 or rr > 100:
                print("Minimal 1, Maksimal 100. Masukan ulang!")
            else:
                return rr
        except:
            print("Tidak valid, masukan angka!")

def hitung_risiko(modal, resiko_persen, entry, titik_sl, posisi, leverage, rr):
    risk_amount = modal * (resiko_persen / 100)
    if posisi == "LONG":
        jarak_sl = entry - titik_sl
        take_profit = entry + (jarak_sl * rr)
    elif posisi == "SHORT":
        jarak_sl = titik_sl - entry
        take_profit = entry - (jarak_sl * rr)
    position_size = round(risk_amount / jarak_sl, 2)
    position_size_leverage = round(position_size * leverage, 2)
    return risk_amount, jarak_sl, position_size, position_size_leverage, take_profit

def tampilkan_hasil(modal, resiko_persen, posisi, entry, titik_sl, risk_amount, jarak_sl, hasil_leverage, position_size, position_size_leverage, rr, take_profit):
    print("╔═════════════════════════════════════╗")
    print("║     RISK MANAGEMENT CALCULATOR      ║")
    print("╠═════════════════════════════════════╣")
    print(f"║  Posisi       : {f'{posisi}'.ljust(20)}║")
    print(f"║  Modal        : {f'${modal}'.ljust(20)}║")
    print(f"║  Risk %       : {f'{resiko_persen}%'.ljust(20)}║")
    print(f"║  Entry        : {f'{entry}'.ljust(20)}║")
    print(f"║  Stop Loss    : {f'{titik_sl}'.ljust(20)}║")
    print(f"║  Take Profit  : {f'{take_profit}'.ljust(20)}║")
    print(f"║  RR Ratio     : {f'1:{rr}'.ljust(20)}║")
    print("╠═════════════════════════════════════╣")
    print(f"║  Risk Amount  : {f'${risk_amount}'.ljust(20)}║")
    print(f"║  Jarak SL     : {f'{jarak_sl}'.ljust(20)}║")
    print(f"║  Leverage     : {f'{hasil_leverage}x'.ljust(20)}║")
    print(f"║  Size Tanpa LV: {f'{position_size}'.ljust(20)}║")
    print(f"║  Size + LV    : {f'{position_size_leverage}'.ljust(20)}║")
    print("╚═════════════════════════════════════╝")

def main():
    while True:
        hasil_modal = input_modal()
        hasil_resiko_persen = input_risk_percent()
        hasil_posisi = input_posisi()
        hasil_leverage = input_leverage()
        hasil_rr = input_rr()
        hasil_entry = input_entry()
        hasil_titik_sl = input_sl(hasil_entry, hasil_posisi)
        risk_amount, jarak_sl, position_size, position_size_leverage, take_profit = hitung_risiko(
            hasil_modal, hasil_resiko_persen, hasil_entry, hasil_titik_sl,
            hasil_posisi, hasil_leverage, hasil_rr
        )
        tampilkan_hasil(hasil_modal, hasil_resiko_persen, hasil_posisi, hasil_entry, 
                        hasil_titik_sl, risk_amount, jarak_sl, hasil_leverage, 
                        position_size, position_size_leverage, hasil_rr, take_profit)
        simpan = input("\nMau simpan hasil? (y/n): ")
        if simpan == "y":
            simpan_hasil(hasil_modal, hasil_resiko_persen, hasil_posisi, hasil_entry,
                        hasil_titik_sl, risk_amount, jarak_sl, hasil_leverage,
                        position_size, position_size_leverage, hasil_rr, take_profit)
            print("Hasil berhasil disimpan!")
        else:
            print("Hasil tidak disimpan.")
        hitung_lagi = input("Mau hitung ulang? (y/n): ")
        if hitung_lagi == "n":
            print("Sampai jumpa! Stay Focus and Consistent 👋")
            break

main()
