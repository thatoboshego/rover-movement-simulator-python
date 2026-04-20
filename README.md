# 🚀 Rover Movement Simulator (Python)

## 📌 Description

This project is a Python-based rover movement simulator that reads navigation commands from a file and updates a rover’s position and direction in real time.

The program processes movement and rotation instructions, tracks the rover’s coordinates, and outputs step-by-step updates of its state.

---

## ⚙️ Features

* File-based command input system
* Supports movement forward and backward
* Supports rotation (clockwise and counterclockwise)
* Real-time position tracking (X, Y coordinates)
* Direction tracking in degrees (0–360°)
* Instruction validation and error handling
* Step-by-step simulation output

---

## 🧠 How It Works

The rover starts at:

* Position: (0, 0)
* Direction: 0°

It processes commands from a file such as:

* `move 10 forward`
* `turn 90 clockwise`

Each instruction updates:

* Position using trigonometry
* Direction using modular arithmetic (0–360°)

---

## 📥 Input Format

Each line in the input file must follow:

```text
move <distance> forward
move <distance> backward
turn <angle> clockwise
turn <angle> counterclockwise
```

Example:

```text
move 10 forward
turn 90 clockwise
move 5 forward
```

---

## 🧮 Logic Overview

* Movement uses sine and cosine to calculate directional movement
* Direction is stored in degrees and normalized using modulo 360
* Invalid instructions cause the program to safely abort with an error message

---

## 🛠️ Technologies Used

* Python
* math module
* sys module
* file I/O
* trigonometry (sin, cos)

---

## ▶️ How to Run

### Requirements

* Python 3.x

### Run the program

```bash id="r8k3aa"
python rover.py instructions.txt
```

---

## 📊 Example Output

* Rover position updates after each instruction
* Direction changes tracked in degrees
* Step-by-step movement logs printed to console

---

## 🚧 Known Limitations

* No obstacle detection
* No graphical visualization
* Requires correctly formatted input file
* Basic error handling (terminates on invalid instruction)

---

## 🚀 Future Improvements

* Add grid visualization
* Add obstacle avoidance
* Add GUI or map rendering
* Support more complex commands (e.g. loops, speed)
* Convert into object-oriented design

---

## 👤 Author

Thato Boshego

---

## 📄 License

This project is licensed under the MIT License.
