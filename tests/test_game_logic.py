from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: out-of-range guesses should be rejected ---

def test_parse_guess_below_range():
    # Guessing 0 when range is 1-100 should fail validation
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_above_range():
    # Guessing 101 when range is 1-100 should fail validation
    ok, value, err = parse_guess("101", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_within_range():
    # Guessing 50 when range is 1-100 should pass
    ok, value, err = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50
    assert err is None

def test_parse_guess_at_boundaries():
    # Boundary values 1 and 100 should both be valid
    ok_low, _, _ = parse_guess("1", 1, 100)
    ok_high, _, _ = parse_guess("100", 1, 100)
    assert ok_low is True
    assert ok_high is True


# --- Bug 2: new game must reset game status ---
# This bug lives in Streamlit session state and cannot be unit tested here.
# The fix: when New Game is clicked, st.session_state.status must be reset
# to "playing" so the st.stop() guard at the top of the game loop does not
# block further input.
