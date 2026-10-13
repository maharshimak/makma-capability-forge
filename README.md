# makma-capability-forge

- Capability Forge skill package with instructions, templates, references, inventory and capability-graph validation scripts.
- Capability Forge reusable engineering skill/templates and two Python inventory/validation scripts; older package without the extra license artifact.

## Source-only publication

The owner explicitly confirmed ownership and permission to publish candidate source. Copyright remains reserved; no permissive license was invented. Third-party media, data, weights and assets were withheld. This repository documents the available source and its actual limits.

## Setup

Python 3 standard library: python scripts/validate_capabilities.py assets/capabilities.example.json. Inventory only a disposable directory.

## Status

READY



## Known limitations and improvements

- Inventory script may disclose supplied fixture paths; test only disposable synthetic trees. Validator checks structure, not evidence truth.
- Unlisted integration/build/training/browser checks were not run. No paid provider or privileged scripts were executed. Dependencies were not installed; original locks retained when available.

## Verification

- capability graph sample structural validity: PASS
- capability graph malformed root and missing arrays: PASS
- capability graph dangling edge rejection: PASS
- inventory excludes credentials dependencies and Git metadata: PASS
