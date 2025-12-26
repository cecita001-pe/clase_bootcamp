import streamlit as st
import requests
import json

# URL de tu webhook de Make
MAKE_WEBHOOK_URL = "https://hook.us2.make.com/8ct8g0uhrjvuilct3f1re6sefrjuaqp6"  # <-- pon tu URL

st.title("Chat con Make + OpenAI")

st.write("Escribe una pregunta y Make la procesará con su escenario que usa OpenAI.")

user_input = st.text_input("Tu pregunta:")

if st.button("Enviar"):
    if not user_input:
        st.warning("Escribe algo antes de enviar.")
    else:
        with st.spinner("Consultando a Make..."):
            try:
                # Enviar mensaje al webhook de Make
                payload = {"pregunta": user_input}

                response = requests.post(MAKE_WEBHOOK_URL, json=payload, timeout=60)

                if response.status_code == 200:
                    data = json.loads(response.text, strict=False)

                    # Se espera que Make devuelva {"respuesta": "..."}
                    respuesta = data.get("respuesta", "Make no envió 'respuesta' en el JSON.")
                    st.success("Respuesta de Make / OpenAI:")
                    st.write(respuesta)
                else:
                    st.error(f"Error: Make devolvió {response.status_code}")
                    st.write(response.text)

            except Exception as e:
                st.error(f"Hubo un error al conectar con Make: {e}")
