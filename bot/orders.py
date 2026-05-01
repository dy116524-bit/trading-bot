def create_order_payload(symbol, side, order_type, quantity, price=None):
    payload = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
    }
    
    if order_type.upper() == "LIMIT":
        if not price:
            raise ValueError("Price is required for LIMIT orders.")
        payload["price"] = str(price)
        payload["timeInForce"] = "GTC"  # Good 'Til Cancelled
        
    return payload
