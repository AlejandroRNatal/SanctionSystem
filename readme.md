# Running project Verbatim

## Requirements
- Python 3.6.x+
- Flask
- Hypothesis

## Note: This assumes working directory is root of project!
> In Linux: `~/path/to/project/`

> In Windows: `C:\Users\UserName\path\to\project\`

`cd SanctionSystem`

## To install requirements manually run:

`pip install -r requirements.txt`

## Running Unit Tests
`cd Rest_API`

`python TestStringSimilarity.py`

## Running CLI
` cd Rest_API`

` python cli.py`

## Running REST API

`cd Rest_API`

`python sanctions_api.py`

-----

## Data stored in local Sanctioned database

- Countries
  - USA
  - Iceland
  - Peru
- Individuals
  - Kristopher Doe
  - Jake Long
  - Jose Juan Rivera
- Organizations
  - Royal Arctic Line
  - Not Disney
  - Machu Pichu


-----

## Adding Data to database

> Open Rest_API/sample.csv with any text editor

> Add a line in format: {Individual},{Country},{Organization}

> Save the changes to the file

> Now we run the _database_setup.py_ script

`python Rest_API/database_setup.py`

> or if already in Rest_API folder

`python database_setup.py`


-----

## Docker Image

## In order to run this Docker app first you must pull the Python image
`docker pull python`

## Build Docker Image
`docker build --tag sanctionsystem:0.1a .`

## Running Docker Image

` sudo docker run --rm -d --network host --name ss sanctionsystem:0.1a`

> NOTE| THE FIX WAS FOUND HERE:

> <https://docs.docker.com/network/network-tutorial-host/>

## THIS IS FAKE, DOCS LIED TO ME

~`docker run --publish 5000:5000 --detach --name ss sanctionsystem:0.1a`~

## Use this command to check if port is free
` sudo nc localhost 5000 < /dev/null; echo $?`

> If result was a 0, then port is not available

## Stop Docker Image
`docker rm --force ss`

## DockerHub Image
> <https://hub.docker.com/repository/docker/ccgmagno/sherpa_module_2>

## To see the container running open a browser and type:
> <localhost:5000>


## SQL Viewer
> <https://inloop.github.io/sqlite-viewer/>
