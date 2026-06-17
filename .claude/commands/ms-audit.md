# /ms-audit — Automated, Evidence-Based Microservices Review

Assess a code repository against the microservices maturity checklist by **inspecting the repo directly** and produce a self-contained HTML report with charts. Works with any stack (Java/Spring, .NET, Python, Node.js, Go, Rust, …). The model does all the work — the user never answers questions.

The checklist lives in `schema/checklist.json` (340 questions, 113 sub-domains, 14 sections). The report contract is `schema/report.schema.json`.

## Input

`$ARGUMENTS` may contain:
- **Target** (required): a local path or a git URL. Clone URLs shallow (`git clone --depth 1`) to a temp dir. Never assess this checklist repo itself.
- **Scope flags** (optional, for cheaper/faster runs):
  - `--quick` → evaluate only **Mandatory** sub-domains (skip Required / Nice-to-have).
  - `--section "<name>"` → evaluate one section only.
  - Default (no flag) → full assessment.

If no target is given, ask once for the path or URL.

## Method — be economical (this matters)

Token cost is dominated by reading files. **Gather evidence once, then answer all questions from that shared context.** Do not search per-question from scratch.

### Phase 1 — Fingerprint (a few cheap reads)
1. List tracked files: `git ls-files` (fallback: `find . -type f` excluding `.git`). This is your file map — most questions are answered from *which files exist*, not their contents.
2. Detect the stack from manifests (read only these): `pom.xml`, `build.gradle*`, `*.csproj`/`*.sln`, `requirements.txt`/`pyproject.toml`/`Pipfile`, `package.json`, `go.mod`, `Cargo.toml`.
3. Read only the **decisive** files, once each: dependency manifest(s), `Dockerfile`(s), CI config (`.github/workflows/*`, `.gitlab-ci.yml`, `Jenkinsfile`, `azure-pipelines.yml`), and the primary app config (`application*.{yml,properties}`, `appsettings*.json`, `settings.py`/`.env*`, `config/*`). Note infra dirs (`k8s/`, `helm/`, `terraform/`, `*.tf`, `manifests/`).

### Phase 2 — One batched signal sweep
Run a **single** broad `grep` pass (one call, many alternation patterns) for capability keywords across the repo, then reuse the hits. Cover: circuit-breaker/retry/timeout libs, service discovery, gateway, tracing/metrics, auth/JWT/mTLS, secrets, messaging/brokers, caching, ORMs/DB, health endpoints, OpenAPI/Swagger, tests. Use the **Capability → signals** map below so the patterns are stack-correct.

### Phase 3 — Answer all questions from the gathered context
Walk `schema/checklist.json` and decide each question from what Phases 1–2 already revealed. Only do a **targeted** follow-up grep when a specific question genuinely hinges on something not yet seen — and cap these.

**Economy rules (hard):**
- Never read a file twice. Never read lockfiles, `node_modules/`, vendored deps, build output, generated code, or large binaries.
- Prefer `git ls-files` + `grep` over reading whole files. Read a file in full only when its contents are decisive.
- Keep total full-file reads modest (aim ≲ 25–35); rely on the file map + grep sweep for the rest.
- Infer the stack once and reuse it. Don't re-derive context between questions.

## Capability → signals (technology-agnostic)

Detect the stack first, then look for that ecosystem's equivalent. Absence across all known equivalents → the capability is missing (No), not unknown.

| Capability | Java/Spring | .NET | Python | Node.js | Go | Platform / language-agnostic |
|---|---|---|---|---|---|---|
| Containerization | `Dockerfile` | `Dockerfile` | `Dockerfile` | `Dockerfile` | `Dockerfile` | OCI image, `.dockerignore` |
| Orchestration | — | — | — | — | — | `k8s/`, Helm, `Deployment`, `kustomization` |
| Probes / health | Actuator `/health` | Health Checks (`AddHealthChecks`) | `/health` route | `/health` route | `/healthz` | k8s `readinessProbe`/`livenessProbe` |
| CI/CD | — | — | — | — | — | `.github/workflows`, GitLab CI, Jenkins, Azure Pipelines |
| Externalized config | `application.yml`, env | `appsettings.json`, env | `pydantic`/env | `dotenv`/env | env, viper | env vars, ConfigMap |
| Service discovery | Eureka, Consul | Steeltoe, Consul | — | — | Consul | k8s Service / DNS |
| Circuit breaker / retry | Resilience4j, Hystrix | Polly | tenacity, pybreaker | opossum, cockatiel | sony/gobreaker | Istio `DestinationRule` |
| API gateway | Spring Cloud Gateway, Zuul | Ocelot, YARP | — | express-gateway | — | Ingress, Istio `Gateway`, Kong, APIM |
| AuthN/AuthZ | Spring Security, JWT | ASP.NET Identity, JWT | OAuthlib, PyJWT | passport, jsonwebtoken | JWT libs | OIDC/OAuth2, API keys |
| mTLS / zero-trust | — | — | — | — | — | Istio `PeerAuthentication`, SPIFFE, cert-manager |
| Secrets | Spring Cloud Vault | — | — | — | — | Vault, sealed-secrets, cloud KMS, k8s Secret |
| Tracing / metrics | Sleuth, Micrometer, OTel | OpenTelemetry .NET | otel-python | otel-js | otel-go | Prometheus, Zipkin/Jaeger, Grafana |
| Messaging / events | spring-kafka, spring-amqp | MassTransit, NServiceBus | kafka-python, pika, celery | kafkajs, amqplib | sarama, watermill | Kafka, RabbitMQ, Pulsar, NATS |
| Caching | Spring Cache, Redis | `IDistributedCache`, Redis | redis-py | ioredis | go-redis | Redis, Memcached |
| Persistence / ORM | JPA/Hibernate | EF Core | SQLAlchemy, Django ORM | Prisma, TypeORM | gorm, sqlc | DB-per-service, migrations |
| API contract | springdoc/Swagger | Swashbuckle | drf-spectacular, FastAPI | swagger-jsdoc | swaggo | OpenAPI/AsyncAPI spec files |
| Testing | JUnit, Pact | xUnit, Pact | pytest, pact | jest, pact | `testing`, pact | contract/regression suites in CI |

## Deciding each answer

For every question assign exactly one, with a confidence (`high`/`medium`/`low`):
- **Yes** — concrete evidence found. Record a real, cited `file:line` or path you actually observed.
- **No** — the relevant artifact class exists but the practice is absent (e.g. k8s manifests present, but no readiness probe).
- **NA** — does not apply to this repo's architecture (e.g. native-mobile questions for a backend-only service).
- **Not determinable from code** — cannot be proven from a repo (team-skill, org-process, live-infra). Report as a gap; exclude from score. **Do not guess and do not ask the user.**

## Evidence-Based Guarantee (non-negotiable)

Zero invented evidence, zero hallucination. These override coverage and score — under-claiming always beats inventing.

- Every Yes/No **must cite real, verifiable evidence** actually observed this run (`file:line` or path). No citation → not a Yes/No.
- **Never fabricate** file names, line numbers, snippets, config keys, dependencies, or tool names.
- **Absence of evidence is never a Yes.** No proof → No or Not-determinable.
- **No inference beyond the code.** Don't assume a practice exists because the framework "usually" provides it or the repo "looks mature." Verify or flag.
- When unsure, lower confidence or mark Not-determinable rather than guess.

## Scoring

- Yes = +5, No = −5, NA = 0. NA and Not-determinable are excluded from a sub-domain's max-possible.
- Weightage multiplier: H = 5, M = 3, L = 1. Weighted score = response × weight.
- Sub-domain / section score, normalized 0–5: `(Σ weighted + max) / (2 × max) × 5`, where `max = Σ(5 × weight)` over scored (Yes/No) questions only.
- Overall = mean of sub-domain scores that have ≥1 scored question.
- Status: ≥4 `✓` Strong · 2–4 `⚠` Needs work · <2 `✗` Critical · no scored questions `n/a`.

## Output — HTML report (data → template)

Keep data and presentation separate so the model never writes HTML.

1. Build a `results.json` object conforming to `schema/report.schema.json`:
   - `meta` (repo, date, commit SHA, detected stack, overall_score)
   - `coverage` + `responses` counts
   - `sections` (all 14 section scores → radar + bar) and `subdomains` (per-sub-domain scores)
   - `findings` — every No (and any low-confidence Yes/No), **each with real cited `evidence`** and a recommendation
   - `gaps` — Not-determinable questions
   - Round displayed scores to one decimal. Mirror `report/example-results.json` exactly.
2. Write it to `report/results.json`.
3. Render the report:
   ```bash
   python3 report/render.py report/results.json report/report.html
   ```
4. Give the user the path to `report.html`, plus a 2–3 line headline (overall score, coverage, top gaps). The report is the deliverable — do not paste the full findings into chat.

The template renders the charts (gauge, doughnut, radar, bar) itself. Never hand-write HTML; only produce JSON and run the renderer.
