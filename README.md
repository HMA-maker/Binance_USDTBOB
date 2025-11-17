# 💵 Binance P2P Rate Fetcher (USDT/BOB)

Este repositorio contiene scripts para obtener la cotización de referencia del **USDT** (dólar digital) en **Bolivianos (BOB)** directamente desde la API pública de Binance P2P.

La cotización obtenida es la del **primer anuncio de COMPRA** (el precio más bajo ofrecido por los vendedores de USDT).

## 🚀 Archivos del Proyecto

| Archivo | Lenguaje | Descripción |
| :--- | :--- | :--- |
| `binance_p2p_python.py` | Python | Script para ejecución en servidor/local. Ideal para tareas de fondo o automatización. |
| `index.html` | HTML/JS | Demostración de cómo obtener y mostrar el precio en una página web usando JavaScript. |

## 🐍 Uso del Script en Python

### Prerrequisitos
Necesitas tener **Python 3** instalado y la librería `requests`.

```bash
pip install requests
