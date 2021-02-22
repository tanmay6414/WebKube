# WebKube
First create a docker image using
sudo docker build -t <dockerhub-repo-name>/<image-name>:tag \n
eg : sudo docker build -t tanmay8898/webkube:v1
  
Run the docker image on local machine 
sudo docker run -p 8082:8082 tanmay8898/webkube:v1

For accesing web application 
URL : http://127.0.0.1:8082

----------------------------------------------------------
For kubernetes deployment 
kubectl apply -f Deployment_service.yaml

After successfull deployment access web application using
URL : http://127.0.0.1:30007

