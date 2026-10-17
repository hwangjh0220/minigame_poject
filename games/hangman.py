import random

GAME_NAME = "행맨"

# 행맨 단계별 아스키 아트 (0번 틀림 ~ 6번 틀림)
HANGMAN_PICS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

# 단어 목록
WORD_LIST = [
    "programming", "algorithm", "computer",
    "developer", "database", "network", "university"
]


def mask_word(word: str, guessed: set[str]) -> str:
    """맞힌 글자만 보여주고, 나머지는 언더스코어(_)로 가립니다."""
    return " ".join([char if char in guessed else "_" for char in word])


def is_solved(word: str, guessed: set[str]) -> bool:
    """단어의 모든 알파벳을 맞혔는지 확인합니다."""
    return set(word).issubset(guessed)


def play() -> None:
    """한 판을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    print(f"\n=== {GAME_NAME} 게임을 시작합니다! ===")

    word = random.choice(WORD_LIST)
    guessed = set()
    wrong_guesses = 0  # 틀린 횟수 (0부터 6까지 증가)
    max_wrong = 6     # 최대 허용 오답 수

    while wrong_guesses < max_wrong:
        # 1. 현재 상태 출력 (그림 + 순수 함수 활용한 단어 마스킹)
        print(HANGMAN_PICS[wrong_guesses])
        print(f"현재 단어: {mask_word(word, guessed)}")
        print(f"남은 기회: {max_wrong - wrong_guesses}번")

        # 2. 사용자 입력
        guess = input("\n알파벳을 하나 추측하세요: ").lower()

        # 입력값 검증
        if len(guess) != 1 or not guess.isalpha():
            print("\n경고: 영문자 알파벳 1개만 입력해주세요.")
            continue

        if guess in guessed:
            print("\n이미 확인해 본 알파벳입니다. 다른 알파벳을 입력하세요.")
            continue

        # 3. 로직 처리
        guessed.add(guess)

        if guess in word:
            print(f"\n[!] 정답입니다! '{guess}' 문자가 포함되어 있습니다.")
            # 승리 조건 확인
            if is_solved(word, guessed):
                print(HANGMAN_PICS[wrong_guesses])  # 최종 상태 출력
                print(f"현재 단어: {mask_word(word, guessed)}")
                print(f"\n★ 축하합니다! 단어 '{word}'를(을) 완벽하게 맞추셨습니다! ★")
                return  # 게임 종료 및 메인 메뉴 복귀
        else:
            print(f"\n[X] 틀렸습니다! '{guess}' 문자는 없습니다.")
            wrong_guesses += 1  # 틀렸을 때만 횟수 증가 -> 다음 루프에서 그림이 변경됨

    # 기회를 모두 소진하여 패배한 경우 (마지막 교수형 그림 출력)
    print(HANGMAN_PICS[wrong_guesses])
    print(f"\n게임 오버... 기회를 모두 잃었습니다. 정답은 '{word}' 였습니다.")
    return


# 단독으로 실행해볼 때 테스트하기 위한 용도 (메인 메뉴 개발 전 테스트용)
if __name__ == "__main__":
    play()
