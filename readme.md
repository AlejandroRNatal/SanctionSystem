
# In order to run this Docker app first you must pull the Python image
> docker pull python

# TO Build and run the Docker image:
> docker build -t {name_of_our_python app}
> docker run -it --rm --name {running_app} {name_of_our_python app}