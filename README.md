# Restful-web-service using DOCKER container

Created a Python Restful webservices using Flask and use docker to run this application.                              
First, docker need to be installed.

## Steps
1. Get inside the app folder in terminal                          
2. Build the docker image:                                           

      ```bash
      docker build -t flask-test-sample .
      ```
3. once the docker image is created, run the "flask-test-sample" in docker container                                                            
      ```bash
      docker run -d -p 5000:5000 flask-test-sample
      ```
4.Now, app will run locally. i.e, if it is run on normal terminal, address will be localhost else docker ip address.                   
  **GET request1**: Go to http://127.0.0.1:5000/gethotels/  to list all Hotels data.                              
  **GET request2**: Go to http://127.0.0.1:5000/gethotel/18/ for specific Hotels with id "18" (example: 18)         
  **GET request3**: Go to http://127.0.0.1:5000/gethotel/type/5/ for specific Hotels with  type "of highest rating" (example: 5)            
  
## COMMANDS (useful)
1. List all images: *docker images*
2. List all containers which are running inside the docker: *docker ps*
3. Stop all running containers: *docker stop $(docker ps -aq)*
4. Remove all containers: *docker rm $(docker ps -aq)*                    
5. Remove all docker images: *docker rmi $(docker images -q)*

  
