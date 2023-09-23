# Global ARG, available to all stages (if renewed)
ARG WORKDIR="/app"

FROM python:3.11 AS builder

# Renew (https://stackoverflow.com/a/53682110):
ARG WORKDIR


# Don't buffer `stdout`:
ENV PYTHONUNBUFFERED=1
# Don't create `.pyc` files:
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install poetry && poetry config virtualenvs.in-project true

WORKDIR ${WORKDIR}

COPY stock-monitor-data /stock-monitor-data
COPY yfinance-client ${WORKDIR}

RUN poetry install --only main

FROM python:3.11-slim

ARG WORKDIR

WORKDIR ${WORKDIR}

COPY --from=builder ${WORKDIR} .

# App-specific settings:
ENTRYPOINT [ "./.venv/bin/python", "-m", "yfinance_client" ]
CMD [ "--kafka_bootstrap_servers=redpanda-0:9092", "--storage=/volumes/.storage.json"]