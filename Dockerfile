FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY src/crypto_precos.py .

# Install necessary dependencies
RUN pip install requests

# Command to run the Python script
CMD ["python", "crypto_precos.py"]