start:
	docker compose  --project-name redpanda up -d
	docker exec -it redpanda-0 rpk topic create events
	docker exec -it redpanda-0 rpk topic alter-config events --set cleanup.policy=delete
stop:
	docker compose  --project-name redpanda down
