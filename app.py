from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hitung", methods=["POST"])
def hitung():
    try:
        modal = float(request.form["modal"])
        risk = float(request.form["risk"])
        posisi = request.form["posisi"]
        leverage = int(request.form["leverage"])
        rr = int(request.form["rr"])
        entry = float(request.form["entry"])
        sl = float(request.form["sl"])

        risk_amount = modal * (risk / 100)
        if posisi == "LONG":
            jarak_sl = entry - sl
            take_profit = entry + (jarak_sl * rr)
        elif posisi == "SHORT":
            jarak_sl = sl - entry
            take_profit = entry - (jarak_sl * rr)
        position_size = round(risk_amount / jarak_sl, 2)
        position_size_leverage = round(position_size * leverage, 2)

        hasil = {
            "risk_amount": risk_amount,
            "take_profit": take_profit,
            "jarak_sl": jarak_sl,
            "position_size": position_size,
            "position_size_leverage": position_size_leverage
        }

        return render_template("index.html", hasil=hasil)
    except:
        return render_template("index.html", error="Input tidak valid!")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)