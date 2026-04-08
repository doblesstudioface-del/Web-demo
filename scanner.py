import requests
import pandas as pd
import os

API_KEY = "AIzaSyBNwQeltWhe854R6s7I0VNCxyF25yA0cB4"
CX = "643aa78d2bd524499"

def auditar_velocidad(url):
    # Conectamos con Google PageSpeed
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={API_KEY}"
    try:
        res = requests.get(api_url, timeout=15).json()
        # Sacamos el puntaje de 0 a 100
        score = res['lighthouseResult']['categories']['performance']['score'] * 100
        return f"{score}%"
    except:
        return "Error en auditoría"

def iniciar_caceria():
    print("🚀 DOBLE S STUDIO: Buscando arquitectos con web lenta...")
    search_url = f"https://www.googleapis.com/customsearch/v1?q=estudio+arquitectura+guatemala&key={API_KEY}&cx={CX}"
    
    res = requests.get(search_url).json()
    items = res.get('items', [])
    
    lista_final = []
    for i in items:
        nombre = i['title']
        web = i['link']
        print(f"🔎 Analizando: {nombre}")
        velocidad = auditar_velocidad(web)
        
        lista_final.append({
            "Estudio": nombre,
            "Sitio Web": web,
            "Rendimiento": velocidad
        })
    
    # Guardamos los resultados
    df = pd.DataFrame(lista_final)
    df.to_csv("prospectos_doble_s.csv", index=False) # Usamos CSV que es más ligero y no falla
    print("✅ Archivo 'prospectos_doble_s.csv' creado con éxito.")

if __name__ == "__main__":
    iniciar_caceria()
