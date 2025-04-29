# Running the project in as a docker container (Linux Mint instructions)

1. Install docker engine: [Link to Docker instructions](https://docs.docker.com/engine/install/ubuntu/ "Link to docker instructions")
	tl;dr copy paste in your terminal
	```
		# Add Docker's official GPG key:
		sudo apt-get update
		sudo apt-get install ca-certificates curl
		sudo install -m 0755 -d /etc/apt/keyrings
		sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
		sudo chmod a+r /etc/apt/keyrings/docker.asc

	# Add the repository to Apt sources:
	echo \
	"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
	$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
	sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt-get update
	```

2. Open terminal in code directory.
3. Run `docker compose up --build`.
4. Containers should run automatically after building. Check localhost:8000 for Django server (it's gonna tell you the webpage is 0.0.0.0:8000 but it's not)

## After Building
Run `docker compose start` or `docker compose stop` to start and stop the containers.
Run `docker exec -it uboard-backend bash` to access terminal (and run commands) inside the container.