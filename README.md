# SENTINEL-X: Cross-Source Incident Intelligence Platform

**SIH 2025** | **Ministry of Home Affairs (MHA) / National Security Guard (NSG)**  
*AI and ML Enabled Video Analysis and Interpretation*

> **Pitch**: *"Surveillance systems record everything — investigators still have to manually piece together what matters. SENTINEL-X turns isolated camera feeds into one connected incident timeline, and generates an evidence-backed report in one click."*

---

## Key Features & 3 Core Locked Scope Modules

### 1. Detect (Multi-Source AI Analytics)
- Heterogeneous feed ingestion (Surveillance Drones, Tactical Scout Robots, Assault Operator Body Cameras, Stationary CCTV).
- Pretrained YOLOv8 / PyTorch object detection & multi-object ID persistence tracking.
- Automated anomaly classification (Person, Vehicle, Unattended Bag, Suspicious Loitering, Forced Entry Breach).

### 2. Connect (Spatial-Temporal Incident Graph Engine)
- Reconstructs single connected incident graph instead of isolated camera siloes.
- Temporal proximity correlation ($\Delta t \le 45\text{ seconds}$).
- Topological zone adjacency matching (Outer Perimeter Gate $\rightarrow$ North Courtyard $\rightarrow$ Building Entrance $\rightarrow$ Restricted Core).
- Cumulative incident threat risk calculation & spatial vector trajectory mapping.

### 3. Report & Explainable AI (AI LLM Incident Summarizer)
- AI LLM plain-language incident summary synthesis.
- 10-30s evidence clip snippet references & audit-ready Explainable AI cards answering "What", "Where", "When", "Why abnormal", and Risk score.
- One-click export options: PDF, Markdown, JSON, Tactical XML.

---

## Project Structure

```
sentinel-x/
├── backend/
│   ├── app/
│   │   ├── config.py
│   │   ├── main.py                  # FastAPI server
│   │   ├── modules/
│   │   │   ├── detect.py            # Module 1: Detect
│   │   │   ├── connect.py           # Module 2: Connect
│   │   │   ├── report.py            # Module 3: Report
│   │   │   └── explainable_ai.py    # XAI Engine
│   │   └── mock_data/
│   │       ├── camera_sources.json
│   │       ├── zone_topology.json
│   │       └── sample_incidents.json
│   └── server.js                    # Node.js backend runner
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── MultiCameraGrid.jsx
│   │   │   ├── IncidentTimeline.jsx
│   │   │   ├── ZoneMapView.jsx
│   │   │   ├── ExplainableAICard.jsx
│   │   │   ├── IncidentReportModal.jsx
│   │   │   └── OperatorFeedback.jsx
│   │   ├── services/
│   │   │   └── mockService.js       # Offline fallback & API client
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
└── README.md
```

---

## How to Run

### Option 1: Launch Backend with Node.js
```bash
cd backend
node server.js
# Backend runs on http://localhost:8000
```

### Option 2: Launch Frontend Development Server
```bash
cd frontend
& "C:\Program Files\nodejs\npm.cmd" install
& "C:\Program Files\nodejs\npm.cmd" run dev
# Frontend runs on http://localhost:3000
```
