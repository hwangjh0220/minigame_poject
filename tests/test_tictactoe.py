"""
tests/test_tictactoe.py
=======================
Comprehensive unit tests for the TicTacToe game engine.

Covers:
- Board initialisation
- Valid and invalid move detection
- Win detection (horizontal, vertical, diagonal)
- Draw detection
- Score tracking
- Symbol and color helpers
- Theme switching
"""

import sys
import os
import unittest

# Allow imports from the project root regardless of how tests are run
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from games.tictactoe import TicTacToe, THEMES


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _fill_board(game: TicTacToe, moves: list[tuple[int, int]]) -> None:
    """
    Apply a sequence of (position, player) moves to *game* without prompts.

    Parameters
    ----------
    game : TicTacToe
        A fresh or existing game instance.
    moves : list of (position, player) tuples
        Each tuple is a 1-based cell position and player number.
    """
    for pos, player in moves:
        game.make_move(pos, player)


# ---------------------------------------------------------------------------
# Test Suite
# ---------------------------------------------------------------------------

class TestBoardInitialisation(unittest.TestCase):
    """Tests that a new board starts in the correct empty state."""

    def setUp(self) -> None:
        self.game = TicTacToe(theme_key="classic")

    def test_board_has_nine_cells(self) -> None:
        self.assertEqual(len(self.game.board), 9)

    def test_cells_are_position_strings(self) -> None:
        expected = [str(i) for i in range(1, 10)]
        self.assertEqual(self.game.board, expected)

    def test_no_winner_on_fresh_board(self) -> None:
        self.assertIsNone(self.game.check_winner())

    def test_no_draw_on_fresh_board(self) -> None:
        self.assertFalse(self.game.check_draw())

    def test_reset_board_restores_initial_state(self) -> None:
        self.game.make_move(1, 1)
        self.game.make_move(2, 2)
        self.game.reset_board()
        expected = [str(i) for i in range(1, 10)]
        self.assertEqual(self.game.board, expected)

    def test_scores_start_at_zero(self) -> None:
        self.assertEqual(self.game.scores["Player 1"], 0)
        self.assertEqual(self.game.scores["Player 2"], 0)
        self.assertEqual(self.game.scores["Draws"], 0)


class TestMoveValidation(unittest.TestCase):
    """Tests for is_valid_move and make_move."""

    def setUp(self) -> None:
        self.game = TicTacToe(theme_key="classic")

    # --- is_valid_move -------------------------------------------------

    def test_all_cells_valid_on_empty_board(self) -> None:
        for pos in range(1, 10):
            with self.subTest(pos=pos):
                self.assertTrue(self.game.is_valid_move(pos))

    def test_zero_is_invalid(self) -> None:
        self.assertFalse(self.game.is_valid_move(0))

    def test_ten_is_invalid(self) -> None:
        self.assertFalse(self.game.is_valid_move(10))

    def test_negative_position_invalid(self) -> None:
        self.assertFalse(self.game.is_valid_move(-1))

    def test_claimed_cell_is_invalid(self) -> None:
        self.game.make_move(5, 1)
        self.assertFalse(self.game.is_valid_move(5))

    def test_other_cells_still_valid_after_move(self) -> None:
        self.game.make_move(5, 1)
        for pos in (1, 2, 3, 4, 6, 7, 8, 9):
            with self.subTest(pos=pos):
                self.assertTrue(self.game.is_valid_move(pos))

    # --- make_move -----------------------------------------------------

    def test_make_move_returns_true_on_valid_move(self) -> None:
        self.assertTrue(self.game.make_move(1, 1))

    def test_make_move_places_correct_symbol_player1(self) -> None:
        self.game.make_move(3, 1)
        self.assertEqual(self.game.board[2], self.game.theme["p1_symbol"])

    def test_make_move_places_correct_symbol_player2(self) -> None:
        self.game.make_move(7, 2)
        self.assertEqual(self.game.board[6], self.game.theme["p2_symbol"])

    def test_make_move_returns_false_on_taken_cell(self) -> None:
        self.game.make_move(1, 1)
        self.assertFalse(self.game.make_move(1, 2))

    def test_make_move_does_not_overwrite_on_false(self) -> None:
        self.game.make_move(1, 1)
        self.game.make_move(1, 2)
        self.assertEqual(self.game.board[0], self.game.theme["p1_symbol"])

    def test_make_move_returns_false_for_out_of_range(self) -> None:
        self.assertFalse(self.game.make_move(0, 1))
        self.assertFalse(self.game.make_move(10, 1))


class TestWinDetection(unittest.TestCase):
    """Tests for check_winner — horizontal, vertical, and diagonal combos."""

    def setUp(self) -> None:
        self.game = TicTacToe(theme_key="classic")

    # --- Horizontal wins -----------------------------------------------

    def test_player1_wins_top_row(self) -> None:
        _fill_board(self.game, [(1, 1), (2, 1), (3, 1)])
        self.assertEqual(self.game.check_winner(), 1)

    def test_player1_wins_middle_row(self) -> None:
        _fill_board(self.game, [(4, 1), (5, 1), (6, 1)])
        self.assertEqual(self.game.check_winner(), 1)

    def test_player1_wins_bottom_row(self) -> None:
        _fill_board(self.game, [(7, 1), (8, 1), (9, 1)])
        self.assertEqual(self.game.check_winner(), 1)

    def test_player2_wins_top_row(self) -> None:
        _fill_board(self.game, [(1, 2), (2, 2), (3, 2)])
        self.assertEqual(self.game.check_winner(), 2)

    def test_player2_wins_middle_row(self) -> None:
        _fill_board(self.game, [(4, 2), (5, 2), (6, 2)])
        self.assertEqual(self.game.check_winner(), 2)

    def test_player2_wins_bottom_row(self) -> None:
        _fill_board(self.game, [(7, 2), (8, 2), (9, 2)])
        self.assertEqual(self.game.check_winner(), 2)

    # --- Vertical wins -------------------------------------------------

    def test_player1_wins_left_column(self) -> None:
        _fill_board(self.game, [(1, 1), (4, 1), (7, 1)])
        self.assertEqual(self.game.check_winner(), 1)

    def test_player1_wins_middle_column(self) -> None:
        _fill_board(self.game, [(2, 1), (5, 1), (8, 1)])
        self.assertEqual(self.game.check_winner(), 1)

    def test_player1_wins_right_column(self) -> None:
        _fill_board(self.game, [(3, 1), (6, 1), (9, 1)])
        self.assertEqual(self.game.check_winner(), 1)

    def test_player2_wins_left_column(self) -> None:
        _fill_board(self.game, [(1, 2), (4, 2), (7, 2)])
        self.assertEqual(self.game.check_winner(), 2)

    def test_player2_wins_right_column(self) -> None:
        _fill_board(self.game, [(3, 2), (6, 2), (9, 2)])
        self.assertEqual(self.game.check_winner(), 2)

    # --- Diagonal wins -------------------------------------------------

    def test_player1_wins_diagonal_top_left_to_bottom_right(self) -> None:
        _fill_board(self.game, [(1, 1), (5, 1), (9, 1)])
        self.assertEqual(self.game.check_winner(), 1)

    def test_player1_wins_diagonal_top_right_to_bottom_left(self) -> None:
        _fill_board(self.game, [(3, 1), (5, 1), (7, 1)])
        self.assertEqual(self.game.check_winner(), 1)

    def test_player2_wins_diagonal_top_left_to_bottom_right(self) -> None:
        _fill_board(self.game, [(1, 2), (5, 2), (9, 2)])
        self.assertEqual(self.game.check_winner(), 2)

    def test_player2_wins_diagonal_top_right_to_bottom_left(self) -> None:
        _fill_board(self.game, [(3, 2), (5, 2), (7, 2)])
        self.assertEqual(self.game.check_winner(), 2)

    # --- No winner yet -------------------------------------------------

    def test_no_winner_midgame(self) -> None:
        _fill_board(self.game, [(1, 1), (2, 2), (3, 1)])
        self.assertIsNone(self.game.check_winner())

    def test_no_winner_on_empty_board(self) -> None:
        self.assertIsNone(self.game.check_winner())

    def test_mixed_symbols_do_not_trigger_win(self) -> None:
        # Row with alternating symbols must NOT be a win
        _fill_board(self.game, [(1, 1), (2, 2), (3, 1)])
        self.assertIsNone(self.game.check_winner())


class TestDrawDetection(unittest.TestCase):
    """Tests for check_draw."""

    def setUp(self) -> None:
        self.game = TicTacToe(theme_key="classic")

    def test_draw_on_full_board_with_no_winner(self) -> None:
        # Known draw board layout:
        # P1 P2 P1
        # P1 P1 P2
        # P2 P1 P2
        moves = [
            (1, 1), (2, 2), (3, 1),
            (4, 1), (5, 1), (6, 2),
            (7, 2), (8, 1), (9, 2),
        ]
        _fill_board(self.game, moves)
        self.assertTrue(self.game.check_draw())

    def test_not_draw_when_winner_exists(self) -> None:
        # P1 wins top row — board is "full" but there IS a winner
        moves = [
            (1, 1), (2, 1), (3, 1),
            (4, 2), (5, 2), (6, 1),
            (7, 2), (8, 1), (9, 2),
        ]
        _fill_board(self.game, moves)
        self.assertFalse(self.game.check_draw())

    def test_not_draw_on_empty_board(self) -> None:
        self.assertFalse(self.game.check_draw())

    def test_not_draw_mid_game(self) -> None:
        _fill_board(self.game, [(1, 1), (2, 2), (3, 1)])
        self.assertFalse(self.game.check_draw())

    def test_draw_requires_all_cells_filled(self) -> None:
        # Fill 8 cells without a winner — still not a draw
        moves = [
            (1, 1), (2, 2), (3, 1),
            (4, 2), (5, 2), (6, 1),
            (7, 1), (8, 2),  # cell 9 left empty
        ]
        _fill_board(self.game, moves)
        self.assertFalse(self.game.check_draw())


class TestThemes(unittest.TestCase):
    """Tests that themes load and work correctly."""

    def test_all_themes_loadable(self) -> None:
        for key in THEMES:
            with self.subTest(theme=key):
                game = TicTacToe(theme_key=key)
                self.assertIn("p1_symbol", game.theme)
                self.assertIn("p2_symbol", game.theme)

    def test_invalid_theme_falls_back_to_classic(self) -> None:
        game = TicTacToe(theme_key="nonexistent_theme")
        self.assertEqual(game.theme, THEMES["classic"])

    def test_space_theme_symbols(self) -> None:
        game = TicTacToe(theme_key="space")
        self.assertEqual(game.theme["p1_symbol"], "🚀")
        self.assertEqual(game.theme["p2_symbol"], "👾")

    def test_pets_theme_symbols(self) -> None:
        game = TicTacToe(theme_key="pets")
        self.assertEqual(game.theme["p1_symbol"], "🐶")
        self.assertEqual(game.theme["p2_symbol"], "🐱")

    def test_win_detected_with_non_classic_theme(self) -> None:
        game = TicTacToe(theme_key="space")
        _fill_board(game, [(1, 1), (2, 1), (3, 1)])
        self.assertEqual(game.check_winner(), 1)


class TestScoreTracking(unittest.TestCase):
    """Tests that scores are updated correctly across rounds."""

    def setUp(self) -> None:
        self.game = TicTacToe(theme_key="classic")

    def test_initial_scores_all_zero(self) -> None:
        self.assertEqual(sum(self.game.scores.values()), 0)

    def test_score_keys_exist(self) -> None:
        self.assertIn("Player 1", self.game.scores)
        self.assertIn("Player 2", self.game.scores)
        self.assertIn("Draws", self.game.scores)

    def test_scores_not_reset_by_reset_board(self) -> None:
        self.game.scores["Player 1"] = 3
        self.game.reset_board()
        self.assertEqual(self.game.scores["Player 1"], 3)


class TestWinCombos(unittest.TestCase):
    """Verify the WIN_COMBOS constant is correct."""

    def test_exactly_eight_win_combos(self) -> None:
        self.assertEqual(len(TicTacToe.WIN_COMBOS), 8)

    def test_combos_are_unique(self) -> None:
        combo_set = set(TicTacToe.WIN_COMBOS)
        self.assertEqual(len(combo_set), 8)

    def test_all_indices_in_valid_range(self) -> None:
        for combo in TicTacToe.WIN_COMBOS:
            for idx in combo:
                with self.subTest(idx=idx):
                    self.assertIn(idx, range(9))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main(verbosity=2)

