docker build . -t pz/image_search:latest
docker run --rm -p 5050:5050 pz/image_search:latest
