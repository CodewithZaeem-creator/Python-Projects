# 🔳 QR Code Generator

A command-line QR code generator built in Python. Type any link or text, customise the colours and size, and it instantly generates and opens a QR code image on your screen.

> My fifth Python project — learning libraries, f-strings, and building a real useful tool. 🐍

---

## 🎮 Demo

```
================================
       🔳 QR Code Generator
================================

What do you want to do?
1 - Generate a QR code
2 - Quit

Enter your choice: 1
Enter the link or text: https://github.com/CodewithZaeem-creator
Save as (e.g. myqr): mygithub

Choose a colour (or press Enter to skip):
QR code colour (e.g. black, darkblue, red): darkblue
Background colour (e.g. white, yellow): white
QR code size 1-20 (or press Enter for default 10): 12

✅ QR code saved as mygithub.png!
```

---

## ✨ Features

- 🔗 Generate a QR code from any link or text
- 🎨 Custom QR code and background colours
- 📐 Custom size — choose how big the image should be
- 💾 Save with a custom filename of your choice
- 🖼️ Automatically opens the image after saving
- 🔁 Generate multiple QR codes without restarting
- ⚠️ Handles empty inputs with friendly error messages
- 🪶 Only one external library needed — `qrcode`

---

## 🚀 Getting Started

### 1. Make sure Python is installed

```bash
python --version
```

Download from [python.org](https://www.python.org/downloads/) if needed.

### 2. Clone the repository

```bash
git clone https://github.com/CodewithZaeem-creator/Python-Projects.git
cd Python-Projects/qr-code-generator
```

### 3. Install the required library

```bash
pip install qrcode[pil]
```

### 4. Run the app

```bash
python qrcode_generator.py
```

---

## 📦 Requirements

| Requirement | Notes |
|---|---|
| Python 3.9+ | Download from [python.org](https://www.python.org) |
| `qrcode[pil]` | Install via pip |
| `os` | Built-in — nothing to install |

---

## 🧠 How It Works

```
You enter a link or text
          ↓
You choose filename, colour, and size
          ↓
qrcode library converts it into a QR pattern
          ↓
make_image() applies your custom colours
          ↓
Saved as filename.png in your project folder
          ↓
os.startfile() opens it automatically 🖼️
```

---

## 📁 Project Structure

```
qr-code-generator/
│
├── qrcode_generator.py   # All the app logic
├── README.md             # This file
└── *.png                 # Your generated QR codes appear here
```

---

## 🎨 Colour Ideas to Try

| Fill Colour | Background | Result |
|---|---|---|
| `black` | `white` | Classic — scans perfectly |
| `darkblue` | `white` | Professional look |
| `darkgreen` | `white` | Fresh style |
| `red` | `white` | Bold and striking |
| `white` | `black` | Inverted classic |

> ⚠️ Always keep strong contrast between fill and background or the QR code won't scan!

---

## 🐛 Bugs I Fixed Along the Way

- **`input()` returns a string** — comparing it to the number `1` or `2` instead of `"1"` or `"2"` meant the menu never worked
- **`.strip` without `()`** — referencing the function instead of calling it meant links weren't being cleaned properly
- **Broken f-string** — wrote `"f{filename}.png"` instead of `f"{filename}.png"` so the filename was never inserted
- **`qr.make(True)` vs `qr.make(fit=True)`** — learned that named arguments matter in Python functions

---

## 💡 Ideas for What to Add Next

- 🖥️ **Tkinter GUI** — buttons, colour pickers, and a live preview of the QR code
- 📋 **Scan history** — save a log of all generated QR codes to a text file
- 🌐 **URL shortener** — shorten the link before turning it into a QR code
- 📱 **Batch generator** — read a list of links from a file and generate them all at once

---

## 🌱 What I Learned

- How to use the `qrcode` library to generate real QR code images
- How f-strings work — putting variables directly inside strings with `{}`
- How `os.startfile()` opens files automatically from Python
- Why `input()` always returns a string and how that affects comparisons
- How to build a menu-driven CLI app with a `while True` loop

---

## 📄 License

MIT License — free to use, modify, and share.

---

*Made with ❤️ as part of my Python learning journey. Try scanning the QR codes it generates! If you liked it, leave a ⭐ on GitHub!*
