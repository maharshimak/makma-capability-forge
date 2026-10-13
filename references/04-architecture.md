# 04 — First-principles systems architecture

## Begin with a traceable outcome
Describe one end-to-end use case as an event sequence. Draw **who owns each state and side effect**. Establish constraints (user-visible latency, costs, reliability, privacy, hardware, maintainability) before picking fashionable frameworks.

## Required architecture artifacts
1. **C4-lite diagram:** user, external systems, services, subsystems, data stores, trust boundaries.
2. **Critical sequence(s):** request/input through decisions, computation, storage, response and recovery.
3. **Interfaces:** schema, validation, error codes, units, versioning, time semantics and idempotency.
4. **State model:** source of truth, derived projections, lifecycle, concurrency, garbage collection and migrations.
5. **Safety model:** identity, roles, capabilities/permissions, sensitive data, approval points and rate limits.
6. **Operation model:** health, logs, trace IDs, alerts, budgets, rollback and DR.
7. **Testability:** injected clocks, deterministic RNG, fixtures, fakes, reproducible benchmarks.

## Control-plane vs data-plane
Separate decisions/policies/configuration (control plane) from high-volume work and execution (data plane). Examples: an AI planner chooses an allowed tool call; the tool executor enforces permissions. The render scheduler decides GPU work; the renderer executes it. Avoid coupling policy to UI behavior.

## State ownership
One authority per mutable state domain, or a documented conflict-resolution protocol. Beware:
- Two animation systems both mutating a camera or DOM node.
- UI and backend separately "owning" an agent's workflow status.
- Workers and HTTP handlers writing the same record without transactional discipline.
- An AI planner executing side effects without rechecking current authorization.

Use explicit state transitions with guards and lifecycle cleanup. Where distributed state is unavoidable, document consistency expectations and reconciliation.

## Interface and event design
For every edge specify request/response shapes, semantic version, schema/validation, idempotency keys, auth scope, timeout, retry class, trace context and sample error payload. **Never** retry non-idempotent external actions blindly. Prefer structured error categories, not string matching.

## Latency/resource budgeting
Break total latency into: input/preprocessing + queue wait + retrieval/compute/inference + network + postprocessing/render. Compute memory for models, intermediate tensors, buffers, render targets and caching. On GPU projects budget VRAM and render passes; on agents budget tokens, tool-call fan-out and tail latency; on streaming systems budget backpressure and sustained throughput.

## AI and agent systems
Use a transparent layered design:
```
Request → input validation → identity/policy gate → task/state machine
                                     ↓
                       retrieval / planning / model inference
                                     ↓
                       structured tool proposal / permission check
                                     ↓
                     executor (bounded time, budget, side effects)
                                     ↓
                      verifier / citations / outcome assessment
                                     ↓
                  event log / final answer / human escalation
```
Distinguish *plans*, *approved actions* and *executed actions*. Use schema-validated outputs; checkpoint long-running workflows; store evidence pointers, not fabricated citations. Test prompt-injection-resistant trust boundaries, tool failures, and corrupted retrieval content. Human approval for destructive/external side effects when required. Support cancellation and replay.

For multi-agent systems, define each role's inputs/outputs and explicit ownership. Added agents do not automatically improve quality; compare against a simple single-agent baseline and measure coordination overhead.

## RAG and data systems
Ingestion → format extraction → normalization → chunking → metadata/provenance → indexing → hybrid retrieval → ranking/reranking → context selection → grounded generation → evaluation. Test both retrieval and end-to-end answer quality. Note ACL filtering **before** disclosing chunks to a model; post-filtering citations alone cannot fix an access-control leak. Use real corpus fixtures and record index versions.

For data pipelines, specify late/out-of-order events, duplicate handling, schema evolution, retention, PII minimization, and the reconciliation process.

## Simulation and 3D/GPU systems
Separate:
- world/simulation state (deterministic if possible),
- camera/interaction rig (single ownership),
- renderer/materials/assets (resource lifecycle),
- user-facing semantic controls (accessible DOM or native UI),
- quality feedback loop (LOD/resolution/passes),
- telemetry and error fallback.

Explicitly map world units, coordinate frames, transforms and time steps. Prefer fixed timestep for simulation state and interpolated rendering; clamp runaway delta time. Do not confuse rendered appearance with physically correct simulation. For WebGL, select render loops deliberately; render-on-demand saves energy for idle scenes, continuous rendering may be necessary for active simulations. Portal render targets have real GPU cost. Self-host runtime decoders/textures/fonts where practicable and respect asset licenses.

## Offline/local and constrained hardware
Consider model quantization, CPU fallback, inference chunking, caching, queued workloads, context budgets, memory spilling, batch sizing, progressive streaming and thermal constraints. **Measure** on target hardware and degrade safely; don't claim a 4GB GPU can run every advanced model/workload.

## Architecture alternatives
Before choosing, compare at least two viable designs on (a) complexity, (b) cost, (c) failure isolation, (d) compatibility, (e) extensibility, (f) user-perceived latency. Avoid premature microservices, abstraction layers or new dependencies without a demonstrated need.

## Reusability boundary
Turn mature primitives into packages only after 2+ real consumers or a clear stable contract. Prefer typed, documented interfaces and integration tests to speculative generic frameworks. Module boundaries should follow independent reasons to change, not diagram aesthetics.
