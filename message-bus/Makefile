start:
	docker compose  --project-name redpanda up -d
stop:
	docker exec -it redpanda-0 rpk topic delete events
	docker compose  --project-name redpanda down
