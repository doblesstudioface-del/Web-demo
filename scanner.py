import requests
import pandas as pd

# CONFIGURACIÓN DE DOBLE S STUDIO
API_KEY = "AIzaSyBNwQeltWhe854R6s7I0VNCxyF25yA0cB4"
SEARCH_ENGINE_ID = "643aa78d2bd524499"
QUERY = "estudio de arquitectura Guatemala" # Puedes cambiar esto por cualquier negocio

def buscar_prospectos():
    print(f"🚀 DOBLE S STUDIO: Iniciando búsqueda de '{QUERY}'...")
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={QUERY}"
    
    response = requests.get(url)
    if response.status_code == 200:
        resultados = response.json().get('items', [])
        prospectos = []
        
        for item in resultados:
            nombre = item.get('title')
            link = item.get('link')
            
            # Simulación de auditoría de velocidad (esto lo conectaremos a PageSpeed después)
            # Por ahora, nos trae la lista base
            prospectos.append({
                "Nombre": nombre,
                "Sitio Web": link,
                "Estado": "Pendiente de Auditoría"
            })
        
        # Guardar en Excel
        df = pd.DataFrame(prospectos)
        df.to_excel("prospectos_doble_s.xlsx", index=False)
        print("✅ ¡Éxito! Lista guardada en 'prospectos_doble_s.xlsx'")
    else:
        print(f"❌ Error: {response.status_code}")

if __name__ == "__main__":
    buscar_prospectos()

