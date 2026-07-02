from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        # Mengambil data dari form dan menyesuaikan dengan variabel bahasa Inggris
        balance = float(request.form["balance"])
        risk_percent = float(request.form["risk"])
        position = request.form["position"]
        leverage = int(request.form["leverage"])
        rr = int(request.form["rr"])
        entry = float(request.form["entry"])
        stop_loss = float(request.form["sl"])

        # Logika kalkulasi (konsisten dengan logika sebelumnya)
        risk_amount = balance * (risk_percent / 100)
        
        if position == "LONG":
            sl_distance = entry - stop_loss
            take_profit = entry + (sl_distance * rr)
        elif position == "SHORT":
            sl_distance = stop_loss - entry
            take_profit = entry - (sl_distance * rr)
        else:
            raise ValueError("Invalid position type")

        position_size = round(risk_amount / sl_distance, 2)
        position_size_leverage = round(position_size * leverage, 2)

        # Mempersiapkan hasil untuk template
        result = {
            "risk_amount": risk_amount,
            "take_profit": take_profit,
            "sl_distance": sl_distance,
            "position_size": position_size,
            "position_size_leverage": position_size_leverage
        }

        return render_template("index.html", result=result)
    except Exception as e:
        # Mengembalikan error dalam bahasa Inggris
        return render_template("index.html", error="Invalid input! Please check your fields.")
