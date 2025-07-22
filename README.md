# ETL Project - Dog API 

This is an **ETL (Extract, Transform, Load) project** designed to consume data from the Dog API, process it, and load it into a PostgreSQL database. The entire workflow is orchestrated using **Apache Airflow** and deployed via **Docker Compose**, emphasizing robust logging for monitoring and checkpoints.

## Project Structure

This project leverages Airflow's structure within a Dockerized environment:

* **`airflow-docker/`**: Contains all the necessary files for the Airflow and PostgreSQL Docker setup.
    * **`dags/`**:
        * `main.py`: This is the main Airflow DAG (Directed Acyclic Graph) file. It defines the ETL pipeline by orchestrating the `extract`, `transform`, and `load` tasks.
    * **`src/`**: Contains the core Python modules for the ETL process. These modules are imported by the Airflow DAG.
        * `__init__.py`: Makes `src` a Python package.
        * `extract.py`: Handles making requests to the Dog API, fetching the raw data, and managing any API-related errors.
        * `transform.py`: Responsible for cleaning and transforming the raw data (e.g., handling weight, height, and life expectancy values).
        * `load.py`: Manages the loading of the transformed data into the PostgreSQL database.
* **`docker-compose.yaml`**: Defines the multi-container Docker application for Airflow (webserver, scheduler, worker, and PostgreSQL database).
* **`requirements.txt`**: Lists all Python dependencies required for the ETL scripts and the Airflow environment.
* **`.gitignore`**: Specifies intentionally untracked files that Git should ignore.

  
## Requirements:
- Docker** and **Docker Compose** installed.
- Python 3.8+
- Postgres SQL
- Packages:
  - pandas
  - requests
  - sqlalchemy
  - psycopg2
  - json
  - logging
  - python-dotenv
  - os
  - sys
  - datetime
  - airflow

All complete requirements are found in requirements.txt


