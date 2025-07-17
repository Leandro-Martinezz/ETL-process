import requests
import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s',level=logging.DEBUG)

def extract(source_url): #this function makes a request to an API and save the result
    
    try: 
        logging.info("STARTING THE EXTRACT MODULE")
        response = requests.get(source_url, timeout=10)  #the request is made to the API
        response.raise_for_status()

        try:
            data = response.json()  #parsing the request
        except json.JSONDecodeError:
            logging.error("The response is not a JSON format")
            return None     
        
    except requests.exceptions.Timeout:  #errors handling
        logging.error("Timeout connecting to the API.")
    except requests.exceptions.ConnectionError:
        logging.error("Error connection.")
    except requests.exceptions.HTTPError as e:
        logging.error(f"Error HTTP: {e}")  
    logging.info("Connection is successfully done")

    if isinstance(data, (list,dict)):  #checking data type
            logging.debug(f"The response is a {type(data)}")
    else :
            logging.warning(f'the response is {type(data)} type') 
    
    logging.info("THE EXTRACT MODULE HAS FINISHED")
    return data


if __name__ == "__main__":
    url = "https://api.thedogapi.com/v1/breeds"
    con = extract(url)
    print(con)
