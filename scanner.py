import requests

def analizar_estudio(url):
    print(f"--- DOBLE S STUDIO: Auditando {url} ---")
    
    # Esta es la URL de la API simplificada
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile"
    
    # Le decimos a Google que somos un navegador real
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()

        # Si Google nos da el puntaje, lo mostramos
        if 'lighthouseResult' in data:
            score = data['lighthouseResult']['categories']['performance']['score'] * 100
            print(f"PUNTUACIÓN DE VELOCIDAD: {int(score)}/100")
            
            if score < 50:
                print("ESTADO: CRÍTICO. ¡Excelente oportunidad de venta!")
            else:
                print("ESTADO: Web optimizada.")
        else:
            # Si Google responde pero sin datos, nos dirá por qué
            error_msg = data.get('error', {}).get('message', 'Error desconocido')
            print(f"Google no pudo analizar esta web: {error_msg}")
            print("Sugerencia: Prueba con una URL que empiece con https://")

    except Exception as e:
        print(f"Error técnico: {e}")

# PRUEBA REAL: Usa una web de un arquitecto de Guatemala
# Ejemplo: "https://www.studioseis.com.gt"
analizar_estudio("https://precisioninmobiliaria.com/")
