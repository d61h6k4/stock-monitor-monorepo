#!/bin/env bash

set -ex;

mkdir -p ${RECOVERY_DIR}

if [ -z "$(ls -A $RECOVERY_DIR)" ]; then
  ./.venv/bin/python -m bytewax.recovery ${RECOVERY_DIR} 1
fi

./.venv/bin/python -m bytewax.run -r ${RECOVERY_DIR} ${BYTEWAX_FLOW}