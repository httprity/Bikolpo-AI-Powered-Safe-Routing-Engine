Bikolpo — AI-Powered Safe Routing Engine During Urban Floods

Bikolpo (বিকল্প) is an AI-powered routing engine designed to help commuters in Dhaka find the safest route during urban floods. Traditional routing focuses only on the fastest path, but during monsoon-season flooding, the fastest path can often be the most dangerous. Bikolpo changes this by predicting flood probability on every road segment and intelligently reranking routes based on real-time risk.

The system integrates a custom machine learning model trained on a physics-informed synthetic flood dataset with an interactive Streamlit interface and a FastAPI backend. The result is a complete end-to-end solution that not only visualizes route safety but also explains why a particular route is safer.

How It Works

At the core of Bikolpo is an ML model that predicts the flood probability of road segments. The model is trained on a synthetic monsoon-driven hourly dataset that simulates rainfall, river levels, temperature, humidity, flood persistence, drainage, elevation, landcover and spatial hotspots. These physics-based simulations allow the system to learn realistic flood behavior without depending on limited real-world flood data.

When a user enters a starting point and a destination, the backend fetches multiple possible routes from the OpenRouteService API. Each route is broken into individual segments, and the ML model assigns a flood probability to each one. A custom scoring algorithm then ranks the available routes as the safest, balanced, or fastest option. The results are returned to the frontend along with color-coded geometry, estimated risk levels and textual explanations for why a route is recommended.

The Streamlit frontend displays an interactive map with clear segment-level risk visualization, intuitive route cards, a Bengali splash screen and a simple mode selector for driving or walking. This makes the system not only intelligent, but also easy to use in real-world flood situations.
