from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mock_ml_engine import generate_telemetry, generate_nlp_news, generate_vit_satellite, generate_geopolitics
from trading_logic import calculate_arbitrage

app = FastAPI(title="Sentient Supply Alpha API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/dashboard")
def get_dashboard_data():
    telemetry_data = generate_telemetry()
    nlp_data = generate_nlp_news()
    vit_data = generate_vit_satellite()
    geo_data = generate_geopolitics()
    signals = calculate_arbitrage(telemetry_data, nlp_data, vit_data)
    
    return {
        "telemetry": telemetry_data,
        "nlp_news": nlp_data,
        "vit_satellite": vit_data,
        "geopolitics": geo_data,
        "arbitrage_signals": signals
    }
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
