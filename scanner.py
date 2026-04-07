import requests

def analizar_estudio(url):
    print(f"--- DOBLE S STUDIO: Auditando {url} ---")
    # API con formato seguro
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if 'lighthouseResult' in data:
            score = data['lighthouseResult']['categories']['performance']['score'] * 100
            print(f"PUNTUACIÓN DE VELOCIDAD: {score}/100")
        else:
            print("Error: Google no pudo analizar esta URL. Prueba con otra de un arquitecto.")
            
    except Exception as e:
        print(f"Error: {e}")

# CAMBIA ESTA URL por la de un estudio de arquitectura real
analizar_estudio("https://www.studioseis.com.gt")


