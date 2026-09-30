# 1. Use a lightweight base image as requested by the assignment
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /home/data

# 3. Copy your Python script and text files into the container
COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .

# 4. Create the required output directory
RUN mkdir -p /home/data/output

# 5. Tell Docker how to run your Python script when the container starts
CMD ["python", "script.py"]
