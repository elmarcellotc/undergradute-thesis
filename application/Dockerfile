FROM python:3.10

# set working directory in container
WORKDIR /app

# Copy and install packages
COPY requirements.txt /
RUN python -m pip install --upgrade pip
RUN pip install --default-timeout=120 -r /requirements.txt

# Copy app folder to app folder in container
COPY . .
EXPOSE 2023

# Run locally
CMD ["python", "app.py"]