# 02 — Capability extraction, contracts and graph algebra

## Extraction method
A feature is a bundle. A **capability** is a mechanism with a stable purpose, contract and constraints. Split bundles until the pieces can be individually tested and recombined without importing the entire original application.

Examples:
- "interactive 3D world" → scene graph, renderer, camera rig, input mapper, interpolation, object picking, LOD/quality controller, resource registry.
- "agent that handles support" → request parser, policy/permission gate, planner, retrieval, tool executor, human-review gate, verifier, event log, escalation.
- "RAG app" → ingestion, parser, chunker, embeddings, lexical retriever, vector retriever, fusion, reranker, context composer, cited synthesis, offline evaluation.
- "real-time dashboard" → event ingestion, stream processing, state projection, aggregation, subscription, visualization, alert policy, backpressure.

## Capability card minimum contract
```
id: unique-stable-name
name:
problem:
algorithm: mechanisms/equations, not brand names
inputs: type, cardinality, units, trust
outputs: type, cardinality, guarantees
state: owner, lifetime, lifecycle, persistence
invariants:
dependencies: internal/external, version constraints
failure_modes: trigger -> detection -> response
budgets: latency, memory, throughput, GPU, cost
security: permissions, data classification
observability: logs, traces, metrics
verification: test cases + observations
provenance: source path, revision, license
confidence: VERIFIED_SOURCE | VERIFIED_RUNTIME | INFERRED | HYPOTHESIS | UNKNOWN | BLOCKED
adapters: how this connects to other capabilities
```

## Directed edges and semantics
- `DEPENDS_ON`: A cannot operate without B.
- `PRODUCES_FOR`: A emits data accepted by B.
- `ADAPTS_TO`: translation layer needed between contracts.
- `CONFLICTS_WITH`: competing state/resource owner, incompatible policy, or simultaneous use impossible.
- `VERIFIED_WITH`: tests/probes that substantiate a capability.
- `SUBSTITUTES`: alternative implementation with sufficiently similar externally visible contract.

A graph should capture **contracts** rather than just names. Two nodes joined on an architecture slide may still be unintegratable in code.

## Composition checklist
1. **Type**: Are input/output schemas compatible? If no, define a versioned adapter.
2. **Semantics**: Same units, coordinate systems, encoding, time zone, identity, null semantics?
3. **Timing**: Polling, push, streaming, batch, request-response, transactional?
4. **State ownership**: Exactly one authoritative writer per controlled resource or explicit arbitration.
5. **Trust**: Does data cross a security boundary? Authenticate and authorize every action.
6. **Resources**: Will combined memory, network, GPU, token/cost and latency exceed budgets?
7. **Failures**: Timeouts, retries, idempotency, partial writes, dead letters, rollback, graceful degradation.
8. **Operations**: Instrument edges so dropped, delayed, duplicated or invalid data is discoverable.
9. **Evidence**: Has the combined path been tested end to end, not just each component separately?

## Compatibility example
`InputProgress` produces normalized `float p ∈ [0, 1]` with timestamp. `CameraRig` consumes timestamped progress in a known coordinate frame. A robotics playback system can reuse the normalized clock, but not necessarily the visual camera transform: translate to the robot's physical units and safety limits. An adapter does not make two systems equivalent; tests must prove the chosen semantics.

## Capability maturity scale
- M0 — idea only (no implementation).
- M1 — proof of concept, synthetic inputs.
- M2 — runnable module with API, meaningful unit tests.
- M3 — integrated and repeatable with real data, failure handling and instrumentation.
- M4 — production-observed with operating history, budgets and security review.
Do not promote maturity based solely on prettier demos or more lines of code.

## Managing the catalog
Use a machine-readable capability graph for larger systems. Sample: `assets/capabilities.example.json`. Run `python scripts/validate_capabilities.py path/to/capabilities.json`. The validator enforces structure, allowed labels, unique IDs, edge targets and minimal evidence but does not prove the code itself works.

## Reuse decisions
Prefer: (a) implement a pure library, (b) expose it behind stable interfaces, (c) build domain-specific adapters, (d) integrate via observability and tests. Reject extraction when it creates a false abstraction, hides incompatible assumptions, or would introduce more maintenance than benefit.
