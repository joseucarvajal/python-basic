from datetime import datetime

class Pasajero:
    nombre:str
    documento:str
    fecha_nacimiento:datetime
    estrato:int

    def es_mayor_de_edad(self, st):
        """Indica si un pasajero es mayor de edad o no"""
        diferencia_anios = datetime.now().year - self.fecha_nacimiento.year
        if(diferencia_anios < 18):
            st.error(f"el pasajero {self.nombre} tiene {diferencia_anios} anios de edad y debe ser mayor de edad")
