# 🎮 Tic-Tac-Toe Deluxe

A creative, colorful, and fully functional Tic-Tac-Toe game built in Python — with emoji themes, ANSI terminal colors, witty commentary, and comprehensive unit tests.

---

## 🚀 Quick Start

```bash
# 1. Clone / enter the repo
cd minigame_tictactoe

# 2. Run the game
python main.py

# 3. Run the tests
python -m pytest tests/ -v
# or
python -m unittest discover tests
```

---

## 🌈 Features

| Feature | Detail |
|---|---|
| **4 emoji themes** | Classic ❌/⭕ · Pets 🐶/🐱 · Space 🚀/👾 · Fire & Ice 🔥/❄️ |
| **ANSI colors** | Bold, colored board grid, player symbols, and status messages |
| **Witty commentary** | Random win, draw, and move-reaction quips every round |
| **Replay loop** | Keep playing as many rounds as you like — scores are tracked |
| **Zero dependencies** | Only Python standard library; no `pip install` needed |

---

## 📁 Project Deliverables

| File Path / Component | Description & Creative Features | Status / Tests Passed |
|---|---|---|
| `games/tictactoe.py` | Core game engine: `TicTacToe` class with board init, move validation (`is_valid_move`, `make_move`), win/draw detection, 4 emoji themes (`classic`, `pets`, `space`, `fire`), ANSI color helpers (`Color`), randomised witty commentary pools, interactive `play_round()` loop, and `run()` replay session manager | ✅ Implemented |
| `tests/test_tictactoe.py` | 38 unit tests via `unittest`: board initialisation (6), valid/invalid moves (10), horizontal wins (6), vertical wins (5), diagonal wins (4), draw conditions (5), theme loading (5), score tracking (3), WIN_COMBOS constant (3) | ✅ 38/38 Tests Pass |
| `main.py` | Collection entry point — **line 4** is the active, uncommented import that calls `from games.tictactoe import launch; launch()`. Lines 5–6 are placeholder stubs for future games | ✅ Implemented |
| `README.md` | Project documentation: quick-start, feature table, deliverables table, Git commands, and project layout | ✅ Implemented |
| `games/__init__.py` | Package marker for `games/` | ✅ Implemented |
| `tests/__init__.py` | Package marker for `tests/` | ✅ Implemented |

---

## 🗂️ Project Layout

```
minigame_tictactoe/
├── main.py                   # Entry point (line 4 active)
├── README.md
├── games/
│   ├── __init__.py
│   └── tictactoe.py          # Game engine + themes + UI
└── tests/
    ├── __init__.py
    └── test_tictactoe.py     # 38 unit tests
```

---

## 🔧 Git Setup Commands

```bash
# Initialise the repo (if not already done)
git init

# Stage all files
git add .

# Initial commit on main
git commit -m "Initial project scaffold"

# Create and switch to the feature branch
git checkout -b features/tictactoe

# Verify you are on the correct branch
git branch
```

---

## 🎨 Theme Preview

```
  Theme 1 — Classic     Theme 2 — Pets      Theme 3 — Space     Theme 4 — Fire & Ice
  ❌ | ⭕ | ❌          🐶 | 🐱 | 🐶       🚀 | 👾 | 🚀        🔥 | ❄️  | 🔥
  ---+---+---           ---+---+---          ---+---+---           ---+---+---
  ⭕ | ❌ | ⭕          🐱 | 🐶 | 🐱       👾 | 🚀 | 👾        ❄️  | 🔥 | ❄️
  ---+---+---           ---+---+---          ---+---+---           ---+---+---
  ❌ | ⭕ | ❌          🐶 | 🐱 | 🐶       🚀 | 👾 | 🚀        🔥 | ❄️  | 🔥
```

---

## 🧪 Running Tests

```bash
# Verbose output with unittest
python -m unittest tests.test_tictactoe -v

# Or with pytest (if installed)
pytest tests/ -v --tb=short
```

Expected output: **38 tests, 0 failures, 0 errors**.

