# Start with a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py

# Expose ports
EXPOSE 5000

# Set the command
CMD ["flask", "run", "--host=0.0.0.0"]