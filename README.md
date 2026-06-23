# system-sculptor

A minimal Python library that recommends micro‑service architectural patterns
based on simple code‑metric “scan data”.

## Features
- Returns one or more patterns with a justification tied to the supplied metrics.
- Patterns are ranked by a relevance score (only scores > 0.7 are returned).
- Guarantees a response in under 2 seconds for typical inputs.

## Usage
