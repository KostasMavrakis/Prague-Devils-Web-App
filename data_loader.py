import pandas as pd
from google.cloud import secretmanager
from google.oauth2.service_account import Credentials
import gspread
import json
from diskcache import Cache

# Setup diskcache (shared cache folder with app.py)
cache = Cache("./cache")
# Config
# Set up the Google Sheets API client
SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
PROJECT_ID = "project_id"
SECRET_ID = "secret_id"
SHEET_NAME = "sheet_name"

# ========= Secret Manager + Client helpers =========
@cache.memoize(expire=3600)  # cache raw JSON credentials safely for 1h
def get_creds_dict():
   """Fetch and return service account JSON from Secret Manager."""
   secret_client = secretmanager.SecretManagerServiceClient()
   name = f"projects/{PROJECT_ID}/secrets/{SECRET_ID}/versions/latest"
   response = secret_client.access_secret_version(name=name)
   secret_payload = response.payload.data.decode("UTF-8")
   return json.loads(secret_payload)

def get_client():
   """Return a new gspread client (not cached)."""
   creds_info = get_creds_dict()
   creds = Credentials.from_service_account_info(creds_info, scopes=SCOPES)
   return gspread.authorize(creds)

# Open the Google Sheet by name or URL and select the worksheet by name
def get_workbook():
   """Return the Google Sheets workbook."""
   return get_client().open(SHEET_NAME)

# ========= Generic Loader =========
# Fetch the data from the worksheet and convert data to pandas DataFrame
def fetch_worksheet_as_df(worksheet_name: str) -> pd.DataFrame:
   """Helper to load a worksheet and return it as DataFrame, with error handling."""
   try:
       worksheet = get_workbook().worksheet(worksheet_name)
       return pd.DataFrame(worksheet.get_all_records())
   except Exception as e:
       print(f"Error loading worksheet '{worksheet_name}': {e}")
       raise

# ========= Cached DataFrame Loaders =========
@cache.memoize(expire=300)  # cache DataFrame for 5 minutes
def load_all_time_results():   
   return fetch_worksheet_as_df("All Time Results")

@cache.memoize(expire=300)
def load_all_players():
   return fetch_worksheet_as_df("All Players")

@cache.memoize(expire=300)
def load_chart_data():
   return fetch_worksheet_as_df("Chart Preparation 2023-2024")

@cache.memoize(expire=300)
def load_goals():
   return fetch_worksheet_as_df("Goals")

@cache.memoize(expire=300)
def load_performance_stats():
   return fetch_worksheet_as_df("Performance Stats")

@cache.memoize(expire=300)
def load_ratings_helper():
   return fetch_worksheet_as_df("Ratings Helper")
