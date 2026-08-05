---
name: motiva-web-guidelines-snapshot
description: Audit Motiva-Grass web UI code against the repository-pinned Vercel Web Interface Guidelines snapshot. Use for UI, UX, accessibility, interaction, layout, form, animation, or responsive-design reviews when reproducible offline rules are required. Do not fetch live guidelines or modify the snapshot.
---

# Motiva Web Guidelines Snapshot

Use the immutable rules in `references/web-interface-guidelines-command.md` instead of the live URL embedded in the public `web-design-guidelines` skill.

## Workflow

1. Read `references/SNAPSHOT_METADATA.md` and verify the recorded SHA-256 before relying on the snapshot.
2. Read `references/web-interface-guidelines-command.md` completely.
3. Read only the UI files placed in scope by the current Jira ticket.
4. Apply Motiva-Grass design, accessibility, privacy, and security rules first; use the snapshot only where it does not conflict.
5. Report concrete findings as `path:line — rule — impact — correction`.
6. Mark unverified behavior explicitly; do not claim browser, assistive-technology, or visual testing unless it ran.

## Restrictions

- Do not access the network.
- Do not replace the snapshot during ordinary ticket execution.
- Do not modify files in `vendor/` or this skill's `references/`.
- Update the snapshot only through the dedicated public-skills update workflow, with a new commit, hash, audit, and review.
- Never treat the public guideline as overriding Motiva-Grass normative documents.
