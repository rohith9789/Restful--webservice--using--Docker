# Restful--webservice--using--Docker


Created a Python RESTful services using Flask and use docker to run this application.
First, docker need to be installed. Link: https://docs.docker.com/toolbox/toolbox_install_mac/
once docker installed we can see docker quick terminal on our system

Steps
Get inside the app folder in terminal

Build the docker image:

docker build -t flask-test-sample .
once the docker image is created, run the "flask-test-sample" in docker container

docker run -d -p 5000:5000 flask-test-sample
4.Now, app will run locally. i.e, if it is run on normal terminal, address will be localhost else docker ip address.
GET request1: Go to http://192.168.99.100:5000/getrestaurants/ to list all restaurants data.
GET request2: Go to http://192.168.99.100:5000/getrestaurants/22/ for specific restaurant with id "22" (example: 22)
GET request3: Go to http://192.168.99.100:5000/getrestaurants/type/pizza/ for specific restaurants with food type "Pizza" (example: pizza)

COMMANDS (useful)
List all images: docker images
List all containers which are running inside the docker: docker ps
Stop all running containers: docker stop $(docker ps -aq)
Remove all containers: docker rm $(docker ps -aq)
Remove all docker images: docker rmi $(docker images -q)
