# Use the official Python image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if any)
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Command to run the app
CMD ["python", "./app.py"]


