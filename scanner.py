import requests

def analizar_estudio(url):
    # Limpiamos la URL para que Google no se confunda
    url_limpia = url.replace("https://", "").replace("http://", "").split('/')[0]
    final_url = f"https://{url_limpia}"
    
    print(f"--- DOBLE S STUDIO: Auditando {final_url} ---")
    
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={final_url}&strategy=mobile"
    
    try:
        res = requests.get(api_url).json()
        
        if 'lighthouseResult' in res:
            score = res['lighthouseResult']['categories']['performance']['score'] * 100
            print(f"PUNTUACIÓN: {int(score)}/100")
            if score < 50:
                print("OPORTUNIDAD: La web es demasiado lenta.")
        else:
            # Esto nos dirá qué está fallando realmente
            print(f"Google dice: {res.get('error', {}).get('message', 'Error de formato en URL')}")

    except Exception as e:
        print(f"Error técnico: {e}")

# Probando con la inmobiliaria
analizar_estudio("https://precisioninmobiliaria.com")
