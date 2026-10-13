# 06 — Evidence, evaluation, QA and performance

## Hypothesis-driven engineering
State claim, independent variable, observed outcome, baseline, measurement method and falsification threshold. Example: "Lazy loading a portal scene decreases first-view transferred bytes on mobile without breaking entry interaction." Measure transferred bytes, TTI/LCP and successful entry on representative hardware. Do not replace an experiment with intuition.

## Quality dimensions
| Dimension | Proof to collect |
|---|---|
| Functional | End-to-end scenario and boundary-value cases pass |
| Correctness | Invariants/property tests, determinism where required |
| Reliability | Recovery from timeout, crash, lost connection, duplication, partial failure |
| Security | Permission denials, tenant isolation, injection boundaries, secrets hygiene |
| Performance | Baseline vs candidate, environment and distributions |
| Accessibility | Keyboard, screen reader, focus, reduced motion, contrast, zoom where applicable |
| Data quality | Provenance, missing values, freshness, schema and privacy |
| AI quality | Eval set, hallucination/grounding, task success, cost, latency, tool correctness |
| Ops | Deployment trace, logs, health/alerts, rollback proof |

## Benchmarks
Report: OS, CPU, GPU, RAM, browser/runtime, network profile, input size, configuration, warm-up, repeat count, date, mean/median/p95 as useful. Avoid percent improvements if measurement conditions differ. Track resource use beyond latency: VRAM, draw calls, frame-time distribution, network bytes, CPU, token/cost consumption.

## AI evaluation
Use task-specific golden datasets with provenance, hidden holdouts where appropriate, negative tests, permission violations, malicious retrieved content, tool error injection, non-answerable questions, and regression comparisons against a baseline. Separate accuracy, retrieval relevance, citation fidelity, task completion, latency and cost. Don't let a generative judge be the only validator of sensitive claims; spot-check human-labeled evidence.

## Rendering and simulation QA
At stable states and fixed random seeds: screenshots at controlled viewports; animation progress/keyframe sampling; GPU metrics; asset failure tests; lifecycle leak tests; controls and reduced-motion path. Record deterministic snapshots when possible, but don't freeze dynamic physics into unrealistic assertions. Test real mobile/low-end devices when claims concern them; emulators alone do not prove hardware performance.

## Security verification
Authorization tests should exercise permitted and forbidden identities/resources and stale session/role changes, not only happy paths. Validate all API inputs and outbound URLs. Prompt injection tests should verify instructions from untrusted files/web content cannot cause unauthorized tool actions. Avoid running potentially dangerous scanning against systems without permission.

## Failure injection
Choose representative fault events: network loss mid-write, tool timeout, rate limit, GPU context loss, process crash, duplicate event, invalid schema, stale cache, interrupted deploy, unavailable model, no data. Verify meaningful error, cleanup, safe retry/no retry, and recovery procedure.

## Visual vs actual completeness
For each UI control verify: action changes state; state reaches backend when expected; error is surfaced; refresh preserves required state; permissions enforced; telemetry records outcome. A working animation is not proof the workflow works.

## Evidence ledger
```
Claim | Status | Evidence (file:line or command/test) | Environment | Date | Confidence | Open question
```

## Release gates
A gate should name exact observable criteria, not "professional quality" or "insane performance". Examples:
- required e2e paths pass with expected data;
- no unauthorized access in regression suite;
- no known P0 defects, all P1 dispositions recorded;
- regressions in frame time or p95 latency below chosen threshold;
- recovery from planned failure scenario works;
- docs match implementation;
- required approvals obtained.

If tools are unavailable, state `NOT_RUN` and give runnable commands. Never change status to passed based on code inspection alone.
