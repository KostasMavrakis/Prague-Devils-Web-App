import pandas as pd
import json
import gspread
from google.oauth2.service_account import Credentials
from diskcache import Cache

# Setup diskcache (shared cache folder with app.py)
cache = Cache("./cache")

# Google Sheets config
SCOPES = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive",]
CREDENTIALS_FILE = "credentials.json"
SHEET_NAME = "sheet_name"

# ========= Client helpers =========
@cache.memoize(expire=3600)
def get_creds():
   """Load service account credentials from local JSON file."""
   with open(CREDENTIALS_FILE, "r") as f:
       creds_info = json.load(f)
   return Credentials.from_service_account_info(
       creds_info, scopes=SCOPES
   )

def get_client():
   """Return a new gspread client."""
   creds = get_creds()
   return gspread.authorize(creds)

def get_workbook():
   """Return the Google Sheets workbook."""
   return get_client().open(SHEET_NAME)

# ========= Generic Loader =========
def fetch_worksheet_as_df(worksheet_name: str) -> pd.DataFrame:
   """Load a worksheet and return it as a DataFrame."""
   try:
       worksheet = get_workbook().worksheet(worksheet_name)
       return pd.DataFrame(worksheet.get_all_records())
   except Exception as e:
       print(f"Error loading worksheet '{worksheet_name}': {e}")
       raise

# ========= Cached DataFrame Loaders =========
@cache.memoize(expire=300)
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
