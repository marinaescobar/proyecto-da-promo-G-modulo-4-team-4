#%%
# Import libraries for data processing
# -----------------------------------------------------------------------
import pandas as pd  # Pandas for data manipulation and analysis in Python.
# Optional libraries (can be removed if not used):
# -----------------------------------------------------------------------
# Import libraries for web scraping and data manipulation
# from bs4 import BeautifulSoup
# import requests
# Import libraries for web browser automation with Selenium
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# ChromeDriverManager manages the installation of the Chrome driver
# from selenium.webdriver.common.keys import Keys  # Keys is useful for simulating keyboard events in Selenium.
# from selenium.webdriver.support.ui import Select  # Select is used to interact with <select> elements on web pages.
# Import libraries for pausing execution
# -----------------------------------------------------------------------
# from time import sleep  # Sleep is used to pause the program execution for a number of seconds.
# Configurations
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None)  # Set a Pandas option to show all columns of a DataFrame.
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.display.max_columns = None
pd.set_option('display.float_format', '{:.2f}'.format)
# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np
# Imputación de nulos usando métodos avanzados estadísticos
# -----------------------------------------------------------------------
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
# Librerías de visualización
# -----------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
# %%
#Method to open files
def open_csv(rute):
  """
  Opens a CSV file and reads it into a pandas DataFrame.
  Args:
      rute(str): The path to the CSV file.
  Returns:
      pd.DataFrame: The DataFrame containing the data from the CSV file.
  """
  # Read the CSV file using pandas.read_csv
  df = pd.read_csv(rute)
  
  # Si al cargar el dataframe se creó una columna de unnamed, la elimina
  if 'Unnamed: 0' in df.columns:
      df.drop('Unnamed: 0', axis = 1, inplace=True)
      
  # Return the DataFrame
  return df
# %%
#%%
# Creation of a function to explore the DataFrames
def explore_df(df):
    """
    This function allows to make an initial data exploration.
    Args:
      df (pandas.DataFrame): The DataFrame to explore. Refering to the ones previously opened.
    Returns:
      None
      """
    # Prints information about the DataFrame
    print("The main information for DataFrame is: ")
    df.info()
    print("______________________")
    # Print the first 5 rows of the DataFrame
    print(f"The first 5 rows for DataFrame are:")
    display(df.head())
# %%
# Define a function to obtain information about a DataFrame
def df_information(df):
    # Print the shape of the DataFrame (number of rows and columns)
    print(f"The shape for the DataFrame is: ")
    print(df.shape)
    print("_________________")
    # Print the list of column names
    print(f"The name of the columns are: {list(df.columns)}")
    print("_________________")
    # Print the number of null values in each column
    print(f"The number of nulls in the DataFrame:")
    print(df.isna().sum())
    print("_________________")
    # Print the number of duplicate rows in the DataFrame
    print(f"The number of values duplicated in the DataFrame:")
    print(df.duplicated().sum())
    print("_________________")
    # Print the transposed descriptive statistics (descriptive statistics for each column)
    print(f"The descriptive statistics for this DataFrame are:")
    display(df.describe().T)
# %%
# Define a function to explore basic characteristics of each column in a DataFrame
def explore_columns(df):
   """
   Explores basic characteristics of each column in a DataFrame.
   Args:
       df (pd.DataFrame): The DataFrame to explore.
   Prints:
       Description of each column, including:
           - Number of values
           - Unique values
           - Data type
           - Number of null values
           - Number of duplicates
   """
   for column in df.columns:
       # Print a header for the current column
       print(f"-------- Exploring {column} --------")
       # Print the number of values in the column
       print(f"Number of values: {len(df[column].to_list())}")
       # Print the number of unique values in the column
       print(f"Unique values: {len(df[column].unique())}")
       # Print the data type of the column
       print(f"Data type: {df[column].dtypes}\n")
       # Print the number of null values in the column
       print(f"Total nulls: {df[column].isnull().sum()}")
       # Print the number of duplicate values in the column
       print(f"Duplicates: {df[column].duplicated().sum()}")
       
       print(f"Unique values count: {df[column].value_counts()}")
       # Add a space for readability
       print("__________________________")
       
       
def limpieza (df):
    # Homogeneización
    
    meses = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }
    
    country_codes = {
    'PRT': 'Portugal',
    'GBR': 'United Kingdom',
    'USA': 'United States',
    'ESP': 'Spain',
    'IRL': 'Ireland',
    'FRA': 'France',
    'ROU': 'Romania',
    'NOR': 'Norway',
    'OMN': 'Oman',
    'ARG': 'Argentina',
    'DEU': 'Germany',
    'CHE': 'Switzerland',
    'GRC': 'Greece',
    'NLD': 'Netherlands',
    'DNK': 'Denmark',
    'RUS': 'Russia',
    'POL': 'Poland',
    'AUS': 'Australia',
    'EST': 'Estonia',
    'CZE': 'Czech Republic',
    'BRA': 'Brazil',
    'BEL': 'Belgium',
    'CN': 'China',
    'SWE': 'Sweden',
    'FIN': 'Finland',
    'MOZ': 'Mozambique',
    'SVN': 'Slovenia',
    'MAR': 'Morocco',
    'ITA': 'Italy',
    'UKR': 'Ukraine',
    'SMR': 'San Marino',
    'LVA': 'Latvia',
    'PRI': 'Puerto Rico',
    'CHL': 'Chile',
    'CHN': 'China',
    'LTU': 'Lithuania',
    'LUX': 'Luxembourg',
    'AUT': 'Austria',
    'TUR': 'Turkey',
    'MEX': 'Mexico',
    'ZAF': 'South Africa',
    'AGO': 'Angola',
    'ISR': 'Israel',
    'IND': 'India',
    'CYM': 'Cayman Islands',
    'ZMB': 'Zambia',
    'CPV': 'Cape Verde',
    'ZWE': 'Zimbabwe',
    'DZA': 'Algeria',
    'KOR': 'South Korea',
    'HUN': 'Hungary',
    'ARE': 'United Arab Emirates',
    'TUN': 'Tunisia',
    'JAM': 'Jamaica',
    'ALB': 'Albania',
    'HRV': 'Croatia',
    'HKG': 'Hong Kong',
    'AND': 'Andorra',
    'GIB': 'Gibraltar',
    'URY': 'Uruguay',
    'BLR': 'Belarus',
    'JEY': 'Jersey',
    'CYP': 'Cyprus',
    'MDV': 'Maldives',
    'FJI': 'Fiji',
    'KAZ': 'Kazakhstan',
    'PAK': 'Pakistan',
    'IDN': 'Indonesia',
    'LBN': 'Lebanon',
    'PHL': 'Philippines',
    'COL': 'Colombia',
    'SEN': 'Senegal',
    'GEO': 'Georgia',
    'AZE': 'Azerbaijan',
    'BHR': 'Bahrain',
    'NZL': 'New Zealand',
    'THA': 'Thailand',
    'DOM': 'Dominican Republic',
    'MYS': 'Malaysia',
    'VEN': 'Venezuela',
    'ARM': 'Armenia',
    'LKA': 'Sri Lanka',
    'CUB': 'Cuba',
    'CMR': 'Cameroon',
    'IRN': 'Iran',
    'NGA': 'Nigeria',
    'COM': 'Comoros',
    'BGR': 'Bulgaria',
    'CIV': "Côte d'Ivoire",
    'SRB': 'Serbia',
    'JOR': 'Jordan',
    'SYR': 'Syria',
    'BDI': 'Burundi',
    'SGP': 'Singapore',
    'KWT': 'Kuwait',
    'PLW': 'Palau',
    'QAT': 'Qatar',
    'SVK': 'Slovakia',
    'SUR': 'Suriname',
    'MLT': 'Malta',
    'MWI': 'Malawi',
    'MDG': 'Madagascar',
    'ISL': 'Iceland',
    'JPN': 'Japan',
    'CAF': 'Central African Republic',
    'TGO': 'Togo',
    'TWN': 'Taiwan',
    'DJI': 'Djibouti',
    'VNM': 'Vietnam',
    'PER': 'Peru',
    'EGY': 'Egypt',
    'SAU': 'Saudi Arabia',
    'KNA': 'Saint Kitts and Nevis',
    'ETH': 'Ethiopia',
    'ECU': 'Ecuador',
    'IRQ': 'Iraq',
    'KHM': 'Cambodia',
    'MCO': 'Monaco',
    'BGD': 'Bangladesh',
    'TJK': 'Tajikistan',
    'NIC': 'Nicaragua',
    'GGY': 'Guernsey',
    'BEN': 'Benin',
    'VGB': 'British Virgin Islands',
    'CRI': 'Costa Rica',
    'TZA': 'Tanzania',
    'GAB': 'Gabon',
    'MKD': 'North Macedonia',
    'BIH': 'Bosnia and Herzegovina',
    'TMP': 'East Timor',
    'GLP': 'Guadeloupe',
    'LIE': 'Liechtenstein',
    'GNB': 'Guinea-Bissau',
    'MAC': 'Macau',
    'IMN': 'Isle of Man',
    'UMI': 'United States Minor Outlying Islands',
    'MYT': 'Mayotte',
    'GHA': 'Ghana',
    'FRO': 'Faroe Islands',
    'MMR': 'Myanmar',
    'PAN': 'Panama',
    'MUS': 'Mauritius',
    'LBY': 'Libya',
    'NAM': 'Namibia',
    'BOL': 'Bolivia',
    'PRY': 'Paraguay',
    'BRB': 'Barbados',
    'ABW': 'Aruba',
    'AIA': 'Anguilla',
    'DMA': 'Dominica',
    'UGA': 'Uganda',
    'MNE': 'Montenegro',
    'GTM': 'Guatemala',
    'ASM': 'American Samoa',
    'KEN': 'Kenya',
    'NCL': 'New Caledonia',
    'STP': 'São Tomé and Príncipe',
    'KIR': 'Kiribati',
    'SDN': 'Sudan',
    'ATF': 'French Southern Territories',
    'SLE': 'Sierra Leone',
    'SLV': 'El Salvador',
    'LAO': 'Laos'
    }
    
    # ISO paises
    
    
    return df


def eliminacion_nulos (df):
    
    # Duplicados, nulos y demás
    df.drop(['0', 'company'], axis=1, inplace=True)
    
    df.dropna(how='all', inplace=True)
    
    min_valores_no_nulos = int(0.8 * len(df.columns))
    
    df.dropna(thresh=min_valores_no_nulos, inplace=True)
    
    df['courtesy'] = df.apply(lambda x: True if x['stays_in_weekend_nights'] == 0 and x['stays_in_week_nights'] == 0 or x['adr'] == 0 else False, axis=1)

    return df


def imputacion_nulos (df):
    return df