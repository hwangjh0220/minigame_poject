from games.rps import decide


def test_decide_win():
    assert decide("1", "3") == "win"  # 가위 vs 보
    assert decide("2", "1") == "win"  # 바위 vs 가위
    assert decide("3", "2") == "win"  # 보 vs 바위


def test_decide_lose():
    assert decide("1", "2") == "lose"  # 가위 vs 바위
    assert decide("2", "3") == "lose"  # 바위 vs 보
    assert decide("3", "1") == "lose"  # 보 vs 가위


def test_decide_draw():
    for choice in ("1", "2", "3"):
        assert decide(choice, choice) == "draw"
