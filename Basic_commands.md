1. Run container from an image if it exists on the host   

       $docker run <image_name>

  NOTE: If the image does not exist on the host, docker will go to docker hub and pull the image down.

2. List running containers and some basic information

        $docker ps

3. List running and previously stopped/exited containers

       $docker ps -a

4. Stop a container

        $docker stop <container_name/container_id>

        NOTE: Container name or Container ID can be found from `docker ps` command's output

5. Remove a container from the `ps` output permanently

        $docker rm <container_name/container_id>

6. List images on host

        $docker images

7. Remove images from host

        $docker rmi <image_name>

8. Pull image from docker hub (do not run it)

       $docker pull <image_name>

9. Append a command

       $docker run <image_name> <command (eg: sleep 5)
       >

10. Execute a command on a container

        $docker exec <container_name> <command (eg: cat /etc/hosts)>

11. Run a container in foreground - shows stdout on your screen

        $docker run <image_name>

12. Run a container in background/backend

        $docker run -d <image_name>

    NOTE: -d will run this in background. Run `docker ps` to see the running container

13. To attach a detached container back

        $docker attach <container_id/container_name>

14. To run an application with old image version

        $docker run <image_name:version>

        NOTE: image_name:version will be added as a tag for this container. If no version is specified, the default tag is `latest`

15. For interactive applications to be containerized, run below command to run interactive applications on docker

        $docker run -it <image_name>

        NOTE: Here, `i` stands for interactive mode and `t` stands for terminal

16. Map ports on docker host and container to serve your webapplication outside docker host

        $docker run -p <docker_host_port>:<container_port> <image_name>

17. Map volume to a directory on docker host (outside container)

        $docker run -v <path_to_directory_on_docker_host>:<path_to_directory_on_container> <image_name>

    NOTE: This will mount the external directory to a folder inside the docker container and so, all your data will be saved on docker host and will not be lost even after deleting the docker container

18. Inspect a container to see additional details about it

         $docker inspect <container_name/container_id>

19. Check container logs

         $docker logs <container_name/container_id>

20. Check size of your docker file steps

          $docker history <image_name>

21. Build a docker file

          $docker build . -f <file_name> -t <image_name>

    NOTE: All the builds are cached by docker. So if it fails in one of the steps, once you fix the issue, it restarts from where it left off. The same is true if you add new steps in the docker file

22. Define environment variables

          $docker run -e <ENV_VARIABLE>=<VALUE> <image_name>

          NOTE: You can check added env variable using `docker inspect` command

23. Limit CPU usage of a container - will ensure that the CPU used by the container will never go above 50%

           $docker run --cpus=.5 <image_name>

24. Limit memory usage of a container - will ensure that the memory used by the container will never go above 100m

           $docker run --memory=100m <image_name>

25. Create a volume on docker host

           $docker volume create <volume_name>

    This will create a new volume folder in location `/var/lib/docker`

26. Map the volume on docker host with volume on container for persistent data storage (data will not be lost even after the container has been terminated)

VOLUME MOUNT: Mounts volume from a volume directory (`/var/lib/docker`)

         $docker run -v <newly_created_volume>:<location_on_docker_container> <image_name>

OR

         $docker run --mount type=<bind/volume/tmpfs>,source=<location_on_host>,targer=<location_on_container>

NOTE: This newly created volume will by default exist in `/var/lib/docker` location and will be assumed to be in there if no path is mentioned

27. If you have a folder with data in a different location, then mention the path to that folder in the command to mount it with the volume inside a container

BIND MOUNT: Mounts a directory from any location on the docker host

        $docker run -v <location_to_directory>:<location_on_docker_container> <image_name>

28. Get information about docker installed on the system

        $docker info | more

29. Get exact disk usage of a docker image

        $docker system df

    Use `-v` option to list containers running through the image along with disk usage information

30. There are 3 types of networks in docker - Bridge, none, and host. Bridge is the default network type
Create a bridge network

        $docker network create --driver bridge --subnet <182.18.0.0/16> <network_name>

31. List all networks

        $docker network ls
    
    NOTE: Run `docker inspect <container_name/container_id>` to get details about network

* The built-in DNS server always runs at `127.0.0.11`

