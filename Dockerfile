FROM python:3.7.3-stretch

## Step 1:
# Create a working directory

## Step 2:
# Copy source code to working directory

## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
WORKDIR /home/devops

COPY app.py /home/devops
COPY model_data /home/devops/model_data
COPY output_txt_files /home/devops/output_txt_files 
COPY requirements.txt /home/devops

RUN pip install -r requirements.txt

## Step 4:
Expose 80 8000

## Step 5:
CMD ["/usr/local/bin/python", "app.py"]
