<h3 align="center">🛠️ System‑Sculptor</h3>

<div align="center">
  <a href="https://github.com/your-org/system-sculptor"><img src="https://img.shields.io/github/license/your-org/system-sculptor?color=blue&style=flat-square" alt="License"></a>
  <a href="https://github.com/your-org/system-sculptor"><img src="https://img.shields.io/badge/language-Python%203.9%2B-blue?style=flat-square" alt="Language"></a>
  <a href="https://github.com/your-org/system-sculptor/actions"><img src="https://img.shields.io/github/workflow/status/your-org/system-sculptor/CI?label=build&style=flat-square" alt="Build Status"></a>
  <a href="https://github.com/your-org/system-sculptor/stargazers"><img src="https://img.shields.io/github/stars/your-org/system-sculptor?style=flat-square" alt="Stars"></a>
</div>

---

# 🚀 System‑Sculptor
**Power developers with data‑driven micro‑service pattern recommendations.** Turn code‑metric scans into actionable architecture guidance in seconds.

## Why System‑Sculptor?
- **Speed** – delivers ranked recommendations in **under 2 seconds** for typical inputs.  
- **Accuracy** – only patterns with a relevance score **≥ 0.7** are returned, ensuring high‑quality advice.  
- **Simplicity** – a **single‑function API**; feed a JSON of metrics, get back patterns and justifications.  
- **Developer‑Centric** – built for **software engineers & architects** who need quick, data‑backed design decisions.  
- **Open‑Source** – MIT‑licensed, free to audit, extend, and integrate into any pipeline.  
- **Extensible** – plug‑in new metric sources or custom pattern libraries via a tiny extension point.  

## Feature Overview
| Feature | Description |
|---------|-------------|
| **Metric Ingestion** | Accepts plain‑JSON or Python dicts containing code‑metric data (e.g., cyclomatic complexity, LOC, coupling). |
| **Pattern Recommendation** | Maps metrics to a curated catalogue of micro‑service patterns (e.g., API‑Gateway, Event‑Sourcing, CQRS). |
| **Relevance Scoring** | Calculates a score 0‑1 for each pattern; only scores **≥ 0.7** are emitted. |
| **Justification Report** | Returns human‑readable explanations linking each metric to the suggested pattern. |
| **Fast Execution** | Guarantees response time **< 2 s** on typical workloads (≤ 10 KB metric payload). |
| **Configurable Threshold** | Override the default 0.7 cutoff via a simple function argument. |
| **Test Suite** | 100 % coverage with pytest, ensuring reliability across Python versions. |

## Tech Stack
- **Python** (≥ 3.9) – core implementation and runtime.

## Project Structure
```
system-sculptor/
├─ business/      # Business‑logic helpers (pattern catalogue, scoring)
├─ docs/          # Documentation assets (README, PRD, etc.)
├─ src/           # Library source code
│   └─ system_sculptor/  # Public Python package
├─ tests/         # pytest test suite
├─ pyproject.toml # Build & dependency configuration
└─ README.md      # This file
```

## Getting Started
```bash
# 1️⃣ Clone the repo (optional if you want to develop)
git clone https://github.com/your-org/system-sculptor.git
cd system-sculptor

# 2️⃣ Install the package (editable mode for development)
pip install -e .

# 3️⃣ Quick sanity check – run the test suite
pytest -q
```

### Basic usage
```python
from system_sculptor import recommend_patterns

metrics = {
    "cyclomatic_complexity": 12,
    "lines_of_code": 850,
    "coupling": 0.42,
    "cohesion": 0.68
}

patterns = recommend_patterns(metrics, threshold=0.7)
print(patterns)
# [{'pattern': 'Event Sourcing', 'score': 0.82, 'justification': '...'}]
```

## Deploy
System‑Sculptor is a pure‑Python library; deployment is simply a **pip install** in any environment (virtualenv, Docker, CI/CD, etc.):

```bash
pip install system-sculptor
```

If you package it inside a container, add the line above to your `Dockerfile`:

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir .
COPY . .
```

## Status
Active development – latest commit **57a868d**: *DR snapshot 20260628-161015*.

## Contributing
We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose changes, run tests, and submit pull requests.

## License
Distributed under the **MIT License**.