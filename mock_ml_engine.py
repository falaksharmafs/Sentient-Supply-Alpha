import random

LOCATIONS = [
    # Energy
    {"name": "Ras Tanura, Saudi Arabia", "type": "OCEAN", "lat": 26.65, "lng": 50.16, "asset": "Crude Oil (CL)", "metric_type": "Tanker Kinematics"},
    {"name": "Henry Hub, LA, USA", "type": "LAND", "lat": 29.88, "lng": -91.98, "asset": "Natural Gas (NG)", "metric_type": "Pipeline Flow Sensors"},
    {"name": "Newcastle Port, Australia", "type": "OCEAN", "lat": -32.92, "lng": 151.78, "asset": "Coal", "metric_type": "Bulk Carrier Telemetry"},
    {"name": "Sullom Voe, UK", "type": "OCEAN", "lat": 60.45, "lng": -1.27, "asset": "Brent Crude (BZ)", "metric_type": "Tanker Kinematics"},
    {"name": "Saskatchewan, Canada", "type": "LAND", "lat": 55.0, "lng": -106.0, "asset": "Uranium (UX)", "metric_type": "Mining Truck GPS"},
    
    # Precious / Industrial Metals
    {"name": "Johannesburg, RSA", "type": "LAIR", "lat": -26.2, "lng": 28.04, "asset": "Gold (GC)", "metric_type": "Flight Radar / Transports"},
    {"name": "Peñasquito, Mexico", "type": "LAND", "lat": 24.69, "lng": -101.62, "asset": "Silver (SI)", "metric_type": "Rail Transponders"},
    {"name": "Antofagasta Port, Chile", "type": "OCEAN", "lat": -23.65, "lng": -70.4, "asset": "Copper (HG)", "metric_type": "Ship Telemetry (AIS)"},
    {"name": "Port Hedland, Australia", "type": "OCEAN", "lat": -20.31, "lng": 118.57, "asset": "Iron Ore", "metric_type": "Bulk Carrier Telemetry"},
    {"name": "Sudbury Basin, Canada", "type": "LAND", "lat": 46.49, "lng": -81.01, "asset": "Nickel", "metric_type": "Rail Transponders"},
    {"name": "Norilsk, Russia", "type": "AIR", "lat": 69.34, "lng": 88.21, "asset": "Palladium/Platinum", "metric_type": "Flight Radar (ADS-B)"},
    {"name": "Red Dog Mine, Alaska", "type": "LAND", "lat": 68.07, "lng": -162.86, "asset": "Zinc", "metric_type": "Trucking GPS"},
    {"name": "Mount Isa, Australia", "type": "LAND", "lat": -20.72, "lng": 139.49, "asset": "Lead", "metric_type": "Rail Transponders"},
    {"name": "Gulf Coast, USA", "type": "OCEAN", "lat": 29.76, "lng": -95.36, "asset": "Aluminum (ALI)", "metric_type": "Ship Telemetry (AIS)"},
    
    # Softs / Agriculture
    {"name": "Port of Odesa, Ukraine", "type": "OCEAN", "lat": 46.48, "lng": 30.73, "asset": "Wheat (ZW)", "metric_type": "Bulk Carrier Telemetry"},
    {"name": "Paranaguá Port, Brazil", "type": "OCEAN", "lat": -25.5, "lng": -48.5, "asset": "Soybeans (ZS)", "metric_type": "Ship Telemetry (AIS)"},
    {"name": "New Orleans, USA", "type": "OCEAN", "lat": 29.95, "lng": -90.07, "asset": "Corn (ZC)", "metric_type": "River Barge Kinematics"},
    {"name": "Port of Santos, Brazil", "type": "OCEAN", "lat": -23.96, "lng": -46.33, "asset": "Coffee (KC)", "metric_type": "Ship Telemetry (AIS)"},
    {"name": "Port of Mumbai, India", "type": "OCEAN", "lat": 18.94, "lng": 72.83, "asset": "Sugar (SB)", "metric_type": "Ship Telemetry (AIS)"},
    {"name": "Port of Abidjan, Ivory Coast", "type": "OCEAN", "lat": 5.3, "lng": -4.01, "asset": "Cocoa (CC)", "metric_type": "Ship Telemetry (AIS)"},
    {"name": "Port of Shanghai, China", "type": "OCEAN", "lat": 31.23, "lng": 121.47, "asset": "Cotton (CT)", "metric_type": "Container Telemetry"},
    {"name": "Port of Singapore", "type": "OCEAN", "lat": 1.29, "lng": 103.85, "asset": "Rubber", "metric_type": "Ship Telemetry (AIS)"},
    {"name": "Vancouver Port, Canada", "type": "OCEAN", "lat": 49.28, "lng": -123.12, "asset": "Lumber (LBS)", "metric_type": "Ship Telemetry (AIS)"},
    
    # Livestock
    {"name": "Chicago, USA", "type": "LAND", "lat": 41.87, "lng": -87.62, "asset": "Live Cattle (LE)", "metric_type": "Weigh Station Transponders"},
    {"name": "Tar Heel, NC, USA", "type": "LAND", "lat": 34.73, "lng": -78.79, "asset": "Lean Hogs (HE)", "metric_type": "Trucking GPS"}
]

def generate_telemetry():
    """Generates mock traffic data across Ocean, Land, and Air."""
    events = []
    for loc in LOCATIONS:
        if loc["type"] == "OCEAN":
            base_volume = random.randint(100, 500)
            unit = "Vessels"
        elif loc["type"] == "LAND":
            base_volume = random.randint(5000, 15000)
            unit = "Transports"
        else: # AIR or LAIR
            base_volume = random.randint(50, 400)
            unit = "Flights"
            
        current_volume = int(base_volume * random.uniform(0.4, 1.3))
        
        anomaly = "Severe Blockage/Delay" if current_volume < base_volume * 0.6 else ("Normal" if current_volume < base_volume * 1.1 else "Surge/Congestion")
        
        events.append({
            "location": loc["name"],
            "type": loc["type"],
            "lat": loc["lat"],
            "lng": loc["lng"],
            "related_asset": loc["asset"],
            "telemetry_source": loc["metric_type"],
            "avg_30d_volume": f"{base_volume} {unit}",
            "current_volume": f"{current_volume} {unit}",
            "status": anomaly
        })
    return events

def generate_nlp_news():
    """Generates mock translated local news sentiment cross-modal."""
    news = [
        {"location": "Ras Tanura, Saudi Arabia", "route_type": "OCEAN", "headline": "Unconfirmed reports of drone activity near pumping stations.", "sentiment": -0.85},
        {"location": "Antofagasta Port, Chile", "route_type": "OCEAN", "headline": "Copper union workers reject pay offer, strike looms.", "sentiment": -0.92},
        {"location": "Port of Odesa, Ukraine", "route_type": "OCEAN", "headline": "Inspections delayed by 48 hours for grain corridor vessels.", "sentiment": -0.65},
        {"location": "Paranaguá Port, Brazil", "route_type": "OCEAN", "headline": "Heavy continuous rains halting soybean loading.", "sentiment": -0.88},
        {"location": "Henry Hub, LA, USA", "route_type": "LAND", "headline": "Compressor station failure reported, pipeline flows restricted.", "sentiment": -0.75}
    ]
    return random.sample(news, 3) 

def generate_vit_satellite():
    """Generates Vision Transformer metrics for all transport types."""
    return [
        {"location": "Paranaguá Port, Brazil", "metric": "Crop Heat Map (NDVI)", "value": "Severe Flooding DamageDetected"},
        {"location": "Johannesburg, RSA", "metric": "Mine Tailings Monitor", "value": "Activity down 25% w/w"},
        {"location": "Ras Tanura, Saudi Arabia", "metric": "Tanker Shadow Tracking", "value": "Vessels floating empty offshore."}
    ]

def generate_geopolitics():
    """Generates country-level macroeconomic and geopolitical data."""
    events = [
        {"country": "China", "event": "Export Quota Reduction", "impact_score": -0.85, "affected_assets": ["Steel", "Rare Earths", "Cotton"]},
        {"country": "Russia", "event": "Sanction Expansion Threat", "impact_score": -0.90, "affected_assets": ["Palladium", "Wheat", "Oil"]},
        {"country": "Brazil", "event": "New Export Tax legislation introduced", "impact_score": -0.65, "affected_assets": ["Soybeans", "Sugar", "Coffee"]},
        {"country": "Australia", "event": "Bilateral Trade Agreement Signed", "impact_score": +0.80, "affected_assets": ["Coal", "Iron Ore", "Lead"]}
    ]
    return random.sample(events, 2)
