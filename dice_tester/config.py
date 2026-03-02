"""Static configuration for the custom die."""

from collections import Counter

FACES = ["oo", "o", "xx", "x", "x", "R"]
VALID_RESULTS = sorted(set(FACES))
EXPECTED_PROBABILITIES = {
    symbol: count / len(FACES) for symbol, count in Counter(FACES).items()
}

