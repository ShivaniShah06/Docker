## Docker Registry

- It is a central repository for all the docker images
- `docker run nginx` :
     
     - nginx - Image/repository name
     - It is actually nginx/nginx: If you don't provide a user/account name before image name, it assumes that they are the same
     - Since we are explicitly not mentioning the location from where the image needs to be pulled, it is pulled from its default docker repository called docker hub: `docker.io/nginx/nginx`

## Private registry

- You can have a webapp which you don't want public to use. In that case, you can have a private repository which needs credentials to access it
- You will first have to login to it using command:
      
          $docker login <private-registry.io>

- And then run your app:
 
          $docker run <private-registry.io/apps/internal-app>

          NOTE: If you run above command without logging into the private registry, then you will get an error "image not found!"

## Deploying your own private registry within an organization

- Docker registry is itself an application and is available as an image `registry` and it exposes the API on port 5000

       $docker run -d -p 5000:5000 --name registry registry:2
  Now you have your own registry running on port 5000

- Push your own image to your private registry - use `tag` command to tag your image with private registry URL in it

        $docker image tag <my-image> <localhost:5000/my-image>

- Push the image to your local private registry

        $docker push localhost:5000/<my-image>

- Pull the image from private registry
     - If accessing from the same host
  
           $docker pull <localhost:5000/my-image>

     - If accessing from the different host in the environment then use the ip or domain name of the docker host
  
            $docker pull <192.168.56.100:5000/my-image>