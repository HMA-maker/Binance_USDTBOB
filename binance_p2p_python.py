import requests
import json
from datetime import datetime

# ==============================================================================
# CONFIGURACIÓN
# ==============================================================================
API_URL = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; GitHubAction/1.0)"
}
PAYLOAD = {
    "asset": "USDT",
    "fiat": "BOB",
    "tradeType": "BUY",
    "page": 1,
    "rows": 5,
    "payTypes": [],
    "publisherType": None
}
OUTPUT_FILE = "rate.json"

# ==============================================================================
# FUNCIÓN PRINCIPAL
# ==============================================================================

def obtener_y_guardar_precio():
    """Obtiene el precio de Binance P2P y lo guarda en un archivo JSON."""
    
    try:
        response = requests.post(API_URL, headers=HEADERS, json=PAYLOAD)
        response.raise_for_status() 

        data = response.json()
        
        if not data.get("data"):
            raise ValueError("No se encontraron anuncios P2P.")

        # Extraer el precio y la hora
        precio_str = data["data"][0]["adv"]["price"]
        precio_referencia = float(precio_str)
        hora_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Preparar el JSON de salida
        output_data = {
            "rate_bob_usdt": precio_referencia,
            "updated_at": hora_actualizacion,
            "source": "Binance P2P (BUY)"
        }
        
        # Guardar en el archivo
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(output_data, f, indent=4)
            
        print(f"Precio actualizado: {precio_referencia:.2f} Bs, guardado en {OUTPUT_FILE}")
        return precio_referencia
        
    except requests.exceptions.RequestException as e:
        print(f"Error de red o HTTP: {e}")
    except (KeyError, ValueError) as e:
        print(f"Error al procesar datos: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    return None

if __name__ == "__main__":
    obtener_y_guardar_precio()
