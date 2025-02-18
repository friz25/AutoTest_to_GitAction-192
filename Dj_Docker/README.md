## INSTALLATION STEPS
~ Create .env file for single service (see .env.dist)
- npm i (manually in each microservice)
- composer install (admin service)
- docker-compose up -d rabbitmq
- docker-compose up -d redis
- docker-compose up -d adminer
- docker-compose up -d postgres
- docker-compose up -d loggerDB
- docker-compose up -d logger
- docker-compose up -d mediaDB
- docker-compose up -d media
- docker-compose up -d mailerDB
- docker-compose up -d mailer
- docker-compose up -d generalDB
- docker-compose up -d general
- docker-compose up -d phpfpm
- docker-compose up -d admin
- docker-compose up -d taskDB
- docker-compose up -d task

## HELPERS

## Docker console install soft
- apt-get update
- apt-get install htop

## PM2
- pm2 status
- pm2 start <service_name>
- pm2 logs
- pm2 restart <id>
- pm2 delete <id>
- pm2 monit
## Open BASH/CLI in docker-container
- docker exec -u root -it <id> bash
- docker exec -u root -it <id> /bin/sh
## Show all containers
- docker ps -a
## Show all active containers
- docker ps
### Docker Volumes (show ids, info by id, remove by id)
- docker volume ls
- docker volume inspect <id_volume>
- docker volume rm <id_volume>
## Statistics of docker usage memory
- docker stats
### Stop or remove the containers
- docker stop <containerId>
- docker-compose rm -s -v <containerName>
- docker-compose rm -f
- docker kill <containerName>
### Rebuild container without cache
- docker-compose up -d --no-deps --build <service_name>
### Clear docker_cache
- docker system prune -a