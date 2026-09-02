# fleet-recall-service -- COPY-based image for anyone who prefers a built image over bootstrap.sh.
#
#   docker build -t fleet-recall-service -f scripts/fleet-recall-service/Dockerfile scripts
#   docker run --rm -p 8080:8080 -e RECALL_API_TOKEN=... -e QDRANT_URL=... (see README.md) fleet-recall-service
#
# Build context is scripts/ so both the package and the service dir are copied.  Stdlib only:
# no pip install step.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app
COPY fleet_rag /app/fleet_rag
COPY fleet-recall-service /app/fleet-recall-service

RUN useradd --system --uid 10001 --no-create-home recall \
 && rm -rf /app/fleet_rag/__pycache__ /app/fleet_rag/tests/__pycache__
USER recall

EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
  CMD python3 -c "import os,sys,urllib.request;sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:%s/health' % os.environ.get('PORT','8080'),timeout=5).status==200 else 1)"

CMD ["python3", "/app/fleet-recall-service/server.py"]
