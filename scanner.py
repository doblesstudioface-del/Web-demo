import os
import requests

def analizar_estudio(url):
    # 1. Consultar PageSpeed (Uso gratuito)
    print(f"Analizando la web de: {url}...")
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile"
    
    try:
        res = requests.get(api_url).json()
        # Multiplicamos por 100 para tener el puntaje real
        score = res['lighthouseResult']['categories']['performance']['score'] * 100
        
        print(f"RESULTADO: {score}/100 puntos de velocidad.")
        
        if score < 50:
            print("--- OPORTUNIDAD DE VENTA DETECTADA ---")
            print("La web es lenta. El arquitecto está perdiendo clientes.")
        else:
            print("La web está sana para móviles.")
            
    except Exception as e:
        print(f"Error al analizar: {e}")

# Prueba con una URL real (puedes cambiar esta por la de un cliente)
analizar_estudio("https://www.google.com")

