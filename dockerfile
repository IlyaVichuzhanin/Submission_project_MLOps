FROM apache/airflow:3.0.0

USER root

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir dvc dvc-s3 && \
    dvc config --global core.analytics false

# Initialize git and dvc
WORKDIR /opt/airflow
RUN git init && \
    dvc init --no-scm

# Add Python path to environment
ENV PATH="/home/airflow/.local/bin:${PATH}"