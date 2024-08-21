import streamlit as st
from datetime import datetime

def validar_si_estudiante_es_mayor_edad(nombre: str, fecha: datetime):
    diferencia_anios = datetime.now().year - fecha.year
    if(diferencia_anios < 18):
        st.error(f"el estudiante {nombre} tiene {diferencia_anios} anios de edad y debe ser mayor de edad")

st.title("Registro estudiante")

name = st.text_input("Ingrese su nombre:")
code = st.text_input("Ingrese su codigo:")
valor_matricula = st.number_input("Ingrese el valor de la matricula:")
genero = st.selectbox("Seleccione su genero:", ("Femenino", "Masculino"))

min_date = datetime(1904, 1, 1)
max_date = datetime.now()
fecha_nacimiento = st.date_input(
    "Fecha de nacimiento:", 
    min_value=min_date, 
    max_value=max_date
)

if st.button("Guardar"):
    if fecha_nacimiento is not None:
        validar_si_estudiante_es_mayor_edad(fecha=fecha_nacimiento, nombre=name)

    st.write("SE va a guardar los datos del estudiante")



