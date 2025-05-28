⚽ Football Team Stats Tracker

This is a multi-page interactive web application built using Dash, Plotly, and dash-bootstrap-components to track and visualize the performance and statistics of an amateur football team. The app pulls data directly from a Google Sheets file stored in Google Drive and is deployed on Google Cloud Platform (GCP).

🌐 Live Demo
https://praguedevilsfc-41916605153.europe-central2.run.app/

📌 Features
This web app includes 7 interactive pages, each designed to present and explore different aspects of the team’s history, players, and performance:

1. 🏟️ Home Page
- A photo carousel showcasing memorable moments from each football season.
2. 📋 Player Roster
- An interactive data table listing all players by season, with sortable and searchable fields.
3. 🌍 Team Overview
- A pie chart showing player distribution by country.
- Cards summarizing general team statistics.
4. 🗺️ Player Origins Map
- An interactive map displaying players’ locations based on their countries of origin.
5. 📊 Match History
- A dynamic data table of all recorded matches with details such as score, opponent, and date.
6. 🏅 Top Performers
- A bar chart showcasing the top five players based on selected metrics (e.g., goals, assists, appearances).
7. 📈 Performance Correlation
- An interactive line chart visualizing the correlation between different performance variables.
- An interactive card displaying the correlation coefficient of these variables.

🔧 Technologies Used
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
- Replace the part of the script in the individual pages that is used for reading the credentials at runtime and for authenticating with the following 3 lines of code that make a reference to the downloaded JSON file:

<br/>#Set up the Google Sheets API client
<br/>scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
<br/>#Add the path to your 'credentials.json' file
<br/>creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
<br/>client = gspread.authorize(creds)  

🧑‍💻 Author
<br/>Kostas
<br/>Built with 💚 by a passionate footballer and data enthusiast.
<br/>Feel free to reach out or contribute!

