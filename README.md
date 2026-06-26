# 📈 Trading Risk Management Calculator

A full-stack Python application that helps traders calculate risk management before entering a trade. Available in **3 versions**: Terminal, Desktop GUI, and Web App.

---

## 🚀 Features

- ✅ LONG & SHORT position support
- ✅ Risk amount calculation based on account balance
- ✅ Stop Loss & Take Profit calculation
- ✅ Leverage support (1x - 150x)
- ✅ Risk Reward Ratio calculation
- ✅ Position size calculation (with & without leverage)
- ✅ Save trading history to `.txt` file
- ✅ Input validation with error handling
- ✅ Calculate multiple trades without restarting

---

## 📦 3 Versions Available

| Version | File | How to Run |
|---------|------|------------|
| 🖥️ Terminal | `utama.py` | `python utama.py` |
| 🪟 Desktop GUI | `gui.py` | `python gui.py` |
| 🌐 Web App | `app.py` | `python app.py` |

---

## 📸 Preview

### 🖥️ Terminal Version
```
╔═════════════════════════════════════╗
║     RISK MANAGEMENT CALCULATOR      ║
╠═════════════════════════════════════╣
║  Posisi       : LONG                ║
║  Modal        : $1000.0             ║
║  Risk %       : 2.0%                ║
║  Entry        : 50000.0             ║
║  Stop Loss    : 48000.0             ║
║  Take Profit  : 54000.0             ║
║  RR Ratio     : 1:2                 ║
╠═════════════════════════════════════╣
║  Risk Amount  : $20.0               ║
║  Jarak SL     : 2000.0              ║
║  Leverage     : 10x                 ║
║  Size Tanpa LV: 0.01                ║
║  Size + LV    : 0.1                 ║
╚═════════════════════════════════════╝
```

### 🪟 Desktop GUI Version
- Dark theme desktop application
- Built with Tkinter
- Real-time calculation with button click
- Save results to history file

### 🌐 Web App Version
- Dark theme web interface
- Built with Flask
- Accessible via browser at `http://localhost:5000`

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.x |
| Desktop GUI | Tkinter |
| Web Framework | Flask |
| Frontend | HTML, CSS |
| Libraries | `datetime`, `tkinter`, `flask` |

---

## ⚙️ How to Use

**1. Clone this repository:**
```bash
git clone https://github.com/aryawirawicaksana029-ui/trading-risk-calculator.git
cd trading-risk-calculator
```

**2. Install dependencies (for Web version):**
```bash
pip install flask
```

**3. Run your preferred version:**

```bash
# Terminal version
python utama.py

# Desktop GUI version
python gui.py

# Web App version
python app.py
# Then open http://localhost:5000 in your browser
```

---

## 📊 Calculation Formula

| Formula | Description |
|--------|-------------|
| `Risk Amount = Balance × (Risk% / 100)` | Dollar amount at risk |
| `SL Distance = Entry - Stop Loss` (LONG) | Price distance to SL |
| `SL Distance = Stop Loss - Entry` (SHORT) | Price distance to SL |
| `Position Size = Risk Amount / SL Distance` | Size without leverage |
| `Position Size (Lev) = Position Size × Leverage` | Size with leverage |
| `TP = Entry + (SL Distance × RR)` (LONG) | Take profit price |
| `TP = Entry - (SL Distance × RR)` (SHORT) | Take profit price |

---

## 📁 Project Structure

```
trading-risk-calculator/
│
├── utama.py              # Terminal version
├── gui.py                # Desktop GUI version (Tkinter)
├── app.py                # Web App version (Flask)
│
├── templates/
│   └── index.html        # Web interface
│
├── history_trading.txt   # Auto-generated trade history
└── README.md             # Project documentation
```

---

## 👨‍💻 Author

**Arya Wira Wicaksana**
🐍 Python Developer | AI Enthusiast
📧 aryawirawicaksana029@gmail.com
🔗 [GitHub](https://github.com/aryawirawicaksana029-ui)

---

## 📌 Changelog

- `v1.0` - Terminal version with full input validation
- `v2.0` - Added LONG/SHORT, Leverage, Risk Reward Ratio
- `v3.0` - Added save history & loop calculation
- `v4.0` - Desktop GUI with Tkinter dark theme
- `v5.0` - Web App with Flask

---

## 🔮 Future Plans

- [ ] Deploy web app to cloud (Railway/Render)
- [ ] Multi-currency support
- [ ] Trading journal integration
- [ ] User authentication
- [ ] Chart visualization
