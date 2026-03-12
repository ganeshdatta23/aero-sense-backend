
# ✈️ AeroSense
### Real-Time Flight & Weather Disruption Analytics Platform

AeroSense is a production-style end-to-end data engineering and full-stack analytics project that ingests live flight and weather data, processes it through a modern ELT pipeline, and visualizes disruption metrics in an interactive dashboard.

This project demonstrates real-world system design by combining data engineering, backend APIs, cloud architecture, and modern frontend analytics.

---

## 🌍 Project Overview

Air traffic is heavily influenced by weather conditions such as:

- 🌪️ High wind speeds  
- 🌧️ Heavy precipitation  
- ⛈️ Storm systems  

AeroSense identifies potential flight disruptions by combining:

- ✈️ Live flight vectors  
- 🌦️ Weather conditions at flight coordinates  

The system then produces analytics and visual insights to help understand disruption patterns.

---

## 🚀 Key Features

### 📡 Real-Time Data Ingestion
- Fetches live flight data from OpenSky Network
- Fetches weather conditions from Open-Meteo

### 🗄️ Raw Data Storage
- Stores original API responses in PostgreSQL JSONB
- Ensures lossless ingestion for reproducibility

### 🔄 ELT Data Pipeline
- Apache Airflow orchestrates extraction
- dbt transforms raw data into analytical models

### ⚡ High-Performance Backend
- FastAPI REST APIs
- Automatic OpenAPI documentation
- Pydantic schema validation

### 📊 Interactive Analytics Dashboard
- Built with Next.js
- Styled using TailwindCSS
- Charts powered by Chart.js

### ☁️ Free-Tier Deployment
- Backend → Render
- Frontend → Vercel
- Database → Neon Serverless PostgreSQL

---

# 🏗 System Architecture

External Data Sources
        │
        ├── OpenSky Network (Flight Data)
        └── Open-Meteo API (Weather Data)
                     │
                     ▼
            Data Ingestion Layer
        Python + Apache Airflow
        (Scheduled every 10 minutes)
                     │
                     ▼
            Data Storage Layer
        Neon Serverless PostgreSQL
        Raw JSON stored in JSONB
                     │
                     ▼
           Data Processing Layer
                  dbt
        SQL transformations & models
                     │
                     ▼
              Backend API
                 FastAPI
          REST endpoints for data
                     │
                     ▼
           Frontend Dashboard
          Next.js + TailwindCSS
              Chart.js Charts

---

# 🛠 Technology Stack

## ⚙️ Data Engineering
- Python
- Apache Airflow
- dbt (Data Build Tool)

## 🗄 Database
- PostgreSQL
- Neon Serverless Postgres

## 🔌 Backend
- FastAPI
- SQLAlchemy
- Pydantic

## 🎨 Frontend
- Next.js
- TailwindCSS
- Chart.js

## 🚀 DevOps
- Docker
- GitHub Actions
- Vercel
- Render

---

# 📊 Data Pipeline

AeroSense follows a modern ELT architecture.

## 1️⃣ Extraction (Airflow)

Airflow DAG executes every 10 minutes.

Tasks:

1. Fetch flight state vectors from OpenSky
2. Extract flight coordinates
3. Fetch weather data from Open-Meteo

Example:

```python
response = requests.get(OPENSKY_API_URL)
flight_data = response.json()
```

Failure handling:
- Automatic retries
- Exponential backoff

---

## 2️⃣ Loading (PostgreSQL)

Raw JSON is stored directly.

Tables:

raw_data.raw_flights  
raw_data.raw_weather  

Each table includes:
- timestamp
- JSONB payload

Benefits:

✔ Data never lost  
✔ Transformations can be rerun anytime  

---

## 3️⃣ Transformation (dbt)

dbt transforms raw JSON into structured models.

### Staging Models

stg_flights  
stg_weather  

Extracts:
- coordinates
- altitude
- velocity
- weather metrics

### Core Models

flights_with_weather

Joins:
- flight coordinates
- nearest weather observation

### Mart Models

hourly_disruption_metrics

Aggregations:
- flights in high wind zones
- precipitation exposure
- disruption probability

---

## 4️⃣ API Serving (FastAPI)

Example endpoints:

GET /api/v1/flights/current  
GET /api/v1/metrics/disruptions  

API documentation available at:

/docs

---

# 📈 Dashboard Features

- 📊 Flights affected by severe weather
- 📉 Hourly disruption metrics
- 🌍 Geographic flight distribution
- 🌪️ Wind speed impact trends

Charts powered by Chart.js.

---

# 🧪 Free Data Sources

### ✈️ OpenSky Network
Provides:
- flight position
- altitude
- velocity
- aircraft identifiers

https://opensky-network.org

### 🌦 Open-Meteo
Provides:
- wind speed
- precipitation
- temperature
- weather codes

https://open-meteo.com

---

# 🖥 Local Development Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/aerosense.git
cd aerosense
```

## 2️⃣ Install Backend Dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

## 3️⃣ Run Backend

```bash
uvicorn main:app --reload
```

Server runs at:

http://localhost:8000

## 4️⃣ Install Frontend

```bash
cd frontend
npm install
```

## 5️⃣ Run Frontend

```bash
npm run dev
```

Open:

http://localhost:3000

---

# 📦 Deployment Architecture

| Component | Platform |
|-----------|----------|
| Frontend | Vercel |
| Backend | Render |
| Database | Neon |
| CI/CD | GitHub Actions |

---

# 🧩 Repository Structure

aerosense/
│
├── airflow/
│   └── dags/
│
├── analytics/
│   └── dbt_project/
│
├── backend/
│   ├── api/
│   ├── models/
│   └── services/
│
├── frontend/
│   ├── components/
│   ├── pages/
│   └── styles/
│
├── docker/
│
├── README.md
└── docker-compose.yml

---

# 🔮 Future Improvements

- 🌍 Real-time WebSocket updates
- 🤖 Machine learning disruption predictions
- 📍 Flight path visualization on map
- 📊 Advanced anomaly detection
- 📨 Alert system for severe disruptions

---

# 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Submit pull request

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Ganesh Datta Padamata

Full Stack & Data Engineering Enthusiast

⭐ If you found this project useful, consider starring the repository.
