from games.hangman import mask_word


def test_mask_word_all_hidden():
    # 추측한 글자가 하나도 없을 때 모두 '_'로 가려지는지 테스트
    assert mask_word("apple", set()) == "_ _ _ _ _"


def test_mask_word_partially_guessed():
    # 일부 글자를 맞혔을 때 해당 글자만 보이는지 테스트
    assert mask_word("apple", {"p", "e"}) == "_ p p _ e"


def test_mask_word_fully_guessed():
    # 모든 글자를 맞혔을 때 단어가 전체 다 보이는지 테스트
    assert mask_word("apple", {"a", "p", "l", "e"}) == "a p p l e"