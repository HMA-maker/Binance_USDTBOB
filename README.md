# 💵 Cotización de Referencia USDT/BOB (Binance P2P)

Este repositorio aloja un proyecto automatizado diseñado para obtener la **tasa de cambio de referencia del USDT (Dólar Digital) a Bolivianos (BOB)** directamente desde la API pública de Binance P2P.

La tasa obtenida se considera una referencia del **precio paralelo o "blue"** del mercado, ya que se basa en la cotización más competitiva de los anuncios de **COMPRA** de USDT.

---

## 🚀 Funcionamiento del Sistema

El proyecto opera en dos fases interconectadas para superar las restricciones de CORS y ofrecer datos actualizados en la web:

1.  **Automatización (GitHub Actions):** El script de **Python** se ejecuta automáticamente cada **4 horas** en los servidores de GitHub.
2.  **Generación de Datos:** El script se conecta a la API de Binance P2P, extrae la tasa y **sobrescribe** el archivo `rate.json` con el último precio y la hora de actualización.
3.  **Presentación Web (GitHub Pages):** La página `index.html` (alojada en GitHub Pages) lee el archivo `rate.json` y muestra el precio en tiempo real, sin necesidad de conectarse directamente a la API de Binance (evitando errores de CORS).

---

## 🛠️ Estructura de Archivos

| Archivo / Carpeta | Propósito |
| :--- | :--- |
| `binance_p2p_python.py` | **Script principal.** Se conecta a Binance, extrae la tasa y serializa el resultado en `rate.json`. Ejecutado por GitHub Actions. |
| `rate.json` | **Archivo de salida.** Contiene la cotización y la marca de tiempo más recientes. Este archivo se actualiza automáticamente en cada ejecución. |
| `index.html` | **Página Web.** Interfaz que el usuario ve. Utiliza JavaScript para leer `rate.json` y mostrar el precio. |
| `.github/workflows/` | Contiene el archivo `update_rate.yml` para la configuración de la automatización. |

---

## ⚙️ Configuración y Despliegue

### 1. GitHub Actions (Automatización)

El archivo `.github/workflows/update_rate.yml` gestiona el flujo de trabajo:

* **Horario:** Se ejecuta automáticamente cada 4 horas (`cron: '0 */4 * * *'`).
* **Proceso:** Instala `requests`, ejecuta `binance_p2p_python.py`, y utiliza `git-auto-commit-action` para subir los cambios en `rate.json`.

### 2. Presentación Web (GitHub Pages)

Para visualizar la tasa en línea:

1.  Ve a **Settings** (Configuración) de tu repositorio.
2.  Haz clic en **Pages** (Páginas).
3.  Selecciona la rama **`main`** como fuente y guarda.
4.  Tu página web estará disponible en la URL proporcionada por GitHub Pages (ej: `https://[usuario].github.io/[repositorio]/`).

---

## 📝 Referencias Técnicas

| Dato | Valor |
| :--- | :--- |
| **API Endpoint** | `https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search` |
| **Moneda Fiat** | BOB (Bolivianos) |
| **Cripto Activo** | USDT (Tether) |
| **Tipo de Trade** | BUY (Compra de USDT) |
