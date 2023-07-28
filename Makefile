
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
