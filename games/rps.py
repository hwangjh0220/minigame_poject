"""가위바위보 — 담당: 팀원 D

[규칙]
- 컴퓨터와 3판 2선승제로 대결한다.
- 입력: 1(가위) 2(바위) 3(보)

[구현 힌트]
- decide(player: str, computer: str) -> str   # "win" | "lose" | "draw"
"""

import random

GAME_NAME = "가위바위보"

NAMES = {"1": "가위", "2": "바위", "3": "보"}
# 키(내 선택)가 값(상대 선택)을 이긴다
BEATS = {"1": "3", "2": "1", "3": "2"}


def decide(player: str, computer: str) -> str:
    """player 기준 결과를 "win" / "lose" / "draw" 로 반환한다."""
    if player == computer:
        return "draw"
    if BEATS[player] == computer:
        return "win"
    return "lose"


def play() -> None:
    """한 판(3판 2선승)을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    print(f"=== {GAME_NAME} (3판 2선승) ===")
    player_wins = 0
    computer_wins = 0

    while player_wins < 2 and computer_wins < 2:
        choice = input("1(가위) 2(바위) 3(보): ").strip()
        if choice not in NAMES:
            print("1, 2, 3 중에서 입력해 주세요.")
            continue

        computer = random.choice(list(NAMES))
        print(f"나: {NAMES[choice]} / 컴퓨터: {NAMES[computer]}")

        result = decide(choice, computer)
        if result == "win":
            player_wins += 1
            print("이겼습니다!")
        elif result == "lose":
            computer_wins += 1
            print("졌습니다...")
        else:
            print("비겼습니다. 다시!")
        print(f"현재 점수 - 나 {player_wins} : {computer_wins} 컴퓨터")

    if player_wins == 2:
        print("최종 승리!")
    else:
        print("최종 패배...")
