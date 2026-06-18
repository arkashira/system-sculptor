# ROADMAP.md – system‑sculptor

**Product Vision**  
system‑sculptor is a developer‑centric analysis and optimization platform that automatically inspects codebases, visualizes architectural dependencies, and recommends refactorings to improve maintainability, scalability, and performance. It integrates with existing CI pipelines and supports the languages and frameworks most common in Axentx’s client portfolio.

---

## 📅 Milestones Overview

| Milestone | Target Release | Theme | MVP‑Critical Items |
|-----------|----------------|-------|--------------------|
| **MVP**   | **2026‑09‑30** | Core analysis & feedback loop | ✅ Language parsers (C/C++, Rust, Python) <br> ✅ Dependency graph generation <br> ✅ Scoring model (maintainability, coupling, cyclomatic complexity) <br> ✅ CLI & VS Code extension (basic UI) <br> ✅ CI integration (GitHub Actions) |
| **v1.0**  | 2026‑12‑15 | Interactive visualization & team collaboration | ✅ Web UI with live graph navigation <br> ✅ Refactoring suggestions (auto‑generated PRs) <br> ✅ Team dashboards & trend analytics <br> ✅ Export formats (SVG, JSON) |
| **v2.0**  | 2027‑03‑31 | Advanced optimization & ecosystem hooks | ✅ Runtime profiling integration (vLLM, SGLang) <br> ✅ AI‑driven “what‑if” scenario simulation <br> ✅ Multi‑repo & monorepo support <br> ✅ Enterprise SSO & RBAC <br> ✅ Marketplace for custom rule packs |

---

## 🏁 MVP – Must‑Have for Launch (2026‑09‑30)

| Category | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|----------------------|
| **Language Support** | Parsers | Static analysis for C/C++, Rust, Python (most used in Axentx projects). | Accurate AST generation for ≥95 % of files in test suite. |
| **Architecture Extraction** | Dependency Graph Engine | Build directed graph of modules, libraries, and external services. | Graph reflects real imports/links; size ≤ O(N) memory for 1 M LOC. |
| **Quality Scoring** | Metric Suite | Compute maintainability index, coupling, cyclomatic complexity, and code churn. | Scores displayed per module; thresholds configurable. |
| **User Interface** | CLI | `system-sculptor analyze <path>` with JSON output. | Runs on Linux/macOS/Windows; completes ≤ 2 min for 500k LOC. |
| | VS Code Extension | Inline diagnostics & “View Architecture” command. | Shows graph thumbnail; opens web view on click. |
| **CI Integration** | GitHub Action | Auto‑run on PRs, post comment with score delta and high‑risk modules. | Fails PR if score drop > 10 % without justification. |
| **Documentation** | Quick‑Start Guide | Installation, first‑run, CI setup. | New user can run analysis on sample repo in ≤ 10 min. |
| **Testing & Reliability** | Test Suite | Unit + integration tests covering 90 % of code paths. | CI pipeline passes on every commit. |
| **Telemetry (opt‑in)** | Usage Metrics | Collect anonymized usage for model improvement. | GDPR‑compliant opt‑in toggle. |

*All MVP items are **shippable** and will be delivered as a single versioned release (`system-sculptor@0.1.0`).*

---

## 🚀 v1.0 – Interactive Visualization & Collaboration (2026‑12‑15)

| Theme | Feature | Description | Ship Date |
|-------|---------|-------------|-----------|
| **Web UI** | Graph Explorer | Interactive, zoomable architecture graph with filterable layers (packages, services, external APIs). | 2026‑10‑15 |
| | Heatmap Overlay | Visual cue for high‑risk components based on MVP scores. | 2026‑10‑30 |
| **Collaboration** | Team Dashboards | Aggregate scores, trend lines, and “technical debt” backlog per team. | 2026‑11‑10 |
| | PR‑Based Refactor Suggestions | Auto‑generate PRs with suggested file moves, dependency inversions, or API wrappers. | 2026‑11‑25 |
| **Export & Integration** | Formats | Export graph to SVG, GraphML, JSON for downstream tools. | 2026‑12‑01 |
| | Slack / Teams Bot | Post daily/weekly health summaries. | 2026‑12‑10 |
| **Quality** | Rule Engine Extensibility | Plug‑in API for custom architectural rules (e.g., “no circular imports”). | 2026‑12‑15 |

---

## 🌐 v2.0 – Advanced Optimization & Enterprise Features (2027‑03‑31)

| Theme | Feature | Description | Ship Date |
|-------|---------|-------------|-----------|
| **Runtime Insight** | Profiling Hooks | Connect to vLLM and SGLang runtimes to correlate static architecture with actual latency/throughput hotspots. | 2027‑01‑20 |
| **AI‑Driven Simulation** | What‑If Engine | Generate “future” architecture scenarios and predict impact on latency, cost, and maintainability using Axentx’s internal LLMs. | 2027‑02‑10 |
| **Scale** | Multi‑Repo & Monorepo Support | Unified view across dozens of repositories, handling cross‑repo dependencies. | 2027‑02‑28 |
| **Enterprise Security** | SSO & RBAC | SAML/OIDC integration, role‑based access to dashboards and rule packs. | 2027‑03‑10 |
| **Marketplace** | Rule Pack Store | Community/partner contributed rule packs (e.g., “micro‑service bounded‑context validator”). | 2027‑03‑20 |
| **Performance** | Incremental Analysis | Cache and only re‑analyze changed modules; sub‑second feedback for CI. | 2027‑03‑31 |

---

## 📦 Release Cadence & Process

1. **Sprint Planning** – 2‑week sprints, backlog prioritized by ROI & validation feedback.  
2. **Feature Freeze** – One week before each target date; only bug fixes allowed.  
3. **Beta Program** – Invite internal Axentx teams & 3 external pilot customers per milestone.  
4. **Post‑Release Review** – Collect usage telemetry, NPS, and WTP (willingness‑to‑pay) signals; feed into next iteration.

---

## 📈 Success Metrics

| Metric | Target (by 2027‑04) |
|--------|--------------------|
| Adoption | 30+ active repositories (≥ 500 k LOC each) |
| Technical Debt Reduction | Avg. maintainability score improvement ≥ 15 % per repo |
| CI Impact | Average PR analysis time ≤ 30 seconds |
| Revenue | Convert 15 % of beta users to paid tier (enterprise) |
| Customer Satisfaction | NPS ≥ 45 |

---

*Prepared by the System‑Sculptor Product & Engineering Lead – Axentx*
