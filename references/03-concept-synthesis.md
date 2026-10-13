# 03 — Generating strong, feasible, truly novel concepts

## Aim
Move beyond "same product with different colors". Transform technology knowledge into genuinely new functionality and useful workflows. Avoid novelty inflation: originality may be architectural, interactional, operational or economic; visual novelty alone is insufficient.

## Six generation operators
1. **Transfer** — Move a mechanism across domains. Example: camera keyframes → deterministic time-travel debugging of event-driven workflows.
2. **Compose** — Combine independently useful systems. Example: provenance graph + AI tool executor + replay log → auditable agent engineering laboratory.
3. **Invert** — Reverse the assumed direction. Example: instead of user exploring static analytics, analytics explores anomalies and asks for human inspection.
4. **Constrain** — Invent under a hard budget. Example: high-quality interactive data explorer at 4GB VRAM or fully offline.
5. **Humanize** — Introduce explicit human control, interpretable decisions, accessibility and override mechanisms.
6. **Simulate** — Reproduce the target process in a sandbox before touching the real environment.

## Concept composition process
1. List the top 10 verified mechanisms in the source.
2. List 5 user problems worth solving, ordered by evidence and importance.
3. Generate at least 3 different **system types**; not three designs of the same idea.
4. For each, map graph path: `input → mechanisms → outcome → feedback`.
5. Identify assumptions and unknown dependencies; put the most uncertain one first in the experiment plan.
6. Specify the **wow moment as functionality**: a capability that was previously awkward or impossible, not a particle effect.
7. Describe why the concept would be valuable even with a plain HTML UI.
8. Run a red-team review: what would make it unsafe, untrustworthy, too expensive or technically fake?
9. Select based on transparent criteria and user priorities, then build a measurable proof.

## Concept card
```
Name / one-sentence benefit:
Audience and evidence of need:
What becomes possible (not the UI):
Mechanism combination (graph path):
What is truly new vs existing alternatives:
Input/data requirements and privacy:
Core state & control loop:
Core algorithm and actual computation:
Feasibility / blockers / hardware and costs:
Biggest unproven assumption:
1-2 day or smallest feasible validation experiment:
Acceptance criteria + negative test:
Minimum vertical slice:
Scaling / monetization / operational implications (only if relevant):
```

## Ranking rubric (1–5 each, subjective)
Assign with short explanation, rather than pretend precise measurement.
- User value × 3
- Technical feasibility × 3
- Differentiation × 2
- Reusable leverage × 2
- Evidence readiness × 2
- Maintainability × 2
- Risk/manageability × 2

Total is a **decision aid**, not a scientific metric. If scores tie, prefer the concept with the cheaper decisive experiment or clearer user proof.

## Feasibility gates
- Is all critical functionality implementable with available tools/hardware/permission?
- Is the data real, simulated or unavailable? Label each.
- Does the implementation require real-time inference that cannot fit the latency or VRAM budget?
- Are claims of autonomy bounded by explicit tool permissions and review gates?
- Can the system demonstrate core value even when its immersive visualization is disabled?
- Is there a minimal end-to-end test that falsifies the central claim?

## A/B thought experiments
"Would I still use it if it looked ordinary?" If no, its value may be visual only. "Can we explain exactly how the system reaches each output?" If no, the architecture is insufficiently understood. "Can we safely stop, undo, replay or inspect actions?" If no, it is not yet ready for sensitive actions.

## Example concept families
**Development** — reproducible codebase graph + test impact prediction + sandbox patch validation.
**Agents** — inspectable multi-agent world with checkpoints, cost tracing, permission gates and replay.
**Creative tools** — procedural scene state + render planner + frame/audio pipeline with deterministic revision history.
**Operational twins** — event streams + typed topology + constrained simulations + anomaly explanation.
**Scientific** — simulation kernels + interactive parameter control + calibrated uncertainty and provenance.

Be explicit when a concept requires new components absent from the analyzed sources.
