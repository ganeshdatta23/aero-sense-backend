[poa.html](https://github.com/user-attachments/files/25811732/poa.html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AeroSense: End-to-End Portfolio Blueprint</title>
    
    <!-- Chosen Palette: Warm Neutrals with Slate and Emerald Accents (stone-50 bg, slate-800 text, emerald-600 highlights) -->
    <!-- Application Structure Plan: A dashboard-style SPA with a left navigation sidebar (bottom nav on mobile). This structure allows recruiters/users to digest a massive, multi-disciplinary engineering architecture in logical chunks without being overwhelmed by a giant wall of text. Sections are divided by engineering domains (Concept, Architecture, Implementation, Code Samples). -->
    <!-- Visualization & Content Choices: 
         1. Concept & Stack -> Doughnut Chart (Chart.js) -> Shows distribution of tech stack -> Quickly communicates full-stack capability -> NO SVG.
         2. Live Dashboard Mockup -> Line/Bar Combo Chart (Chart.js) -> Simulates final product data -> Proves understanding of analytics frontend -> NO SVG.
         3. Architecture Diagram -> ASCII Art within <pre> tags -> Represents system flow -> Avoids Mermaid/SVG constraints while maintaining technical feel -> NO SVG. 
         4. Roadmap -> Interactive HTML list -> Allows step-by-step exploration -> NO SVG. -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->

    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

        body {
            font-family: 'Inter', sans-serif;
            background-color: #fafaf9; /* stone-50 */
            color: #1e293b; /* slate-800 */
        }
        
        .code-font {
            font-family: 'JetBrains Mono', monospace;
        }

        /* Strict Chart Container Styling */
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            height: 40vh;
            max-height: 400px;
            min-height: 250px;
        }

        .section-content {
            display: none;
            animation: fadeIn 0.4s ease-in-out;
        }

        .section-content.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .nav-item {
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .nav-item.active {
            background-color: #d1fae5; /* emerald-100 */
            color: #059669; /* emerald-600 */
            font-weight: 600;
            border-left: 4px solid #059669;
        }

        /* Custom Scrollbar for code blocks */
        pre::-webkit-scrollbar {
            height: 8px;
            width: 8px;
        }
        pre::-webkit-scrollbar-track {
            background: #f1f5f9; 
        }
        pre::-webkit-scrollbar-thumb {
            background: #cbd5e1; 
            border-radius: 4px;
        }
    </style>
</head>
<body class="flex flex-col md:flex-row h-screen overflow-hidden">

    <!-- Mobile Header -->
    <div class="md:hidden bg-slate-900 text-stone-50 p-4 flex justify-between items-center z-20 shadow-md">
        <h1 class="text-xl font-bold tracking-tight">✈️ AeroSense Blueprint</h1>
        <button id="mobile-menu-btn" class="text-2xl">☰</button>
    </div>

    <!-- Sidebar Navigation -->
    <nav id="sidebar" class="bg-white border-r border-stone-200 w-full md:w-64 h-auto md:h-full flex-shrink-0 absolute md:relative z-10 transition-transform transform -translate-x-full md:translate-x-0 overflow-y-auto shadow-xl md:shadow-none">
        <div class="hidden md:block p-6 border-b border-stone-100">
            <h1 class="text-2xl font-bold text-slate-900 tracking-tight">✈️ AeroSense</h1>
            <p class="text-xs text-slate-500 mt-1 uppercase tracking-wider font-semibold">Portfolio Blueprint</p>
        </div>
        <ul class="py-4 flex flex-col gap-1">
            <li class="nav-item active px-6 py-3" data-target="exec-summary">📊 Executive Summary</li>
            <li class="nav-item px-6 py-3" data-target="architecture">🏗️ Architecture & Stack</li>
            <li class="nav-item px-6 py-3" data-target="data-pipeline">🔄 Data Pipeline</li>
            <li class="nav-item px-6 py-3" data-target="implementation">🛣️ Implementation Plan</li>
            <li class="nav-item px-6 py-3" data-target="code-samples">💻 Code & Specs</li>
            <li class="nav-item px-6 py-3" data-target="demo-dashboard">📈 Mock Dashboard</li>
        </ul>
        <div class="p-6 mt-auto hidden md:block border-t border-stone-100">
            <p class="text-xs text-slate-400">Designed for Senior Full Stack & Data Engineering Portfolios.</p>
        </div>
    </nav>

    <!-- Main Content Area -->
    <main class="flex-1 h-full overflow-y-auto bg-stone-50 p-6 md:p-10 relative">
        
        <!-- SECTION: Executive Summary -->
        <section id="exec-summary" class="section-content active max-w-5xl mx-auto">
            <header class="mb-8">
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-3">Project Concept: AeroSense</h2>
                <p class="text-lg text-slate-600 leading-relaxed">
                    AeroSense is a complete, production-grade <strong>Real-Time Flight & Weather Disruption Analytics Platform</strong>. It ingests live global flight vectors and weather conditions to identify potential routing delays. This section outlines the core value proposition and the skill distribution required to build it.
                </p>
            </header>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-10">
                <div class="bg-white p-6 rounded-xl shadow-sm border border-stone-100">
                    <h3 class="text-xl font-semibold mb-4 text-slate-800">💼 Resume Value</h3>
                    <ul class="space-y-3">
                        <li class="flex items-start"><span class="mr-2">✔️</span> <span><strong>Proves Full-Stack Mastery:</strong> Spans complex backend data engineering to responsive frontend visualization.</span></li>
                        <li class="flex items-start"><span class="mr-2">✔️</span> <span><strong>Handles Real-World Messiness:</strong> Integrates public APIs with rate limits and unstandardized JSON.</span></li>
                        <li class="flex items-start"><span class="mr-2">✔️</span> <span><strong>Modern Data Stack (MDS):</strong> Utilizes industry-standard patterns like ELT, orchestrators (Airflow), and transformation (dbt).</span></li>
                        <li class="flex items-start"><span class="mr-2">✔️</span> <span><strong>Cloud & DevOps:</strong> Demonstrates CI/CD and containerization without spending a dime.</span></li>
                    </ul>
                </div>
                
                <div class="bg-white p-6 rounded-xl shadow-sm border border-stone-100 flex flex-col items-center justify-center">
                    <h3 class="text-xl font-semibold mb-2 text-slate-800 self-start">🛠️ Skill Distribution</h3>
                    <p class="text-sm text-slate-500 mb-4 self-start">The balance of disciplines utilized in this end-to-end architecture.</p>
                    
                    <!-- Strict Chart Container -->
                    <div class="chart-container w-full h-[250px] max-h-[300px]">
                        <canvas id="techStackChart"></canvas>
                    </div>
                </div>
            </div>

            <div class="bg-emerald-50 border border-emerald-200 p-6 rounded-xl">
                <h3 class="text-lg font-bold text-emerald-800 mb-2">FREE Data Sources Identified:</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <strong>1. OpenSky Network API:</strong><br>
                        <span class="text-sm text-emerald-700">Provides live airspace data, flight vectors, and historical tracks. Free for non-commercial use.</span>
                    </div>
                    <div>
                        <strong>2. Open-Meteo API:</strong><br>
                        <span class="text-sm text-emerald-700">Free, open-source weather API requiring no API key. Perfect for joining weather data to flight coordinates.</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION: Architecture & Stack -->
        <section id="architecture" class="section-content max-w-5xl mx-auto">
            <header class="mb-8">
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-3">System Architecture & Tech Stack</h2>
                <p class="text-lg text-slate-600 leading-relaxed">
                    A highly scalable, decoupled architecture utilizing 100% free-tier services. It separates data ingestion, storage, analytical processing, API serving, and frontend consumption.
                </p>
            </header>

            <div class="bg-slate-900 text-stone-100 p-6 rounded-xl overflow-x-auto shadow-lg mb-8 code-font text-sm md:text-base leading-tight">
<pre>
[ External Data ]                        [ Free Deployment Tier ]
       │
  OpenSky (Flights) ──────┐                 ┌──────────────────────────┐
  Open-Meteo (Weather) ───┤                 │ GitHub Actions (CI/CD)   │
                          ▼                 └──────────────────────────┘
             [ Data Ingestion Layer ]
             Python + Apache Airflow (Local/Docker)
             Extracts data every 10 mins
                          │
                          ▼
              [ Data Storage Layer ]
              Neon.tech (Serverless PostgreSQL)
              Raw JSON stored in JSONB columns
                          │
                          ▼
            [ Data Processing Layer ]
              dbt (Data Build Tool)
              Cleans, joins, creates materialized views
              (e.g., 'flights_with_severe_weather')
                          │
                          ▼
              [ Backend / API Layer ]
              FastAPI (Python)
              Deployed on Render.com (Free Tier)
              Serves aggregated JSON to UI
                          │
                          ▼
              [ Frontend / UI Layer ]
              Next.js + Tailwind + Chart.js
              Deployed on Vercel (Free Tier)
              Interactive Analytics Dashboard
</pre>
            </div>

            <h3 class="text-2xl font-bold text-slate-800 mb-4">The 100% Free Stack Selection</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="bg-white p-5 rounded-lg shadow-sm border border-stone-200">
                    <div class="text-2xl mb-2">⚙️</div>
                    <h4 class="font-bold text-slate-900">Data Eng</h4>
                    <p class="text-sm text-slate-600 mt-1">Python, Apache Airflow (Dockerized), dbt-core.</p>
                </div>
                <div class="bg-white p-5 rounded-lg shadow-sm border border-stone-200">
                    <div class="text-2xl mb-2">🗄️</div>
                    <h4 class="font-bold text-slate-900">Database</h4>
                    <p class="text-sm text-slate-600 mt-1">Neon.tech (Serverless Postgres) or Railway Free Tier.</p>
                </div>
                <div class="bg-white p-5 rounded-lg shadow-sm border border-stone-200">
                    <div class="text-2xl mb-2">🔌</div>
                    <h4 class="font-bold text-slate-900">Backend</h4>
                    <p class="text-sm text-slate-600 mt-1">FastAPI, Uvicorn, SQLAlchemy. Hosted on Render.</p>
                </div>
                <div class="bg-white p-5 rounded-lg shadow-sm border border-stone-200">
                    <div class="text-2xl mb-2">🎨</div>
                    <h4 class="font-bold text-slate-900">Frontend</h4>
                    <p class="text-sm text-slate-600 mt-1">Next.js (React), TailwindCSS, Chart.js. Hosted on Vercel.</p>
                </div>
            </div>
        </section>

        <!-- SECTION: Data Pipeline -->
        <section id="data-pipeline" class="section-content max-w-5xl mx-auto">
            <header class="mb-8">
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-3">Full Data Pipeline Design</h2>
                <p class="text-lg text-slate-600 leading-relaxed">
                    This section details the journey of a data point from extraction to visualization. Click through the phases to understand the ELT (Extract, Load, Transform) process implemented in this architecture.
                </p>
            </header>

            <div class="flex flex-col md:flex-row gap-6">
                <!-- Pipeline Navigation -->
                <div class="w-full md:w-1/3 flex flex-col gap-2">
                    <button class="pipe-btn w-full text-left p-4 bg-white border border-stone-200 rounded-lg shadow-sm hover:border-emerald-500 font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500 active-pipe" data-step="extract">1. Extraction (Airflow)</button>
                    <button class="pipe-btn w-full text-left p-4 bg-white border border-stone-200 rounded-lg shadow-sm hover:border-emerald-500 font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500" data-step="load">2. Raw Loading (Postgres)</button>
                    <button class="pipe-btn w-full text-left p-4 bg-white border border-stone-200 rounded-lg shadow-sm hover:border-emerald-500 font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500" data-step="transform">3. Transformation (dbt)</button>
                    <button class="pipe-btn w-full text-left p-4 bg-white border border-stone-200 rounded-lg shadow-sm hover:border-emerald-500 font-semibold focus:outline-none focus:ring-2 focus:ring-emerald-500" data-step="serve">4. API Serving (FastAPI)</button>
                </div>

                <!-- Pipeline Content Details -->
                <div class="w-full md:w-2/3 bg-white p-6 md:p-8 rounded-xl border border-stone-200 shadow-sm min-h-[300px]">
                    <div id="pipe-extract" class="pipe-content block">
                        <div class="flex items-center mb-4"><span class="text-3xl mr-3">🎣</span><h3 class="text-2xl font-bold">Extraction (The "E")</h3></div>
                        <p class="text-slate-600 mb-4">An Apache Airflow DAG is triggered every 10 minutes. It executes Python tasks using the <code>requests</code> library.</p>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2 mb-4">
                            <li><strong>Task 1:</strong> Hits OpenSky API to pull current state vectors for flights over a specific bounding box (e.g., North America).</li>
                            <li><strong>Task 2:</strong> Extracts coordinates from flights and hits Open-Meteo API to get localized weather data (wind speed, precipitation) for those coordinates.</li>
                        </ul>
                        <div class="bg-slate-100 p-3 rounded code-font text-sm text-slate-800 border border-slate-200">
                            Failure handling: Retries set to 3 with exponential backoff.
                        </div>
                    </div>
                    
                    <div id="pipe-load" class="pipe-content hidden">
                        <div class="flex items-center mb-4"><span class="text-3xl mr-3">📥</span><h3 class="text-2xl font-bold">Raw Loading (The "L")</h3></div>
                        <p class="text-slate-600 mb-4">Instead of transforming data in Python memory, we dump the raw JSON responses directly into our cloud database. This is modern ELT practice.</p>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2 mb-4">
                            <li>Target: Neon Serverless PostgreSQL.</li>
                            <li>Schema: <code>raw_data</code> schema.</li>
                            <li>Tables: <code>raw_flights</code> and <code>raw_weather</code>. Both feature a timestamp and a <code>JSONB</code> column containing the entire API payload.</li>
                        </ul>
                        <div class="bg-emerald-50 text-emerald-800 p-3 rounded text-sm border border-emerald-200">
                            <strong>Why?</strong> If our transformation logic breaks later, we never lose the historical raw data. We can re-run transformations at any time.
                        </div>
                    </div>

                    <div id="pipe-transform" class="pipe-content hidden">
                        <div class="flex items-center mb-4"><span class="text-3xl mr-3">🏗️</span><h3 class="text-2xl font-bold">Transformation (The "T")</h3></div>
                        <p class="text-slate-600 mb-4">Data Build Tool (dbt) takes over. It connects to PostgreSQL and runs SQL-based transformations to create analytical models.</p>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2 mb-4">
                            <li><strong>Staging Models:</strong> Extracts fields from the <code>JSONB</code> columns, casts data types (string to float for coordinates), and handles nulls.</li>
                            <li><strong>Core Models:</strong> Joins <code>stg_flights</code> and <code>stg_weather</code> based on time and nearest coordinate proximity.</li>
                            <li><strong>Mart Models:</strong> Creates aggregated views like <code>hourly_disruption_metrics</code> (count of flights in high wind zones).</li>
                        </ul>
                        <p class="text-sm text-slate-500 italic mt-2">Includes dbt tests to ensure no duplicate flight IDs exist per timestamp.</p>
                    </div>

                    <div id="pipe-serve" class="pipe-content hidden">
                        <div class="flex items-center mb-4"><span class="text-3xl mr-3">🚀</span><h3 class="text-2xl font-bold">API Serving</h3></div>
                        <p class="text-slate-600 mb-4">A FastAPI application exposes the finalized dbt mart tables to the frontend via RESTful endpoints.</p>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2 mb-4">
                            <li><code>GET /api/v1/flights/current</code> - Returns latest active flights.</li>
                            <li><code>GET /api/v1/metrics/disruptions?timeframe=24h</code> - Queries the aggregated dbt views for chart generation.</li>
                        </ul>
                        <p class="text-sm text-slate-600">FastAPI utilizes Pydantic for strict output validation and automatically generates OpenAPI (Swagger) documentation.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION: Implementation Plan -->
        <section id="implementation" class="section-content max-w-5xl mx-auto">
             <header class="mb-8">
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-3">Roadmap & Repository Structure</h2>
                <p class="text-lg text-slate-600 leading-relaxed">
                    A structured approach to building the portfolio project to ensure you don't get overwhelmed. Build sequentially, testing at each phase.
                </p>
            </header>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <!-- Roadmap -->
                <div>
                    <h3 class="text-2xl font-bold text-slate-800 mb-4">Step-by-Step Roadmap</h3>
                    <div class="space-y-4 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-slate-300 before:to-transparent">
                        
                        <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                            <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-slate-900 text-slate-100 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 relative z-10">1</div>
                            <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-4 rounded border border-stone-200 shadow-sm">
                                <h4 class="font-bold text-slate-800">Local Infrastructure Setup</h4>
                                <p class="text-sm text-slate-600 mt-1">Setup Docker Compose with Postgres and Airflow. Initialize Git repo.</p>
                            </div>
                        </div>

                        <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                            <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-slate-200 text-slate-700 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 relative z-10">2</div>
                            <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-4 rounded border border-stone-200 shadow-sm">
                                <h4 class="font-bold text-slate-800">Python Ingestion (DAG)</h4>
                                <p class="text-sm text-slate-600 mt-1">Write scripts to ping OpenSky/Open-Meteo and insert raw JSONB to Postgres.</p>
                            </div>
                        </div>

                        <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                            <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-slate-200 text-slate-700 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 relative z-10">3</div>
                            <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-4 rounded border border-stone-200 shadow-sm">
                                <h4 class="font-bold text-slate-800">dbt Modeling</h4>
                                <p class="text-sm text-slate-600 mt-1">Initialize dbt core. Write staging and dimensional models to clean data.</p>
                            </div>
                        </div>

                         <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                            <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-slate-200 text-slate-700 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 relative z-10">4</div>
                            <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-4 rounded border border-stone-200 shadow-sm">
                                <h4 class="font-bold text-slate-800">FastAPI Backend</h4>
                                <p class="text-sm text-slate-600 mt-1">Build endpoints connecting to dbt mart tables. Test locally with Swagger.</p>
                            </div>
                        </div>

                        <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                            <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-slate-200 text-slate-700 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 relative z-10">5</div>
                            <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-4 rounded border border-stone-200 shadow-sm">
                                <h4 class="font-bold text-slate-800">Next.js Frontend</h4>
                                <p class="text-sm text-slate-600 mt-1">Build UI layout, integrate Chart.js, fetch data from local FastAPI.</p>
                            </div>
                        </div>

                        <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                            <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-slate-200 text-slate-700 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 relative z-10">6</div>
                            <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-4 rounded border border-stone-200 shadow-sm border-l-4 border-l-emerald-500">
                                <h4 class="font-bold text-slate-800">Cloud Deployment</h4>
                                <p class="text-sm text-slate-600 mt-1">Migrate DB to Neon. Deploy API to Render. Deploy UI to Vercel. Setup GitHub Actions.</p>
                            </div>
                        </div>

                    </div>
                </div>

                <!-- Repo Structure -->
                <div>
                    <h3 class="text-2xl font-bold text-slate-800 mb-4">Repository Structure</h3>
                    <div class="bg-slate-900 text-emerald-400 p-5 rounded-xl code-font text-sm h-full max-h-[600px] overflow-y-auto shadow-inner">
<pre>
aerosense-portfolio/
├── .github/
│   └── workflows/
│       ├── test_api.yml
│       └── deploy_dbt.yml
├── data_pipeline/         # Data Eng
│   ├── airflow/
│   │   ├── dags/
│   │   │   └── ingest_flights.py
│   │   └── Dockerfile
│   └── dbt_models/
│       ├── dbt_project.yml
│       ├── models/
│       │   ├── staging/
│       │   └── marts/
│       └── tests/
├── backend/               # Backend API
│   ├── main.py
│   ├── database.py
│   ├── routers/
│   │   ├── flights.py
│   │   └── metrics.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/              # Web UI
│   ├── package.json
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx
│   │   │   └── globals.css
│   │   └── components/
│   │       ├── ChartContainer.tsx
│   │       └── KPIBoxes.tsx
├── docker-compose.yml     # Local Env
└── README.md              # Documentation
</pre>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION: Code Samples (BONUS) -->
        <section id="code-samples" class="section-content max-w-5xl mx-auto">
             <header class="mb-8">
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-3">Code Previews (Bonus)</h2>
                <p class="text-lg text-slate-600 leading-relaxed">
                    Snippets demonstrating the complexity and production-readiness of the architecture. This shows recruiters you write clean, documented code.
                </p>
            </header>

            <div class="space-y-6">
                <!-- Sample 1 -->
                <div class="bg-white border border-stone-200 rounded-xl overflow-hidden shadow-sm">
                    <div class="bg-stone-100 px-4 py-2 border-b border-stone-200 font-semibold text-sm text-slate-700 flex justify-between">
                        <span>data_pipeline/airflow/dags/ingest_flights.py</span>
                        <span class="text-xs bg-slate-200 px-2 py-1 rounded text-slate-600">Python / Airflow</span>
                    </div>
                    <div class="p-4 bg-slate-900 text-stone-100 code-font text-sm overflow-x-auto">
<pre>
<span class="text-emerald-400">from</span> airflow <span class="text-emerald-400">import</span> DAG
<span class="text-emerald-400">from</span> airflow.operators.python <span class="text-emerald-400">import</span> PythonOperator
<span class="text-emerald-400">from</span> datetime <span class="text-emerald-400">import</span> datetime, timedelta
<span class="text-emerald-400">import</span> requests, psycopg2, json

<span class="text-slate-400"># Default arguments with robust retry logic</span>
default_args = {
    <span class="text-yellow-300">'owner'</span>: <span class="text-yellow-300">'data_engineer'</span>,
    <span class="text-yellow-300">'depends_on_past'</span>: <span class="text-emerald-400">False</span>,
    <span class="text-yellow-300">'start_date'</span>: datetime(2023, 1, 1),
    <span class="text-yellow-300">'retries'</span>: 3,
    <span class="text-yellow-300">'retry_delay'</span>: timedelta(minutes=2),
}

<span class="text-emerald-400">def</span> <span class="text-blue-400">extract_and_load_raw_flights</span>():
    <span class="text-slate-400">"""Pulls from OpenSky and dumps raw JSONB to Postgres"""</span>
    url = <span class="text-yellow-300">"https://opensky-network.org/api/states/all"</span>
    response = requests.get(url, timeout=10)
    data = response.json()
    
    conn = psycopg2.connect(<span class="text-yellow-300">"postgresql://user:pass@host:5432/neon_db"</span>)
    cursor = conn.cursor()
    cursor.execute(
        <span class="text-yellow-300">"INSERT INTO raw_data.raw_flights (ingest_time, payload) VALUES (%s, %s)"</span>,
        (datetime.now(), json.dumps(data))
    )
    conn.commit()
    conn.close()

<span class="text-emerald-400">with</span> DAG(<span class="text-yellow-300">'aerosense_ingestion'</span>, default_args=default_args, schedule_interval=<span class="text-yellow-300">'*/10 * * * *'</span>) <span class="text-emerald-400">as</span> dag:
    
    task_extract_flights = PythonOperator(
        task_id=<span class="text-yellow-300">'extract_opensky_data'</span>,
        python_callable=extract_and_load_raw_flights
    )
</pre>
                    </div>
                </div>

                <!-- Sample 2 -->
                 <div class="bg-white border border-stone-200 rounded-xl overflow-hidden shadow-sm">
                    <div class="bg-stone-100 px-4 py-2 border-b border-stone-200 font-semibold text-sm text-slate-700 flex justify-between">
                        <span>backend/routers/metrics.py</span>
                        <span class="text-xs bg-slate-200 px-2 py-1 rounded text-slate-600">Python / FastAPI</span>
                    </div>
                    <div class="p-4 bg-slate-900 text-stone-100 code-font text-sm overflow-x-auto">
<pre>
<span class="text-emerald-400">from</span> fastapi <span class="text-emerald-400">import</span> APIRouter, Depends
<span class="text-emerald-400">from</span> sqlalchemy.orm <span class="text-emerald-400">import</span> Session
<span class="text-emerald-400">from</span> dependencies <span class="text-emerald-400">import</span> get_db

router = APIRouter()

<span class="text-yellow-300">@router.get</span>(<span class="text-yellow-300">"/api/v1/metrics/disruptions"</span>)
<span class="text-emerald-400">def</span> <span class="text-blue-400">get_disruption_metrics</span>(hours: int = 24, db: Session = Depends(get_db)):
    <span class="text-slate-400">"""
    Queries the dbt mart table to serve analytical data to the Next.js frontend.
    """</span>
    query = <span class="text-yellow-300">f"""
        SELECT 
            hour_bucket, 
            flights_in_severe_weather,
            total_active_flights
        FROM 
            marts.hourly_disruption_metrics
        WHERE 
            hour_bucket >= NOW() - INTERVAL '{hours} hours'
        ORDER BY 
            hour_bucket ASC;
    """</span>
    result = db.execute(query).fetchall()
    
    <span class="text-emerald-400">return</span> [{
        <span class="text-yellow-300">"timestamp"</span>: row.hour_bucket,
        <span class="text-yellow-300">"impacted"</span>: row.flights_in_severe_weather,
        <span class="text-yellow-300">"total"</span>: row.total_active_flights
    } <span class="text-emerald-400">for</span> row <span class="text-emerald-400">in</span> result]
</pre>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION: Mock Dashboard -->
        <section id="demo-dashboard" class="section-content max-w-5xl mx-auto">
            <header class="mb-8">
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-3">Live Application Mockup</h2>
                <p class="text-lg text-slate-600 leading-relaxed">
                    This represents what the final Next.js / Tailwind frontend will look like. It consumes the FastAPI endpoints (simulated here with JavaScript) to present actionable insights derived from the Airflow/dbt pipeline.
                </p>
            </header>

            <!-- Dashboard Container -->
            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 md:p-6 shadow-sm">
                
                <!-- Dashboard Header -->
                <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-6 pb-4 border-b border-slate-200">
                    <div>
                        <h3 class="text-2xl font-bold text-slate-800">AeroSense Ops Center</h3>
                        <p class="text-sm text-slate-500">Live Global Airspace & Weather Anomalies</p>
                    </div>
                    <div class="mt-4 md:mt-0 flex gap-2">
                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800">
                            <span class="w-2 h-2 mr-1.5 bg-emerald-500 rounded-full animate-pulse"></span>
                            Pipeline: Healthy
                        </span>
                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                            Last Sync: Just now
                        </span>
                    </div>
                </div>

                <!-- KPI Cards -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                    <div class="bg-white p-4 rounded-lg shadow border border-slate-100">
                        <p class="text-sm font-medium text-slate-500 truncate">Total Active Flights</p>
                        <p class="mt-1 text-3xl font-semibold text-slate-900">14,203</p>
                    </div>
                    <div class="bg-white p-4 rounded-lg shadow border border-slate-100 border-l-4 border-l-orange-500">
                        <p class="text-sm font-medium text-slate-500 truncate">Flights in Weather Alert Zones</p>
                        <p class="mt-1 text-3xl font-semibold text-orange-600">842</p>
                    </div>
                    <div class="bg-white p-4 rounded-lg shadow border border-slate-100">
                        <p class="text-sm font-medium text-slate-500 truncate">Ingestion Latency</p>
                        <p class="mt-1 text-3xl font-semibold text-slate-900">1.2s</p>
                    </div>
                </div>

                <!-- Main Chart Area -->
                <div class="bg-white p-4 rounded-lg shadow border border-slate-100 mb-4">
                    <h4 class="text-base font-semibold text-slate-800 mb-2">24H Disruption Trend (Total Flights vs. Weather Impacted)</h4>
                    <p class="text-xs text-slate-500 mb-4">Data aggregated via dbt and served by FastAPI.</p>
                    
                    <!-- Strict Chart Container -->
                    <div class="chart-container w-full h-[300px] max-h-[400px]">
                        <canvas id="disruptionChart"></canvas>
                    </div>
                </div>

            </div>
        </section>

    </main>

    <!-- JavaScript Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // --- Navigation Logic ---
            const navItems = document.querySelectorAll('.nav-item');
            const sections = document.querySelectorAll('.section-content');
            const mobileMenuBtn = document.getElementById('mobile-menu-btn');
            const sidebar = document.getElementById('sidebar');

            function switchSection(targetId) {
                // Update active nav item
                navItems.forEach(item => {
                    item.classList.remove('active');
                    if(item.dataset.target === targetId) {
                        item.classList.add('active');
                    }
                });

                // Update active section
                sections.forEach(section => {
                    section.classList.remove('active');
                    if(section.id === targetId) {
                        section.classList.add('active');
                    }
                });

                // Close mobile menu if open
                if(window.innerWidth < 768) {
                    sidebar.classList.add('-translate-x-full');
                }
            }

            navItems.forEach(item => {
                item.addEventListener('click', () => {
                    switchSection(item.dataset.target);
                    
                    // Specific chart initializations if navigating to tabs with charts
                    if(item.dataset.target === 'exec-summary' && !window.techChartRendered) {
                        renderTechChart();
                    }
                    if(item.dataset.target === 'demo-dashboard' && !window.dashChartRendered) {
                        renderDashboardChart();
                    }
                });
            });

            // Mobile menu toggle
            mobileMenuBtn.addEventListener('click', () => {
                sidebar.classList.toggle('-translate-x-full');
            });

            // --- Pipeline Interaction Logic ---
            const pipeBtns = document.querySelectorAll('.pipe-btn');
            const pipeContents = document.querySelectorAll('.pipe-content');

            pipeBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // Reset styling
                    pipeBtns.forEach(b => {
                        b.classList.remove('border-emerald-500', 'bg-emerald-50');
                        b.classList.add('border-stone-200');
                    });
                    // Hide all content
                    pipeContents.forEach(content => {
                        content.classList.add('hidden');
                        content.classList.remove('block', 'animate-[fadeIn_0.3s_ease-in-out]');
                    });

                    // Set active
                    btn.classList.add('border-emerald-500', 'bg-emerald-50');
                    btn.classList.remove('border-stone-200');
                    
                    const targetContent = document.getElementById(`pipe-${btn.dataset.step}`);
                    targetContent.classList.remove('hidden');
                    targetContent.classList.add('block', 'animate-[fadeIn_0.3s_ease-in-out]');
                });
            });


            // --- Chart.js Initializations ---
            
            // 1. Tech Stack Doughnut Chart (Exec Summary)
            function renderTechChart() {
                const ctx = document.getElementById('techStackChart').getContext('2d');
                new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: ['Data Eng (Airflow/dbt)', 'Backend (FastAPI)', 'Frontend (Next.js)', 'DevOps (Docker/CI)'],
                        datasets: [{
                            data: [35, 25, 25, 15],
                            backgroundColor: [
                                '#0ea5e9', // sky-500
                                '#10b981', // emerald-500
                                '#f59e0b', // amber-500
                                '#64748b'  // slate-500
                            ],
                            borderWidth: 0,
                            hoverOffset: 4
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false, // Critical for custom container sizing
                        plugins: {
                            legend: {
                                position: 'right',
                                labels: { font: { family: "'Inter', sans-serif" } }
                            }
                        },
                        cutout: '70%'
                    }
                });
                window.techChartRendered = true;
            }

            // Render Tech chart immediately since it's on the first active tab
            renderTechChart();

            // 2. Dashboard Mockup Combo Chart
            function renderDashboardChart() {
                const ctxDash = document.getElementById('disruptionChart').getContext('2d');
                
                // Mock data generation
                const labels = Array.from({length: 24}, (_, i) => `${i}:00`);
                const totalFlights = labels.map(() => Math.floor(Math.random() * 5000) + 10000); // 10k - 15k
                const impactedFlights = totalFlights.map(total => Math.floor(total * (Math.random() * 0.15))); // 0-15% impacted

                new Chart(ctxDash, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                type: 'bar',
                                label: 'Weather Impacted Flights',
                                data: impactedFlights,
                                backgroundColor: 'rgba(249, 115, 22, 0.8)', // orange-500
                                yAxisID: 'y1',
                                borderRadius: 4
                            },
                            {
                                type: 'line',
                                label: 'Total Global Flights',
                                data: totalFlights,
                                borderColor: '#334155', // slate-700
                                backgroundColor: 'transparent',
                                borderWidth: 2,
                                tension: 0.3,
                                pointRadius: 0,
                                yAxisID: 'y'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false, // Critical for custom container sizing
                        interaction: {
                            mode: 'index',
                            intersect: false,
                        },
                        plugins: {
                            legend: {
                                position: 'top',
                                labels: { font: { family: "'Inter', sans-serif" } }
                            },
                            tooltip: {
                                callbacks: {
                                    // Custom tooltip logic if needed (e.g. 16 char wrap can be done here by splitting strings, but standard handles numbers well)
                                }
                            }
                        },
                        scales: {
                            y: {
                                type: 'linear',
                                display: true,
                                position: 'left',
                                title: { display: true, text: 'Total Flights' },
                                grid: { color: '#f1f5f9' }
                            },
                            y1: {
                                type: 'linear',
                                display: true,
                                position: 'right',
                                title: { display: true, text: 'Impacted' },
                                grid: { drawOnChartArea: false } // only draw grid lines for one axis
                            },
                            x: {
                                grid: { display: false }
                            }
                        }
                    }
                });
                window.dashChartRendered = true;
            }
        });
    </script>
</body>
</html>
