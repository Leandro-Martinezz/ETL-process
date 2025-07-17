# ETL Project - Dog API 

This is a simple ETL project that consumes data from the Dog API, transforms the information, and loads it into a SQL Server database, focusing on the use of loggins as monitoring and checkpoints.

## Project Structure

- **extract.py**: module that makes a request to the API and handles errors.
- **transform.py**: cleans and transforms data (weight, height, life expectancy).
- **load.py**: loads the transformed data into a SQL Server table.
- **main.py**: testing and execution of the complete ETL process.

  
## Requirements:
- Python 3.8+
- SQL Server local
- Packages:
  - pandas
  - requests
  - sqlalchemy
  - pyodbc
  - json
  - logging
  - python-dotenv
