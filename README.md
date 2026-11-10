# Resilient Edge Telemetry Gateway for DIL Environments

An immutable offline-first tactical edge gateway designed for DIL Operational Environments

## System Domain & Utility

* **Defence Application:** Resilient field tracking, remote sensor mesh logging, and drone/UGV telemetry ingestion over unstable tactical SATCOM or radio backhauls.
* **Commercial Dual-Use:** Precision agriculture telemetry, maritime vessel monitoring, and disaster-relief logistics tracking under complete infrastructure blackouts.

## Technical Differentiators
1. **Zero Data Loss Assurance:** Utilizes an atomic transactional SQL Write-ahead logging implementation to store telemetry locally when upstream signals drop.
2. **Deterministic & Hardened Footprint:** Multi-stage Docker builds compiled out of OCI-compliant `python:3.11-slim` runtimes, stripped of shell utilities, running under exclusive non-root privileges (`UID 10001`).
3. **Transactional Reconciliation Engine:** Implements a strict acknowledgement-first drainage routine. Buffered records are deleted from the local database only after an HTPP 200 OK delivery confirmation from the HQ controller.

## Project Development Tracking & Roadmap

### Phase 1: Core Engine & Container Security Hardening
- [x] Write hardened, multi-stage, multi-architecture `Dockerfile.gateway`.
- [x] Build core edge resilience engine (`app.py`) featuring transactional SQLite fallback queuing.
- [ ] Implement integrated artifact scanning pipeline with `Trivy` to target zero open CVEs.

### Phase 2: Live Visualization & Network Emulation Framework
- [ ] Build a streamlit Dashboard (`ui.py`) visualizing real-time system (Buffer Size, Packet Delivery Rates, Signal Stability).
- [ ] Deploy a Mock HQ Ingest server to gracefully accept and acknowledge incoming telemetry streams.
- [ ] Author a network toggle script utilizing Linux `tc` (Traffic Control) or a Virtual network interface switch to simulate tactical blackout.

### Phase 3: Declarative Local Orchestration (K3s/K3d Deployment)

- [ ] Write a local environment setup scripts (`K3s-setup.sh`) to build a localized edge kubernetes node cluster.
- [ ] Construct declarative Kubernetes manifests (`deployment.yaml`, `storage.yaml`) provisioning local `hostPath` persistent volumes.
- [ ] Implement strict Kubernetes Network Policies ensuring zero leakage out if the edge enclave.

### Phase 4: Validation & Deficit Testing Proof

- [ ] Execute an automated 10-minute network volatility stress test.
- [ ] Record and document execution logs proving 100% telemetry capture accuracy before, during, and after connection disruptions.