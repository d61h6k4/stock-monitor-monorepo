.PHONY: clean

clean:
	docker exec -it redpanda-0 rpk topic delete events
	docker exec -it redpanda-0 rpk topic delete features
	docker compose down --remove-orphans --volumes
	rm -rf volumes
	

infrastructure:
	docker compose up -d --force-recreate --remove-orphans --detach

produce:
	docker build -t yfinance-client -f yfinance-client/Dockerfile .
	mkdir volumes
	# network vai-development_vai_network is defined in docker-compose.yml
	docker run -d --network stock-monitor_sm_network -v `pwd`/volumes:/volumes yfinance-client

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

