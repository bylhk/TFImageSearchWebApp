FROM tensorflow/tensorflow:2.11.0

WORKDIR /image_search
COPY requirements.txt requirements.txt

USER root

RUN apt-get update -y \ 
 && python3 -m pip install --no-cache-dir -U pip \
 && python3 -m pip install --no-cache-dir -r requirements.txt \
 && rm -rf /var/lib/apt/lists/*

COPY app/ ./

RUN python preprocess.py

EXPOSE 5050

ENTRYPOINT ["python", "app.py"]
