import random
from faker import Faker

fake = Faker('es_AR')

TOTAL_REGISTROS = 10000

PORC_NULL = {
    "DOCUMENTO": 0.05,
    "CUIL": 0.1,
    "APELLIDO": 0.02,
    "NOMBRE": 0.02,
    "DOMICILIO": 0.1,
    "INHIBIENTE": 0.15,
    "MONTO": 0.5,
    "CARATULA": 0.1,
    "JUZGADO": 0.4,
    "FECHA": 0.05,
    "ENTRO": 0.6,
    "ALCANCE": 0.7,
    "OBSERVACIONES": 0.8,
    "VIGENCIA": 0.5
}

PORC_SUCIO = {
    "DOCUMENTO": 0.03,
    "CUIL": 0.03,
    "APELLIDO": 0.02,
    "NOMBRE": 0.02,
    "DOMICILIO": 0.05
}

def dato_limpio(col):
    if col == "DOCUMENTO":
        return str(fake.random_int(min=10000000, max=99999999))
    if col == "CUIL":
        return f"{fake.random_int(20, 27)}-{fake.random_int(10000000, 99999999)}-{fake.random_int(0,9)}"
    if col == "APELLIDO":
        return fake.last_name().upper()
    if col == "NOMBRE":
        return fake.first_name().upper()
    if col == "DOMICILIO":
        return fake.street_name().upper() + " " + str(fake.random_int(1, 5000))
    if col == "INHIBIENTE":
        return random.choice(["AFIP", "BANCO NACIÓN", "FISCO DE LA PROVINCIA", "ADMINISTRACIÓN FEDERAL DE INGRESOS PÚBLICOS"])
    if col == "MONTO":
        return str(fake.random_int(1000, 1000000))
    if col == "CARATULA":
        return f"{random.choice(['EJECUCIÓN FISCAL', 'COBRO DE PESOS', 'CONCURSO PREVENTIVO'])} - {fake.last_name().upper()} {fake.first_name().upper()}"
    if col == "JUZGADO":
        return f"JUZGADO N° {fake.random_int(1, 30)}"
    if col == "FECHA":
        return fake.date_between(start_date="-10y", end_date="today")
    if col == "ENTRO":
        return fake.date_this_decade()
    if col == "ALCANCE":
        return random.choice(["TOTAL", "PARCIAL"])
    if col == "OBSERVACIONES":
        return random.choice(["SIN OBSERVACIONES", "EN REVISIÓN", ""])
    if col == "VIGENCIA":
        return random.choice(["ACTIVO", "CADUCADO"])
    return None

def dato_sucio(col):
    return random.choice(["###", "NULL", "   ", "???", "0000", fake.text(max_nb_chars=10)])

# Generar el archivo SQL
with open("insert_inhibiciones.sql", "w", encoding="utf-8") as f:
    for _ in range(TOTAL_REGISTROS):
        fila = {}
        fila["FOLIO_PERSONAL"] = f"{fake.random_int(1000, 99999)}/{fake.random_int(1, 25)}"
        for col in PORC_NULL:
            if random.random() < PORC_NULL[col]:
                fila[col] = None
            elif col in PORC_SUCIO and random.random() < PORC_SUCIO[col]:
                fila[col] = dato_sucio(col)
            else:
                fila[col] = dato_limpio(col)

        # Preparar valores para SQL
        valores = []
        for col in ["FOLIO_PERSONAL", "DOCUMENTO", "CUIL", "APELLIDO", "NOMBRE", "DOMICILIO",
                    "INHIBIENTE", "MONTO", "CARATULA", "JUZGADO", "FECHA", "ENTRO",
                    "ALCANCE", "OBSERVACIONES", "VIGENCIA"]:
            if fila[col] is None:
                valores.append("NULL")
            elif isinstance(fila[col], str):
                valores.append("'" + fila[col].replace("'", "''") + "'")
            else:
                valores.append(f"'{fila[col]}'")

        f.write(f"INSERT INTO inhibiciones VALUES ({', '.join(valores)});\n")

print("✅ Archivo 'insert_inhibiciones.sql' generado con 10,000 registros.")
