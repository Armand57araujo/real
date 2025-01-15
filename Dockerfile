# # Base image
# FROM python:3.9

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container
# COPY backend/requirements.txt .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the application code into the container
# COPY . .

# # Expose the port the app runs on
# EXPOSE 8000

# # Command to run the app
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# FROM python:3.10

# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
