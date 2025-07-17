from extract import extract
from transform import transform
from load import load

url = "https://api.thedogapi.com/v1/breeds"

raw_data = extract(url)

cleaned_data = transform(raw_data)

load(cleaned_data,"dogs")
