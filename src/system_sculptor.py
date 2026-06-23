import time
from dataclasses import dataclass
from typing import List, Dict


@dataclass(frozen=True)
class Pattern:
    """A recommended architectural pattern."""
    name: str
    justification: str
    relevance_score: float


def _validate_scan_data(scan_data: Dict) -> None:
    """Validate that required metric keys are present and have sensible types."""
    if not isinstance(scan_data, dict):
        raise TypeError("scan_data must be a dict")
    required = {"module_size", "coupling"}
    missing = required - scan_data.keys()
    if missing:
        raise ValueError(f"Missing required metric(s): {', '.join(sorted(missing))}")
    if not isinstance(scan_data["module_size"], (int, float)):
        raise TypeError("module_size must be a number")
    if not isinstance(scan_data["coupling"], (int, float)):
        raise TypeError("coupling must be a number")


def recommend_patterns(scan_data: Dict) -> List[Pattern]:
    """
    Recommend micro‑service patterns based on simple code metrics.

    Parameters
    ----------
    scan_data: dict
        Must contain:
        - ``module_size`` (int/float): lines of code in the module.
        - ``coupling`` (int/float): number of external dependencies.

    Returns
    -------
    List[Pattern]
        Patterns with relevance_score > 0.7, sorted descending by relevance.
    """
    start = time.perf_counter()
    _validate_scan_data(scan_data)

    size = float(scan_data["module_size"])
    coupling = float(scan_data["coupling"])

    patterns: List[Pattern] = []

    # Pattern 1: Service Decomposition (triggered by large module size)
    if size > 500:
        relevance = min(1.0, size / 1000)  # 500 -> 0.5, 800 -> 0.8, etc.
        if relevance > 0.7:
            justification = (
                f"Module size {int(size)} lines suggests splitting the monolith "
                f"into smaller, independently deployable services."
            )
            patterns.append(
                Pattern(
                    name="Service Decomposition",
                    justification=justification,
                    relevance_score=relevance,
                )
            )

    # Pattern 2: API Gateway (triggered by high coupling)
    if coupling > 10:
        relevance = min(1.0, coupling / 20)  # 10 -> 0.5, 15 -> 0.75, etc.
        if relevance > 0.7:
            justification = (
                f"Coupling count {int(coupling)} indicates many external calls; "
                f"an API Gateway can centralise routing and concerns."
            )
            patterns.append(
                Pattern(
                    name="API Gateway",
                    justification=justification,
                    relevance_score=relevance,
                )
            )

    # Sort by relevance descending
    patterns.sort(key=lambda p: p.relevance_score, reverse=True)

    # Ensure we respect the 2‑second response guarantee (no artificial delay)
    elapsed = time.perf_counter() - start
    if elapsed > 2.0:
        # In a real system we might log a warning; here we simply raise.
        raise RuntimeError("Recommendation engine exceeded time budget")

    return patterns
