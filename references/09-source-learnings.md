# 09 — Case study: engineering lessons from the provided source files

This chapter is explicitly grounded in two user-provided inputs reviewed on **2026-10-13**:
1. `immersive-3d-website.skill` — contains `SKILL.md`, seven engineering reference documents and two JavaScript inspection/probe scripts.
2. `portfolio-reverse-engineering-report.md` — detailed read-only audit titled "Portfolio Reverse-Engineering Report — maharshipatel-portfolio.vercel.app", dated 2026-10-13. File line numbers below reference that report's lines as supplied, not independent re-verification by this new skill.

**Evidence boundary:** the audit's claim labels (VERIFIED, BROKEN, UNVERIFIED) were assigned by its original author. This skill has read the report; it has **not independently rerun** the original benchmark, GitHub commands, browser probes or deployments. Do not mislabel inherited observations as newly verified in a different project.

## A. Confirmed *in the provided report* — what exists in that specific implementation
- Production was described as a Next.js/React Three Fiber/Three.js single-canvas scroll experience with camera choreography, three zustand stores, a scene graph, portals, GLB models and a theme switcher. (Report §§A-B, lines 11–15, 40–65.)
- Scroll progress controlled camera/objects via damped interpolation, keyframes and scoped/unscoped GSAP interactions; portals used `MeshPortalMaterial`, timeline used a Catmull–Rom spline; text used troika SDF. (Report §§C,E,F, lines 69–87, 112–139.)
- The original rendering design's geometry and visuals were largely inherited from a third-party repo with no discovered license; 3D assets required attribution. (Report lines 13, 96–105, 200–205.)
- Identified issues included 3D-only content with inaccessible links, scroll/camera contention, broken phone/mail mobile SVGs, third-party runtime asset dependencies, font fallback blocked by CSP and always-on portal rendering. (Report lines 16, 199–220.)
- A newer dependency fix in `main` was reported as not deployed at the audit date; repo code and production deploy were distinct. (Report lines 12, 24–35, 143–153.)
- The audit measured one specific Chrome-class RTX 3050 environment (FCP/LCP/draw calls/FPS) and explicitly marked lower-end GPU results unverified. **Do not generalize those numbers to every device or present them as independently retested.** (Report line 15.)
- A proposed modular future architecture separated semantic content, asset registry, scroll timeline, camera ownership, chapters, shader FX, adaptive quality and QA. **That was a proposal, not implemented functionality.** (Report §§J–L, lines 227–295.)

## B. Extracted reusable mechanisms
| Source feature | Mechanism to abstract | Real engineering invariant |
|---|---|---|
| Scroll choreography | Time normalization + deterministic keyframe evaluation | Input progress has defined range/time semantics |
| Camera movement | Single owner + interpolation + transition arbitration | No competing writes without handoff |
| Portals | Lazy scene/render-target lifecycle | Allocate/render only when needed; dispose cleanly |
| 3D worlds | Scene graph + coordinate transformations | Explicit coordinate system and units |
| Day/night transition | Shared state and visual uniform mapping | UI and GPU observe coherent state |
| Adaptive quality proposal | Feedback controller with thresholds | Requires actual measurements to activate |
| 3D typography | Asset pipeline + glyph coverage | Missing assets/glyphs must have fallback |
| Mobile accessibility defect | Semantic control layer | Every critical action has a keyboard/assistive path |
| CI advisory gap | Source-to-deploy traceability | Patch isn't done until running artifact is verified |
| Provenance issue | Rights/attribution registry | Copy rights and assets are verified before reuse |

## C. What the sources do NOT establish
- They do not provide a completed general AI operating system, autonomous agent world, digital twin, code intelligence platform or film generator.
- They do not demonstrate physical robot control, reliable LLM agency, production ML retrieval benchmarks or unrestricted performance at any hardware tier.
- They do not grant licenses for the upstream website or third-party assets.
- They do not prove that any present-day version/deployment still matches the October 13 report after future changes.

## D. How to reuse the learnings without copying a site
1. Isolate the underlying math/API/state semantics from source-specific visual implementation.
2. Translate into a capability card; derive pure logic tests.
3. Implement a clean original module or licensed integration.
4. Prove it on one unrelated application (e.g., simulation replay, workflow debugger, code graph), not just a website copy.
5. Benchmark composition overhead and failure modes.
6. Attribute any retained third-party implementations/assets appropriately.

## E. High-leverage lessons
- Multiple systems writing the same camera/state is an *ownership failure*, transferable to concurrency and agent orchestration.
- Nested scroll containers fighting for interaction are an *input-arbitration failure*, transferable to workflow routing.
- GPU portals rendering unnecessarily are a *resource scheduling failure*, transferable to model inference scheduling.
- A client-only canvas masking content is a *separation-of-concerns failure*, transferable to inaccessible agent dashboards.
- Deployed old dependencies despite patched source is a *release provenance failure*, transferable to model and infrastructure updates.

These are analogies for designing new systems. An analogy is not proof that the new system works.
