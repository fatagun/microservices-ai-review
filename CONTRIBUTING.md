# Contributing

Thanks for your interest in improving **Microservices AI Review**! 🙌

This project is intentionally lightweight — it's prompt + schema + a small HTML renderer, with no application backend. That makes it easy to contribute to.

## Ground rules

1. **Keep the two checklist files in sync.** `schema/checklist.json` (machine-readable) and `prompts/microservices-ai-review.md` (human-readable) are parallel representations of the same content. Any change to questions, weightings, sections, or maturity drivers must be applied to **both**.
2. **Preserve the evidence-based guarantee.** The assessor must never fabricate evidence or guess. Questions that can't be proven from a repository are reported as gaps — never invented, never asked of the user. Don't add behavior that weakens this.
3. **Keep it economical.** Favor changes that gather evidence once and reuse it. Avoid per-question file reads.

## Common contributions

### Add or edit a checklist question
- Edit the relevant sub-domain in `schema/checklist.json` (`questions[]`, each with `question` + `weightage` of `H`/`M`/`L`).
- Mirror it in `prompts/microservices-ai-review.md` under the same `#### <sub-domain>` block, formatted as `N. <question> *(Weightage: High|Medium|Low)*`.
- Update `meta.subdomains` / `meta.total_questions` in `schema/checklist.json`.

Quick parity check:

```bash
python3 - <<'PY'
import json, re
d = json.load(open("schema/checklist.json"))
md = open("prompts/microservices-ai-review.md").read()
print("schema:", len(d["checklist"]), "sub-domains /",
      sum(len(e["questions"]) for e in d["checklist"]), "questions")
print("prompt:", len(re.findall(r"^#### ", md, re.M)), "sub-domains /",
      len(re.findall(r"\*\(Weightage:", md)), "questions")
PY
```

### Add a stack mapping
Extend the **Capability → signals** table in `.claude/commands/ms-ai-review.md` so the assessor recognizes another ecosystem's equivalent (e.g. a new circuit-breaker or messaging library).

### Improve the report
- Edit `report/template.html` (self-contained: inline CSS + Chart.js via CDN).
- Preview with sample data — no audit run needed:

```bash
python3 report/render.py report/example-results.json report/example-report.html
```

- If you change the data shape, update `schema/report.schema.json` and `report/example-results.json` together.

## Submitting

1. Branch from `main`.
2. Make your change; run the parity check and preview the report if relevant.
3. Open a PR describing what changed and why.

That's it — no build step, no dependencies beyond Python's standard library. 🐍
