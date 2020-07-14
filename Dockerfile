# Use the official image as a parent image.
FROM python:3

# Set the working directory.
WORKDIR /usr/src/app

# Copy the file from your host to your current location.
COPY requirements.txt ./

# Run the command inside your image filesystem.
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8080

# Run the specified command within the container.
CMD [ "python", "./sanctions_api.py" ]

# Copy the rest of your app's source code from your host to your image filesystem.

