# 05 — Reliable implementation protocol

## Before touching code
- Re-state precise target behavior and non-goals. Inspect existing branch, tests, runtime and worktree; don't overwrite unrelated changes.
- Identify affected files, public interfaces, migrations, security implications and user-visible regressions.
- Preserve the existing technology stack unless changing it solves a demonstrated blocker.
- For complex tasks, write a small, prioritized implementation plan with verification checkpoints.
- If an audit was requested, remain read-only. For authorized edit tasks, use focused changes. Production deploys, merges, repository deletion/history rewrites and credential updates require their own authority.

## Small risk-first slices
1. **Baseline:** run existing tests/lint/build where possible; record *preexisting* failures.
2. **Proof spike:** isolate one uncertain dependency, GPU capacity, API call, schema behavior or concurrency mechanism; dispose of throwaway code carefully.
3. **Contract:** add typed interface, validation, invariants and expected failure mode.
4. **Core:** implement deterministic/pure logic first, keep external side effects behind interfaces.
5. **Vertical integration:** connect user action or input to logic, output, persistence and observable result.
6. **Edge cases:** corrupted input, empty data, cancellation, retries, missing permission, slow/unavailable service, concurrent requests.
7. **Telemetry:** error classification, correlation IDs, key metrics, privacy-conscious logs.
8. **Proof:** unit/integration/e2e/security/performance tests appropriate to scope.
9. **Review:** inspect diff, architecture trade-offs, docs and dependency impacts; report exact changed paths.
10. **Release:** preview/staging with smoke test; authorized deploy and rollback rehearsal where available.

## Reliability patterns
- Use explicit state machines for complex workflows rather than unstructured booleans.
- Represent cancellation with clear cleanup; prevent orphaned jobs and GPU allocations.
- External side effects: authorize at execution time; record idempotency keys, result and error.
- Migrations: backwards-compatible stages, reversible plan, backup validation when required.
- Concurrency: define consistency guarantees and test races/deadlocks; avoid silent lost updates.
- Queue consumers: visibility timeouts, retry budget, poison-message handling and dead letter queues.
- File/assets: atomic write/rename, checksums or content addressing, cleanup on failure.
- UI controls: meaningful disabled/loading/empty/error states; no controls that only pretend to work.
- Renderer: dispose GPU resources, remove listeners, avoid updating React state every frame for geometry, isolate frame ownership.

## Handling large repos
Create a dependency-aware worklist and avoid broad refactors when tests are weak. Group commits by coherent behavior. Run unit tests after local changes, integration tests after cross-module changes and system tests before release. Don't claim *all repos are fixed* when only a subset was inspected.

## Testing ladder
1. Pure algorithm tests for key transformations/invariants.
2. Contract/schema tests at boundaries.
3. Integration tests with representative fixtures and injected failures.
4. End-to-end journeys with browser/CLI/API where relevant.
5. Security checks and dependency/license scans proportional to exposure.
6. Performance benchmark with named environment, warm-up, sample count and baseline.
7. Post-deploy smoke/monitoring only when deployment was actually authorized and performed.

## Do not do these
- Remove a failing test instead of fixing the implementation.
- Add excessive abstraction "for future scale" with no consumer.
- Install packages or bring in cloud services where an existing primitive suffices.
- Introduce arbitrary retry loops or surprise persistent automations.
- Replace data with invented metrics, placeholder handlers or fake integrations while describing them as complete.
- Delete an existing feature to satisfy a new snapshot test.
- Move secrets from environment variables into source/configuration.

## Completion record
Use `assets/completion-report.md`. Record exactly what was implemented; commands actually run, results, what remains unverified, expected operational changes, upgrade notes and rollback route. For patches, show concise diff/file references.
