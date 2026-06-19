# RoguePlanet

> Defensive research brief and lab notes for a Windows Defender race-condition vulnerability study.

## Status

This repository is maintained as a **defensive vulnerability research artifact**. It is not a public exploitation product, dropper, privilege-escalation kit, or operational tool. Any proof-of-concept material in this repository is intended only for controlled lab validation, patch-awareness education, and responsible remediation planning.

## Purpose

RoguePlanet documents a race-condition class of issue affecting Windows Defender workflows. The professional value of this repository is not the exploitability claim — it is the defensive process:

- identify the affected workflow;
- reproduce safely in an isolated lab;
- collect evidence without targeting third-party systems;
- document affected versions and constraints;
- build a patch-validation checklist;
- turn findings into detection and hardening guidance.

## Public safety boundary

Do **not** use this repository against systems you do not own or administer. Do **not** treat this project as a weaponized tool. If you are validating exposure, use an isolated VM snapshot, do not connect the test host to production networks, and record only the minimum evidence needed for remediation.

## Defensive validation workflow

1. Create a disposable Windows VM snapshot.
2. Record OS build, Defender engine/platform versions, update channel, and patch date.
3. Run only lab-safe validation steps.
4. Capture Defender event logs and relevant timestamps.
5. Revert the VM snapshot after validation.
6. Apply updates and repeat validation to confirm remediation.
7. Document the result as `affected`, `not affected`, `inconclusive`, or `not tested`.

## Recommended report fields

```text
Host type: Lab VM / owned endpoint / authorized test scope
Windows build:
Defender platform version:
Defender engine version:
Security intelligence version:
Patch date:
Validation date:
Result: affected / not affected / inconclusive / not tested
Evidence collected:
Remediation action:
Retest result:
```

## Detection and hardening ideas

- Monitor Defender platform and engine version drift.
- Track failed or suspicious archive/mount operations in endpoint logs.
- Alert on unexpected privileged process creation after removable media or image-mount events.
- Enforce least privilege for local users.
- Keep Defender platform, engine, and intelligence updates current.
- Prefer controlled enterprise update rings with validation snapshots.

## FLLC positioning

This repo belongs in the FLLC portfolio as a **vulnerability research and patch-validation note**, not as an offensive showcase. The public story should be:

> We study vulnerability classes, validate defensive impact in controlled labs, and translate findings into remediation workflows.

## Responsible use

If you believe a vulnerability is unpatched or actively exploitable, follow coordinated disclosure practices and notify the appropriate vendor/security response channel. Do not publish working exploit chains or operational bypass instructions.

## License

See repository license files if present. If no explicit license is present, treat all content as all rights reserved until clarified.
