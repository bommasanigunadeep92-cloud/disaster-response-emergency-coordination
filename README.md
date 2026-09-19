# AI-Assisted Smart Disaster Response & Emergency Coordination Platform

> **A Full-Stack, AI-Powered Crisis Coordination & Multi-Agency Emergency Management Platform**

---

## 1. Project Overview & Objective

During major natural and man-made disasters (such as flash floods, earthquakes, building structural collapses, and industrial chemical/gas leaks), emergency dispatch networks are overwhelmed with frantic, unstructured calls for help. 

This platform bridges the gap between distressed citizens and tactical rescue agencies (e.g., National Disaster Response Force, Fire Brigades, Trauma Ambulances, and Emergency Command Centers) through:
1. **Citizen SOS Reporting** with GPS auto-detection and casualty estimation.
2. **Relative / Proxy SOS Reporting** for victims unable to operate mobile devices.
3. **Automated AI Severity Triage** calculating 1–10 priority scores and dispatch suggestions.
4. **Geospatial Command Center Map** built on Leaflet to visualize incidents, hospitals, and squads.
5. **Dynamic Hazard-Avoiding Rescue Routing** providing alternate routes around blocked bridges/debris.
6. **Offline-First Synchronization** via browser storage (IndexedDB/LocalStorage) to survive telecom outages.
7. **Autonomous Aerial Drone AI Stream** for thermal and smoke early warning alerts.
8. **Real-time Incident Status & Lifecycle Tracking** (`New` → `Assigned` → `In Progress` → `Resolved`).
9. **Emergency Statistical Analytics** using Chart.js.

---

## 2. Technology Stack

| Layer | Technologies Used | Description / Role |
| :--- | :--- | :--- |
| **Frontend UI** | **React.js 18**, **Tailwind CSS**, **HTML5** | Modern, accessible emergency-themed user interface |
| **Geospatial Maps**| **Leaflet.js**, **OpenStreetMap Tiles** | Dynamic map plotting, pin popups, route polyline overlays |
| **Data Analytics** | **Chart.js** | Interactive charts for disaster type distributions and inflow trends |
| **Backend API** | **Python 3**, **FastAPI**, **Uvicorn** | High-performance asynchronous RESTful microservice |
| **Data Validation**| **Pydantic v2** | Strict schema validation and typed JSON payloads |
| **AI Triage Engine**| **Rule-Based NLP Heuristics** + **Google Gemini API Ready** | 1–10 Severity priority classifier & entity extraction |
| **Offline Storage**| **IndexedDB / LocalStorage** | Client-side queue for disaster network outages |
| **Authentication** | **Role-Based Access (RBAC) + JWT Concept** | Citizen, Field Responder (NDRF), Command Center Director |

---

## 3. Project Directory Structure

```
Disaster Response and Emergency Coordination Website/
│
├── backend/
│   ├── models/
│   │   └── incident.py           # Pydantic schemas: SOS, AI Triage, Routes, Drone Telemetry
│   ├── routes/
│   │   ├── incidents.py        # REST API endpoints for SOS, AI, routes, drones, sync
│   │   └── auth.py             # Role-based login and demo JWT token issuer
│   ├── services/
│   │   ├── ai_triage.py        # AI Triage classifier (NLP heuristics + Gemini LLM fallback)
│   │   ├── routing_service.py  # Dynamic rescue routing & hazard avoidance engine
│   │   ├── drone_detection.py  # Autonomous drone sensor telemetry stream
│   │   └── mock_database.py    # Thread-safe in-memory database with sample disaster data
│   ├── requirements.txt        # Python dependencies (FastAPI, Uvicorn, Pydantic)
│   ├── .env.example            # Environment variables template
│   └── main.py                 # FastAPI application root & static file server
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx             # React application source module
│   │   └── main.jsx            # React root mount
│   ├── index.html              # Complete self-contained single-page web application
│   └── package.json            # Node/npm metadata
│
├── run_app.bat                 # One-click Windows launcher (FastAPI + Browser)
├── run_app.ps1                 # PowerShell launcher script
└── README.md                   # Complete viva documentation & architectural guide
```

---

## 4. Current Demonstration vs. Full Production Architecture

As required by college presentation guidelines, this project provides a **100% working, zero-crash demonstration** out of the box while embedding clean production connection points:

| Component | Demonstration Version (Active) | Full Production Architecture |
| :--- | :--- | :--- |
| **AI Severity Triage** | **Intelligent Rule-Based NLP Classifier**<br>Analyzes 35+ danger tokens, casualty count weighting, and output scoring. Zero cost, no API key needed. | **Google Gemini 1.5 Flash API**<br>Activated by adding `GEMINI_API_KEY` to `.env`. Uses JSON schema parsing for complex audio/image/text SOS descriptions. |
| **Database** | **In-Memory Store with LocalStorage Cache**<br>Pre-seeded with realistic disaster incidents, hospitals, and rescue teams. | **PostgreSQL 16 + PostGIS**<br>Spatial geometry columns (`ST_DWithin`, `ST_Distance`), spatial indexing (`GIST`), and relational tables. |
| **Geospatial Maps** | **Leaflet with OpenStreetMap Tiles**<br>Real GPS coordinates, custom priority pins, polyline rerouting. | **Leaflet / Mapbox GL + PostGIS Vector Tiles**<br>Live GPS telemetry streaming via WebSockets. |
| **Offline Sync** | **LocalStorage / IndexedDB Queue**<br>Captures offline reports and batch-syncs upon reconnection. | **ServiceWorker + Background Sync API + PWA**<br>Full offline caching and automated background sync. |
| **Authentication** | **Simulated Role-Based JWT**<br>Instant switching between Citizen, Responder, and Command Center. | **FastAPI OAuth2 with JWT + Bcrypt Passwords**<br>Database-backed credential storage and token expiration. |

---

## 5. How to Run the Project

### Option 1: One-Click Launcher (Windows)
Double-click `run_app.bat` or run:
```powershell
.\run_app.bat
```
This automatically starts the FastAPI server and launches the web application in your default browser.

### Option 2: Manual Command Line
1. Open a terminal in the project directory.
2. Start the FastAPI backend server:
```powershell
python backend/main.py
```
3. Open your web browser and navigate to:
```
http://localhost:8000/
```

> **Interactive API Documentation:** View and test all REST endpoints directly in Swagger UI at `http://localhost:8000/docs`.

---

## 6. REST API Endpoints Reference

| HTTP Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/health` | Service health status and active engine metadata |
| `GET` | `/api/incidents` | Fetch all incidents with filters (`status`, `priority`, `search`) |
| `GET` | `/api/incidents/{id}` | Fetch detailed incident dossier and timeline audit log |
| `POST`| `/api/incidents/sos` | Submit citizen emergency SOS (triggers automated AI triage) |
| `POST`| `/api/incidents/proxy-sos` | Submit relative / third-party emergency SOS |
| `PUT` | `/api/incidents/{id}/status` | Update incident status (`New`, `Assigned`, `In Progress`, `Resolved`) |
| `POST`| `/api/ai-triage/analyze` | Standalone AI triage classifier for testing custom text |
| `GET` | `/api/routing/calculate` | Dynamic hazard-avoiding rescue route calculator |
| `GET` | `/api/drone-detections` | Live autonomous UAV sensor alert feed |
| `POST`| `/api/drone-detections/{id}/dispatch` | Convert drone detection alert directly into active SOS |
| `GET` | `/api/analytics` | Statistical summaries and casualty breakdowns |
| `POST`| `/api/offline/sync` | Batch synchronization of queued offline reports |
| `POST`| `/api/auth/login` | Role-based authentication and JWT simulation |

---

## 7. College Viva Guide & Demonstration Storyline

When presenting this project to examiners, demonstrate this narrative:

1. **The Citizen Crisis:**
   - Go to **Report SOS**. Enter details of a severe disaster (e.g. *"5 people trapped in collapsed building basement with gas leak"*).
   - Point out the **Live AI Pre-Triage meter** in the right panel calculating a **Priority 9/10 (CRITICAL)** score in real time.
   - Click **Submit Critical Emergency SOS**.

2. **Command Center Ingestion:**
   - The platform transitions to the **Responder Dashboard**.
   - Show how the newly created incident appears at the top of the queue with a red `CRITICAL` badge.
   - Click **View Dossier** to explain the AI reasoning and audit timeline log.
   - Assign a tactical rescue unit (e.g. `NDRF USAR Alpha`) and change status to `In Progress`.

3. **Geospatial Map Monitoring:**
   - Navigate to **Map Monitoring**.
   - Show the interactive Leaflet map with color-coded incident pins, nearby emergency hospitals (with live free ICU bed counts), and rescue squad bases.

4. **Dynamic Hazard Rerouting:**
   - Navigate to **Rescue Routing**.
   - Select the *"Riverside Flood"* scenario. Show examiners how the primary road is flagged in red with a flood hazard warning, while an elevated bypass flyover is calculated in green to ensure responder safety.

5. **Offline-First Resilience:**
   - Navigate to **Offline Sync**. Toggle network state to `Offline (Simulated)`.
   - Submit an SOS: show that the application does not crash, but safely buffers the report in the local queue with status `Pending Sync`.
   - Toggle back to `Online` and click **Sync Pending Reports** to demonstrate batch database ingestion.

6. **Autonomous Drone Feeds & Analytics:**
   - Show the **Drone AI** section with FLIR thermal heat detection and 1-click dispatch.
   - Conclude with the **Analytics** page displaying Chart.js distributions.

---

## 8. License & Acknowledgements
Built for academic and emergency management evaluation. Designed with clean modular code following professional software engineering standards.
