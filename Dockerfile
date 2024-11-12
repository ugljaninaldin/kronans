#Use an official Python runtime as a parent image
 FROM python:3.10-slim

# Set environment variables
 ENV PYTHONDONTWRITEBYTECODE=1
 ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
 WORKDIR /app

# Install dependencies
 COPY requirements.txt /app/
 RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
 COPY . /app/

# Collect static files
 RUN python manage.py collectstatic --noinput

# Expose port 8000
 EXPOSE 8000

# Run the application with Gunicorn (production-ready WSGI server)
 CMD ["gunicorn", "kronans.wsgi:application", "--bind", "0.0.0.0:8000"]

