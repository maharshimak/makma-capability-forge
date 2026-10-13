# 07 — Transferable mechanisms across domains

These examples propose reuses of general mechanisms. They are **not** claims that the user's uploaded portfolio has implemented them.

## 3D and GPU → systems engineering
- Scene graph ↔ dependency graph: hierarchy, transforms, traversal, picking/selection. Caveat: real dependencies may be cyclic; a scene tree cannot directly represent every graph without extra linking.
- Render-to-texture ↔ virtualization: show a small live preview of a complex subsystem; activate full fidelity only when needed. Caveat: independently executing worlds still incur computation if not suspended.
- Frame-rate-independent damped movement ↔ stable feedback smoothing: sensor dashboards, virtual cameras, event visualizers. Caveat: physical control loops need system-identification/safety validation; visual damping is not a robotics controller.
- Adaptive quality ↔ budget-based scheduler: choose GPU effect quality, LLM model size, number of parallel tasks based on measured throughput/latency. Caveat: a quality tier policy is not a complete fair scheduler.
- GPU instancing ↔ parallel structured computation: swarms, large graph node fields, particle physics, point clouds. Caveat: algorithm/data layout and GPU occupancy determine speed.
- Event/scroll timeline ↔ deterministic replay: project histories, monitoring incidents, robot simulations; decouple event time from wall time.

## Agents + verification → inspectable automation
`Intent → plan → policy gate → tool call → observed result → verifier → checkpoint`. Add a replayable event log and explicit state transitions. This creates explainability about what was **executed**, not access to a model's hidden internal reasoning. Handle retries, isolation and irreversible actions.

## RAG + source lineage → trusted engineering search
Parse docs/code → lexical + semantic retrieval → reranking → evidence links → grounded synthesis. Integrate with AST/graph traversal for code navigation; add permission filtering to search, not only answer text. Evaluate retrieval separately from generation.

## Digital twin + events + constraints
Real telemetry → typed domain events → state projection → graph/model → sandbox scenario runner → comparison against actual observed behavior. Label simulated predictions clearly. A digital twin without data synchronization is a simulation prototype, not a continuously updated twin.

## Creative AI systems
Timeline/storyboard/state graph → job queue → constrained asset generator → render/composite → inspectable lineage → revision controls. Include explicit seed/configuration, model version, asset rights, failure recovery and GPU/VRAM scheduling; support partial outputs and resume.

## Autonomous experimentation
Hypothesis → generated experiment configuration → sandbox execution → measured observations → statistical comparison → ranking → human decision. Restrict side effects and preserve experiment lineage. Define hard budgets and stop conditions to prevent expensive uncontrolled loops.

## Code intelligence
Repository parse (AST/types/dep graph) → change-impact map → risk analysis → propose test → isolated patch → CI verification. Avoid claiming semantic correctness from static similarity; dynamic tests and human review remain necessary.

## Concept combinations to test
1. **Agent simulation observatory:** typed actor state + event replay + knowledge graph + 3D/2D explorer + test harness. Novel value: debug decisions and inter-agent coordination. Required new components: event log/agent runtime.
2. **Repository world model:** AST/dep graph + spatial graph layout + embeddings/search + test impact tracer. Novel value: navigate behavior from architecture to code line. Requires static analyzer and trace capture.
3. **Adaptive local AI studio:** GPU budget controller + task queue + model pipeline + deterministic storyboard + asset cache. Novel value: reliable creation under constrained hardware. Requires actual video/image models and workers.
4. **Operational digital twin:** event stream + simulation kernel + visual exploration + anomaly explanations + rollbackable hypotheses. Requires domain model and real telemetry.
5. **Evidence-first research environment:** retrieval + claim ledger + experiment runner + provenance graph. Novel value: every answer tied to observations and reproducible tests.

## Anti-patterns
- 3D "neural network" as a purely decorative backdrop while claimed as an operational model.
- "Autonomous" agent with no actual tool execution or checkpoints.
- "Production ready" app dependent on unaudited demo keys or untested local-only assumptions.
- Complex multi-agent swarm when a deterministic script or simple pipeline suffices.
- Arbitrary scale claims without capacity measurements.
