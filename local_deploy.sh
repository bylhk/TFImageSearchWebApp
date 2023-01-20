docker build . -t pz/image_search:latest
# kubectl apply -f deployment.yaml
docker run --rm -p 5050:5050 pz/image_search:latest
