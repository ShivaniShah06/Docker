## ENTRYPOINT VS COMMAND

- Command is what gets appended when you run `docker run <image_name>`
- ENTRYPOINT is what runs right after a container is created.
- If we specify both ENTRYPOINT and Command in a dockerfile, they will get appended and become a single command that will run after container gets created
- We can have a default command defined and can overwrite it while creating a container

### Scenario 1:
.
.
.

ENTRYPOINT ["sleep"]

CMD ["5"]

.
.
.

- If the user runs `docker run ubuntu` command here, the actual command that will run will be `docker run ubuntu sleep 5`
- If the user runs `docker run ubuntu 10` command here, the command that will run will be `docker run ubuntu sleep 10`

### Scenario 2:
.
.
.

ENTRYPOINT ["sleep"]

.
.
.

- If the user runs `docker run ubuntu 10`, then the actual command that runs will be `docker run ubunutu sleep 10`
- If the user does not give any argumet and runs `docker run ubuntu`, then the command will fail since no default value for command has been provided

### Scenario 3:
.
.
.

CMD ["sleep 5"]

.
.
.

- If the user runs `docker run ubuntu`, the command that runs will be `docker run ubuntu sleep 5`
- If the user runs `docker run ubuntu 10`, the command will fail because 10 will overwrite `sleep 5` CMD in dockerfile and we don't have ENTRYPOINT defined



