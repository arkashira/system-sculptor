# STORIES.md
**Project:** system‑sculptor  
**Product Vision:** A software‑architecture analysis and optimization tool that empowers developers and architects to model, evaluate, and continuously improve the maintainability, scalability, and performance of their systems.

---

## Epic 1 – Core Modeling & Visualization (MVP)

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 1 | **As a developer, I want to import my existing codebase (via a `manifest.json` or direct directory scan) so that I can instantly generate a visual architecture diagram.** | - The tool accepts a `manifest.json` describing modules, services, and dependencies **or** scans a supplied directory recursively.<br>- Generates a directed graph (nodes = components, edges = dependencies).<br>- Diagram is viewable in the web UI with pan/zoom and searchable node list.<br>- Export options: PNG, SVG, and GraphViz DOT. |
| 2 | **As an architect, I want to annotate components with metadata (e.g., language, runtime, criticality) so that the model reflects real‑world attributes.** | - UI allows adding/editing key‑value metadata per node.<br>- Metadata is persisted in the project file (`.sculptor` JSON).<br>- Annotations appear as tool‑tips on the diagram.<br>- Exported diagrams include metadata as node labels when requested. |
| 3 | **As a QA engineer, I want to run a “dependency health” check that flags circular dependencies and high‑fan‑in nodes so that I can identify risky coupling early.** | - Analyzer runs on the generated graph.<br>- Reports: <br>  • List of cycles with involved nodes.<br>  • Nodes with fan‑in > configurable threshold.<br>- Results displayed in a sortable table with links to the diagram.<br>- Exportable as CSV/JSON. |

---

## Epic 2 – Quality Metrics & Scoring

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 4 | **As a product manager, I want a single “maintainability score” for the whole system so that I can track architectural health over time.** | - Score calculated from weighted metrics: cyclomatic complexity (from static analysis), coupling, cohesion, and test coverage (if provided).<br>- Score displayed on a dashboard gauge (0‑100).<br>- Historical trend chart persists across analysis runs. |
| 5 | **As a developer, I want to see per‑component metrics (e.g., lines of code, number of public APIs, test coverage) so that I can pinpoint hotspots.** | - Metrics panel lists each component with numeric values.<br>- Clicking a component highlights it on the diagram.<br>- Data source: optional integration with `vLLM`‑based static analysis plugin (plug‑and‑play). |
| 6 | **As a security lead, I want the tool to flag components that lack unit/integration tests so that I can prioritize testing effort.** | - Analyzer checks for presence of test files matching common patterns (`*_test.py`, `*.spec.js`, etc.).<br>- Components with < 80 % coverage are highlighted in red on the diagram and listed in a “Testing Gaps” report. |

---

## Epic 3 – Optimization Recommendations

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 7 | **As an architect, I want actionable refactoring suggestions (e.g., split a monolithic service, introduce an interface) so that I can improve scalability.** | - Engine matches anti‑patterns (large fan‑in, high cyclomatic complexity) to a library of refactor templates.<br>- Each suggestion includes: description, affected components, estimated impact on score, and step‑by‑step guidance.<br>- UI presents suggestions in a “Roadmap” view with priority tags. |
| 8 | **As a DevOps engineer, I want to simulate the effect of moving a component to a separate deployment (e.g., container) and see the projected score change.** | - “What‑if” sandbox lets the user drag a node into a new “deployment zone”.<br>- Re‑calculates coupling and latency metrics instantly.<br>- Shows delta of maintainability and scalability scores. |
| 9 | **As a stakeholder, I want to export a PDF report summarizing the current architecture, metrics, and recommendations so that I can share it with non‑technical teams.** | - One‑click “Generate Report”.<br>- Includes executive summary, diagrams, metric tables, and recommendation list.<br>- PDF is downloadable and also stored in the project’s `reports/` folder. |

---

## Epic 4 – Collaboration & CI Integration

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 10 | **As a team lead, I want to version‑control the architecture model alongside source code so that changes are tracked over time.** | - Model files (`.sculptor`, diagrams) live in the repo root.<br>- CLI command `sculptor sync` updates the model from code and commits changes with a conventional commit message.<br>- Git diff shows added/removed nodes and metric changes. |
| 11 | **As a CI engineer, I want a GitHub Action that runs the analysis on every PR and fails if the maintainability score drops more than a configurable threshold.** | - Action `axentx/system-sculptor@vX` installs the tool, runs analysis on the PR branch, and compares scores to the base branch.<br>- Configurable `max_score_drop` input (default 5).<br>- Action annotates the PR with a summary table and sets status check to failure when threshold exceeded. |
| 12 | **As a developer, I want to comment inline on a PR with a link to the specific component’s analysis so that reviewers can see the architectural impact directly.** | - CLI provides a `sculptor comment <component>` command that posts a formatted comment via the GitHub API.<br>- Comment includes a snapshot of metrics, current score, and a link to the live diagram view (hosted on Axentx SaaS). |

---

## Epic 5 – Extensibility & Plug‑in Ecosystem (Post‑MVP)

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 13 | **As a platform engineer, I want to add custom metric calculators (e.g., latency budgets) via a plug‑in so that the tool fits our domain.** | - Plug‑in API exposes `registerMetric(name, fn(component) -> number)`.<br>- Plug‑ins are discovered from a `plugins/` directory and loaded at runtime.<br>- New metrics appear alongside built‑in ones in the UI and can be used in scoring formulas. |
| 14 | **As an open‑source contributor, I want clear documentation and a template repo for building new visual themes so that the UI can match our brand.** | - `docs/plugins/theme.md` describes required CSS variables and component overrides.<br>- A `theme‑starter` repo is linked in the README.<br>- The UI includes a theme selector that loads a theme from `themes/` folder. |
| 15 | **As a data scientist, I want to export the full graph and metric dataset to a Parquet file so that I can run advanced analytics offline.** | - CLI command `sculptor export --format parquet` produces `architecture.parquet` containing nodes, edges, and all metric columns.<br>- File conforms to a documented schema and can be imported into pandas/SQL for further analysis. |

---

### Prioritization for MVP
1. Core Modeling & Visualization (Stories 1‑3)  
2. Quality Metrics & Scoring (Stories 4‑6)  
3. Optimization Recommendations (Stories 7‑9) – limited to static suggestions  
4. Collaboration & CI Integration (Stories 10‑12) – essential for adoption  

Post‑MVP epics (13‑15) will be tackled after the first production release to foster ecosystem growth.
