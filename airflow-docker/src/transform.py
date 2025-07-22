import pandas as pd
import logging

logging.basicConfig(format='%(levelname)s: %(message)s',level=logging.DEBUG)

def transform(raw_data): #this function transform the extract's response into a dataframe
    logging.info("STARTING THE TRANSFORM MODULE")
    if not isinstance(raw_data, (list,dict)):
        logging.warning(f"Entry data are not a list or dict data are {type(raw_data)}")
        return pd.DataFrame() #if the answer is not a list or dict, return an empty data frame.
    
    df = pd.DataFrame(raw_data) #transforming raw_data into a dataframe.
    logging.info("Starting the exploratory analysis")
    print(f"Head{ df.head()}")
    print(f"\nShape\n{ df.shape}")
    print(f"\nInfo")
    df.info()
    print(f"\nNull Values\n{df.isna().sum()}")

    logging.info("Starting the transformation phase.")
    def clean_range_column(val, suffix_to_remove=None): #This function splits two values delimited by a '-' and removes a suffix if exists
        try:
            if suffix_to_remove:
                val = val.replace(suffix_to_remove, "")
                val = val.replace("–", "-")
            nums = [float(n) for n in val.split(" - ")]
            return sum(nums) / len(nums)
        except:
            return None # in case there are missing or incorrectly formatted values

    #new avg columns are created and the clean_range_column function is applied
    df["avg_weight_kg"] = df["weight"].apply(lambda x: clean_range_column(x["metric"]))
    df["avg_height_cm"] = df["height"].apply(lambda x: clean_range_column(x["metric"]))
    df["avg_life_span"] = df['life_span'].apply(lambda x: clean_range_column(x, " years"))
    logging.debug("weight, height and life span columns have been transformed to average columns")

    #dropping duplicates columns and columns with null values greater than 50% of all rows
    columns_to_drop = df.columns[df.isna().sum() > df.shape[0]*0.5]
    df.drop(columns=["weight","height","reference_image_id","life_span"], axis=1, inplace=True)
    df.drop(columns_to_drop,axis=1, inplace=True)
    logging.debug(f"weight, height, reference_image_id, life_span and columns with nulls greater than 50% of all values have been eliminated")

    #filling missing values with mean for numerics and 'Unknown' for strings
    df = df.fillna(df.mean(numeric_only=True))
    df = df.fillna('Unknown')
    logging.debug("Missing values have been filled")
    logging.info("THE TRANSFORM MODULE HAS FINISHED")
    return df