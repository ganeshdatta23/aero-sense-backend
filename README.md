# ✈️ AeroSense

### Real-Time Flight & Weather Disruption Analytics Platform

AeroSense is a production-style, end-to-end data engineering and full-stack analytics project that ingests live flight and weather data, processes it through a modern ELT pipeline, and visualizes disruption metrics in an interactive dashboard.

This project demonstrates real-world system design by combining data engineering, backend APIs, cloud architecture, and modern frontend analytics.

---

## 🌍 Project Overview

Air traffic is heavily influenced by weather conditions such as high wind speeds, heavy precipitation, and storm systems. AeroSense identifies potential flight disruptions by combining live flight vectors with real-time weather conditions at flight coordinates, producing analytics and visual insights to help understand disruption patterns.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| 📡 **Real-Time Ingestion** | Live flight data from OpenSky Network + weather from Open-Meteo |
| 🗄️ **Raw Data Storage** | Original API responses stored in PostgreSQL JSONB — lossless & reproducible |
| 🔄 **ELT Pipeline** | Apache Airflow orchestrates extraction; dbt transforms raw data into analytical models |
| ⚡ **High-Performance API** | FastAPI with automatic OpenAPI docs and Pydantic schema validation |
| 📊 **Interactive Dashboard** | Next.js + TailwindCSS frontend with Chart.js visualizations |
| ☁️ **Free-Tier Deployment** | Backend → Render · Frontend → Vercel · Database → Neon |

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────┐
│                   External Data Sources                  │
│                                                          │
│   ┌─────────────────────────┐   ┌─────────────────────┐ │
│   │   OpenSky Network API   │   │   Open-Meteo API    │ │
│   │      (Flight Data)      │   │   (Weather Data)    │ │
│   └────────────┬────────────┘   └──────────┬──────────┘ │
└────────────────┼──────────────────────────┼─────────────┘
                 └──────────────┬───────────┘
                                ▼
                 ┌──────────────────────────┐
                 │    Data Ingestion Layer   │
                 │   Python + Apache Airflow │
                 │    Runs every 10 minutes  │
                 └─────────────┬────────────┘
                               ▼
                 ┌──────────────────────────┐
                 │     Data Storage Layer   │
                 │  Neon Serverless Postgres │
                 │   Raw JSON stored in JSONB│
                 └─────────────┬────────────┘
                               ▼
                 ┌──────────────────────────┐
                 │   Data Processing Layer  │
                 │           dbt            │
                 │   SQL Transformations    │
                 └─────────────┬────────────┘
                               ▼
                 ┌──────────────────────────┐
                 │        Backend API       │
                 │          FastAPI         │
                 │      REST Endpoints      │
                 └─────────────┬────────────┘
                               ▼
                 ┌──────────────────────────┐
                 │    Frontend Dashboard    │
                 │   Next.js + TailwindCSS  │
                 │        Chart.js          │
                 └──────────────────────────┘
```

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| ⚙️ **Data Engineering** | Python · Apache Airflow · dbt |
| 🗄️ **Database** | PostgreSQL · Neon Serverless Postgres |
| 🔌 **Backend** | FastAPI · SQLAlchemy · Pydantic |
| 🎨 **Frontend** | Next.js · TailwindCSS · Chart.js |
| 🚀 **DevOps** | Docker · GitHub Actions · Vercel · Render |

---

## 📊 Data Pipeline

AeroSense follows a modern **ELT** (Extract → Load → Transform) architecture.

### 1️⃣ Extraction — Apache Airflow

An Airflow DAG runs every 10 minutes and executes the following tasks in sequence:

1. Fetch flight state vectors from OpenSky Network
2. Extract flight coordinates
3. Fetch weather data from Open-Meteo for those coordinates

```python
response = requests.get(OPENSKY_API_URL)
flight_data = response.json()
```

Failure handling includes automatic retries with exponential backoff.

---

### 2️⃣ Loading — PostgreSQL

Raw JSON payloads are stored directly into two tables:

```
raw_data.raw_flights
raw_data.raw_weather
```

Each record includes a `timestamp` and a `JSONB` payload. Because raw data is never discarded, transformations can be re-run at any time and no information is lost during ingestion.

---

### 3️⃣ Transformation — dbt

dbt converts raw JSONB into structured, analytics-ready models across three layers:

**Staging Models** — `stg_flights`, `stg_weather`
Extracts coordinates, altitude, velocity, and weather metrics from raw JSON.

**Core Models** — `flights_with_weather`
Joins flight coordinates with the nearest weather observation.

**Mart Models** — `hourly_disruption_metrics`
Aggregates flights in high-wind zones, precipitation exposure, and disruption probability scores.

---

### 4️⃣ API Serving — FastAPI

```
GET  /api/v1/flights/current
GET  /api/v1/metrics/disruptions
```

Interactive API documentation is available at `/docs`.

---

## 📈 Dashboard Features

- 📊 Flights affected by severe weather
- 📉 Hourly disruption metrics over time
- 🌍 Geographic flight distribution
- 🌪️ Wind speed impact trends

All charts are powered by Chart.js.

---

## 🧪 Data Sources

### ✈️ OpenSky Network
Provides free, real-time flight state vectors including position, altitude, velocity, and aircraft identifiers.
🔗 https://opensky-network.org

### 🌦️ Open-Meteo
Provides free weather forecasts and historical data including wind speed, precipitation, temperature, and weather codes.
🔗 https://open-meteo.com

---

## 🖥️ Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/aerosense.git
cd aerosense
```

### 2. Install Backend Dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

### 3. Run the Backend

```bash
uvicorn main:app --reload
```

API available at `http://localhost:8000`

### 4. Install Frontend Dependencies

```bash
cd frontend
npm install
```

### 5. Run the Frontend

```bash
npm run dev
```

Dashboard available at `http://localhost:3000`

---

## 📦 Deployment

| Component | Platform |
|---|---|
| Frontend | Vercel |
| Backend | Render |
| Database | Neon |
| CI/CD | GitHub Actions |

---

## 🧩 Repository Structure

```
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
├── docker-compose.yml
└── README.md
```

---

## 🔮 Future Improvements

- 🌍 Real-time WebSocket updates for live dashboard streaming
- 🤖 Machine learning model for disruption predictions
- 📍 Interactive flight path visualization on a map
- 📊 Advanced anomaly detection
- 📨 Alert system for severe weather disruptions

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch and submit a pull request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Ganesh Datta Padamata**
** Madati Venkatesh**
---

⭐ If you found this project useful, please consider starring the repository!
