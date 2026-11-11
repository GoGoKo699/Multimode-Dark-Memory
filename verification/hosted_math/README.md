# Checking the hosted mathematics

The [workflow](../../.github/workflows/hosted-math.yml) compares every mathematical expression in the exact proposed commit with its actual GitHub rendering. It opens public, commit-pinned pages in a fresh anonymous Chromium context at widths 1440 and 760. All tracked Markdown pages are included: science, learning, references and verification.

The comparison retains operands, subscripts, superscripts, fractions, matrices, relations and labels. Missing expressions, renderer errors, structural differences or overflowing displays fail the check. The artifact contains source inventories, actual DOM captures, screenshots, comparison results and a report binding their hashes to the checked commit and tree.

The collector, checker and representative probe are unchanged copies of the canonical verification tools inspected at revision edaf97f8104704383c4ecffa644aa37171e10955. They require Node.js 18 or later, Python 3.10 or later, Git, Playwright 1.56.1 and MathJax 3.2.1. Install dependencies outside the checkout, then run:

```bash
NODE_PATH=/absolute/dependencies/node_modules node verification/hosted_math/capture_hosted_math.cjs \
  --root /absolute/repository \
  --repository GoGoKo699/Multimode-Dark-Memory \
  --revision FULL_40_CHARACTER_COMMIT \
  --output /absolute/new-empty-evidence-directory
```

A passing automated comparison still requires inspection of screenshots against source, especially substantial proofs, tables and repaired displays. It does not establish scientific correctness or future rendering behavior.

The job uses repository read access, does not persist checkout credentials and does not authenticate the captured browser. Artifacts expire after 14 days; retain necessary review evidence separately.

[Finite verification](../README.md) · [Repository overview](../../README.md)
