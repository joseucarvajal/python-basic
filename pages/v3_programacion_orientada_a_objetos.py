import streamlit as st
from datetime import datetime

from v3_objetos.pasajero import Pasajero

st.title("Registrar pasajero")

nombre = st.text_input("Ingrese el nombre:")
documento = st.text_input("Ingrese el documento:")
min_date = datetime(1904, 1, 1)
max_date = datetime.now()
fecha_nacimiento = st.date_input(
    "Fecha de nacimiento:", 
    min_value=min_date, 
    max_value=max_date
)
estrato = st.number_input("Ingrese el estrato:")

if st.button("Guardar"):
    obj_pasajero = Pasajero()
    obj_pasajero.nombre = nombre
    obj_pasajero.documento = documento
    obj_pasajero.fecha_nacimiento = fecha_nacimiento
    obj_pasajero.estrato = estrato

    obj_pasajero.es_mayor_de_edad(st=st)

    st.write(obj_pasajero)



