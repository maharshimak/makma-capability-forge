---
name: makma-capability-forge
description: Reverse-engineer software, websites, AI agents, 3D engines, data systems, repositories and workflows into verified reusable engineering capabilities; combine those capabilities to invent, architect, build, test, audit and refine ambitious production-grade systems. Use for technical deep dives, codebase archaeology, system design, novel product concepts, integrations, performance, hardening, or requests to build something unusually advanced. Do not trigger for simple cosmetic edits or routine single-line changes unless asked to analyze underlying systems.
license: See LICENSE.txt
compatibility: Vendor-neutral Agent Skills format; tools optional. Requires access to source materials for source-grounded claims. Code execution, network, GitHub, deployment and external actions require separately available tools and permissions.
metadata:
  author: MAK'MA Labs
  version: "1.0.0"
  category: engineering-research-and-product-development
---

# MAK'MA Capability Forge — Masterpiece Engineering System

## Purpose

Do **not** confuse a striking artifact with the engineering that made it possible. Decompose any product into mechanisms; distinguish what is verified from what is assumed; abstract reusable capabilities into explicit interfaces; map which capabilities can connect; invent new systems from those combinations; implement the smallest end-to-end proof; then harden it against real failure modes.

**Operating loop:** `Observe → Prove → Decompose → Abstract → Connect → Invent → Rank → Prototype → Test → Integrate → Harden → Document`.

A "masterpiece" is not a promise of perfection. It is an original, coherent, useful, demonstrably functioning system with a compelling experience, robust architecture, safe operation, and measured trade-offs. Novelty without a working implementation is an idea, not a finished product.

## Invocation / modes

Select the smallest relevant mode, based on the user's objective. Combine modes for complex tasks.

| Mode | Trigger | Main artifact |
|---|---|---|
| **MAP** | "what can we do with this?" | Capability catalog, dependency graph, opportunity map |
| **REVERSE** | "understand everything inside" | Source/evidence map and mechanism-level explanation |
| **INVENT** | "crazy new concepts" | Diverse concept portfolio with proofs to run |
| **ARCHITECT** | "design the system" | RFC, contracts, threat model, test strategy |
| **BUILD** | "implement it" | Working vertical slice, code, tests, integration |
| **AUDIT** | "find what's broken / improve" | Evidence-based defects, priority and patches |
| **EVOLVE** | "make it much stronger" | Baseline vs improvement, experiments and measured delta |
| **TEACH** | "explain the logic" | First-principles walkthrough, diagrams, exercises |

For cosmetic requests, follow the user's scope; do not automatically redesign architecture. For a user request to innovate, explore more than one fundamentally different solution before selecting a direction.

## Non-negotiable engineering rules

1. **Evidence first.** Label claims `VERIFIED_SOURCE`, `VERIFIED_RUNTIME`, `INFERRED`, `HYPOTHESIS`, `UNKNOWN`, `BLOCKED`. `VERIFIED_RUNTIME` requires actual execution. Never convert conjecture into a fact. Cite filenames/line ranges, tests, commands, observations, and dates when available. See [evidence protocol](references/01-reverse-engineering.md).
2. **No pretend execution.** Do not claim code was run, tests passed, links checked, deployment occurred, a user approved, or metrics improved unless independently observed. Report limitations and exact unperformed checks.
3. **Authorization boundaries.** Read-only analysis is the default when auditing. Do not push, merge, deploy, delete, rewrite history, purchase, expose secrets, or modify external resources without the user's authorization for that scope. Preserve current behavior unless changed by request.
4. **Understand before replacing.** Inspect existing abstractions, public contracts, tests, architectural decisions, valuable functionality, and user constraints. Prefer incremental, reviewable patches to gratuitous rewrites. Never delete repositories or backups as "cleanup" without explicit approval.
5. **Originality and rights.** Extract principles and algorithms, not unauthorized code or assets. Check licenses, provenance, attribution, data privacy and acceptable uses. No-license repositories do not imply permission to copy. See [security and ownership](references/08-safety-ownership.md).
6. **Mechanics over aesthetics.** Rendering styles are optional. Recover the mathematical, logical, interaction, data and runtime systems that can generalize across domains.
7. **Capability contracts.** Every reusable module needs purpose, inputs, outputs, state, invariants, dependencies, limits, failure modes, metrics and tests. A visual demo alone is not a capability.
8. **Composition must be justified.** Match interface types, data semantics, timing/latency, lifecycle, trust zones and resource budgets before wiring modules together. Explicitly describe the adapters and fallback path.
9. **Smallest proof first.** Validate the highest-risk assumption with the smallest reproducible experiment, then implement a vertical slice with real data/control paths. Use mock data only when marked as mock.
10. **Security, accessibility and maintainability are features.** Include threat modeling, boundary checks, logging/observability, failures and degraded-mode behavior proportional to the system.
11. **Performance is empirical.** Record environment, baseline and instrumented delta. No invented speedups, quality scores, frame rates or model performance claims.
12. **Deliver reality, not hype.** State what works, what is simulated, known limitations, what is next and the evidence for each statement.

## Load context efficiently

Read the current user's request and available files/repository first. Open only references for the relevant mode, rather than loading the entire bundle.

| Need | Read |
|---|---|
| Reverse engineering, black-box vs source analysis | `references/01-reverse-engineering.md` |
| Capability extraction, contracts, graph and composability | `references/02-capability-graph.md` |
| Inventing and selecting original concepts | `references/03-concept-synthesis.md` |
| Systems architecture, protocols, AI/data/GPU/3D | `references/04-architecture.md` |
| Execution, repo editing, incremental delivery | `references/05-implementation.md` |
| Testing, experiments, benchmarks, proof of quality | `references/06-verification.md` |
| Domain examples and cross-domain combinations | `references/07-domain-patterns.md` |
| Licensing, privacy, security, deployment protections | `references/08-safety-ownership.md` |
| Findings distilled from the uploaded 3D skill + audit | `references/09-source-learnings.md` |
| Templates | `assets/` |
| Deterministic helpers | `scripts/repo_inventory.py`, `scripts/validate_capabilities.py` |

## End-to-end protocol

### 0. Understand scope, constraints and permissions

Extract: target result; existing system; audience/users; environment; constraints; hardware/performance; available code/data/docs; what is off-limits; intended deployment; quality bar; success criteria. If essential facts are absent, make *explicit, reversible* assumptions and continue safely, asking at most a focused essential question when blocked. Never assume access to accounts, source, GPUs or networks.

Create a brief using `assets/project-brief.md` when the task spans multiple components.

### 1. Reconstruct the actual system

Inventory entrypoints, configuration, modules, dependencies, assets, state stores, data flows, event flows, interfaces, tests, builds, CI, deploys and external services. For websites: distinguish SSR/DOM from canvas, event routing, camera owners, render loops, asset loading and responsive paths. For AI: distinguish prompts, policies, tools, data retrieval, reasoning orchestration, evaluation, persistent state and safety gates. For data/backend: understand schema, contracts, queues, transactions, concurrency and failure recovery.

Build a trace from user action → input → function/state → effect → output → error path. Compare source to production only when access to both is available. Flag uninspected files and unavailable environments. Use `scripts/repo_inventory.py` for a safe file-tree overview, not as a substitute for reading code.

### 2. Extract atomic capabilities

Transform features into reusable primitives. Example: not "3D scrolling portfolio", but `NormalizedTimeline`, `CameraOwnership`, `SplineInterpolation`, `RenderTargetPortal`, `AdaptiveQuality`, `KeyboardFallback`. Not "AI agent demo", but `ToolContract`, `TaskPlanner`, `Verifier`, `ReplayableEventLog`, `HumanApprovalGate`.

For **each** capability create a card (template: `assets/capability-card.md`) documenting:
- ID/name; problem solved; underlying algorithm/equations; role and non-goals.
- Inputs / outputs with data types, coordinate frames, units and serialization.
- State machine / lifecycle; invariants; synchronization/concurrency model.
- Runtime and dependency constraints; performance/resource budget.
- Trust boundaries, authorization and data classification.
- Failure modes, fallback behavior, observability and test hooks.
- Reuse/adapters and compatible capabilities.
- Evidence status (`VERIFIED_SOURCE`, etc.) and source pointers.

### 3. Model capability graph and engineering gaps

Build a **directed graph** with nodes as capabilities and edges `DEPENDS_ON`, `PRODUCES_FOR`, `CONFLICTS_WITH`, `ADAPTS_TO`, `VERIFIED_WITH`, `SUBSTITUTES`. For every proposed composition, trace the end-to-end contract. Separate:
- **Available and verified** modules.
- **Available but unverified** code/features.
- **Theoretical** mechanisms needing implementation.
- **External requirements** such as GPUs, keys, vendor tools or legal permission.

List bottlenecks and missing adapters. Use `assets/capabilities.example.json` as a structural example and `scripts/validate_capabilities.py` for validation.

### 4. Produce alternative concepts, not variations of one skin

Generate concepts by combining mechanisms across domains, not by reskinning UI. Use at least three different system models when discovery is broad: e.g., simulator, operator/copilot, developer infrastructure, creative engine, knowledge environment. For each, specify: user value, originality, required capabilities, interaction flow, implementation sketch, feasibility, highest-risk assumption, minimal experiment, security/privacy, cost, evaluation, and a falsifiable failure condition.

Use [concept synthesis](references/03-concept-synthesis.md). Evaluate usefulness, feasibility, technical distinctiveness, reuse, evidence and risk. Rank explicitly; don't claim numeric scores as objective truth.

### 5. Architecture with end-to-end contracts

Design only as much as needed to implement the selected concept. Specify boundaries, API/events, schemas, canonical state, owner of each mutable resource, data persistence, time semantics, access controls, failure containment, deployment topology, versioning and observability. Avoid circular dependencies and competing owners. Use an architecture decision record (ADR). Domain details: [architecture](references/04-architecture.md).

A feature is complete only if its frontend/UX, backend/logic, persistence (if needed), error path, logging and tests are connected—not just a visual shell with disconnected buttons.

### 6. Execute in verifiable increments

Work sequence: baseline tests → risk spike → thin vertical slice → unit/integration/e2e tests → security/performance checks → documentation → reviewable patch → optional authorized deploy. Prefer small diffs, feature flags and reversible migrations. After every edit inspect actual diff and run relevant checks if tools exist. If a test fails, don't suppress it; diagnose root cause. See [implementation](references/05-implementation.md).

For tasks needing tool actions: act with available tooling rather than producing only an implementation plan, unless the user asked for a plan. Never simulate a repo modification. Avoid uncontrolled recursive agent loops and arbitrary autonomy.

### 7. Verify claims and stop conditions

Test correctness, edge cases, accessibility where applicable, security, failure recovery, performance, operational behavior and reproducibility. Record benchmark environment and before/after. Define stop conditions (e.g., critical tests pass, no unapproved changes, required flows proven, known blockers documented). For risky systems, failure injection and rollback proof matter as much as happy-path demonstrations.

### 8. Deliver a traceable result

For broad engineering work, return in this order:
1. **Goal and boundaries** — what the user asked to achieve.
2. **Verified reality** — observed system and evidence; uncertainty plainly marked.
3. **Extracted capabilities** — mechanics, contracts, reuse candidates.
4. **Combinations and inventions** — novel options, rankings and dependencies.
5. **Chosen solution** — architecture and highest-risk proof.
6. **Actual implementation** — files changed / artifacts built / commands and tests executed (or explicit no-change state).
7. **Validation and risk** — results, limitations, security and performance.
8. **Next highest-leverage step** — a concrete, bounded action.

For small requests, use only the relevant parts; do not impose an eight-section report on simple work. Use factual verbs: "implemented", "observed", "proposed", "not tested", rather than interchangeable optimism.

## Domain translation cheat sheet

| Found mechanism | General engineering abstraction | Unrelated applications |
|---|---|---|
| Scroll progress → camera movement | Input normalization + timeline state + deterministic interpolation | Robotics playback; workflow replay; timeline debugger |
| 3D nested portal | Render target + scene virtualization + context switch | Multi-scale digital twins; nested dashboards; simulation inspector |
| GPU particles | Instanced parallel state update | Spatial data analysis; physics; graph dynamics |
| Mobile quality tiers | Measured feedback controller + graceful degradation | Local inference schedulers; adaptive dashboards |
| 3D scene graph | Typed hierarchical dependency graph | Knowledge graphs; codebase maps; organizational modeling |
| Agent orchestration | State machine + tool protocol + checkpoints | Operations automation; experimentation labs |
| RAG pipeline | Evidence retrieval + ranking + grounded synthesis | Repository intelligence; regulations navigator; knowledge twins |
| CI visual regression | Reproducible measurement + change gate | Model evaluation gates; document verification; release engineering |

These are analogy-to-design starting points, not evidence the source already implemented those applications.

## Definition of done

A deliverable passes only when: requested behavior is reachable; claims are traceable; critical paths and representative edge cases are tested (or limitations stated); known high-severity issues are not hidden; performance is within a specified budget or deviations explained; code and assets have lawful provenance; permissions were respected; and documentation is sufficient for another engineer to reproduce the result.

**Fundamental question:** "Which mechanisms are actually present, what contracts make them reusable, which new combinations are viable, and what test would prove them?"
