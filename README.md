[![CircleCI](https://circleci.com/gh/raghavendrak89/udacity_proj.svg?style=svg)](https://circleci.com/gh/raghavendrak89/udacity_proj)

## Project Overview

This is a lab project for what I have learnt so far with the Microservices as Scale using AWS & Kubernetes

### Project Tasks

I have operationalised the deployment of machine learning microservice using [kubernetes](https://kubernetes.io/), which is an open-source system for automating the management of containerized applications. In this project I have:
* Tested the project code using linting
  ```#!/bin/bash -eo pipefail
    . venv/bin/activate
      make lint
      # See local hadolint install instructions:   https://github.com/hadolint/hadolint
      # This is linter for Dockerfiles
      hadolint Dockerfile
      # This is a linter for Python source code linter: https://www.pylint.org/
      # This should be run from inside a virtualenv
      pylint --disable=R,C,W1203,W1202 app.py
      ------------------------------------

      Your code has been rated at 10.00/10

      CircleCI received exit code 0
```

* Completed a Dockerfile to containerize the application
* Deployed the containerized application using Docker and made prediction
* Improved the log statements in the source code for the application
* Configured Kubernetes and created a Kubernetes cluster
* Deployed a container using Kubernetes and made predictions
* Uploaded a complete Github repo to CircleCI and have tested the same. CircleCI status badge is updated with the repo



---

## Project Files
Dockerfile                          # Dockerfile for the app containerisation
Makefile                            # Make file for the app installation and linting
README.md                           # README explaining the project
app.py                              # Flask application
make_prediction.sh                  # Bash script to make prediction
model_data                          # Project modules
output_txt_files                    # Directory with docker and kubernetes outputs
requirements.txt                    # pip packages in requirements file
run_docker.sh                       # Bash script to build docker image and execute it
run_kubernetes.sh                   # Bash script to create kuberenete deployment
upload_docker.sh                    # Bash script to upload Docker image to git repo


---

## Setup the Environment

* Created a virtualenv and activated it
* Executed `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:                  `python app.py`
2. Executed Docker:             `./run_docker.sh`
3. Uploaded the Docker image:   `./upload_docker.sh`  
3. Run in Kubernetes:           `./run_kubernetes.sh`


### Kubernetes Steps

* Setup and Configure Docker locally
* Setup and Configure Kubernetes locally
* Create Flask app in Container
* Run via kubectl

### Output files

output_txt_files
├── docker_out.txt
└── kubernetes_out.txt

### Docker image:
docker pull raghavendrak/udacity_devops:latest
