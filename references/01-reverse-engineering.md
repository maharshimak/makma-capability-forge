# 01 — Evidence-led reverse engineering

## Objective
Recover the true behavior, runtime mechanisms, boundaries and provenance of an unfamiliar system without confusing appearance, intent, source code or deployment state.

## Evidence taxonomy
- `VERIFIED_SOURCE`: directly visible in an inspected file/commit/config at a cited path and revision. Means the code says X, **not** that X runs in production.
- `VERIFIED_RUNTIME`: observed with explicit environment, version, action and reproducible result.
- `INFERRED`: supported by multiple facts, but not directly measured; explain reasoning and what could disprove it.
- `HYPOTHESIS`: plausible untested mechanism or expectation; identify proof needed.
- `UNKNOWN`: no evidence; don't fill with a confident narrative.
- `BLOCKED`: inspection/test attempted but unavailable; include blocker and alternative.

## Reconnaissance order
1. Inventory root folders, package manifests, lockfiles, CI, secrets *filenames only*, README, docs, deployment config, commit branches/tags.
2. Find executable entry points: framework init, router, dependency injection, app boot, tasks/cron, workers, edge functions, service launch.
3. Build a dependency and **control flow map**. Ask: who calls whom, what state changes, where data originates, when effects occur?
4. Build a **data lineage map**: source → transformation → persistence → retrieval → display/decision; trace schema and trust boundaries.
5. Model state and timing: event ordering; retries; transactions; locks; queues; lifecycle; rendering frame updates; network latency.
6. Inspect assets: provenance, size, license, runtime hosts and caching, and whether compiled artifacts differ from source.
7. Compare docs/claims against code and tests; label stale or unverified features.
8. If permitted, run baseline builds/tests and an isolated probe. Record commands, outputs, versions, hardware and date.
9. Create a source-to-behavior map. Read actual implementation before citing functionality from a label or filename.
10. Preserve a snapshot of findings and update it when evidence changes.

## Cross-cutting audit tracks
| Track | Questions |
|---|---|
| Product | Which journeys actually work end to end? Which links/buttons are dead? |
| Architecture | Where is canonical state? Which dependencies are cyclic or duplicated? |
| Correctness | What are invariants and counterexamples? Tests for empty, malformed, concurrent and large input? |
| Security | Identity, authorization, data boundaries, secret handling, supply chain, SSRF/injection? |
| Performance | CPU/GPU/memory/network/query costs, lazy loading, caching, budget and baseline? |
| Accessibility | Keyboard, screen reader, focus, motion, contrast, zoom, nonvisual alternative? |
| Ops | Builds, deploy provenance, rollback, health checks, alerting, incident playbook? |
| Provenance | Ownership and license for code, artwork, training data and assets? |

## Useful reverse-engineering representations
- **Component graph:** module → dependency, with boundary labels.
- **Sequence trace:** user event → front end → API → authorization → service → data store → output.
- **State transition table:** state, trigger, guard, action, next state, rollback.
- **Timing diagram:** concurrent writers, request/response, task queue, render cycle.
- **Resource profile:** asset bytes, initialization cost, heap, query count, draw calls, GPU/CPU time.
- **Behavior-to-source index:** feature, source file:line, runtime evidence, uncertainty.

## Reverse engineering a production website/3D engine
Determine whether rendering is server-side, static or client-only. Identify DOM vs canvas responsibility; scroll source(s), normalized time, camera owner(s), animation engine, render loop, renderer settings, asset loaders, portals/render-to-texture, shaders, fonts, interaction and fallbacks. Check mobile/desktop at multiple widths, reduced-motion behavior, keyboard paths, canvas failure, network errors. Don't assume a visually identical screenshot implies equivalent accessibility or data flow.

## Reverse engineering an AI application
Distinguish: actual model call; retrieval method and corpus; prompt templates; deterministic business rules; tools and permission scopes; human confirmation; checkpoints; persistent memory; external side effects; eval data; hallucination controls; observability. Use recorded traces to reconstruct failure rather than accepting marketing diagrams.

## Reverse engineering an unavailable source (black-box)
Treat black-box traces as behavioral evidence, not source proof. Generate controlled test cases, observe I/O, timing and error modes, infer only externally supported invariants. Avoid bypassing authorization, protections, licensing, or access constraints. Prefer documentation or permission to inspect source.

## Output template
```
System and revision:
Access and exclusions:
Topology / entrypoint:
Control flow:
State and data owners:
External dependencies and trust boundaries:
Observed journeys:
Source-to-feature evidence table:
Defects by severity + reproduction:
Unknowns/blockers:
Reusable primitives:
Minimal experiments to verify disputed claims:
```

## Priority classification
- P0: immediate exploit, severe data loss/exposure, unrecoverable corruption.
- P1: material vulnerability, broken core path, systemic reliability failure.
- P2: substantial performance, correctness or accessibility degradation.
- P3: localized polish, maintainability or lower-impact issue.
Always justify severity with impact, reachability and evidence; don't automatically call every security concern critical.
