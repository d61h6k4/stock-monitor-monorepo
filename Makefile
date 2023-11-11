.PHONY: clean

clean:
	docker exec -it redpanda-0 rpk topic delete events
	docker exec -it redpanda-0 rpk topic delete features
	docker compose down --remove-orphans --volumes
	rm -rf cache

infrastructure:
	docker compose up -d --force-recreate --remove-orphans --detach --build
	mkdir cache

produce:
	docker build -t yfinance-client -f yfinance-client/Dockerfile .
	# network vai-development_vai_network is defined in docker-compose.yml
	docker run --env-file=.env -d --network stock-monitor_sm_network -v `pwd`/cache:/cache yfinance-client

produce-system:
	sudo systemctl start produce.service
	sudo systemctl enable produce.timer

update-crm:
	docker build -t crm -f crm/Dockerfile .
	# network vai-development_vai_network is defined in docker-compose.yml
	docker run --env-file=.env -it --network stock-monitor_sm_network -v `pwd`/cache:/cache crm

cot:
	docker build -t cot-client -f cot-client/Dockerfile cot-client
	# network vai-development_vai_network is defined in docker-compose.yml
	docker run --env-file=.env -d --network stock-monitor_sm_network cot-client

cot-system:
	sudo systemctl start cot.service
	sudo systemctl enable cot.timer