# Checkers AI

This project implements a playable version of **Checkers** with an AI opponent using **Minimax** and **Alpha-Beta Pruning**.

The goal is to model the game as an adversarial search problem and compare the performance of different decision-making algorithms.

---


## Folder Structure

```
Checkers/
├── ai/
│   ├── __init__.py
│   └── algorithm.py
├── checkers/
│   ├── board.py
│   ├── constants.py
│   ├── game.py
│   └── piece.py
├── main.py
├── run.sh
├── README.md
└── __init__.py
```

---

## Cloning the Repository

```bash
git clone https://github.com/suprajski/Checkers.git
cd Checkers
```

---

## Installing Python Environment

### Option 1 — micromamba / conda (recommended)

```bash
micromamba create -n checkers python=3.11 -y
micromamba activate checkers
pip install pygame
```

or:

```bash
conda create -n checkers python=3.11 -y
conda activate checkers
pip install pygame
```

---

### Option 2 — venv (Linux/macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pygame
```

---

### Option 3 — venv (Windows PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install pygame
```

---

## Running the Program

### Standard run

```bash
python main.py
```

If that does not work:

```bash
python3 main.py
```

On Windows:

```powershell
py main.py
```

---

### Run with algorithm selection (Linux/macOS)

Make the script executable (only once):

```bash
chmod +x run.sh
```

Run:

```bash
./run.sh
```

Then choose:

- 1 → Minimax  
- 2 → Alpha-Beta  

---

### Running without run.sh (all platforms)

```bash
python main.py minimax
python main.py alphabeta
```

---

## AI Algorithms

### Minimax
- Explores the game tree assuming optimal play  
- White is maximizing, Red is minimizing  

### Alpha-Beta Pruning
- Optimized version of minimax  
- Prunes unnecessary branches  
- Allows deeper search with better performance  

---

## Development

To run the project:

```bash
python main.py
```

You can modify:
- `ai/algorithm.py` → AI logic  
- `checkers/board.py` → game rules  
- `checkers/game.py` → game flow  

---

## Known Limitations

- Mandatory captures are not globally enforced  
- The game does not detect "no legal moves" as a terminal condition  
- Draw conditions are not implemented  
- The evaluation function is based only on piece count and kings  
