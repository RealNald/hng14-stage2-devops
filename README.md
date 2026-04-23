# hng14-stage2-devops

A distributed job processing system consisting of a FastAPI backend, a Redis‑backed worker, and an Express frontend. All services run in Docker containers and communicate over an internal network.

## Prerequisites

- **Docker** (≥ 20.10) + **Docker Compose** (≥ 2.0) – [Install Docker](https://docs.docker.com/engine/install/)
- **Git** – to clone the repository
- **curl** / **jq** – for testing (optional, see health check verification)

## Quick Start (on a clean Ubuntu 22.04 / 24.04 machine)

```bash
# 1. Install Docker if not present
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker

# 2. Clone your public fork
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# 3. (Optional) Create .env from example – adjust if needed
cp .env.example .env
# The default values already work for local development

# 4. Start the full stack
docker compose up -d

# 5. Wait for all health checks to pass (30‑60 seconds)
watch docker compose ps
# Expected output: all services show "healthy"

#   What a successful startup looks like
Redis – Up (healthy); listens only on the internal Docker network.
API – Up (healthy); internal port 8000.
Worker – Up (healthy); continuously polls Redis.
Frontend – Up (healthy); maps host port 3000 → container 3000.

#            project structure
hng14-stage2-devops
├── api/               # FastAPI application
├── worker/            # Python worker with infinite loop
├── frontend/          # Express.js server
├── docker-compose.yml # Full stack definition
├── .env.example       # Template for environment variables
└── FIXES.md           # Bug documentation

#   Stopping the stack
docker compose down -v

#CI/CD pipeline
 GitHub Actions workflow (.github/workflows/ci-cd.yml) runs on every push.
Stages: lint → test → build → security scan → integration test → deploy
Deployments occur only on the main branch and use a rolling update with health checks.
