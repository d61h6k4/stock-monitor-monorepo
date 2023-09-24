# Global ARG, available to all stages (if renewed)
ARG WORKDIR="/app"

FROM python:3.11 AS builder

# Renew (https://stackoverflow.com/a/53682110):
ARG WORKDIR
ARG BUILDPLATFORM

# Don't buffer `stdout`:
ENV PYTHONUNBUFFERED=1
# Don't create `.pyc` files:
ENV PYTHONDONTWRITEBYTECODE=1

RUN \
if [ "$BUILDPLATFORM" = "linux/arm64" ]; \
then  wget --progress=dot:giga -N -P librdkafka/ https://github.com/confluentinc/librdkafka/archive/refs/tags/v2.0.2.tar.gz && \
  tar -xvf librdkafka/v2.0.2.tar.gz -C librdkafka/ && \
  mkdir /kafka && \
  cd librdkafka/librdkafka-2.0.2 && ./configure --prefix=/usr && make && make install; \
fi

RUN pip install poetry && poetry config virtualenvs.in-project true

WORKDIR ${WORKDIR}

COPY . ${WORKDIR}

RUN poetry install --only main

# App-specific settings:
ENTRYPOINT [ "./.venv/bin/python", "-m", "bytewax.run", "-r", "/cache" ]