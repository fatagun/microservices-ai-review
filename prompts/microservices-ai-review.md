# Microservices Review Checklist

You are conducting a structured Microservices Implementation Review. Your role is to assess how well a project follows microservices design principles, architecture patterns, deployment practices, API standards, and team skill coverage.

## How to Use This Checklist

This is the question catalog for the assessment. Each question is answered by inspecting the target repository (see `/ms-ai-review`), not by manual data entry. For every question, determine a response:

- **Yes** — Evidence found in the repo and the practice is being followed
- **No** — The relevant artifact exists but the practice is absent
- **NA** — Not applicable to this repository's architecture or context

Answers that cannot be proven from code (e.g. team-skill or live-infra questions) are reported as gaps and excluded from the score — never guessed, and never solicited from the user.

### Scoring

Each question carries a **Weightage** (H / M / L) and produces a **Response Score**:

| Response | Score |
|---|---|
| Yes | +5 |
| No | −5 |
| NA | 0 |

Weighted score per question = Response Score × Weightage Points (H=5, M=3, L=1)

Domain scores are normalized to a **0–5 scale**. Overall maturity is the average across all domains.

### Maturity Drivers

- **Mandatory** — Must be implemented; directly impacts core microservices maturity
- **Required** — Should be implemented; important for operational readiness
- **Nice to have** — Recommended; enhances maturity but not critical

---

## 1. Microservices Implementation

### 1.1. Microservices foundation

#### 12 Factor Principles
**Maturity Driver:** Mandatory

**Description:**
12 factor principles when applied to application development  ensures that apps are basically isolated processes that :
Have a clean contract with the underlying operating system, offering maximum portability between execution environments;
Are suitable for deployment on modern cloud platforms, obviating the need for servers and systems administration;
Minimize divergence between development and production, enabling continuous deployment for maximum agility;
And can scale up without significant changes to tooling, architecture, or development practices.

**Best Practices:**
I. Codebase - One codebase tracked in revision control, many deploys
II. Dependencies - Explicitly declare and isolate dependencies
III. Config - Store config in the environment
IV. Backing services - Treat backing services as attached resources
V. Build, release, run - Strictly separate build and run stages
VI. Processes - Execute the app as one or more stateless processes
VII. Port binding - Export services via port binding
VIII. Concurrency - Scale out via the process model
IX. Disposability - Maximize robustness with fast startup and graceful shutdown
X. Dev/prod parity - Keep development, staging, and production as similar as possible
XI. Logs - Treat logs as event streams
XII. Admin processes - Run admin/management tasks as one-off processes

**Reference:** https://12factor.net/

**Questions:**

1. Does your infrastructure support centralized logging by aggregating log from multiple processes? *(Weightage: Medium)*
2. Does environments similarity exist between dev, test and production? *(Weightage: High)*
3. Does you app support graceful shutdown by handling SIGTERM and SIGKILL? *(Weightage: Medium)*
4. Does you app support fast startup in few seconds? *(Weightage: High)*
5. Does your infrastructure support rapid elasticity through horizontal scaling? *(Weightage: High)*
6. Is your app stateless and does not depend on any specific affinity for subsequent processesing of requests? *(Weightage: Medium)*
7. Is application CI/CD pipeline confirming to separate build, release and run stages. Build stages would bundle the application and a release stage would deploy the app with enviroment specific config. *(Weightage: High)*
8. Do you see environment specific configuration maintained as a separate repository and being injected into application during deployment process. *(Weightage: High)*
9. Do you see separation between application code and configuration. *(Weightage: High)*
10. Do you see evidence of dependencies being isolated, distributed and eventually bundled when building the application? Example maven or package manager based application builds. *(Weightage: Medium)*
11. Do you see that same code base moves up the environment chain as part of deployment process? *(Weightage: High)*
12. Do you see one code base per microservice? *(Weightage: High)*
13. Do you see several clear evidence of 12 factor principles being applied? *(Weightage: High)*

---

#### Modern Tool Chain (CI/CD)
**Maturity Driver:** Mandatory

**Description:**
Modern set of tool chain ensure that your changes are automatically deployed across environment quickly and predictably.

**Best Practices:**
Per Microservices Ci/CD
Devops Automation Integrated Tool set implemented across all aspects of Continuous Business planning, Collaborative development, Continuous Integration, Continuous Release & Deployment, Continuous Testing, Continuous Monitoring, Continuous feedback and Optimization

**Questions:**

1. Have you implemented SRE (Site Reliability Enginnering) practices within your application? *(Weightage: Low)*
2. Do you quantitively measure effectiveness of your CI/CD pipelines and generate matrix that helps your continuously improve development and Operational KPIs. *(Weightage: Medium)*
3. Have you implemented continues business monitoring for Business KPIs? *(Weightage: High)*
4. Have you implemented continues monitoring practices for monitoring/alerting of application, interfaces and infrastructure components. *(Weightage: High)*
5. Does your pipeline support automated security testing within your CI/CD pipelines? *(Weightage: Low)*
6. Does your pipeline support automated performance testing within your CI/CD pipelines? *(Weightage: Low)*
7. Does your pipeline support Automated and Continuous functional testing within your CI/CD pipelines? *(Weightage: High)*
8. Do you have automated quality gates within different stages of your deployment on an automated CI/CD pipeline? *(Weightage: Medium)*
9. Are your deployments automated with CI/CD pipeline? *(Weightage: High)*
10. Have you implemented per microservice CI/CD? *(Weightage: High)*

---

#### Elastic Infrastructure available
**Maturity Driver:** Mandatory

**Description:**
Ability to increase or decrease infrastructure on demand to support business spikes

**Best Practices:**
Cloud deployments (Public, Private, Hybrid)

**Questions:**

1. Does your application infrastructure support multi-cloud deployments? *(Weightage: High)*
2. Do you have fine grained controls over automated scaling parameters such as memory, CPU? *(Weightage: Medium)*
3. Does your infrastructure support automated scalability? *(Weightage: High)*
4. Do you have the ability to rapidly and consistently scale up/down your microservices application infrastcuture based on business needs? *(Weightage: High)*
5. Are you microservices infrastructure backend by cloud? *(Weightage: High)*

---

#### Cloud Native Patterns
**Maturity Driver:** Mandatory

**Description:**
Multi Cloud application development. 
Microservices architecture processes and patterns are fully established and Continously Optimizing.

**Best Practices:**
Microservices (Business Microservices, Integration/Adapter Microservices, Caching, Polyglot)
12 factor abstraction, Restful APIs
Circuit breaker
Service Registery and discovery
Modern Web Architecture 
Self-healing
Backend for FrontEnd 
Single Page Application
Centralized Logging
Distributed Tracing
API Gateway
Event Driven
Caching
Polyglot

**Questions:**

1. Are eligible cloud native patterns have been implemented and being optimized specific to client scenario. Few patterns have been tweaked to client needs or available infrastructure. *(Weightage: High)*
2. Are microservices appropriately secured when being accessed by other microservices within the same application, internal applications within the enterprise or external applications. *(Weightage: Medium)*
3. Are interfaces and capabilities well defined, documented and contuniously updated *(Weightage: Low)*
4. Do microservices communicate with each other as network APIs? *(Weightage: High)*
5. Are cross cutting concerns and common capabilities implemented as separated adapter microservices and not duplicated across multiple microservices? *(Weightage: Medium)*
6. Are your microservices decomposed as business capabilities leveraging domain driven design. *(Weightage: High)*

---

#### Microservices Governance
**Maturity Driver:** Required

**Description:**
Decentralized Governance

**Best Practices:**
Independent services owned by smaller teams
Smaller Multifunctional devops teams
Polygolt programming
Contract driven development with backward compatibility
Services catalog

**Questions:**

1. Is your infrastructure capabilities support the speed and expectations business and enterprise transformation in terms of agility, speed to market. *(Weightage: High)*
2. Do you see yourself as a multi functional team providing full stack coverage for your supported microservices? *(Weightage: Medium)*
3. Are your microservices owned and supported by smaller teams? *(Weightage: High)*
4. Is there an enterprise service catalog? *(Weightage: Medium)*
5. Did you had a choice of runtime and persistence capabilities that enabled you to select the right technology for the right use case? *(Weightage: High)*

---

#### Containerization
**Maturity Driver:** Mandatory

**Description:**
Package each microservice as an immutable, self-contained container image for portability and consistent runtime behavior across environments.

**Best Practices:**
Use minimal base images, run as a non-root user, and build with multi-stage builds. Version images and store them in a registry. Keep state and config out of the image. Scan images for vulnerabilities before promotion.

**Reference:** https://microservices.io/patterns/deployment/service-per-container.html

**Questions:**

1. Are your microservices packaged as immutable container images? *(Weightage: High)*
2. Do your container images follow best practices such as minimal base image, non-root user, and multi-stage builds? *(Weightage: Medium)*
3. Are container images versioned and stored in a container registry? *(Weightage: High)*
4. Are images scanned for vulnerabilities before being promoted to higher environments? *(Weightage: High)*
5. Do containers externalize all state and configuration rather than baking it into the image? *(Weightage: Medium)*

---

#### Container Orchestration
**Maturity Driver:** Mandatory

**Description:**
Run and manage containerized microservices on an orchestration platform that handles scheduling, scaling, self-healing, and isolation.

**Best Practices:**
Leverage Kubernetes (or equivalent). Define resource requests/limits per service, configure horizontal autoscaling, enforce workload security context (least privilege), and isolate environments/teams with namespaces.

**Reference:** https://kubernetes.io/docs/concepts/

**Questions:**

1. Are your microservices deployed and managed by a container orchestration platform such as Kubernetes? *(Weightage: High)*
2. Do you define resource requests and limits (CPU/memory) for each service? *(Weightage: High)*
3. Have you configured horizontal autoscaling based on load? *(Weightage: Medium)*
4. Are workload/pod security policies such as least privilege and security context enforced? *(Weightage: Medium)*
5. Do you use namespaces or equivalent isolation between environments and teams? *(Weightage: Medium)*

---

#### GitOps and Infrastructure as Code
**Maturity Driver:** Required

**Description:**
Define infrastructure declaratively and drive deployments from version control so the desired state is auditable and reproducible.

**Best Practices:**
Define infrastructure as code (Terraform, Helm, Kustomize). Drive deployment via GitOps where Git is the source of truth (ArgoCD, Flux). Detect and reconcile drift automatically. Peer-review and version control all infra changes.

**Reference:** https://opengitops.dev/

**Questions:**

1. Is your infrastructure defined declaratively as code, for example with Terraform, Helm, or Kustomize? *(Weightage: High)*
2. Is deployment driven by a GitOps workflow where Git is the source of truth, for example ArgoCD or Flux? *(Weightage: Medium)*
3. Can you detect and reconcile configuration drift automatically? *(Weightage: Medium)*
4. Are infrastructure changes peer-reviewed and version controlled? *(Weightage: Medium)*

---

#### Supply Chain Security
**Maturity Driver:** Required

**Description:**
Secure the build-and-release supply chain so that what is deployed is trusted, traceable, and free of known vulnerabilities.

**Best Practices:**
Generate a Software Bill of Materials (SBOM). Scan dependencies and images for known vulnerabilities in CI. Sign and verify images before deployment. Pin and control the provenance of build dependencies and base images.

**Reference:** https://slsa.dev/

**Questions:**

1. Do you generate and track a Software Bill of Materials (SBOM) for your services? *(Weightage: Medium)*
2. Are third-party dependencies scanned for known vulnerabilities in your CI pipeline? *(Weightage: High)*
3. Are container images signed and verified before deployment? *(Weightage: Medium)*
4. Do you pin and control the provenance of build dependencies and base images? *(Weightage: Medium)*

---

## 2. Microservices Architecture Tenants

### 2.1. Microservices foundation

#### Service Registration and Discovery
**Maturity Driver:** Mandatory

**Description:**
Calling applications or Clients should not really be worried about where microservices are hosted. Depending on the workload, microservices will scale up and tier down. We need a way to be able to automatically register new instances, deregister instances when unavailable, loosely couple clients without dependency on where our services are hosted.

**Best Practices:**
Implementation Guidance - Eureka is recommended from Spring ecosystem standpoint. There are other capabilities as well such as Consul, Zookeeper.
Service Discovery is one of the key tenets of a microservice based architecture. Eureka is the Netflix Service Discovery Server and Client. The server can be configured and deployed to be highly available, with each server replicating state about the registered services to the others.
When your microservices startup, they register with Eureka (assuming Eureka service is already running) and provide meta-data, such as host and port, health indicator URL, home page, etc. Eureka receives heartbeat messages from each instance belonging to a service. If the heartbeat fails over a configurable timetable, the instance will be removed from the registry.
Eureka metrics can be easily monitored using the eureka dashboard supported by the Eureka Server microservice application 
Additional Information
Many PAAS Platforms also provide inbuilt Services Registry and discovery.

**Reference:** https://microservices.io/patterns/service-registry.html

https://istio.io/

**Questions:**

1. Are you leveraging framework/library or container platform capabilities to implement service registration and discovery? *(Weightage: Medium)*
2. Do you have the ability to perform health checks for your microservices through a centralized dashboard *(Weightage: Medium)*
3. Have you implemented client side or server side service discovery? *(Weightage: High)*
4. Do you perform service discovery based microservices lookup? *(Weightage: High)*
5. Do your microservices register themselves to a central registry during startup *(Weightage: High)*

---

#### Fault Tolerance
**Maturity Driver:** Mandatory

**Description:**
Design for failures for down stream service.
What happens on failures: Degrade functionality or Default functionality
Design to fail fast and self-heal

**Best Practices:**
Implementation Guidance - Hystrix (Spring), Istio
Hystrix implements Circuit Breaker pattern allowing to identify and manage downstream network failures and latency better. This helps to fail fast and recover allowing systems to become self-healing
With Hystrix backed up with several default configuration, our microservices can create fallback functionality when the default functionality degrades or failures.
Hystrix metrics can be monitored independently to a monitoring dashboard. With multiple microservices built using Hystrix, all metrics can be pushed and aggregated to a Turbine dashboard.

**Questions:**

1. Are you leveraging framework/library or container platform capabilities to implement fault tolerance? *(Weightage: Medium)*
2. Is timeout implemented for backend dependencies? *(Weightage: High)*
3. Are exponential backoff retries implemented for backend dependencies? *(Weightage: Medium)*
4. Are you leveraging framework/library or container platform capabilities to implement fault tolerance? *(Weightage: Medium)*
5. Have microservices implemented bulkhead pattern? *(Weightage: High)*
6. Have your microservices implemented Circuit breaker pattern? *(Weightage: High)*

---

#### Service proxy/API Gateway
**Maturity Driver:** Mandatory

**Description:**
Provide capabilities such as server side load balancing
Routing
Edge Security
Analytics, Insights
Reverse Proxy

**Best Practices:**
Implementation Guidance - Zuul (Spring), Istio
It is a single entry point into the system, used to handle requests by routing them to the appropriate backend service or by invoking multiple backend services and aggregating the results. Also, it can be used for authentication, insights, stress and canary testing, service migration, static response handling, active traffic management.
Spring Cloud has created an embedded Zuul proxy to ease the development of a very common use case where a UI application wants to proxy calls to one or more back end services. This feature is useful for a user interface to proxy to the backend services it requires, avoiding the need to manage CORS and authentication concerns independently for all the backend.

**Questions:**

1. Are you leveraging framework/library or container platform capabilities to implement API Gateway or Service proxy? *(Weightage: High)*
2. Can you perform intelligent routing of incoming traffic to your microservices? *(Weightage: Medium)*
3. Can you load balance your incoming traffic to your microservice? *(Weightage: High)*
4. Are you peforming A/B testing through the use of intelligent routing for your microservices? *(Weightage: High)*
5. Do you have a consistent URL for others to access your service without depending on knowing the physical location of your services and where they are running *(Weightage: High)*
6. Are your microservices secure when being accessed by other microservices within the same application/cluster? *(Weightage: Low)*
7. Are your microservices secure from external (outside enterprise) access? *(Weightage: High)*
8. Are your microservices secure from internal (within enterprise) access? *(Weightage: Medium)*

---

#### Externalized Configuration
**Maturity Driver:** Mandatory

**Description:**
Externalize application configuration, secure it and be able to refresh application configuration without a need to restart application.

**Best Practices:**
Implementation Guidance - Spring Cloud Config
Spring Cloud Config is horizontally scalable centralized configuration service for distributed systems. It uses a pluggable repository layer that currently supports local storage, Git, and Subversion. 
With Spring Cloud Config, We can change app configuration dynamically without having to start the application.
Spring Cloud Config also provides out of the box capabilities to secure configuration by allowing you to encrypt and decrypt configuration either on server or client side using JCE (Java Cryptography Extensions)
Configuration files can be nested within folders and visible to the Config Server.

**Questions:**

1. Is your devops pipeline enabled to inject runtime environmental and sensitive configuration when building or deploying microservices? *(Weightage: High)*
2. Is sensitive information such as userid, passwords version controlled? *(Weightage: Medium)*
3. Is sensitive information such as userid, passwords encypted *(Weightage: Medium)*
4. Are environmental configuration version controlled? *(Weightage: High)*
5. Are environmental configuration externalized? *(Weightage: Medium)*

---

#### Service Authentication and authorization
**Maturity Driver:** Mandatory

**Description:**
Use Auth Server for user authorization as well as for secure machine-to-machine communication inside a perimeter.

**Best Practices:**
Implementation Guidance - Spring Security, Istio
There are multiple other way to implement services authorization, refer security guidance above
Spring Cloud Security provides convenient annotations and auto configurations to make this really easy to implement from both the server and client side.

**Questions:**

1. Are your microservices secure when being accessed by other microservices within the same application/cluster? *(Weightage: Medium)*
2. Are your microservices secure from external (outside enterprise) access? *(Weightage: High)*
3. Are your microservices secure from internal (within enterprise) access? *(Weightage: Medium)*
4. Are you leveraging framework/library or container platform capabilities to implement microservices security? *(Weightage: High)*
5. Can you perform intelligent routing of incoming traffic to your microservices? *(Weightage: High)*
6. Can you load balance your incoming traffic to your microservice? *(Weightage: High)*
7. Are you peforming A/B testing through the use of intelligent routing for your microservices? *(Weightage: Medium)*

---

#### Distributed Tracing
**Maturity Driver:** Required

**Description:**
Ability to trace a particular request end to end across multiple micro services and be able to find latency.

**Best Practices:**
Implementation Guidance - Spring Cloud Sleuth + Zipkin  (Spring), Istio
Spring Cloud Sleuth allows to have all the core application interaction patterns instrumented automatically. Its even taken care when using hystrix, zuul, Rest templates for Http endpoints and others. 
Tracing systems that our application to collect process and present data from tracers, and so we have all these tracers coming out of Spring Cloud Sleuth. Zipkin allows to visualize trace outcomes from Cloud Sleuth by collecting timing data and making it easy to see them, letting you query them, visualizing them. 
Zipkin also shows service dependencies.

**Questions:**

1. Are you leveraging framework/library or container platform capabilities to implement Distributed tracing? *(Weightage: Medium)*
2. Do you add a coorelation Id within your payload to support distributed tracing *(Weightage: Medium)*
3. Are you persisting tracing information for future analysis and troubleshooting? *(Weightage: Medium)*
4. Do you have a distributed tracing dashboard? *(Weightage: Low)*
5. Are you able to trace a particular business transaction end to end across your microservices? *(Weightage: High)*

---

#### Centralized Logging
**Maturity Driver:** Mandatory

**Description:**
Ability to aggregate logs to a centralized location, be able to filter logs (if needed),query/visualize logs and persist logs to a persistent store.

**Best Practices:**
Implementation Guidance - These are several OpenSource and product based implementation for this. A popular one is ELK Stack – ElasticSearch, Logstash and Kibana
Application will store logs into a log file. Logstash will read and parse the log file and ship log entries to an Elasticsearch instance. Finally, we will use Kibana 4 (Elasticsearch web frontend) to search and analyze the logs.

**Questions:**

1. Do you have the ability to run ad-hoc queries against your microservices application logs? *(Weightage: Medium)*
2. Do you have the ability to visualize logs on multiple dimensions as a time series information? *(Weightage: Low)*
3. Do you have the ability to search/filter logs? *(Weightage: High)*
4. Are you logs aggregated to a centralized repository? *(Weightage: High)*
5. Do you have a standard logging format across all your microservices? *(Weightage: High)*
6. Are you logging to standard.out? *(Weightage: High)*

---

#### Client side load balancing
**Maturity Driver:** Required

**Description:**
The problem of server side load balancing is if one or more servers stop responding, we have to manually remove those servers from the load balancer by updating the IP table of the load balancer. Another problem is that we have to implement a failover policy to provide the client with a seamless experience.

**Best Practices:**
Implementation Guidance - Ribbon (for Spring framework) or Istio
If one microservice wants to communicate with another microservice, it generally looks up the service registry using DiscoveryClient and Eureka server returns all the instances of the calling microservice to the caller service. It isa caller service headache which instance it calls. Here, client side load balancing stepped in. Client side load balancing maintains an algorithm like round robin or zone specific, by which it can invoke instances of calling services. The advantage is s service registry always updates itself; if one instance goes down, it removes it from its registry, so when the client side load balancer talks to the Eureka server, it always updates itself, so there is no manual intervention- unlike server side load balancing- to remove an instance.
Another advantage is, as the load balancer is in the client side, you can control its load balancing algorithm programmatically. Ribbon provides this facility.

**Questions:**

1. Are you leveraging framework/library or container platform capabilities to implement client side load balancing? *(Weightage: Medium)*
2. Is your client side load balancing integrated with service discovery? *(Weightage: Medium)*
3. Are you leveraging intelligent routing as part of client side load balancing? *(Weightage: Medium)*
4. Have you implemented client side load balancing? *(Weightage: High)*

---

#### Centralized Monitoring
**Maturity Driver:** Mandatory

**Description:**
Ability to monitor system (multiple microservices) from a centralized place.

**Best Practices:**
Implementation Guidance - These are several OpenSource and product based implementation for this.
Applications health check, response monitoring, time statistics, alert management, SLA management can all be done from a central place.

**Questions:**

1. Do you have automated alert management to page out support when anomolies occur? *(Weightage: Medium)*
2. Can you monitor your business transactions through a centralized dashboard and identify anomolies? *(Weightage: Medium)*
3. Do you have the ability to troubleshoot production issues quickly by leveraging monitoring dashboards? *(Weightage: Medium)*
4. Can you monitor response times for your microservices enabling SLA management? *(Weightage: Medium)*
5. Can you monitor health checks for your microservices? *(Weightage: Medium)*
6. Do you have one/more monitoring dashboards to manage your microservices? *(Weightage: Medium)*

---

#### Traffic Management and Intelligent Routing
**Maturity Driver:** Nice to have

**Description:**
Ability to do A/B testing, canary rollouts, and staged rollouts with percentage-based traffic splits

**Best Practices:**
Implementation Guidance - Istio (if containor platform) provides these capabilities
Istio’s easy rules configuration and traffic routing lets you control the flow of traffic and API calls between services. Istio simplifies configuration of service-level properties like circuit breakers, timeouts, and retries, and makes it a breeze to set up important tasks like A/B testing, canary rollouts, and staged rollouts with percentage-based traffic splits.
With better visibility into your traffic, and out-of-box failure recovery features, you can catch issues before they cause problems, making calls more reliable, and your network more robust – no matter what conditions you face.

**Questions:**

1. Are you leveraging framework/library or container platform capabilities to manage traffic through intelligent routing ? *(Weightage: High)*
2. Have you implemented Intelligent routing to support A/B testing or canary rollouts? *(Weightage: Medium)*

---

#### Application Metrics and Golden Signals
**Maturity Driver:** Mandatory

**Description:**
Instrument services to emit application-level metrics so health and performance can be measured and alerted on.

**Best Practices:**
Expose metrics via Prometheus/OpenMetrics endpoints. Track the golden signals (latency, traffic, errors, saturation) per service. Capture RED metrics for request-driven services and USE metrics for resources. Visualize on dashboards.

**Reference:** https://sre.google/sre-book/monitoring-distributed-systems/

**Questions:**

1. Do your microservices expose application metrics, for example Prometheus or OpenMetrics endpoints? *(Weightage: High)*
2. Do you track the golden signals (latency, traffic, errors, saturation) per service? *(Weightage: High)*
3. Are application and business metrics visualized on dashboards? *(Weightage: Medium)*
4. Do you capture RED and/or USE metrics appropriate to each service type? *(Weightage: Medium)*

---

#### Service Level Objectives and Error Budgets
**Maturity Driver:** Required

**Description:**
Define measurable reliability targets and use error budgets to balance reliability against delivery velocity.

**Best Practices:**
Define SLIs and SLOs for critical services. Track error budgets and use them to govern release pace. Alert on and review SLO breaches.

**Reference:** https://sre.google/workbook/implementing-slos/

**Questions:**

1. Have you defined SLIs and SLOs for your critical services? *(Weightage: High)*
2. Do you track error budgets and use them to balance reliability versus delivery speed? *(Weightage: Medium)*
3. Are SLO breaches alerted on and reviewed? *(Weightage: Medium)*

---

#### Unified Observability and OpenTelemetry
**Maturity Driver:** Required

**Description:**
Correlate logs, metrics, and traces into a single observability discipline using vendor-neutral instrumentation.

**Best Practices:**
Correlate the three pillars through a shared trace ID. Use a vendor-neutral standard such as OpenTelemetry. Aggregate exception/error tracking centrally. Enable fast navigation from an alert to the relevant traces and logs.

**Reference:** https://opentelemetry.io/

**Questions:**

1. Are logs, metrics, and traces correlated through a common identifier such as a trace ID? *(Weightage: High)*
2. Are you using a vendor-neutral instrumentation standard such as OpenTelemetry? *(Weightage: Medium)*
3. Do you have exception and error tracking aggregated in a central place? *(Weightage: Medium)*
4. Can you navigate from an alert to the relevant traces and logs quickly? *(Weightage: Medium)*

---

#### Health Check API
**Maturity Driver:** Mandatory

**Description:**
Expose endpoints that report whether a service instance is alive and ready, so the platform can route and restart correctly.

**Best Practices:**
Provide liveness and readiness endpoints. Have readiness verify critical downstream dependencies. Ensure the orchestration platform consumes these for traffic routing and restarts.

**Reference:** https://microservices.io/patterns/observability/health-check-api.html

**Questions:**

1. Does each microservice expose health-check endpoints for liveness and readiness? *(Weightage: High)*
2. Do readiness checks verify critical downstream dependencies? *(Weightage: Medium)*
3. Are health-check endpoints consumed by the orchestration platform for routing and restarts? *(Weightage: High)*

---

#### Service-to-Service Security (mTLS and Zero Trust)
**Maturity Driver:** Mandatory

**Description:**
Secure internal traffic by encrypting and mutually authenticating service-to-service communication, trusting identity rather than network location.

**Best Practices:**
Encrypt service-to-service traffic with mTLS. Authenticate workload identity, not just network location. Adopt a zero-trust posture where no internal traffic is implicitly trusted. Enforce least-privilege authorization between services.

**Reference:** https://www.nist.gov/publications/zero-trust-architecture

**Questions:**

1. Is service-to-service traffic encrypted in transit, for example with mTLS? *(Weightage: High)*
2. Do services authenticate each other's workload identity rather than relying on network location? *(Weightage: High)*
3. Have you adopted a zero-trust posture where no internal traffic is implicitly trusted? *(Weightage: Medium)*
4. Is least-privilege authorization enforced between services? *(Weightage: Medium)*

---

#### Secrets Management
**Maturity Driver:** Mandatory

**Description:**
Manage credentials, keys, and tokens through a dedicated secrets system rather than storing them in code, images, or config files.

**Best Practices:**
Store secrets in a dedicated manager (Vault, cloud KMS/secret manager). Keep secrets out of source control and images. Rotate secrets and audit access. Inject secrets at runtime rather than at build time.

**Reference:** https://owasp.org/www-project-secrets-management/

**Questions:**

1. Are secrets such as credentials, keys, and tokens stored in a dedicated secrets manager, for example Vault or a cloud KMS? *(Weightage: High)*
2. Are secrets kept out of source control and container images? *(Weightage: High)*
3. Are secrets rotated and is access to them audited? *(Weightage: Medium)*
4. Are secrets injected at runtime rather than baked into builds? *(Weightage: Medium)*

---

#### Rate Limiting and Throttling
**Maturity Driver:** Required

**Description:**
Protect services from overload and abuse by limiting request rates and shedding load under sustained pressure.

**Best Practices:**
Enforce rate limiting/throttling at the gateway and/or service. Apply per-client quotas where appropriate. Use backpressure or load shedding under sustained overload.

**Reference:** https://microservices.io/patterns/reliability/circuit-breaker.html

**Questions:**

1. Do you enforce rate limiting or throttling to protect services from overload and abuse? *(Weightage: High)*
2. Are quotas applied per client or consumer where appropriate? *(Weightage: Medium)*
3. Do you apply backpressure or load shedding under sustained overload? *(Weightage: Medium)*

---

#### Chaos Engineering and Resilience Testing
**Maturity Driver:** Nice to have

**Description:**
Proactively validate that the system withstands failure by injecting faults and verifying recovery behavior.

**Best Practices:**
Run fault-injection or chaos experiments. Validate failover, retries, and circuit breakers under realistic failure conditions. Make resilience testing part of the delivery process.

**Reference:** https://principlesofchaos.org/

**Questions:**

1. Do you proactively test resilience through fault injection or chaos experiments? *(Weightage: Medium)*
2. Do you validate failover, retries, and circuit breakers under realistic failure conditions? *(Weightage: Medium)*
3. Are resilience tests part of your delivery process? *(Weightage: Low)*

---

#### Service Mesh
**Maturity Driver:** Nice to have

**Description:**
Offload cross-cutting communication concerns (mTLS, traffic policy, observability) to a mesh layer rather than embedding them in each service.

**Best Practices:**
Adopt a service mesh such as Istio or Linkerd where complexity warrants it. Use the mesh to provide mTLS, traffic policy, and observability transparently to application code.

**Reference:** https://istio.io/

**Questions:**

1. Are you leveraging a service mesh such as Istio or Linkerd for cross-cutting concerns? *(Weightage: Medium)*
2. Does the mesh provide mTLS, traffic policy, and observability without changes to application code? *(Weightage: Medium)*

---

## 3. Common Microservices app dev Patterns

### 3.1. Microservices foundation

#### BFF (Backend for FrontEnd)
**Maturity Driver:** Mandatory

**Description:**
Implement BFF to isolate User Experience for backing microservices. Allows to represent a channel-specific service interface that is consistent with an
overall microservices architecture but allows enough uniqueness that it can be adapted to the needs of a specific client type

**Best Practices:**
Pattern that allows front-end teams to deploy their own backend aggregator service (the BFF) that handles the entirety of external service calls needed for their specific user experience
Usually built for a specific browser, mobile platform, or IOT device. User experience and BFF built in the same language to increase application performance
Microservices break one set of functionality into multiple APIs. The easiest way for a client to interface with a server is through a single API. Different types of clients—browser, mobile, CLI—want different APIs for the same functionality. Business logic is rarely specific to a single client type. It should be implemented such that all client types can share it.
A BFF can perform the following actions:
• Orchestration – It can orchestrate several calls to business microservices that result from a single client action.
• Translation – It can translate the results of a microservice into a channel-specific representation that more cleanly maps to the needs of the ux of that client.
• Filtering – It can filter results from a business microservice that are not needed by a particular client type.

**Questions:**

1. Is your BFF responsible for managing security (authentication and authorization) before the calls access business microservices? *(Weightage: High)*
2. Is your BFF responsible for managing caching in support of what is mostly used by your front-end? *(Weightage: Medium)*
3. Is your BFF service responsible for filtering results from business microservice to support in support of only what is required on the front-end? *(Weightage: High)*
4. Is your BFF service responsible for orchestration with other business microservices? *(Weightage: Medium)*
5. For multiple Frontends, have you implemented different BFF services that acts as a gateway to support that particular front-end? *(Weightage: High)*

---

#### Modern Web architecture
**Maturity Driver:** Mandatory

**Description:**
Design an application that meets the needs of your users, while still working within the capabilities of the different interface devices that now exist?

**Best Practices:**
Adopt a Modern Web Architecture that combines intelligent front-end components with general purpose back-end components.

**Questions:**

1. Your front-end should not depend on any session capabilities to be supported on the backend *(Weightage: High)*
2. Do you have a modern web architecture that is accessing your microservices via web APIs? *(Weightage: High)*

---

#### Single Page Application
**Maturity Driver:** Required

**Description:**
Simplifies the frontend experience with the trade-off of more responsibility on the backing services

**Best Practices:**
Web-based interface that provides the user with a single entry point to the application and never reloads the page or navigates away from that initial experience
Built using a combination of HTML, CSS, and JavaScript framework such as React, Angular which are natively implemented/supported in modern browsers. Store page state within the client and connect to the backend through REST services. This approach is called the “Single Page Application” because all of the HTML, CSS and JavaScript code necessary for a complex set of business functions, which may represent multiple logical screens or pages, is retrieved as a single page request.
The main benefit of the Single Page Application approach is that it allows much more responsive and intuitive application designs than the dynamic page approach.

**Questions:**

1. Are you leveraging client side data model that allows you to eliminate server side session implementation. *(Weightage: Medium)*
2. Are you taking advantages of new/improved browser based capabilities such as caching to improve user experience. *(Weightage: Medium)*
3. Are you leveraging SPA (Single Page Application) to better manage your web presentation tier, along with providing a more intutive/responsive experience to the users? *(Weightage: Medium)*

---

#### Native Mobile Application
**Maturity Driver:** Required

**Description:**
You would like to provide the most optimized user experience on a mobile device and take
advantage of the features that make mobile computing unique?

**Best Practices:**
Write a Native Mobile Application for each of the two major platforms (iOS and Android).
While Single Page Applications provide a good user interface that can be adapted to different screen sizes and orientations using Responsive Design no browser-based application can take advantage of all the features and capabilities of a mobile device. What’s more, even though advances have been made in the speed and performance of Javascript in many browsers, the performance of browser-based applications still noticeably falls behind those of native applications

**Questions:**

1. Have you implemented a native mobile application over SPA to ensure better performance and a more feature rich experience for your end users *(Weightage: Low)*

---

#### Adapter Microservices
**Maturity Driver:** Required

**Description:**
How do you handle translation of existing service implementations into good microservices APIs.  Your microservices want to incorporate existing services (e.g. SOAP, JMS, or mainframe-based services) but their APIs do
not use the RESTful or queue-based approach that is consistent with the microservices architecture.

**Best Practices:**
Adapter Microservice that converts the existing service’s nonmicroservice API to an API that client microservies will expect. An Adapter Microservice follows the Adapter pattern in that it converts one API to another. Wraps and translates existing services into an entity-based REST interface. Treats each new entity interface as a microservice and builds, manages, and scales it independently. This helps when:
If you have existing services that run well enough as is, you don’t want to rewrite them, you want to reuse them instead.
Changing the APIs of existing services can break existing clients.

**Questions:**

1. Have you implemented adapter services to integrate with legacy backends that cannot directly integrate with your microservices? *(Weightage: Medium)*

---

#### Co-Existence and Stangler Pattern
**Maturity Driver:** Nice to have

**Description:**
Provides a consistent way to migrate a large monolith application into microservices architecture in multiple attempts where for sometime both the monolith and existing application co-exist.

**Best Practices:**
The Strangler pattern helps us manage the refactoring of a monolithic application in stages.
Divide an application into different functional domains, and replace those domains with a new microservices-based implementation one domain at a time. This creates two separate applications that live side by side in the same URI space. 
Over time, the newly refactored application “strangles” or replaces the original application until finally you can shut off the monolithic application. Thus, the Strangler Application steps are transform, coexist, and eliminate.

**Questions:**

1. Does your adapter services allow you to perform co-existence and data replication? *(Weightage: Low)*

---

#### Domain Driven Design
**Maturity Driver:** Required

**Description:**
Develop software for complex needs by deeply connecting the implementation to an evolving model of the core business concepts.

**Best Practices:**
1. Focus on the core domain and domain logic.
2. Base complex designs on models of the Domain (Entity, Aggregate Root  ,Bounded context etc.)
3. Domain layer should have a well defined boundary to avoid the corruption of the layer from non-core domain layer concerns such as vendor-specific translations, data filtering, transformations, etc

**Questions:**

1. Have you modelled your microservices to support domain deiven design and bounded context principles? *(Weightage: High)*
2. Do you duplicate data between microservices to support bounded context? *(Weightage: High)*
3. Do you publish data that different microservices can consume? *(Weightage: Medium)*
4. Do you Constantly collaborate with domain experts, in order to improve the application model and resolve any emerging domain-related issues? *(Weightage: Medium)*
5. Are your Domain elements designed to hold the domain state and behavior correctly? *(Weightage: High)*

---

#### Business Microservice
**Maturity Driver:** Mandatory

**Description:**
Guides Where to put business logic in an application built using a Microservices architecture.

**Best Practices:**
Performs one comprehensive business function
Implementation to decide how to implement a microservice and how that relates to other services in the overall application
Each microservice should implement one complete business function.
The primary quality of a business function is that it implements or otherwise provides business logic.
Business logic should be encapsulated inside an API.

**Questions:**

1. Do you have well defined business microservices? *(Weightage: High)*

---

#### Caching
**Maturity Driver:** Required

**Description:**
Improve the performance of your application or microservice when it makes many repeated calls to services

**Best Practices:**
Use Results Cache can be as simple as a Key-Value Store (either in-memory or in a Scalable Store). 
Determining what to cache is often as difficult as setting up a cache itself. A common approach that is sometimes taken is to try to reproduce the data in a database locally to the application that is making requests of that data. The logic here is that if the problem is that database calls are expensive and slow, then by making those calls locally (perhaps in-memory) then you can reduce that overhead. Another concern to remediate is to ensure that information does not become stale. TTL (Time to Live) is a good strategy to determine information staleness that results in information purging and new cached data being loaded.

**Questions:**

1. Do you have a caching implementation to improve your microservices performance? *(Weightage: Medium)*
2. Do you have a distributed cache? i.e. your cache is not implemented locally? *(Weightage: Medium)*
3. Do you see performance challenges with your microservices especialy for end to end business transactions? *(Weightage: Medium)*

---

#### Integration Mediation Layer
**Maturity Driver:** Nice to have

**Description:**
When you would like one application (part of a larger suit that accomplishes a business process) to modernize without impacting other interfacing applications which may modernize at their own pace.

**Best Practices:**
Leverage integration mediation layer that supports enterprise modernization efforts around business process modernization within constrains of a siloed culture where budgets and organization boundaries derive multi speed IT decisions and limit speed of innovation.

**Questions:**

1. Are you leveraging an integration mediation layer to support incremental business process modernization *(Weightage: Low)*

---

#### Service Pattern
**Maturity Driver:** Mandatory

**Description:**
How to manage IT operations that do not conceptually belong to any specific object/entity or aggregate into an entity-based approach.

**Best Practices:**
Services patterns offer a way to map operations that do not conceptually belong to any specific object/entity or aggregate into an entity-based approach. This pattern can be used login service, authentication, authorization and logging. Model such objects as standalone interfaces called services that follow these rules:
They should be stateless.
The service’s interface is defined in terms of other elements of your domain model (entities and value objects).
The service refers to a domain concept that does not naturally correspond to any particular entity or value object.

**Questions:**

1. Have you implemented common services as microservices that do not belong to a particular business domain? *(Weightage: Medium)*

---

#### Persistent Storage and Polyglot Persistence
**Maturity Driver:** Mandatory

**Description:**
Decide on persistence storage for your microservices

**Best Practices:**
Database Per Service (Recommended) 
Shared Databases supporting multiple services
Each of these approaches have their own pros and cons. Database per service is the recommended approach as it helps ensure that the services are loosely coupled. Changes to one service’s database does not impact any other services. Each service can use the type of database that is best suited to its needs. 
Database per service also brings in complexity in terms of transactional consistency as Implementing business transactions that span multiple services is not straightforward. Also, Implementing queries that join data that is now in multiple databases is challenging.

**Questions:**

1. Have you implemented the right database strategy per microservice? Shared db v per microservice db *(Weightage: High)*
2. Have you implemented polyglot persistence for appropiate use cases? *(Weightage: High)*

---

#### Distributed Transactions
**Maturity Driver:** Required

**Description:**
Monlith applications implemented transactions using 2 phase commit that worked on business entities at the same time which now need to be separated out into multiple microservices

**Best Practices:**
Saga - A saga is a sequence of local transactions where each transaction updates data within a single service. The first transaction is initiated by an external request corresponding to the system operation, and then each subsequent step is triggered by the completion of the previous one. There are a couple of different ways to implement a saga transaction,

Events/Choreography: When there is no central coordination, each service produces and listen to other service’s events and decides if an action should be taken or not.

Command/Orchestration: when a coordinator service is responsible for centralizing the saga’s decision making and sequencing business logic

**Questions:**

1. When distributed transactions are applicable, have you implemented choreography or orchestration patterns? *(Weightage: High)*

---

#### Event-Driven Architecture and Messaging
**Maturity Driver:** Mandatory

**Description:**
Use asynchronous events/messages to decouple services, improve resilience, and avoid tight synchronous call chains.

**Best Practices:**
Communicate asynchronously via events where appropriate, using a broker or event streaming platform (Kafka, RabbitMQ, Pulsar). Define, version, and govern event schemas (schema registry, AsyncAPI). Handle out-of-order and duplicate events gracefully.

**Reference:** https://microservices.io/patterns/data/event-driven-architecture.html

**Questions:**

1. Do your microservices communicate asynchronously via events or messages where appropriate? *(Weightage: High)*
2. Are you using a message broker or event streaming platform such as Kafka, RabbitMQ, or Pulsar? *(Weightage: High)*
3. Are event schemas defined, versioned, and governed, for example via a schema registry or AsyncAPI? *(Weightage: Medium)*
4. Do consumers handle out-of-order and duplicate events gracefully? *(Weightage: Medium)*
5. Are events used to decouple services and avoid synchronous call chains? *(Weightage: Medium)*

---

#### Event Sourcing and CQRS
**Maturity Driver:** Nice to have

**Description:**
Where appropriate, separate read and write models and persist state as a sequence of events to enable scaling, auditability, and temporal queries.

**Best Practices:**
Apply CQRS to separate read and write responsibilities. Use event sourcing to persist state changes as an immutable event log. Support state rebuilds and temporal/audit queries from that log.

**Reference:** https://microservices.io/patterns/data/cqrs.html

**Questions:**

1. Where appropriate, do you separate read and write models using CQRS? *(Weightage: Medium)*
2. Do you persist state changes as an immutable sequence of events (event sourcing)? *(Weightage: Medium)*
3. Can you rebuild state and support temporal or audit queries from the event log? *(Weightage: Low)*

---

#### Transactional Messaging (Outbox and Idempotent Consumer)
**Maturity Driver:** Required

**Description:**
Guarantee consistency between local data changes and the messages a service publishes, and tolerate redelivery on the consumer side.

**Best Practices:**
Use a transactional outbox (with transaction log tailing or polling publisher) so database updates and message publishing are atomic. Make consumers idempotent to tolerate redelivery. Avoid dual-write inconsistency between datastore and broker.

**Reference:** https://microservices.io/patterns/data/transactional-outbox.html

**Questions:**

1. Do you ensure atomicity between database updates and message publishing, for example via a transactional outbox? *(Weightage: High)*
2. Are your message consumers idempotent so they tolerate redelivery? *(Weightage: High)*
3. Do you avoid dual-write inconsistencies between your datastore and the broker? *(Weightage: Medium)*

---

#### Inter-Service Communication Styles
**Maturity Driver:** Required

**Description:**
Deliberately choose the right communication style and protocol for each interaction rather than defaulting to chatty synchronous REST everywhere.

**Best Practices:**
Choose sync (REST/gRPC) vs async (messaging) per use case. Use an efficient protocol such as gRPC for low-latency/high-throughput RPC. Use API Composition or a dedicated query service for cross-service aggregation rather than chatty calls.

**Reference:** https://microservices.io/patterns/communication-style/messaging.html

**Questions:**

1. Have you deliberately chosen communication styles (synchronous REST/gRPC versus asynchronous messaging) per use case? *(Weightage: High)*
2. Where low-latency or high-throughput RPC is needed, do you use an efficient protocol such as gRPC? *(Weightage: Medium)*
3. For aggregation across services, do you use API Composition or a query service rather than many chatty calls? *(Weightage: Medium)*

---

## 4. Microservices Deployment Patterns

### 4.1. Microservices foundation

#### Blue green deployments
**Maturity Driver:** Mandatory

**Description:**
Ability to reduce application downtime via support for blue green deployments allowing setting up new instances of microservices without impacting existing ones until team is good to migrate of existing version to new version.

**Best Practices:**
Support health check for microservices
Support for Draining
Support for Switch back
Support readiness probe and Liveliness probe for Microservices
Platform support to route traffic to new service once Platform confirms that new service is ready to accept traffic

**Questions:**

1. Does your platform support health check (readiness probes) for microservices before declaring deployments successful? *(Weightage: High)*
2. Does your platform support health check (liveliness probes) for microservices before declaring deployments successful? *(Weightage: High)*
3. Does your platform support blue green deployments *(Weightage: High)*
4. Does your Platform support to route traffic to new service once Platform confirms that new service is ready to accept traffic *(Weightage: High)*

---

#### Rolling Upgrades
**Maturity Driver:** Mandatory

**Description:**
Ability to support Rolling upgrades that basically do an inplace migration of existing microservices instance

**Best Practices:**
Support health check for microservices
Support for Backward Compatibility
Support for Roll Back
Support readiness probe and Liveliness probe for Microservices
Platform support to route traffic to new service once Platform confirms that new service is ready to accept traffic

**Questions:**

1. Does your platform support health check (readiness probes) for microservices before declaring deployments successful? *(Weightage: Medium)*
2. Does yor platform support health check (liveliness probes) for microservices before declaring deployments successful? *(Weightage: Medium)*
3. Does your platform support rolling upgrades? *(Weightage: Medium)*
4. Does your platform support automatic rollback of deployments *(Weightage: Medium)*
5. Does your Platform support to route traffic to new service once Platform confirms that new service is ready to accept traffic *(Weightage: High)*

---

#### Canary Deployments
**Maturity Driver:** Required

**Description:**
Deploy the new version into production alongside the old one.. Controlling traffic routing at high level

**Best Practices:**
Support health check for microservices
Support for Backward Compatibility
Support for Roll Back
Support readiness probe and Liveliness probe for Microservices
High level traffic routing support

**Questions:**

1. Does your platform support health check (readiness probes) for microservices before declaring deployments successful? *(Weightage: Medium)*
2. Does yor platform support health check (liveliness probes) for microservices before declaring deployments successful? *(Weightage: Medium)*
3. Does your platform support canary upgrades? *(Weightage: Medium)*
4. Does your platform support automatic rollback of deployments *(Weightage: High)*
5. Does your Platform support to route traffic to new service once Platform confirms that new service is ready to accept traffic *(Weightage: Medium)*

---

#### A/B testing Support
**Maturity Driver:** Nice to have

**Description:**
Deploy the new version into production alongside the old one.. More granular attribute/domain/Business based traffic routing

**Best Practices:**
Support health check for microservices
Support for Backward Compatibility
Support for Roll Back
Support readiness probe and Liveliness probe for Microservices
Granular traffic routing support

**Questions:**

1. Does your platform support health check (readiness probes) for microservices before declaring deployments successful? *(Weightage: Medium)*
2. Does yor platform support health check (liveliness probes) for microservices before declaring deployments successful? *(Weightage: Medium)*
3. Does your platform support a/b upgrades? *(Weightage: Medium)*
4. Does your platform support Granular/intelligent traffic routing support *(Weightage: Medium)*
5. Does your Platform support to route traffic to new service once Platform confirms that new service is ready to accept traffic *(Weightage: Medium)*

---

## 5. Reuse - Code Generators and Reference Implementations

### 5.1. Microservices foundation

#### Microservices Reference Architecture
**Maturity Driver:** Mandatory

**Description:**
Use reference architecture and tailor it for client specific requirements

**Best Practices:**
Leverage Spring Mircoservices reference architecture

**Reference:** https://spring.io/microservices

**Questions:**

1. Validate applicability and usage *(Weightage: High)*

---

#### Microservices Code generator
**Maturity Driver:** Mandatory

**Description:**
Time saving when generating Microservices code and associated artifacts to be deployed on cloud.

**Best Practices:**
A workflow engine to automatically generate, build and deploy identified microservices to Kubernetes Platform (Cloud/On-Prem).

Features/Functions
Microservices development time reduction conservatively by up to 30%
Microservices Development project jump start within hours
Developers to focus on business logic instead of spending time on creating project framework, CI/CD pipeline and deployment configurations

Value Proposition/Benefits
Possibly reduction of development time by 15%-20%

**Reference:** https://www.jhipster.tech/

**Questions:**

1. Validate applicability and usage *(Weightage: Medium)*

---

#### Microservices Chasis
**Maturity Driver:** Nice to have

**Description:**
A microservices bootstrap framework for rapidly building and deploying complex solutions

**Best Practices:**
MicroServices Chassis provides necessary technical services (build and runtime) for the developed micro-services. It provides technical capabilities such as: Service Discovery, Proxy/Gateway, Security, Service Configuration Management, Monitoring, DevOps, etc to Microservices. It is a critical element of a successful ecosystem of microservices. We have created this chassis based upon Spring Framework for developers to help improve their productivity in developing and testing microservices.

**Reference:** https://microservices.io/patterns/microservice-chassis.html

**Questions:**

1. Validate applicability and usage *(Weightage: Low)*

---

## 6. API Implementation

### 6.1. API Documentation

#### Are APIs well documented? 
**Maturity Driver:** Mandatory

**Description:**
Well documented APIs are critical to ensure consistent visibility and conformance to your APIs

**Best Practices:**
Leverage Swagger to document your APIs and Host them centrally so that all partners have on demand access to them.

**Reference:** https://swagger.io/resources/articles/best-practices-in-api-documentation/

**Questions:**

1. Are you leveraging swagger and have hosted it at a common location accessible by everyone? *(Weightage: Medium)*

---

### 6.2. API Design

#### Are APIs designed considering Service Design principles?
**Maturity Driver:** Mandatory

**Description:**
A service refers to functionality pertaining to a particular capability, exposed as an API

**Best Practices:**
Loose Coupling - Services and consumers must be loosely coupled from each other.
Encapsulation - A domain service can access data and functionality it does not own through other service contracts only.
Stability - Service contracts must be stable.
Reusable - Services must be developed to be reusable across multiple contexts and by multiple consumers.
Contract-based - Functionality and data must only be exposed through standardized service contracts.
Consistency - Services must follow a common set of rules, interaction styles, vocabulary and shared type
Ease Of Use - Services must be easy to use and compose in consumers (and applications).
Externalizable - Service must be designed so that the functionality it provides is easily externalizable.

**Reference:** https://github.com/paypal/api-standards/blob/master/api-style-guide.md

**Questions:**

1. Are your APIs and Consumers loosely coupled? *(Weightage: Medium)*
2. Are your APIs and Consumers highly cohesive? *(Weightage: Medium)*
3. Are your APIs functionality exposed via well defined service contracts? *(Weightage: Medium)*
4. Are all your APIs following a common set of rules, interaction styles and vocabulary? *(Weightage: High)*
5. Are your services reusable across different contexts by different consumers? *(Weightage: High)*

---

#### Are APIs designed with consistent usage of HTTP Method, Status and Headers? 
**Maturity Driver:** Mandatory

**Description:**
HTTP methods should be used consistently along with consistent usage of Status and HTTP headers

**Best Practices:**
Http methods - Ensure CRUD mapping with HTTP methods
Data processing - Content type headers must match the data format being processed example JSON which is a light-weight data representation for an object composed of unordered key-value pairs
Standard Http Headers - HTTP headers is to provide metadata information about the body or the sender of the message in a uniform, standardized, and isolated way. 
Custom Http Headers - Avoid custom headers unless required for special processing
Http Status codes - Use consistent HTTP status codes appropriate to the response (Succeeded, Request Issue or Server Issues)

**Questions:**

1. Are you leveraging apropriate HTTP method to support your entitiy's exposed CRUD operations *(Weightage: Medium)*
2. Are you using appropriate http headers? *(Weightage: Medium)*
3. Are you avoiding custom Http headers unless required for special processing *(Weightage: Medium)*
4. Are your APIs using consistent http status codes as appropriate to your response. *(Weightage: Medium)*

---

#### Is API supporting Hypermedia? 
**Maturity Driver:** Nice to have

**Description:**
Hypermedia As The Engine Of Application State (HATEOAS) is a constraint of the REST application architecture. a client could interact with a service entirely through hypermedia provided dynamically by the service. A hypermedia-driven service provides representation of resource(s) to its clients to navigate the API dynamically by including hypermedia links in the responses

**Best Practices:**
Hypermedia compliant APIs have a well defined entry point for an API which a client navigates to in order to access all other resources.
The client does not need to build the logic of composing URIs to execute different requests or code any kind of business rule by looking into the response details (more in detail is described in the later sections) that may be associated with the URIs and state changes.

**Questions:**

1. If your APIs need to be hypermedia compliant, do you have well defined entry points that allows API clients to traverse through all the other dependent resources? *(Weightage: Medium)*

---

#### Are standard API Naming Conventions followed? 
**Maturity Driver:** Mandatory

**Description:**
APIs should have a standard naming convention for URIs, Resources, QueryParameters, Fields etc.

**Best Practices:**
URI Naming convention and standards should be established and leveraged. 
Names are a part of the API consumer’s domain. 
Names should have meaning to that consumer. 
Do not expose back end models to the end users.This is an anti-pattern.
Do not add packaging to your name. (e.g.com.example.commerce.resource_name)
URLs depth are upto 3 levels only. Optional states and attributes are behind the HTTP question mark and not as part of the base URL 
Guidance should be established on resource name, Query parameters, Resource names etc. Types of Resource
Member Resource
– A resource that points to a single entity.
– Are identified by an id. Id can be generated by the provider or
created by the client on a POST.
– Use singular noun or id
Collections
– Made up of more then one member.
– Can be ordered or unordered.
– Use plural nouns.
Algorithmic
– Resources can be algorithms
– Business Process, Façade, etc…
– Should Follow HTTP Verb semantics like any other resource
Resources in RESTful URLs can be chained together to form a hierarchy of relationships.
– <Resource1>/<id>/<Resource2>/<id>
– Always use a collection followed by a member - …/customers/123/orders/456/items/789

**Questions:**

1. Is your project/application following a well defined URL naming convention and standard? *(Weightage: High)*
2. Are your URI names providing meaning to the API consumer? *(Weightage: Medium)*
3. Your API URI names should not be exposing backend models to the end user? *(Weightage: High)*
4. Your API URI names should not add packaging? *(Weightage: Medium)*
5. Are you limiting the URI depth to maxium 3 levels only? *(Weightage: High)*
6. Are your optional parameters part of Query string? *(Weightage: Medium)*

---

#### Are APIs designed with a well defined contract?
**Maturity Driver:** N/A

**Description:**
There are various options available to define the API's contract interface (API specification or API description). Examples are: OpenAPI (fka Swagger), Google Discovery Document, RAML, API BluePrint etc.

**Best Practices:**
Use JSON Schema to define API contracts.
Use JSON data types.

**Questions:**

1. Are you leveraging JSON data types within your API contracts? *(Weightage: Medium)*
2. With none enterprise or other constraints, Are you using JSON schema to define your API contracts? *(Weightage: Medium)*

---

#### Do APIs implement consistent error handling based on HTTP Specifications?
**Maturity Driver:** Mandatory

**Description:**
As per HTTP specifications, the outcome of a request execution could be an integer and a message. The number is known as the status code and the message as the reason phrase. The reason phrase is a human readable message used to clarify the outcome of the response. The HTTP status codes in the 4xx range indicate client-side errors (validation or logic errors), while those in the 5xx range indicate server-side errors (usually defect or outage)

**Best Practices:**
Custom Error handling and status codes can be used with appropriate business reasons and well defined contracts.
Error handling should be implemented for Input Validation, Content type validation
As a best practice, Http status codes and human readable reason phrase are not sufficient to convey enough information about an error in a machine-readable manner or providing enough information about business scenario exceptions. APIs MUST return a JSON error representation that conforms to the error.json schema defined in the Common Types repository. Refer following link for more details - https://github.com/paypal/api-standards/blob/master/api-style-guide.md#error-handling

**Questions:**

1. Are your APIs using consistent http status codes as appropriate to your response? Success, error? *(Weightage: High)*
2. Are your APIs performing appropriate input validation and returning consistent error codes? *(Weightage: High)*
3. Are your APIs performing appropriate content validation and returning consistent error codes? *(Weightage: High)*
4. Are you not relying on Http status code only to communicate error information back to the caller? Your APIs should wrap an error representation around HTTP status codes and response. *(Weightage: High)*

---

#### Is API versioning implemented, Supported, Standardized? 
**Maturity Driver:** Required

**Description:**
API versioning should support Backward Compatibility (where applicable), and support API lifecycle states such as beta, deprecated and retired.

**Best Practices:**
API specifications MUST follow the versioning scheme where where the v introduces the version, the major is an ordinal starting with 1 for the first LIVE release, and minor is an ordinal starting with 0 for the first minor release of any major release.
Every time there is an incremental change to an API, whether or not backward compatible, the API specification MUST be versioned. This allows the change to be labeled, documented, reviewed, discussed, published and communicated.

API endpoints MUST only reflect the major version.
API specification versions reflect interface changes and MAY be separate from service implementation versioning schemes.
A minor API version MUST maintain backward compatibility with all previous minor versions, within the same major version.
A major API version MAY maintain backward compatibility with a previous major version.
Version is maintained in the URL
Version is maintained to the left of resource in the URL
API version contains whole number e.g. v1 is fine but v1.1 should not be used

Place version numbers in the URI top level API for major versions
– Major version means breaking change. Since the API is a contract with the consumer, a breaking change really results in a new API – hence changing the version in the URI is the best practice.
– Must be specified.
– Do not version each Resource.
– Do not remove old versions without a formal deprecation.
– If there is a security flash needed (mandatory change), send an immediate communication via all available channels, make the change, but do not increment the major version.
Use version in Media-Type for minor revisions (when necessary)
– A particular consumer may be dependent on a behavior that is changed that seems safe. Allowing for a minor version in the media-type gives consumers a way out of these niche cases until they can fix their code.
– Minor versions may not ever be needed unless a consumer runs into this type of scenario and at that point a service offering can add them via a defect.
– Does not have to be specified; default to latest minor version.

**Questions:**

1. Do you have a versioning strategy for your APIs? *(Weightage: High)*
2. Are your APIs backward compatible? *(Weightage: High)*
3. Do you test backward compatibility when rolling out new versions of APIs *(Weightage: High)*
4. Do you have a strategy to ensure that consumers can move to new versions of APIs when new versions are not backward compatible. *(Weightage: High)*

---

#### Do APIs handle pagination effectively
**Maturity Driver:** Required

**Best Practices:**
API response contains only the fields required by the consumer and not all the attributes
Required fields for a resource are specified in a comma-delimited list in request URL
"limit" and "offset" are used for pagination
Metadata is included with each response 
Default value for "offset" is set (0 as a rule of thumb)
Default value for "limit" is set (10 as a rule of thumb although it depends on data size)
Leverage compression when browsers are consuming APIs response

**Questions:**

1. Are you leveraging effective strategies like limits and offset to manage pagination? *(Weightage: Medium)*

---

### 6.3. API Security

#### Are your APIs secured?
**Maturity Driver:** Mandatory

**Description:**
API Security is critical to ensure unauthorized access to your APIs

**Best Practices:**
Use JWT or API Keys to provide access to your APIs. 
Tokens should be be temporary and should have TTL (Time to Live). 
If required, consider other approaches such as framework driven security implementation (eg Spring Security).

**Reference:** https://www.owasp.org/index.php/REST_Security_Cheat_Sheet

**Questions:**

1. Are your APIs secured when being accessed by other components within the same application? *(Weightage: High)*

---

#### Are access policies for your APIs defined? 
**Maturity Driver:** Required

**Description:**
API should have appropriate security policies for external v/s internal access.

**Best Practices:**
Separate access policies and gateways should be defined for API that are to be exposed to different types of channels

**Questions:**

1. Are your APIs appropriately secured when being accessed by other apps within the enterprise? *(Weightage: Medium)*
2. Are your APIs appropriately secured when being accessed by other apps outside the enterprise? *(Weightage: Medium)*

---

#### Are API security best practices implemented?
**Maturity Driver:** Mandatory

**Description:**
API Security best practices ensure that your APIs are secure and designed keeping security in mind.

**Best Practices:**
These best practices cover the following key topics
Protocol access
Input Type Validation
Content Type Validation
Access Controls
Audit Logging
Security Headers and Managing Sensitive Information
CORS poilicies

**Questions:**

1. Are your APIs perfoming input type validation? *(Weightage: High)*
2. Are your APIs performing content type validation? *(Weightage: High)*
3. Are your APIs or infrasructure performing audit logging for API access? *(Weightage: High)*
4. Have you implemented the right CORS headers? *(Weightage: High)*

---

### 6.4. API Testing

#### Is API testing automated?
**Maturity Driver:** N/A

**Description:**
API testing should be automated. Beyond initial unit testing, there should not be any manual testing that should be done for testing APIs.

Whereever feasibile, API testing should be part of devops Continuous testing Pipeline

**Best Practices:**
If your spec is written in Swagger/OpenAPI, you can autogen tests using Swagger Test Templates. For API Blueprint there’s Dredd.

**Questions:**

1. Is your API testing automated? *(Weightage: High)*

---

#### is TDD implemented for API Unit and function testing?
**Maturity Driver:** N/A

**Description:**
Test Driven development implemented

**Best Practices:**
Developers use TDD (Test Driven Develoment) and create unit/FVTtests that invoke each REST API. TDD may require additional REST APIs (some may delivered in the product, and some may be for test only).

**Questions:**

1. Are you using TDD for perfoming Unit and functional testing agaist your APIs *(Weightage: Medium)*

---

#### Regression Automation
**Maturity Driver:** N/A

**Description:**
Consider it critical to automate your full regression suite not just few critical APIs.

**Best Practices:**
Execute Regression testing as part of CI/CD Pipeline.

**Questions:**

1. Is complete regression suite automated? *(Weightage: High)*

---

#### Business process automation
**Maturity Driver:** N/A

**Description:**
APIs testing should not just be transactional. Care should be taken to ensure that functional testing tests business processes that are composed or orchestrated as APIs.

**Questions:**

1. Are API tested in Isolation or testing orchestrated for a business process? *(Weightage: Medium)*

---

#### Consumer driven contracts
**Maturity Driver:** N/A

**Description:**
Contract Testing is writing tests to ensure that the explicit and implicit contracts of microservices work as advertised

**Best Practices:**
Pact is an excellent tool to use to do Contract Testing from a consumer’s perspective. Pact allows consumers to create, execute and evaluate tests against a “pact”, the contract, if you will. The provider is represented as a set of mock services. Then, later on in the Software Test Lifecycle that pact is executed against the provider to ensure that the contract is accurately in force.
Pact is one of the more popular tools for Contract Testing with microservices and it’s a good way to start writing consumer code while the provider behavior is underway in parallel.

**Reference:** https://docs.pact.io/

**Questions:**

1. Are consumer driven contracts based testing being implemented? *(Weightage: Low)*

---

#### Backward compatibility
**Maturity Driver:** N/A

**Description:**
Whenever APIs are changed and versioned, tesing needs to ensure that APIs are backward compatible and tested. (Refer API versioning above for more details)

**Best Practices:**
APIs that have specifications to support backward compatiility should be tested for backward compatibility.

**Questions:**

1. Are APIs being tested for backward compatibility? *(Weightage: High)*

---

### 6.5. API Management

#### Do we need to manage API Externalization?
**Maturity Driver:** N/A

**Description:**
API exploration
Self-service sign up
Interactive API testing
App key provisioning
API usage analytics
Rate limit notification
Multiple dev communities

**Best Practices:**
Leverage API Management tools to support API Externalization and Productization capabilities

Multiple tools available in the market including Apigee, Kong, AWS API Gateway, Mulesoft, and others

**Questions:**

1. Applicable and compliant? *(Weightage: Medium)*

---

#### Do we need to manage and scale API realization and lifecycle.
**Maturity Driver:** N/A

**Description:**
Multi-tenancy
Rate limiting
Runtime policy enforcement
API deployment
OAuth security management
Data transformation/redaction
Backend service discovery
Version management
Analytics support
Role-based access control
Environment management
Monitoring and notification

**Best Practices:**
Leverage API Management tools to support API Externalization and Productization capabilities

Multiple tools available in the market including Apigee, Kong, AWS API Gateway, Mulesoft, and others

**Questions:**

1. Applicable and compliant? *(Weightage: Medium)*

---

## 7. Code Quality & Maintainability

### 7.1. Code Quality & Maintainability

#### Code Complexity & Structure
**Maturity Driver:** Required

**Description:**
Code is structured for readability and low complexity, avoiding oversized classes/methods.

**Best Practices:**
Keep cyclomatic complexity bounded; factor shared logic; remove dead code and commented-out blocks.

**Questions:**

1. Is cyclomatic complexity kept within reasonable bounds, with no oversized God classes or methods? *(Weightage: Medium)*
2. Is code duplication minimized and shared logic factored into reusable units? *(Weightage: Medium)*
3. Is dead code (unused functions, unreferenced imports, commented-out blocks) kept out of the codebase? *(Weightage: Low)*

---

#### Coding Standards & Tooling
**Maturity Driver:** Required

**Description:**
Consistent style and idioms enforced through automated tooling.

**Best Practices:**
Configure and enforce a linter and auto-formatter in CI; follow language-idiomatic conventions.

**Questions:**

1. Is a linter configured and enforced (ideally in CI)? *(Weightage: High)*
2. Is an auto-formatter configured for consistent code style? *(Weightage: Medium)*
3. Does the code follow language-idiomatic conventions consistently? *(Weightage: Medium)*

---

#### Technical Debt Management
**Maturity Driver:** Nice to have

**Description:**
Technical debt is tracked and kept under control rather than accumulating silently.

**Best Practices:**
Track TODO/FIXME/HACK markers; avoid or migrate deprecated APIs and libraries.

**Questions:**

1. Are TODO/FIXME/HACK markers tracked and kept to a manageable level? *(Weightage: Low)*
2. Is deprecated API or library usage avoided or actively being migrated? *(Weightage: Medium)*

---

## 8. Testing & Quality Assurance

### 8.1. Testing & Quality Assurance

#### Test Coverage
**Maturity Driver:** Mandatory

**Description:**
A meaningful automated test suite covers critical behavior, enforced by a coverage gate.

**Best Practices:**
Maintain unit + integration tests; measure coverage and gate on a threshold; cover critical paths.

**Questions:**

1. Is there a meaningful automated test suite spanning unit and integration tests? *(Weightage: High)*
2. Is code coverage measured and enforced by a threshold gate? *(Weightage: High)*
3. Are critical paths (auth, data mutations, external calls) covered by tests? *(Weightage: High)*

---

#### Test Quality & Isolation
**Maturity Driver:** Required

**Description:**
Tests are reliable, isolated, and assert meaningful behavior.

**Best Practices:**
Avoid shared mutable state and order dependence; assert behavior rather than over-mocking.

**Questions:**

1. Are tests isolated and free of shared mutable state or order dependence? *(Weightage: Medium)*
2. Do tests assert meaningful behavior rather than over-mocking implementation details? *(Weightage: Medium)*

---

#### Test Types & CI Gate
**Maturity Driver:** Required

**Description:**
Multiple test types run automatically and block merges on failure.

**Best Practices:**
Include integration/e2e tests beyond unit tests; enforce a CI test gate.

**Questions:**

1. Are end-to-end or integration tests present beyond unit tests? *(Weightage: Medium)*
2. Does CI block merges on test failure? *(Weightage: High)*

---

## 9. Data Architecture & Management

### 9.1. Data Architecture

#### Schema Design Quality
**Maturity Driver:** Required

**Description:**
Database schema/ORM models are well-structured, consistently named, and appropriately indexed.

**Best Practices:**
Use consistent naming; define indexes for common queries; apply nullability/constraints intentionally.

**Questions:**

1. Are database schemas or ORM models well-structured with consistent naming conventions? *(Weightage: Medium)*
2. Are appropriate indexes defined for common query patterns? *(Weightage: Medium)*
3. Is nullability and constraint discipline applied intentionally rather than by default? *(Weightage: Low)*

---

#### Migration Management
**Maturity Driver:** Mandatory

**Description:**
Schema changes are managed by a versioned, source-controlled migration tool.

**Best Practices:**
Use Flyway/Liquibase/Alembic/Knex/Prisma/EF Migrations; commit migrations; make them reversible.

**Questions:**

1. Are schema changes managed by a versioned migration tool (Flyway, Liquibase, Alembic, EF Migrations, etc.)? *(Weightage: High)*
2. Are migrations committed to source control and reversible where feasible? *(Weightage: Medium)*

---

#### Data Access Patterns
**Maturity Driver:** Required

**Description:**
Data access is consistent, transactional, and uses pooled connections.

**Best Practices:**
Keep transaction boundaries tight; configure connection pooling; use a consistent repository/ORM approach.

**Questions:**

1. Are transaction boundaries correct and tightly scoped? *(Weightage: Medium)*
2. Is connection pooling configured with sensible limits? *(Weightage: Medium)*
3. Is the data-access approach consistent (repository/ORM) rather than raw queries scattered across business logic? *(Weightage: Medium)*

---

#### Multi-tenancy & Data Isolation
**Maturity Driver:** Nice to have

**Description:**
Tenant data is isolated with no risk of cross-tenant leakage.

**Best Practices:**
Enforce tenant scoping (row-level/schema/db-per-tenant); guard queries against missing tenant filters.

**Questions:**

1. If the system is multi-tenant, is tenant isolation enforced with no cross-tenant data-leakage risk? *(Weightage: High)*

---

#### Audit Trails & Data Lifecycle
**Maturity Driver:** Required

**Description:**
Data changes are auditable and lifecycle/retention is managed.

**Best Practices:**
Capture created/updated/by and change history; apply soft-delete consistently; define retention/purge.

**Questions:**

1. Are audit fields (created/updated/by) and change history captured where needed? *(Weightage: Medium)*
2. Is a data retention or purge strategy in place rather than unbounded growth? *(Weightage: Low)*

---

#### Backup & Disaster Recovery
**Maturity Driver:** Mandatory

**Description:**
Data is protected by backups with defined recovery objectives.

**Best Practices:**
Automate backups with retention; define RPO/RTO; document and test recovery procedures.

**Questions:**

1. Is there a documented or automated backup strategy with defined retention? *(Weightage: High)*
2. Are RPO/RTO targets defined and recovery procedures documented? *(Weightage: Medium)*

---

## 10. Security Posture

### 10.1. Security Posture

#### Authentication & Credential Security
**Maturity Driver:** Mandatory

**Description:**
Authentication uses a vetted mechanism and credentials are stored safely.

**Best Practices:**
Use OAuth2/OIDC/JWT/session with proper expiry and rotation; hash passwords with bcrypt/argon2/PBKDF2.

**Reference:** https://owasp.org/Top10/

**Questions:**

1. Is authentication implemented with a vetted mechanism (OAuth2/OIDC/JWT/session) and proper token expiry? *(Weightage: High)*
2. Are passwords hashed with a strong algorithm (bcrypt/argon2/PBKDF2) and never stored in plaintext/MD5/SHA1? *(Weightage: High)*

---

#### Secrets & Configuration Security
**Maturity Driver:** Mandatory

**Description:**
No secrets are committed; they are sourced from a manager and excluded from artifacts.

**Best Practices:**
Keep secrets out of code/images; use a vault/manager or env injection; exclude secret files via ignore lists.

**Questions:**

1. Is the codebase free of hardcoded secrets (API keys, passwords, connection strings, tokens)? *(Weightage: High)*
2. Are secrets sourced from a manager/vault or injected via environment rather than committed? *(Weightage: High)*
3. Do .gitignore/.dockerignore exclude secret and credential files? *(Weightage: Medium)*

---

#### OWASP Top 10 Coverage
**Maturity Driver:** Mandatory

**Description:**
Common web risks (access control, injection, misconfiguration) are mitigated.

**Best Practices:**
Enforce server-side authorization; parameterize queries; disable debug endpoints and verbose client errors.

**Reference:** https://owasp.org/Top10/

**Questions:**

1. Is access control enforced server-side, with no broken or object-level authorization gaps? *(Weightage: High)*
2. Are injection risks mitigated via parameterized queries and safe APIs? *(Weightage: High)*
3. Is security misconfiguration avoided (no debug endpoints, default credentials, or verbose errors to clients)? *(Weightage: Medium)*

---

#### Security Headers & Transport
**Maturity Driver:** Required

**Description:**
Traffic is protected by security headers, TLS, and restricted CORS.

**Best Practices:**
Set CSP/HSTS/X-Content-Type-Options; enforce TLS minimum version; restrict CORS origins.

**Questions:**

1. Are HTTP security headers configured (CSP, HSTS, X-Content-Type-Options, etc.)? *(Weightage: Medium)*
2. Is TLS enforced with a sane minimum version and CORS restricted (no blanket wildcard with credentials)? *(Weightage: High)*

---

#### Input Validation & Injection Prevention
**Maturity Driver:** Mandatory

**Description:**
Inputs are validated and outputs encoded to prevent injection/XSS.

**Best Practices:**
Validate/sanitize at trust boundaries; encode output; validate file uploads and deserialization.

**Questions:**

1. Is input validated and sanitized at trust boundaries? *(Weightage: High)*
2. Is output encoding applied to prevent XSS where applicable? *(Weightage: Medium)*

---

#### PII & Data Privacy
**Maturity Driver:** Required

**Description:**
Personal data is protected and privacy rights are supported.

**Best Practices:**
Encrypt PII in transit and at rest; provide consent and right-to-erasure where regulated.

**Questions:**

1. Is PII encrypted both in transit and at rest? *(Weightage: High)*
2. Are privacy mechanisms (consent, right-to-erasure) present where regulated data is handled? *(Weightage: Medium)*

---

#### Container & IaC Security
**Maturity Driver:** Required

**Description:**
Containers and infrastructure follow least-privilege, hardened configuration.

**Best Practices:**
Run containers as non-root with pinned base images; avoid secrets in layers; least-privilege IaC.

**Questions:**

1. Does the container run as non-root with a pinned base image and no secrets baked into layers? *(Weightage: High)*
2. Do infrastructure manifests apply least privilege (no wildcard IAM, no 0.0.0.0/0 exposure, resource limits set)? *(Weightage: Medium)*

---

## 11. Reliability & Operations

### 11.1. Reliability & Operations

#### Error Handling
**Maturity Driver:** Mandatory

**Description:**
Errors are handled consistently with no silent swallowing and graceful shutdown.

**Best Practices:**
Avoid empty catch blocks; add global handlers; handle SIGTERM with connection draining.

**Questions:**

1. Is error handling consistent, with no silent error swallowing (empty catch/except blocks)? *(Weightage: High)*
2. Are global error handlers or unhandled-rejection catchers in place? *(Weightage: Medium)*
3. Is graceful shutdown handled (SIGTERM, connection draining, in-flight request completion)? *(Weightage: Medium)*

---

#### Observability — Three Pillars
**Maturity Driver:** Mandatory

**Description:**
Logs, metrics, and traces are present and correlated.

**Best Practices:**
Use structured logging with disciplined levels; export metrics; correlate via trace/correlation IDs.

**Questions:**

1. Is structured logging used with disciplined levels and no sensitive data leakage? *(Weightage: High)*
2. Are metrics instrumented and exported (Prometheus/StatsD/OpenTelemetry/APM)? *(Weightage: High)*
3. Are logs, metrics, and traces correlated via trace/correlation IDs end-to-end? *(Weightage: Medium)*

---

#### Resilience Patterns
**Maturity Driver:** Mandatory

**Description:**
Outbound calls are protected by timeouts, retries, breakers, and fallbacks.

**Best Practices:**
Set timeouts on every dependency; add retries with backoff/jitter and circuit breakers; define fallbacks.

**Questions:**

1. Do outbound calls have timeouts on every dependency (HTTP, DB, cache, queue)? *(Weightage: High)*
2. Are retries with backoff/jitter and circuit breakers used for unstable dependencies? *(Weightage: High)*
3. Is fallback or degraded-mode behavior defined for external service failures? *(Weightage: Medium)*

---

#### Health & Readiness
**Maturity Driver:** Mandatory

**Description:**
Liveness/readiness endpoints report real dependency health.

**Best Practices:**
Expose liveness and readiness probes; verify critical dependencies in readiness.

**Questions:**

1. Are liveness and readiness endpoints exposed? *(Weightage: High)*
2. Do health checks verify critical downstream dependencies? *(Weightage: Medium)*

---

#### Load & Chaos Testing
**Maturity Driver:** Nice to have

**Description:**
Performance and failure modes are validated proactively.

**Best Practices:**
Add load/stress tests (k6/Locust/JMeter/Gatling); use chaos/fault injection.

**Questions:**

1. Are load or stress tests present (k6, Locust, JMeter, Gatling)? *(Weightage: Medium)*
2. Is chaos or fault-injection testing used to validate resilience? *(Weightage: Low)*

---

#### Feature Flags & Rollout
**Maturity Driver:** Nice to have

**Description:**
Risky changes ship safely behind flags with kill switches.

**Best Practices:**
Use a feature-flag system for gradual rollout and kill switches.

**Questions:**

1. Is a feature-flag mechanism used for safe rollout and kill switches? *(Weightage: Medium)*

---

## 12. Performance & Scalability

### 12.1. Performance & Scalability

#### Performance Hotspots
**Maturity Driver:** Required

**Description:**
Request paths avoid common performance pitfalls.

**Best Practices:**
Eliminate N+1 queries; paginate unbounded lists; offload CPU-heavy work from request handlers.

**Questions:**

1. Is the data layer free of N+1 query patterns (batching/DataLoader/joins used)? *(Weightage: Medium)*
2. Are unbounded list operations avoided in critical paths via pagination? *(Weightage: Medium)*
3. Are CPU-intensive operations offloaded out of synchronous request handlers? *(Weightage: Medium)*

---

#### Database Performance
**Maturity Driver:** Required

**Description:**
Queries are optimized and large result sets handled efficiently.

**Best Practices:**
Use indexes and projections; avoid full scans and fat selects; stream/paginate large results.

**Questions:**

1. Are queries optimized with appropriate indexes and projections (no full scans or fat selects)? *(Weightage: Medium)*
2. Are large result sets streamed or paginated rather than loaded wholesale? *(Weightage: Medium)*

---

#### Caching Strategy
**Maturity Driver:** Required

**Description:**
Expensive reads are cached with a clear invalidation strategy.

**Best Practices:**
Cache expensive, frequently-read, rarely-changing data; define TTL/event-driven invalidation.

**Questions:**

1. Is caching applied to expensive, frequently-read, rarely-changing data? *(Weightage: Medium)*
2. Is there a clear cache invalidation strategy (TTL or event-driven)? *(Weightage: Medium)*

---

#### Async & Concurrency
**Maturity Driver:** Required

**Description:**
Long operations are async and pools are sized appropriately.

**Best Practices:**
Offload long work to queues/workers; size thread/connection pools sensibly.

**Questions:**

1. Are long-running operations handled asynchronously (queues, workers, background jobs)? *(Weightage: Medium)*
2. Are thread and connection pools sized appropriately? *(Weightage: Medium)*

---

#### Scalability
**Maturity Driver:** Mandatory

**Description:**
The service scales horizontally without state coupling.

**Best Practices:**
Keep services stateless; avoid sticky sessions and local filesystem coupling.

**Questions:**

1. Is the service horizontally scalable (stateless, no sticky sessions or local filesystem coupling)? *(Weightage: High)*

---

#### Dependency Health
**Maturity Driver:** Nice to have

**Description:**
Dependencies are current and update automation is in place.

**Best Practices:**
Keep dependencies reasonably current; avoid unmaintained packages; automate updates.

**Questions:**

1. Are dependencies reasonably current and free of unmaintained or abandoned packages? *(Weightage: Medium)*
2. Is automated dependency update tooling configured (Dependabot, Renovate)? *(Weightage: Low)*

---

## 13. Developer Experience & Delivery

### 13.1. Developer Experience

#### Git Workflow & Version Control
**Maturity Driver:** Required

**Description:**
Source control follows a clear, protected, well-versioned workflow.

**Best Practices:**
Use a clear branching strategy; enforce branch protection and reviews; tag releases with changelogs.

**Questions:**

1. Is a clear branching strategy followed with consistent branch naming? *(Weightage: Medium)*
2. Are branch protection, required reviews, and status checks enforced? *(Weightage: High)*
3. Are releases tagged with changelogs and semantic versioning? *(Weightage: Medium)*

---

#### Local Development Setup
**Maturity Driver:** Required

**Description:**
A new engineer can run the app locally quickly from documented steps.

**Best Practices:**
Provide setup docs (README/CONTRIBUTING/Makefile/devcontainer); local deps via compose; complete .env.example.

**Questions:**

1. Is there a documented local setup path (README, CONTRIBUTING, Makefile, or devcontainer)? *(Weightage: High)*
2. Is local dependency orchestration provided (docker-compose or equivalent)? *(Weightage: Medium)*
3. Is an .env.example (or equivalent) present and complete? *(Weightage: Medium)*

---

#### CI/CD Pipeline Quality
**Maturity Driver:** Mandatory

**Description:**
The pipeline automates quality stages and supports safe deployment.

**Best Practices:**
Automate lint/test/security-scan/build; automate deployment with one-command rollback.

**Questions:**

1. Does the pipeline automate lint, test, security-scan, and build stages? *(Weightage: High)*
2. Is production deployment automated with a one-command rollback path? *(Weightage: Medium)*

---

#### Documentation Quality
**Maturity Driver:** Required

**Description:**
Documentation lets engineers understand and operate the system.

**Best Practices:**
Keep an accurate README (purpose/setup/usage/architecture); add ADRs and runbooks.

**Questions:**

1. Does the README cover purpose, setup, usage, and architecture accurately and up to date? *(Weightage: High)*
2. Are Architecture Decision Records (ADRs) and operational runbooks present? *(Weightage: Low)*

---

#### DORA Metrics
**Maturity Driver:** Nice to have

**Description:**
Delivery performance reflects elite/high DORA benchmarks.

**Best Practices:**
Optimize deployment frequency, lead time, change-failure rate, and MTTR.

**Reference:** https://dora.dev/

**Questions:**

1. Is deployment frequency high (frequent, automated production releases)? *(Weightage: Medium)*
2. Is lead time for changes short (a fast commit-to-production path)? *(Weightage: Medium)*
3. Are change-failure rate and MTTR controlled (rollbacks, alerting, runbooks)? *(Weightage: Medium)*

---

#### Developer Tooling
**Maturity Driver:** Nice to have

**Description:**
Local tooling automates quality and common tasks.

**Best Practices:**
Use pre-commit hooks (lint/format/test) and a task runner/Makefile.

**Questions:**

1. Are pre-commit hooks configured (lint/format/test on commit)? *(Weightage: Low)*
2. Is a task runner or Makefile provided for common operations? *(Weightage: Low)*

---

## 14. AI/ML & LLM

### 14.1. AI/ML & LLM

#### AI/ML Stack
**Maturity Driver:** Nice to have

**Description:**
AI/ML components and providers are clearly declared and versioned.

**Best Practices:**
Declare ML libraries, models, and LLM providers with versions; track model artifacts.

**Questions:**

1. If AI/ML is used, are libraries, models, and providers clearly declared and versioned? *(Weightage: Medium)*

---

#### LLM Integration Quality
**Maturity Driver:** Required

**Description:**
LLM usage is safe, validated, and resilient.

**Best Practices:**
Version-control/templated prompts; sanitize user input against prompt injection; validate output; retry/fallback.

**Questions:**

1. Are prompts version-controlled and templated rather than hardcoded inline? *(Weightage: Medium)*
2. Are user-supplied inputs sanitized to mitigate prompt injection? *(Weightage: High)*
3. Is LLM output validated before use, with retry/backoff and a fallback? *(Weightage: Medium)*

---

#### RAG Pipeline Quality
**Maturity Driver:** Nice to have

**Description:**
Retrieval is correct, consistent, and tenant-isolated.

**Best Practices:**
Scope retrieval to authorized docs per tenant; keep chunking/embedding consistent; mitigate hallucination.

**Questions:**

1. Is retrieval scoped to authorized documents per user/tenant with no cross-tenant leakage? *(Weightage: High)*
2. Are chunking and embedding consistent between indexing and retrieval, with hallucination mitigation? *(Weightage: Medium)*

---

#### MLOps & Evaluation
**Maturity Driver:** Nice to have

**Description:**
Models are tracked, evaluated, and monitored in production.

**Best Practices:**
Use experiment tracking and a model registry with promotion; add eval/regression tests and drift detection.

**Questions:**

1. Is there experiment tracking and a model registry with promotion stages? *(Weightage: Medium)*
2. Are there regression/evaluation tests for model quality and drift detection in production? *(Weightage: Medium)*

---
