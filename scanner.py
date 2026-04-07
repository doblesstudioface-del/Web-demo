import requests
import csv
import os

def analizar_y_guardar(url):
    url_limpia = url.replace("https://", "").replace("http://", "").split('/')[0]
    final_url = f"https://{url_limpia}"
    
    print(f"--- DOBLE S STUDIO: Auditando {final_url} ---")
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={final_url}&strategy=mobile"
    
    try:
        res = requests.get(api_url).json()
        if 'lighthouseResult' in res:
            score = int(res['lighthouseResult']['categories']['performance']['score'] * 100)
            
            # Guardar en Excel (CSV)
            archivo_existe = os.path.isfile('reporte_ventas.csv')
            with open('reporte_ventas.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                if not archivo_existe:
                    writer.writerow(['Web', 'Puntaje', 'Estado'])
                
                estado = "CRÍTICO (Vender)" if score < 50 else "Aceptable"
                writer.writerow([final_url, score, estado])
                
            print(f"PUNTUACIÓN: {score}/100 - Guardado en reporte_ventas.csv")
        else:
            print("Error: Cuota de Google agotada. Espera un poco.")
    except Exception as e:
        print(f"Error: {e}")

# Aquí puedes poner la lista de webs que quieras
analizar_y_guardar("https://precisioninmobiliaria.com")
