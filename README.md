# <center>MARCELLO COLETTI</center>
## <center>UNDERGRADUATE THESIS</center>

Thsi is how I'd like to show my replicable working paper for my undergradute thesis. I wanted a dockerized enviroment to show my results in Python Dash library.

This code requires docker for windows, and docker compose-up for linux

 To use the docker file, you need to run the following commands in this order:

- "docker build -t mc_undergradute_thesis ." This will create the docker container named 'mc_undergradute_thesis', but you can change
that name. This command only needs to be ran once instead you remove the container, or something were wrong during the container creation.

- "docker run mc_undergradute_thesis" Use this after tha container build is complete. Every time you need to use the repository,
what you need to do is on this command.

- Use "control+c" to stop the container.

The container is using the port 2023, you can change it or stop other services at that port