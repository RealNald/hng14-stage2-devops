# ---------- Builder ----------
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---------- Final ----------
FROM python:3.12-slim

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

COPY --from=builder /root/.local /home/appuser/.local

WORKDIR /app
COPY worker.py .

ENV PATH=/home/appuser/.local/bin:$PATH

# Healthcheck using redis module (already installed)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import redis, os; r=redis.Redis(host=os.getenv('REDIS_HOST','localhost')); r.ping()" || exit 1

USER appuser
CMD ["python", "worker.py"]
