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

<br/>1.	Data Source – Google Sheets
<br/>All raw data is stored in Google Sheets. This allows easy updates without redeploying the application and acts as a lightweight data layer suitable for a small analytics platform.

<br/>2.	Authentication
<br/>Secure access to Google Sheets is handled via OAuth/service account credentials stored in Google Cloud Secret Manager. At runtime, the application retrieves these credentials securely, ensuring that no sensitive information is exposed in the codebase or configuration files.

<br/>3.	Backend & Data Processing
<br/>•	The Dash application (built on Flask) serves as both the backend and frontend framework.
<br/>•	data_loader.py handles authentication, data extraction, cleansing, transformation, and caching.
<br/>•	Processed datasets are kept in memory or cache and reused across multiple pages to optimize performance.

<br/>4.	Visualization & User Interface
<br/>•	Dash components define the multi-page structure and interactivity.
<br/>•	Plotly generates interactive charts, maps, and tables.
<br/>•	style.css and Dash Bootstrap Components ensure a responsive and consistent UI across devices.

<br/>5.	Containerization & Deployment
<br/>•	The entire application is containerized using Docker (Dockerfile).
<br/>•	requirements.txt defines all dependencies for reproducible builds.
<br/>•	The container is deployed on Google Cloud Platform, enabling easy scaling, portability, and consistent runtime behavior.
 
📊 Web App Framework & UI
- Dash – Python framework for building interactive web applications
- dash-bootstrap-components – Bootstrap integration for Dash for polished, responsive layouts
- Plotly – For rich, interactive visualizations (charts, maps, and more)
<br/>🧮 Data Handling & Analysis
- Pandas – Powerful data manipulation and analysis
- NumPy – Support for numerical operations
<br/>🌐 Data Source & API Integration
- gspread – Python library for interacting with Google Sheets
- google-auth, google-auth-oauthlib – For secure OAuth 2.0 authentication with Google APIs
- oauth2client, requests-oauthlib – Additional OAuth helpers for legacy and modern flows
<br/>🔐 Security & Cloud Integration
- google-cloud-secret-manager – Secure storage and access to credentials using GCP Secret Manager
- cachetools, rsa, pyasn1, pyasn1-modules – Utilities for token management and secure API access
<br/>🌐 Web Framework
- Flask – Lightweight backend server used under the hood by Dash
- Werkzeug, Jinja2, itsdangerous, click – Flask core dependencies for routing, templating, and secure sessions

🔐 Authentication & Data Access
- The application accesses Google Sheets using a service account.
- Credentials are stored securely in GCP Secret Manager and accessed during runtime to authenticate and pull the latest data.

🚀 Deployment
The app is deployed on Google Cloud Platform (App Engine or Cloud Run). Make sure to:
- Set up a Google Cloud project.
- Enable the Google Sheets and Secret Manager APIs.
- Store your service account key as a secret.
- Retrieve the secret in your app's startup code to authenticate and fetch data.

🛠️ Getting Started Locally
To run this app locally:
- Create a Service Account Key from Google Cloud Console and download it as a JSON file.
- Replace the part of the script in the individual pages that is used for reading the credentials at runtime and for the Secret Manager authentication with the following 3 lines of code that make a reference to the downloaded JSON file:

<br/>#Set up the Google Sheets API client
<br/>scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
<br/>#Add the path to your 'credentials.json' file
<br/>creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
<br/>client = gspread.authorize(creds)  

🧑‍💻 Author
<br/>Kostas
<br/>Built with 💚 by a passionate footballer and data enthusiast.
<br/>Feel free to reach out or contribute!

