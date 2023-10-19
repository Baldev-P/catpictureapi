# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables for Python to run in unbuffered mode and prevent creating .pyc files
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory inside the container
WORKDIR /app

# Copy the project code into the container
COPY . /app

# Install system-level dependencies (if any)
RUN apt-get update #&& apt-get install -y some-package

# Create a virtual environment and activate it
RUN python3.11 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

# Install the project dependencies
RUN pip install -r requirements.txt

# Apply database migrations (you might need to customize this)
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose the port your application runs on
EXPOSE 8000

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
