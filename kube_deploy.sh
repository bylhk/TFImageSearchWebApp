eval $(minikube docker-env)
docker build . -t pz/image_search:latest
minikube image load pz/image_search:latest
minikube kubectl -- apply -f kube_deploy.yaml
echo $(minikube service imagesearch --url)
