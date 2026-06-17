#!/usr/bin/env python3
"""Render a self-contained HTML report from /ms-audit results.

Usage:
    python3 report/render.py <results.json> [output.html]

Injects the evidence-based results JSON into report/template.html at the
__AUDIT_DATA__ placeholder and writes a standalone report.html. The template
is presentation-only — this step adds nothing to the findings; it only places
the model's data into the page. Stdlib only, no dependencies.
"""
import json
import sys
from pathlib import Path

PLACEHOLDER = "__AUDIT_DATA__"


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    results_path = Path(argv[1])
    out_path = Path(argv[2]) if len(argv) > 2 else results_path.with_name("report.html")
    template_path = Path(__file__).with_name("template.html")

    # Validate the data parses as JSON before injecting.
    data = json.loads(results_path.read_text(encoding="utf-8"))
    payload = json.dumps(data, ensure_ascii=False)
    # Neutralize sequences that could break out of the <script type="application/json"> block.
    payload = payload.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")

    template = template_path.read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        print(f"error: placeholder {PLACEHOLDER} not found in {template_path}", file=sys.stderr)
        return 2
    html = template.replace(PLACEHOLDER, payload)
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
