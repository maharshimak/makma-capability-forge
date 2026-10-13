# MAK'MA Capability Forge — Quick start

## Contents
- `SKILL.md` — portable Agent Skills entrypoint (YAML frontmatter and instructions).
- `references/` — nine technical playbooks, including explicit lessons from the supplied 3D skill and portfolio audit.
- `assets/MASTER_PROMPT.md` — standalone copy/paste master prompt for any assistant.
- `assets/` — capability, architecture, experiment, project brief and completion templates.
- `scripts/repo_inventory.py` — deterministic, read-only repository metadata inventory.
- `scripts/validate_capabilities.py` — capability graph structural validator.

## Three ways to use

**A. In a tool supporting Agent Skills**
Extract the skill archive and copy the entire `makma-capability-forge` folder to the skills directory supported by your tool. The important entrypoint is `makma-capability-forge/SKILL.md`. Reference paths are relative, so keep the entire folder. Invoke it by describing a reverse-engineering, invention or system-build task, or by explicitly naming the skill.

**B. In a regular AI chat without skill support**
Open `MAKMA_UNIVERSAL_MASTER_PROMPT.md` and paste the whole prompt; complete the `PROJECT INPUT` section for your actual task. If you want answers grounded in a repository, attach the code/relevant reports or connect the repository. Pasting the prompt alone does not grant source access.

**C. As an IDE/repository instruction**
Link or copy the entrypoint methodology into your IDE's custom instructions/project rules (e.g. `AGENTS.md` when supported), and leave the detailed references accessible by file path. Do not assume every client automatically discovers `.skill` archives.

## Example invocations

**Extract capabilities from existing software**
> Use MAK'MA Capability Forge in REVERSE + MAP mode. Read this repository deeply, identify its real algorithms, state machines, data flows, test coverage and limits. Derive reusable capability cards and suggest 5 non-visual applications. Read-only: do not edit, push or deploy.

**Invent a completely new system**
> Use MAK'MA Capability Forge in INVENT + ARCHITECT mode. Combine the verified capabilities of my engine and agent toolkit to generate 5 technically distinct original concepts. Rank by useful novelty, feasibility and hardware cost. Choose one and specify a falsifiable prototype.

**Build a new high-quality product**
> Use MAK'MA Capability Forge in BUILD mode. Inspect the current repo, preserve functionality, implement the selected capability as a real end-to-end vertical slice, add tests and failure handling, and report which checks were actually run. Do not push, merge or deploy without my separate authorization.

**Audit and strengthen an existing product**
> Use MAK'MA Capability Forge in AUDIT + EVOLVE mode. Establish an evidence-based baseline and rank issues by reproducible impact. Prepare focused patches and regression tests for actual defects, measure outcomes, and avoid replacing the product with a new aesthetic.

## Local scripts

```bash
python scripts/repo_inventory.py /path/to/project --output inventory.json
python scripts/validate_capabilities.py assets/capabilities.example.json
```

Scripts are standard-library Python and require no API keys. The inventory reads file names and sizes only (not source contents); it is not a security scan or a substitute for code review. The validator verifies JSON shape, not truth of engineering claims.

## Important boundaries
The skill supplies instructions and structure, **not** new permissions, repo access, autonomous background execution, GPUs, API keys or a guarantee of flawless output. Verify licenses of third-party materials independently. Its 3D case study is sourced to user-provided documents, not re-tested live in this package.
