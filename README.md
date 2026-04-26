# 🚀 Scalable Sensor Data Platform

A scalable real-time backend system for ingesting, processing, and analyzing high-frequency sensor time-series data with a focus on reliability, low latency, and digital twin readiness.

---

## 📌 Problem Statement

Modern engineering systems — especially in aerospace, industrial automation, and structural monitoring — generate massive volumes of high-frequency sensor data.

These systems require:
- Reliable ingestion of continuous data streams  
- Low-latency processing for real-time decisions  
- Scalable architecture to handle increasing sensor loads  

Traditional approaches struggle with:
- Data bottlenecks  
- Latency issues  
- Lack of real-time health insights  

This project addresses these challenges by building a **scalable, fault-tolerant backend system** for real-time sensor analytics.

---

## 🏗️ High-Level Architecture

The system is designed as a **modular, loosely coupled data pipeline**:

1. **Sensor Layer**
   - Simulated sensors generate high-frequency telemetry data

2. **Ingestion Layer**
   - Validates and receives incoming sensor data
   - Ensures reliable and consistent data flow

3. **Processing Layer**
   - Computes statistical metrics (avg, min, max)
   - Detects anomalies and stale sensors
   - Classifies sensor states (ACTIVE / STALE)

4. **Storage Layer**
   - Efficient handling of time-series data

5. **API Layer**
   - Exposes processed insights via FastAPI endpoints

6. **Monitoring Layer**
   - Tracks system health and sensor behavior


---

## ⚙️ Core Components

### 🔹 Sensor Simulator
Simulates high-frequency sensor data under varying conditions to mimic real-world systems.

### 🔹 Ingestion Service
Handles incoming data streams with validation and normalization.

### 🔹 Processing Engine
- Performs real-time and batch processing  
- Computes statistics  
- Detects anomalies and stale sensors  

### 🔹 API Layer
- Provides REST endpoints for accessing processed data  
- Enables external systems to consume insights  

### 🔹 Monitoring & Alerts
- Detects abnormal sensor behavior  
- Supports early failure detection  

---

## 🧠 Digital Twin Relevance

This system forms the **backend foundation of a Digital Twin architecture**.

### 🔄 Digital Twin Data Flow
1. **Physical System**
   - Sensors generate real-time telemetry data  

2. **Data Processing Layer (This Project)**
   - Processes raw sensor data  
   - Computes health metrics  
   - Classifies system state  

3. **API Layer**
   - Exposes structured data for external use  

4. **Digital Twin Layer (Future Integration)**
   - Virtual model consumes API data  
   - Updates system state in real time  
   - Enables simulation and prediction  

### 🎯 Outcome
- Real-time system monitoring  
- Predictive maintenance capability  
- Failure detection and diagnostics  

---
## 🚀 Aerospace Applications

### ✈️ Aircraft Health Monitoring
- Monitor engine and structural parameters  
- Detect inactive or faulty sensors  
- Improve safety and maintenance planning  

### 🚀 Rocket Systems
- Track combustion, pressure, and vibration  
- Detect anomalies during launch  
- Increase mission reliability  

### 🛰️ Satellite Systems
- Process limited telemetry efficiently  
- Identify critical subsystem failures  

---

## 📡 API Endpoints

- `GET /api/v1/health` → System health  
- `GET /api/v1/health/summary` → Sensor summary  
- `GET /api/v1/sensors/{sensor_id}` → Sensor details  
- `GET /api/v1/sensors` → All sensors  
- `GET /api/v1/sensors?state=STALE` → Filter sensors  

---

## 🛠️ Tech Stack

- Python  
- FastAPI  
- Pydantic  
- Uvicorn  

---

## 📂 Project Structure

src/
├── api.py
├── analysis.py
├── schemas.py
├── errors.py
├── logger.py

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
uvicorn src.api:app --reload

Open:
http://127.0.0.1:8000/docs

🚀 Future Improvements
Cloud deployment (AWS / GCP)
Real-time streaming (Kafka / WebSockets)
Advanced anomaly detection (ML-based)
Full Digital Twin simulation layer

👨‍💻 Author
  CHANDRAKALA KOTAPATI
  