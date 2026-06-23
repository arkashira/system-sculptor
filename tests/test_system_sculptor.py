import time
import pytest
from system_sculptor import recommend_patterns, Pattern


def test_recommend_patterns_happy_path():
    """Engine should return at least one pattern with relevance > 0.7."""
    scan = {"module_size": 800, "coupling": 15}
    patterns = recommend_patterns(scan)

    # At least one pattern must be returned
    assert len(patterns) >= 1

    # All patterns must have relevance > 0.7 and be sorted descending
    prev_score = float("inf")
    for pat in patterns:
        assert isinstance(pat, Pattern)
        assert pat.relevance_score > 0.7
        assert pat.relevance_score <= prev_score  # descending order
        prev_score = pat.relevance_score
        # Justification must mention the metric that triggered it
        if pat.name == "Service Decomposition":
            assert "Module size" in pat.justification
        if pat.name == "API Gateway":
            assert "Coupling count" in pat.justification


def test_recommend_patterns_missing_metric():
    """Missing required metric should raise ValueError."""
    scan_missing = {"module_size": 800}  # coupling missing
    with pytest.raises(ValueError) as exc:
        recommend_patterns(scan_missing)
    assert "Missing required metric(s)" in str(exc.value)


def test_recommend_patterns_performance():
    """Engine must respond within 2 seconds."""
    scan = {"module_size": 1200, "coupling": 25}
    start = time.perf_counter()
    patterns = recommend_patterns(scan)
    duration = time.perf_counter() - start

    assert duration < 2.0, f"Duration {duration:.3f}s exceeds 2‑second limit"
    # Ensure we still get patterns (the data is large enough)
    assert len(patterns) >= 1
