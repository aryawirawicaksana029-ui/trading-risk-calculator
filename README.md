# 📈 Trading Risk Management Calculator

A terminal-based Python application that helps traders calculate risk management before entering a trade.

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

## 📸 Preview

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

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** `datetime` (built-in)
- **Interface:** Terminal / Command Line

---

## ⚙️ How to Use

**1. Clone this repository:**
```bash
git clone https://github.com/aryawirawicaksana029-ui/trading-risk-calculator.git
```

**2. Navigate to the project folder:**
```bash
cd trading-risk-calculator
```

**3. Run the program:**
```bash
python utama.py
```

**4. Follow the input prompts:**
```
- Enter account balance (min $100)
- Enter risk percentage (1% - 100%)
- Choose position: LONG or SHORT
- Enter leverage (1x - 150x)
- Enter Risk Reward Ratio
- Enter entry price
- Enter stop loss price
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
├── utama.py              # Main program
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

## 📌 Future Plans

- [ ] GUI Desktop version (Tkinter)
- [ ] Web App version (Flask)
- [ ] Mobile App version
- [ ] Multi-currency support
- [ ] Trading journal integration
