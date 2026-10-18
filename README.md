# 🎮 Game Hub

콘솔에서 즐기는 미니 게임 모음입니다. (GitHub 협업 실습 프로젝트)

## 실행 방법

```bash
python -m venv venv
# Windows: venv\Scripts\activate    /  macOS·Linux: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## 팀원 소개

> **[충돌 지점 ③]** 자기 이름 줄을 채워 주세요. (모두 같은 표를 고치므로 충돌이 납니다!)

| 역할 | 이름  | GitHub ID | 담당 |
|---|---|---|---|
| A | 황정호 | hwangjh0220 | 팀장 · `main.py`, `utils.py`, README, 병합 관리 |
| B | 고세진 | kos070721-eng  | `games/hangman.py` (행맨) |
| C | --- | --- | `games/baseball.py` (숫자 야구) |
| D | 양소제 | yangsoje | `games/rps.py` (가위바위보) |
| E | 싱 프라쉬나 | prashnaraa-byte | `games/tictactoe.py` (틱택토) |

## 게임 목록

| 게임 | 이름 | 상태 |
|---|---|---|
| 행맨 | 고세진 | 완료 |
| 숫자 야구 | --- | 🚧 |
| 가위바위보 | 컴퓨터와 3판 2선승제 대결 | 완료 |
| 틱택토 | 싱프라쉬나 | 완료 |

# 🎮 Tic-Tac-Toe Deluxe

A creative, colorful, and fully functional Tic-Tac-Toe game built in Python — with emoji themes, ANSI terminal colors, witty commentary, and comprehensive unit tests.


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

## 🔤 행맨

무작위로 선택된 단어를 알파벳 한 글자씩 추측하는 콘솔 게임입니다. 맞힌 글자는 공개되고, 틀릴 때마다 행맨 그림이 한 단계씩 완성됩니다. 오답 6회에 도달하기 전에 모든 글자를 맞히면 승리합니다.

### 주요 기능

| 기능 | 설명 |
|---|---|
| 무작위 단어 선택 | 프로그래밍·컴퓨터·대학 관련 영단어 7개 중 하나를 선택 |
| 단계별 ASCII 아트 | 오답 0회부터 6회까지 총 7개의 그림으로 진행 상황 표시 |
| 단어 마스킹 | 아직 맞히지 못한 글자는 `_`로 가리고 맞힌 글자는 해당 위치에 모두 표시 |
| 남은 기회 안내 | 오답 횟수에 따라 남은 기회를 표시 |
| 중복 추측 방지 | 이미 입력한 글자는 안내 후 다시 입력받으며 기회를 차감하지 않음 |
| 입력 검증 | 한 글자가 아니거나 `isalpha()`를 만족하지 않으면 다시 입력 |
| 대소문자 처리 | 입력을 소문자로 변환하여 비교 |
| 승패 판정 | 모든 글자를 맞히면 승리, 오답 6회면 패배 및 정답 공개 |
| 허브 연동 | 게임 종료 후 호출한 허브 메뉴로 복귀 |

### 플레이 방법

1. 프로젝트 최상위 폴더에서 `python main.py`를 실행합니다.
2. 허브 메뉴에서 `1`번을 선택합니다.
3. 그림, 현재 단어, 남은 기회를 확인합니다.
4. 영문 알파벳 한 글자를 입력하여 단어를 추측합니다.
5. 단어를 완성하거나 오답 기회를 모두 사용하면 게임이 종료됩니다.

정답 글자, 중복 입력, 형식에 맞지 않는 입력은 오답 횟수를 증가시키지 않습니다.

### 단어 목록

`programming`, `algorithm`, `computer`, `developer`, `database`, `network`, `university`

### 화면 구성 예시

아래는 정답이 `computer`이고 `c`, `o`를 맞힌 상태를 가정한 예시입니다. 실제 단어는 무작위로 선택됩니다.

```text
  +---+
  |   |
      |
      |
      |
      |
=========

현재 단어: c o _ _ _ _ _ _
남은 기회: 6번

알파벳을 하나 추측하세요:
```

### 주요 코드 구성

| 항목 | 역할 |
|---|---|
| `GAME_NAME` | 허브 메뉴에 표시할 게임 이름 |
| `HANGMAN_PICS` | 오답 횟수별 ASCII 아트 저장 |
| `WORD_LIST` | 무작위 선택 대상 단어 목록 |
| `mask_word(word, guessed)` | 맞힌 글자와 숨겨진 글자를 조합하여 표시 문자열 생성 |
| `is_solved(word, guessed)` | 단어에 필요한 모든 글자를 추측했는지 판정 |
| `play()` | 단어 선택, 입력 검증, 상태 출력 및 승패 처리 |

### 관련 파일 및 테스트

- 구현: `games/hangman.py`
- 테스트: `tests/test_hangman.py`

```bash
python -m pytest tests/test_hangman.py -v
```

### 현재 구현의 참고 사항

- 게임 내부의 재경기 질문은 없으며, 다시 하려면 허브에서 행맨을 재선택합니다.
- 입력 검증에 사용하는 `isalpha()`는 영문자 외의 문자도 허용합니다. 화면 안내와 달리 영문자만 엄격하게 제한하는 구현은 아닙니다.
- 입력 양끝의 공백을 제거하지 않으므로 ` a `처럼 입력하면 형식 오류로 처리됩니다.

---

## ✊ 가위바위보

컴퓨터와 가위바위보로 먼저 2승을 달성하는 쪽이 이기는 콘솔 게임입니다. 각 대결에서 컴퓨터는 가위·바위·보 중 하나를 무작위로 선택하며, 사용자는 숫자로 자신의 선택을 입력합니다.

### 주요 기능

| 기능 | 설명 |
|---|---|
| 숫자 기반 선택 | `1`은 가위, `2`는 바위, `3`은 보 |
| 컴퓨터 무작위 선택 | 유효한 사용자 입력 후 컴퓨터의 선택을 무작위로 결정 |
| 승패 판정 함수 | `decide()`에서 사용자 기준 승리·패배·무승부 판정 |
| 2선승제 | 사용자 또는 컴퓨터가 먼저 2승을 달성하면 종료 |
| 무승부 재대결 | 무승부는 양쪽 승수를 올리지 않고 계속 진행 |
| 입력 검증 | `1`, `2`, `3` 이외의 입력에는 안내 후 다시 입력받음 |
| 공백 처리 | 입력 양끝의 공백 제거 |
| 점수 표시 | 각 유효한 대결 후 사용자와 컴퓨터의 누적 승수 출력 |
| 허브 연동 | 최종 결과 출력 후 호출한 허브 메뉴로 복귀 |

### 플레이 방법

1. 프로젝트 최상위 폴더에서 `python main.py`를 실행합니다.
2. 허브 메뉴에서 `3`번을 선택합니다.
3. `1`(가위), `2`(바위), `3`(보) 중 하나를 입력합니다.
4. 컴퓨터의 선택, 대결 결과, 현재 점수를 확인합니다.
5. 어느 한쪽이 2승에 도달할 때까지 진행합니다.

게임에서는 ‘3판 2선승’으로 안내하지만, 무승부는 승수에 포함하지 않으므로 실제 선택 횟수는 3회를 넘을 수 있습니다.

### 승패 규칙

| 사용자 선택 | 컴퓨터 선택 | 사용자 기준 결과 |
|---|---|---|
| 가위 | 보 | 승리 |
| 바위 | 가위 | 승리 |
| 보 | 바위 | 승리 |
| 같은 선택 | 같은 선택 | 무승부 |
| 위 승리 조건의 반대 조합 | | 패배 |

### 화면 구성 예시

아래는 사용자가 가위를, 컴퓨터가 보를 선택한 첫 대결의 예시입니다. 실제 컴퓨터 선택은 무작위입니다.

```text
=== 가위바위보 (3판 2선승) ===
1(가위) 2(바위) 3(보): 1
나: 가위 / 컴퓨터: 보
이겼습니다!
현재 점수 - 나 1 : 0 컴퓨터
```

### 주요 코드 구성

| 항목 | 역할 |
|---|---|
| `GAME_NAME` | 허브 메뉴에 표시할 게임 이름 |
| `NAMES` | 입력 번호를 가위·바위·보 이름과 연결 |
| `BEATS` | 각 선택이 이기는 상대 선택을 정의 |
| `decide(player, computer)` | 유효한 선택을 받아 `win`, `lose`, `draw` 중 하나를 반환 |
| `play()` | 사용자 입력, 컴퓨터 선택, 점수 갱신 및 최종 승패 처리 |

### 관련 파일 및 테스트

- 구현: `games/rps.py`
- 테스트: `tests/test_rps.py`

```bash
python -m pytest tests/test_rps.py -v
```

### 현재 구현의 참고 사항

- 점수는 한 경기 안에서만 유지되며, 허브에서 새로 실행하면 초기화됩니다.
- `decide()`는 유효한 번호를 전달받는 것을 전제로 하며, 사용자 입력 검증은 `play()`에서 수행합니다.
- 재경기는 허브에서 가위바위보를 다시 선택하여 시작합니다.


## 협업 규칙

- `main` 브랜치에는 **직접 push 하지 않습니다.** 반드시 Pull Request!
- 브랜치 이름: `feature/<게임이름>` (예: `feature/hangman`)
- 커밋 메시지: `feat:` `fix:` `test:` `docs:` `chore:` 로 시작 (예: `feat: 행맨 글자 마스킹 함수 추가`)
- PR은 **다른 팀원 1명 이상의 승인** 후 병합합니다.
- 비밀번호·토큰·`.env`는 절대 커밋하지 않습니다.

