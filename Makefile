.PHONY: clean

clean:
	docker exec -it redpanda-0 rpk topic delete events
	docker exec -it redpanda-0 rpk topic delete features
	docker compose  --project-name redpanda --file message-bus/docker-compose.yml down
	rm .storage.json

message_bus:
	docker compose --project-name redpanda --file message-bus/docker-compose.yml up -d

produce:
	/Users/danilapetrov/Library/Caches/pypoetry/virtualenvs/yfinance-client-Y23vWbMW-py3.11/bin/yfinance_client --kafka_bootstrap_servers 0.0.0.0:19092

calculator:
	/Users/danilapetrov/Library/Caches/pypoetry/virtualenvs/calculator-o5s_v8mb-py3.11/bin/python -m bytewax.run "calculator.main:calculate_features()"

sink_to_db:
	/Users/danilapetrov/Library/Caches/pypoetry/virtualenvs/interavtive-data-consumer-c1FYRO9G-py3.11/bin/python -m bytewax.run "interavtive_data_consumer.flow:sink_to_db()"

install-backend:
	python3.11 -m poetry lock --directory /home/ubuntu/stock-monitor-monorepo/stock-monitor-backend
	python3.11 -m poetry install --directory /home/ubuntu/stock-monitor-monorepo/stock-monitor-backend

install-data:
	python3.11 -m poetry install --directory /home/ubuntu/stock-monitor-monorepo/stock-monitor-data

run-backend:
	sudo service stock-monitor-backend restart

monitor: install-data
	sudo service stock-monitor-monitor restart

backend: install-data install-backend run-backend

all: backend monitor

