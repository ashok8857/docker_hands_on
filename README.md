# This project is for doker better underStandig

Steps used to create docker container with more than one services
1. Create Doker file.
   * The Dockerfile uses DSL (Domain Specific Language) and contains instructions for generating a Docker  
     image. Dockerfile will define the processes to quickly produce an image
2. Create the compose file.
   * Docker Compose is a tool that helps you define and share multi-container applications. With Compose, you 
     can create a YAML file to define the services and with a single command, you can spin everything up or tear 
     it all down.

Run following commands:
* docker-compose up  

To update any container use below commands
* docker-compose build <container-name>
* docker-compose up -d <container-name>      