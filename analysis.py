# Fleet Fuel Theft Detection - Uganda
import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv('fleet_fuel_data_300.csv')
print(f"Total trips: {len(df)}")
print(f"Theft cases: {df['Anomaly_Flag'].sum()}")

# Route Analysis
route_stats = df.groupby('Route')['Variance_%'].mean().sort_values(ascending=False)
print("\nRoute-wise Variance %:")
print(route_stats)

# Driver Risk Score
driver_risk = df.groupby('Driver_ID')['Variance_%'].mean().sort_values(ascending=False)
print("\nTop Risky Drivers:")
print(driver_risk.head())

# AI Detection
model = IsolationForest(contamination=0.12, random_state=42)
df['AI_Detected'] = model.fit_predict(df[['Variance_%']])
print(f"\nAI detected {len(df[df['AI_Detected']==-1])} anomalies")

# Business Impact
fuel_loss = df[df['Variance_%']>20]['Fuel_Consumed_L'].sum() - df[df['Variance_%']>20]['Fuel_Expected_L'].sum()
print(f"Estimated loss: UGX {fuel_loss*5000:,.0f}")
