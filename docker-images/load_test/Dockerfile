FROM python:3.9-slim

# Install requests library
RUN pip install requests

# Copy the load test script
COPY load_test.py /load_test.py

# Set the entrypoint to run the script
ENTRYPOINT ["python", "/load_test.py"]
