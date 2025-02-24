# Use official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirement.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]