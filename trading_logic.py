def calculate_arbitrage(ais_data, nlp_data, vit_data):
    """Combines all multi-modal metrics into a trading signal."""
    # Simplified mock logic to showcase the UI
    signals = []
    signals.append({
        "asset": "Soybean Futures (ZS)",
        "action": "LONG",
        "confidence": "94%",
        "reasoning": "ViT detected drought stress + NLP localized flood news"
    })
    signals.append({
        "asset": "Apple Suppliers (AAPL)",
        "action": "SHORT",
        "confidence": "88%",
        "reasoning": "AIS tracking shows 40% drop in container shipments leaving Shanghai."
    })
    signals.append({
        "asset": "Crude Oil (CL)",
        "action": "LONG",
        "confidence": "76%",
        "reasoning": "NLP implies incoming sandstorm in Suez limiting tanker throughput."
    })
    return signals
