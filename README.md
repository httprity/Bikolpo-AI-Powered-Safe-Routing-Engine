Bikolpo — AI-Powered Safe Routing Engine During Urban Floods
Bikolpo (বিকল্প) is an AI-powered routing engine that helps Dhaka citizens find the safest route during urban floods.
 Instead of choosing the fastest route only, Bikolpo evaluates flood probability on every road segment and reranks routes based on real-time risk.
Built with a custom ML model, synthetic physics-informed flood data, and an interactive Streamlit UI.

Key Features
AI Flood-Risk Prediction
ML model predicts flood probability for each road segment.


Trained on synthetic monsoon-driven hourly flood data.


Uses rainfall intensity, river levels, elevation, drainage, landcover, and historic flood patterns.


Safe Route Generation
Retrieves multiple possible routes using OpenRouteService.


Reranks them using a flood-aware scoring algorithm:


Safest Route


Balanced Route


Each segment is color-coded based on risk.


Interactive Frontend (Streamlit)
Clean UI with Bengali splash screen (বিকল্প).


Shows route cards with flood probability, distance, and ETA.


Users can switch between Car/Rickshaw and Walking modes.


Highlights “Why this route is the safest” using ML-driven insights.


Backend FastAPI Service
Exposes a /predict endpoint.


Geocodes Dhaka locations using a curated dataset.


Integrates ML model + routing service + risk scoring.


Returns route geometry + per-segment risk.
