import requests

TOKEN = "8680535057:AAH8NCi8va9vdNaNXQc2UljF649dTOhHzoI"
CHAT_ID = "8684365994"

def buscar_y_enviar():
    # Filtros basados en tu perfil: Jefatura/Gerencia Finanzas
    query = "site:bumeran.com.ar OR site:linkedin.com/jobs intitle:('Gerente' OR 'Jefe') 'Administracion y Finanzas' CABA"
    url_google = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    mensaje = (
        "🚀 *¡Hola Romina! Aquí tienes tu reporte diario de vacantes:*\n\n"
        "📌 *Perfil:* Gerencia / Jefatura de Administración y Finanzas\n"
        "📍 *Zona:* CABA / Zona Norte\n"
        "💰 *Filtro sugerido:* > $4.000.000 brutos\n\n"
        f"🔗 [VER VACANTES DE HOY]({url_google})\n\n"
        "⚠️ _Recuerda postularte solo a las que cumplan con tu pretensión salarial._"
    )
    
    url_tg = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown", "disable_web_page_preview": False}
    
    response = requests.post(url_tg, json=payload)
    if response.status_code == 200:
        print("Mensaje enviado con éxito")
    else:
        print(f"Error: {response.text}")

if __name__ == "__main__":
    buscar_y_enviar()
