# binance_p2p_python.py

import requests
import json
from datetime import datetime

# ==============================================================================
# CONFIGURACIÓN DE LA API DE BINANCE P2P
# ==============================================================================

# URL del endpoint para buscar anuncios P2P
API_URL = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"

# Headers sugeridos, el User-Agent ayuda a identificar la petición
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) DolarBlueBot/1.0"
}

# Payload (Cuerpo de la Petición POST)
# Buscar los 5 primeros anuncios de COMPRA de USDT usando BOB.
PAYLOAD = {
    "asset": "USDT",      # Criptomoneda
    "fiat": "BOB",        # Moneda local (Bolivianos)
    "tradeType": "BUY",   # Tipo de operación: BUY (compra USDT con BOB)
    "page": 1,
    "rows": 5,            # Menos filas para una referencia rápida
    "payTypes": [],       # No filtrar por tipo de pago
    "publisherType": None # No filtrar por tipo de publicador
}

# ==============================================================================
# FUNCIÓN PRINCIPAL
# ==============================================================================

def obtener_precio_referencia():
    """
    Realiza una petición a la API de Binance P2P y extrae el precio del 
    primer anuncio de compra (el precio más bajo ofrecido por vendedores).
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Conectando a Binance P2P...")
    
    try:
        # Realizar petición POST
        response = requests.post(API_URL, headers=HEADERS, json=PAYLOAD)
        response.raise_for_status() # Lanza un error para códigos de estado HTTP 4xx/5xx

        data = response.json()
        
        if not data.get("data"):
            print("Error: No se encontraron anuncios disponibles.")
            return None

        # El precio de referencia es el precio del primer anuncio de la lista
        precio_str = data["data"][0]["adv"]["price"]
        precio_referencia = float(precio_str)
        
        print("-" * 40)
        print(f"✅ Precio USDT/BOB (P2P Compra Ref.): {precio_referencia:.2f} Bs")
        print("-" * 40)
        
        return precio_referencia
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de red o HTTP: {e}")
    except KeyError:
        print("❌ Error de estructura de datos: La respuesta de la API no tiene el formato esperado.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        
    return None

if __name__ == "__main__":
    obtener_precio_referencia()
