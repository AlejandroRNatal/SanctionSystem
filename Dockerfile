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
EXPOSE 5000

# Run the specified command within the container.
# CMD [ "python3 -m","venv SanctionSystem",]
# CMD ["source", "SanctionSystem/bin/activate"]
# CMD ["pip install", "-r requirements.txt"]
CMD ["python3", "./Rest_API/sanctions_api.py" ]
# CMD ["python3","./Rest_API/cli.py"]

# Copy the rest of your app's source code from your host to your image filesystem.

