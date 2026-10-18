"""
games/tictactoe.py
==================
A creative, colorful, and fully functional Tic-Tac-Toe game.

Features:
- Customizable themes / emoji symbol pairs
- ANSI terminal colors (no external dependencies required)
- Witty, dynamic commentary for wins, draws, and gameplay moments
- Move validation, win / draw detection, and replay loop
"""

import random
import time

GAME_NAME = "틱택토"

# ---------------------------------------------------------------------------
# ANSI Color Helpers
# ---------------------------------------------------------------------------


class Color:
    """Lightweight ANSI color codes — no third-party library needed."""

    RESET = "\033[0m"
    BOLD = "\033[1m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

    BG_DARK = "\033[40m"

    @staticmethod
    def paint(text: str, *codes: str) -> str:
        """Wrap *text* in one or more ANSI codes and reset at the end."""
        return "".join(codes) + text + Color.RESET


# ---------------------------------------------------------------------------
# Theme Definitions
# ---------------------------------------------------------------------------

THEMES: dict[str, dict] = {
    "classic": {
        "name": "Classic ❌ vs ⭕",
        "p1_symbol": "❌",
        "p2_symbol": "⭕",
        "p1_color": Color.RED,
        "p2_color": Color.BLUE,
        "board_color": Color.CYAN,
    },
    "pets": {
        "name": "Pets 🐶 vs 🐱",
        "p1_symbol": "🐶",
        "p2_symbol": "🐱",
        "p1_color": Color.YELLOW,
        "p2_color": Color.MAGENTA,
        "board_color": Color.GREEN,
    },
    "space": {
        "name": "Space 🚀 vs 👾",
        "p1_symbol": "🚀",
        "p2_symbol": "👾",
        "p1_color": Color.CYAN,
        "p2_color": Color.MAGENTA,
        "board_color": Color.BLUE,
    },
    "fire": {
        "name": "Fire & Ice 🔥 vs ❄️",
        "p1_symbol": "🔥",
        "p2_symbol": "❄️ ",
        "p1_color": Color.RED,
        "p2_color": Color.CYAN,
        "board_color": Color.YELLOW,
    },
}

# ---------------------------------------------------------------------------
# Witty commentary pools
# ---------------------------------------------------------------------------

_WIN_QUIPS = [
    "🎉 Absolutely DEMOLISHED! The crowd goes wild!",
    "🏆 Victory tastes sweet — especially against THIS opponent!",
    "👑 All hail the reigning Tic-Tac-Toe champion!",
    "🌟 Brilliant play! Shakespeare himself would slow-clap.",
    "🎸 LEGENDARY. Pure tic-tac-toe poetry.",
    "🔥 That was FIRE. Your opponent might need a therapist.",
]

_DRAW_QUIPS = [
    "🤝 A draw! Two geniuses cancel each other out perfectly.",
    "😅 Nobody wins... nobody loses. The perfect diplomatic outcome.",
    "🌀 It's a tie! The universe maintains its balance.",
    "🎭 A classic stalemate — Shakespeare called it 'Much Ado About Nothing'.",
    "🤯 Both players are TOO equally matched. Suspicious.",
]

_TAUNT_QUIPS = [
    "🤔 Bold move, cotton. Let's see if it pays off...",
    "👀 Interesting choice. Very... *interesting*.",
    "😏 Oh? Planning something sneaky, are we?",
    "🧠 The big brain plays. The crowd whispers.",
    "⚡ Fast and decisive! No regrets... right?",
]


def _random_quip(pool: list[str]) -> str:
    return random.choice(pool)


# ---------------------------------------------------------------------------
# Core TicTacToe Class
# ---------------------------------------------------------------------------


class TicTacToe:
    """
    Core Tic-Tac-Toe game engine.

    Attributes
    ----------
    board : list[str]
        9-element list representing the 3×3 grid.
        Empty cells hold their 1-based position string ("1"–"9").
    theme : dict
        Active theme configuration dictionary.
    scores : dict
        Cumulative wins per player and draws across a session.
    """

    # Win condition index triplets (0-based)
    WIN_COMBOS: list[tuple[int, int, int]] = [
        (0, 1, 2),  # top row
        (3, 4, 5),  # middle row
        (6, 7, 8),  # bottom row
        (0, 3, 6),  # left column
        (1, 4, 7),  # middle column
        (2, 5, 8),  # right column
        (0, 4, 8),  # diagonal ↘
        (2, 4, 6),  # diagonal ↙
    ]

    def __init__(self, theme_key: str = "classic") -> None:
        """
        Initialise the game with a chosen theme.

        Parameters
        ----------
        theme_key : str
            Key into the THEMES dictionary. Defaults to ``"classic"``.
        """
        self.theme: dict = THEMES.get(theme_key, THEMES["classic"])
        self.board: list[str] = [str(i) for i in range(1, 10)]
        self.scores: dict[str, int] = {"Player 1": 0, "Player 2": 0, "Draws": 0}
        self._current_player: int = 1  # 1 or 2

    # ------------------------------------------------------------------
    # Board Helpers
    # ------------------------------------------------------------------

    def reset_board(self) -> None:
        """Reset the board to its initial empty state."""
        self.board = [str(i) for i in range(1, 10)]

    def _symbol(self, player: int) -> str:
        """Return the emoji symbol for *player* (1 or 2)."""
        return self.theme["p1_symbol"] if player == 1 else self.theme["p2_symbol"]

    def _color(self, player: int) -> str:
        """Return the ANSI color code for *player* (1 or 2)."""
        return self.theme["p1_color"] if player == 1 else self.theme["p2_color"]

    def _cell_display(self, cell: str) -> str:
        """Return a display string for a single board cell."""
        bc = self.theme["board_color"]
        if cell == self.theme["p1_symbol"]:
            return Color.paint(cell, self._color(1), Color.BOLD)
        if cell == self.theme["p2_symbol"]:
            return Color.paint(cell, self._color(2), Color.BOLD)
        # Empty cell — show position number in muted board color
        return Color.paint(f" {cell} ", bc)

    def display_board(self) -> None:
        """Print the current board to stdout with colors and grid lines."""
        bc = self.theme["board_color"]
        sep = Color.paint("---+---+---", bc)
        rows = []
        for row_start in (0, 3, 6):
            cells = [self._cell_display(self.board[row_start + c]) for c in range(3)]
            rows.append(" | ".join(cells))
        print()
        print(f"  {rows[0]}")
        print(f"  {sep}")
        print(f"  {rows[1]}")
        print(f"  {sep}")
        print(f"  {rows[2]}")
        print()

    def display_scoreboard(self) -> None:
        """Print the running scoreboard."""
        header = Color.paint(" 🏅  SCOREBOARD  🏅 ", Color.BOLD, Color.YELLOW)
        print(f"\n  {header}")
        for label, val in self.scores.items():
            color = (
                Color.RED
                if "1" in label
                else Color.BLUE if "2" in label else Color.WHITE
            )
            print(Color.paint(f"  {label:>10}: {val}", color))
        print()

    # ------------------------------------------------------------------
    # Game Logic
    # ------------------------------------------------------------------

    def is_valid_move(self, position: int) -> bool:
        """
        Check whether *position* is a legal move.

        Parameters
        ----------
        position : int
            1-based cell index (1–9).

        Returns
        -------
        bool
            True when the cell is in range and not yet claimed.
        """
        if not (1 <= position <= 9):
            return False
        return self.board[position - 1] not in (
            self.theme["p1_symbol"],
            self.theme["p2_symbol"],
        )

    def make_move(self, position: int, player: int) -> bool:
        """
        Place *player*'s symbol on *position* if valid.

        Parameters
        ----------
        position : int
            1-based cell index (1–9).
        player : int
            Active player (1 or 2).

        Returns
        -------
        bool
            True when the move was placed successfully.
        """
        if not self.is_valid_move(position):
            return False
        self.board[position - 1] = self._symbol(player)
        return True

    def check_winner(self) -> int | None:
        """
        Determine whether there is a winner.

        Returns
        -------
        int or None
            1 or 2 if that player has won, else None.
        """
        for combo in self.WIN_COMBOS:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] in (
                self.theme["p1_symbol"],
                self.theme["p2_symbol"],
            ):
                return 1 if self.board[a] == self.theme["p1_symbol"] else 2
        return None

    def check_draw(self) -> bool:
        """
        Determine whether the board is full with no winner.

        Returns
        -------
        bool
            True when all 9 cells are claimed and there is no winner.
        """
        all_claimed = all(
            cell in (self.theme["p1_symbol"], self.theme["p2_symbol"])
            for cell in self.board
        )
        return all_claimed and self.check_winner() is None

    # ------------------------------------------------------------------
    # Interactive Play
    # ------------------------------------------------------------------

    def _prompt_theme() -> str:  # noqa: N805  (static-like helper called before init)
        """Display theme menu and return the chosen theme key."""
        print(Color.paint("\n🎨  Choose your battle theme!", Color.BOLD, Color.YELLOW))
        keys = list(THEMES.keys())
        for i, key in enumerate(keys, 1):
            print(f"  {Color.paint(str(i), Color.CYAN)}. {THEMES[key]['name']}")
        while True:
            raw = input(Color.paint("  Enter choice (1–4): ", Color.WHITE)).strip()
            if raw.isdigit() and 1 <= int(raw) <= len(keys):
                return keys[int(raw) - 1]
            print(Color.paint("  ⚠️  Invalid choice, try again.", Color.RED))

    def _get_move(self, player: int) -> int:
        """Prompt the active player for a valid move and return it."""
        symbol = Color.paint(self._symbol(player), self._color(player), Color.BOLD)
        name = Color.paint(f"Player {player}", self._color(player), Color.BOLD)
        while True:
            raw = input(f"  {name} {symbol}  → Enter cell (1-9): ").strip()
            if raw.isdigit():
                pos = int(raw)
                if self.is_valid_move(pos):
                    print(Color.paint(f"  {_random_quip(_TAUNT_QUIPS)}", Color.YELLOW))
                    time.sleep(0.4)
                    return pos
                else:
                    print(
                        Color.paint(
                            "  ❌ That cell is taken or out of range!", Color.RED
                        )
                    )
            else:
                print(Color.paint("  ❌ Numbers only, please!", Color.RED))

    def play_round(self) -> None:
        """Play a single round of Tic-Tac-Toe interactively."""
        self.reset_board()
        self._current_player = 1

        print(
            Color.paint(
                f"\n  🎮  Theme: {self.theme['name']}", Color.BOLD, Color.MAGENTA
            )
        )
        print(
            Color.paint(
                "  Cells are numbered 1-9 (left→right, top→bottom).", Color.WHITE
            )
        )

        while True:
            self.display_board()
            pos = self._get_move(self._current_player)
            self.make_move(pos, self._current_player)

            winner = self.check_winner()
            if winner is not None:
                self.display_board()
                name = Color.paint(f"Player {winner}", self._color(winner), Color.BOLD)
                sym = Color.paint(self._symbol(winner), self._color(winner), Color.BOLD)
                print(
                    Color.paint(f"\n  🎊  {name} {sym} WINS! ", Color.GREEN, Color.BOLD)
                )
                print(Color.paint(f"  {_random_quip(_WIN_QUIPS)}", Color.YELLOW))
                self.scores[f"Player {winner}"] += 1
                break

            if self.check_draw():
                self.display_board()
                print(Color.paint("\n  🤝  It's a DRAW!", Color.YELLOW, Color.BOLD))
                print(Color.paint(f"  {_random_quip(_DRAW_QUIPS)}", Color.WHITE))
                self.scores["Draws"] += 1
                break

            # Switch player
            self._current_player = 2 if self._current_player == 1 else 1

    def run(self) -> None:
        """
        Entry point: display intro, run game loop with replay option.

        Keeps running until the player declines a rematch.
        """
        # Banner
        banner = Color.paint(
            "\n╔══════════════════════════════╗\n"
            "║   🎮  TIC-TAC-TOE  DELUXE   ║\n"
            "╚══════════════════════════════╝",
            Color.BOLD,
            Color.CYAN,
        )
        print(banner)

        # Theme selection
        theme_key = TicTacToe._prompt_theme()
        self.theme = THEMES[theme_key]

        while True:
            self.play_round()
            self.display_scoreboard()

            again = (
                input(Color.paint("  🔄  Play again? (y/n): ", Color.CYAN))
                .strip()
                .lower()
            )
            if again not in ("y", "yes"):
                print(
                    Color.paint(
                        "\n  👋  Thanks for playing! May your Xs and Os forever align.\n",
                        Color.BOLD,
                        Color.GREEN,
                    )
                )
                break


# ---------------------------------------------------------------------------
# Module-level convenience launcher
# ---------------------------------------------------------------------------


def launch() -> None:
    """Create a TicTacToe instance and start the interactive session."""
    game = TicTacToe()
    game.run()


def play() -> None:
    """게임 허브에서 틱택토를 실행한다."""
    launch()


if __name__ == "__main__":
    launch()
