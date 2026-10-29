# 🚛 Fleet Fuel Analytics Uganda - Fuel Theft Detection

Detecting fuel anomalies and theft in 300+ fleet trips across Kampala-Gulu-Mombasa-Kigali routes using Python.

*Author:* Egwelu Amos | IVMS & Fleet Officer (9 Years @ Mota-Engil) | Aspiring Data Analyst

### 📊 Business Problem
Vehicles face 15-20% fuel variance monthly. Manual checks in Wialon/VSS miss sophisticated siphoning. Goal: Build automated detection to save monthly.

### 📁 Dataset
- 300 trips (Synthetic but based on real IVMS patterns)
- Columns: Vehicle_ID, Route, Distance_km, Fuel_Consumed_L, Fuel_Expected_L, Variance_%, Driver_ID, Anomaly_Flag
- Tools: Wialon, Galooli patterns simulated
- File: data/fleet_fuel_data_300.csv

### 🛠️ Tech Stack
- Python (Pandas, NumPy, Matplotlib, Scikit-learn)
- SQL (for trip aggregation)
- Power BI (Dashboard - coming)
- Anomaly Detection: Isolation Forest

### 🔍 Key Findings (From Python Analysis)
1. 12% trips flagged as high variance (>20%)
2. Gulu-Mombasa route has highest theft rate
3. Night trips 3x more likely to have variance
4. 5 vehicles contribute 40% of total fuel loss

### 📈 Visuals
- Fuel Variance Distribution
- Route-wise Theft Analysis
- Driver Risk Scoring

### 💰 Business Impact
- Simulated savings: *UGX 12M/month*
- Accident reduction correlation
- Predictive maintenance opportunity

### 🚀 How to Run
```bash
pip install pandas scikit-learn matplotlib
python analysis.py
