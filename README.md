⚽ Football Team Stats Tracker

This is a multi-page interactive web application built using Dash, Plotly, and dash-bootstrap-components to track and visualize the performance and statistics of my amateur football team. The app pulls data directly from a Google Sheets file stored in Google Drive and is deployed on Google Cloud Platform (GCP).

🌐 Live Demo
https://praguedevilsfc-41916605153.europe-central2.run.app/

📌 Features
<br/>This web app includes 12 interactive pages, each designed to present and explore different aspects of the team’s history, players, and performance:

• Gallery: Introductory page featuring a carousel photo gallery by season
<br/>• Overview: Nationality distribution and key team statistics
<br/>• Roster: Interactive table listing all players by season
<br/>• Map: Interactive map showing players’ geographic origins
<br/>• Coaches & Captains: Data tables summarizing the results under different coaches and captains
<br/>• All-Time Results: Complete match history in an interactive table
<br/>• Goals: Charts visualizing goals scored and conceded per season
<br/>• Fields: Map of pitch locations and performance breakdown per field
<br/>• The Top: Bar charts ranking the top five players based on selectable metrics
<br/>• Trackers: Performance metrics per player, including embedded heat-map screenshots
<br/>• Ratings: Dynamic player valuation cards that update based on user input via an online form
<br/>• Correlation: Interactive line chart and summary card showing correlations between performance variables

🔧 Technologies and Approach Used

1.	Data Source (Google Sheets)
<br/>All raw data is stored in Google Sheets. This allows easy updates without redeploying the application and acts as a lightweight data layer suitable for a small analytics platform.

2.	Authentication (Google Cloud Platform)
<br/>Secure access to Google Sheets is handled via OAuth/service account credentials stored in Google Cloud Secret Manager. At runtime, the application retrieves these credentials securely, ensuring that no sensitive information is exposed in the codebase or configuration files.

3.	Backend & Data Processing (Dash / Flask)
<br/>•	The Dash application (built on Flask) serves as both the backend and frontend framework.
<br/>•	data_loader.py handles authentication, data extraction, cleansing, transformation, and caching.
<br/>•	Processed datasets are kept in memory or cache and reused across multiple pages to optimize performance.

4.	Visualization & User Interface (Dash + Plotly)
<br/>•	Dash components define the multi-page structure and interactivity.
<br/>•	Plotly generates interactive charts, maps, and tables.
<br/>•	style.css and Dash Bootstrap Components ensure a responsive and consistent UI across devices.

5.	Containerization & Deployment (Docker + Google Cloud Platform)
<br/>•	The entire application is containerized using Docker (Dockerfile).
<br/>•	requirements.txt defines all dependencies for reproducible builds.
<br/>•	The container is deployed on Google Cloud Platform, enabling easy scaling, portability, and consistent runtime behavior.

🛠️ Running the app locally

• Create a Service Account Key from Google Cloud Console and download it as a JSON file.
<br/>• Replace the part of the script in the data_loader.py file that is used for reading the credentials at runtime and for the Secret Manager authentication with the following lines of code that make a reference to the downloaded JSON file:

import pandas as pd
<br/>import json
<br/>import gspread
<br/>from google.oauth2.service_account import Credentials
<br/>from diskcache import Cache

<br/># Setup diskcache (shared cache folder with app.py)
<br/>cache = Cache("./cache")

<br/>#Set up the Google Sheets API client
<br/># Google Sheets config
<br/>SCOPES = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive",]
<br/>#Add the path to your 'credentials.json' file
<br/>CREDENTIALS_FILE = "credentials.json"
<br/>SHEET_NAME = "sheet_name"

<br/># ========= Client helpers =========
<br/>@cache.memoize(expire=3600)
<br/>def get_creds():
<br/>"""Load service account credentials from local JSON file."""
  <br/>with open(CREDENTIALS_FILE, "r") as f:
  <br/>creds_info = json.load(f)
  <br/>return Credentials.from_service_account_info(
  <br/>creds_info, scopes=SCOPES
  <br/>)

<br/>def get_client():
<br/>"""Return a new gspread client."""
  <br/>creds = get_creds()
<br/>return gspread.authorize(creds)
 
🧑‍💻 Author
<br/>Kostas
<br/>Built with 💚 by a passionate footballer and data enthusiast.
<br/>Feel free to reach out or contribute!

