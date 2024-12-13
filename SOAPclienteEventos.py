from zeep import Client
from zeep.transports import Transport
from requests import Session
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from datetime import datetime

# Deshabilitar advertencias SSL durante las pruebas
warnings.simplefilter('ignore', InsecureRequestWarning)

# Configurar sesión HTTP para ignorar la verificación SSL
session = Session()
session.verify = False
transport = Transport(session=session)

# URL del WSDL del servidor
wsdl_url = "http://localhost:53538/Service1.svc?wsdl"
client = Client(wsdl=wsdl_url, transport=transport)

# Validaciones de entrada

def validate_text_input(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        else:
            print("El campo no puede estar vacío. Intente nuevamente.")

def validate_date_input(prompt):
    while True:
        try:
            date_str = input(prompt).strip()
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            year = date_obj.year
            if year < 2024:
                raise ValueError("La fecha de inicio debe ser desde 2024 en adelante.")
            if year > 2026:
                raise ValueError("La fecha de fin no puede ser posterior a 2026.")
            return date_obj
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intente nuevamente.")

def validate_date_range(start_date, end_date):
    if end_date < start_date:
        raise ValueError("La fecha de inicio no puede ser mayor que la fecha de fin.")

def validate_number_input(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 0:
                raise ValueError("El valor no puede ser negativo.")
            return value
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intente nuevamente.")

# Manejo de errores SOAP
def handle_soap_fault(exception):
    print(f"Error: {exception}")


# Funciones CRUD
def get_all_eventos():
    try:
        eventos = client.service.GetAllEventos()
        if not eventos:
            print("\nNo hay eventos disponibles en la base de datos.")
            return
        print("\nLista de eventos:")
        for evento in eventos:
            fecha_inicio = evento.FechaInicio.strftime("%Y-%m-%d")
            fecha_fin = evento.FechaFin.strftime("%Y-%m-%d") if evento.FechaFin else "N/A"
            print(f"- ID: {evento.EventoID}, Nombre: {evento.Nombre}, Lugar: {evento.Lugar}, Fecha Inicio: {fecha_inicio}, Fecha Fin: {fecha_fin}, Descripción: {evento.Descripcion}")
    except Exception as e:
        handle_soap_fault(e)

def get_evento_by_id():
    try:
        evento_id = validate_number_input("Ingrese el ID del evento: ")
        evento = client.service.GetEventoById(evento_id)
        if evento:
            fecha_inicio = evento.FechaInicio.strftime("%Y-%m-%d")
            fecha_fin = evento.FechaFin.strftime("%Y-%m-%d") if evento.FechaFin else "N/A"
            print(f"Detalles del evento - ID: {evento.EventoID}, Nombre: {evento.Nombre}, Lugar: {evento.Lugar}, Fecha Inicio: {fecha_inicio}, Fecha Fin: {fecha_fin}, Descripción: {evento.Descripcion}")
        else:
            print(f"No se encontró el evento con ID {evento_id}.")
    except Exception as e:
        handle_soap_fault(e)

def create_evento():
    try:
        nombre = validate_text_input("Ingrese el nombre del evento: ")
        lugar = validate_text_input("Ingrese el lugar del evento: ")
        fecha_inicio = validate_date_input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = validate_date_input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        validate_date_range(fecha_inicio, fecha_fin)
        descripcion = validate_text_input("Ingrese la descripción del evento: ")

        nuevo_evento = {
            "Nombre": nombre,
            "Lugar": lugar,
            "FechaInicio": fecha_inicio,
            "FechaFin": fecha_fin,
            "Descripcion": descripcion
        }
        result = client.service.CreateEvento(nuevo_evento)
        if result:
            print("Evento creado exitosamente.")
        else:
            print("No se pudo crear el evento.")
    except Exception as e:
        handle_soap_fault(e)

def update_evento():
    try:
        evento_id = validate_number_input("Ingrese el ID del evento a actualizar: ")
        nombre = validate_text_input("Ingrese el nuevo nombre del evento: ")
        lugar = validate_text_input("Ingrese el nuevo lugar del evento: ")
        fecha_inicio = validate_date_input("Ingrese la nueva fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = validate_date_input("Ingrese la nueva fecha de fin (YYYY-MM-DD): ")
        validate_date_range(fecha_inicio, fecha_fin)
        descripcion = validate_text_input("Ingrese la nueva descripción del evento: ")

        evento = {
            "EventoID": evento_id,
            "Nombre": nombre,
            "Lugar": lugar,
            "FechaInicio": fecha_inicio,
            "FechaFin": fecha_fin,
            "Descripcion": descripcion
        }
        result = client.service.UpdateEvento(evento=evento)
        if result:
            print("Evento actualizado exitosamente.")
        else:
            print("No se pudo actualizar el evento.")
    except Exception as e:
        handle_soap_fault(e)

def delete_evento():
    try:
        eventos = client.service.GetAllEventos()
        if not eventos:
            print("\nNo hay eventos disponibles para eliminar.")
            return

        evento_id = validate_number_input("Ingrese el ID del evento a eliminar: ")
        confirm = input(f"¿Está seguro que desea eliminar el evento con ID {evento_id}? (s/n): ").strip().lower()
        if confirm != 's':
            print("Operación cancelada.")
            return
        result = client.service.DeleteEvento(evento_id)
        if result:
            print("Evento eliminado exitosamente.")
        else:
            print("No se pudo eliminar el evento.")
    except Exception as e:
        handle_soap_fault(e)

def menu():
    while True:
        print("\n===== Menú de Operaciones CRUD =====")
        print("1. Obtener todos los eventos")
        print("2. Obtener un evento por ID")
        print("3. Crear un evento")
        print("4. Actualizar un evento")
        print("5. Eliminar un evento")
        print("6. Salir")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            get_all_eventos()
        elif opcion == "2":
            get_evento_by_id()
        elif opcion == "3":
            create_evento()
        elif opcion == "4":
            update_evento()
        elif opcion == "5":
            delete_evento()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()