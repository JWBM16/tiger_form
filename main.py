import sqlitecloud
import hashlib
import time
from fasthtml.common import *
from contextlib import contextmanager
from datetime import datetime

custom_styles = Style("""
.mw-960 { max-width: 960px; }
.mw-480 { max-width: 480px; }
.mx-auto { margin-left: auto; margin-right: auto; }

""")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@contextmanager
def open_db_connection_diez(db_name):
    conn = sqlitecloud.connect("sqlitecloud://cz7ig9e6sk.sqlite.cloud:8860?apikey=yvHUJJbgxNRa3bFERweuVHFvTOnhO67LgwabT0NW4TY")
    try:
        yield conn
    finally:
        conn.close()
        
db_name = 'jhotem.db'       
# Using the context manager to manage a database connection
with open_db_connection_diez('jhotem.db') as conn:
    conn.execute(f"USE DATABASE {db_name}")
    cursor = conn.execute("SELECT usuario, clave FROM usuarios WHERE estatus = 'activo'")
    usuarios_activos = cursor.fetchall()
    print("FUNCIONO conexion diez")

users_db = {}
for usuario, clave in usuarios_activos:
    users_db[usuario] =hash_password(clave) 

# print(users_db)



def add_message_login(username, password):
    if username in users_db and users_db[username] == hash_password(password):
        return True
    return False
    

def add_message(name, lastname, identification,phone_number, address, email,comments, date):
    nombre = name
    apellido = lastname
    cedula = identification
    telefono =phone_number
    direccion = address
    correo_electronico = email
    nota = comments
    fecha_variable =date
    
    @contextmanager
    def open_db_connection_dieciocho(db_name):
        conn = sqlitecloud.connect("sqlitecloud://cz7ig9e6sk.sqlite.cloud:8860?apikey=yvHUJJbgxNRa3bFERweuVHFvTOnhO67LgwabT0NW4TY")
        try:
            yield conn
        finally:
            conn.close()
            
    db_name = 'jhotem.db' 
    
        
    # Using the context manager to manage a database connection
    with open_db_connection_dieciocho('jhotem.db') as conn:
        conn.execute(f"USE DATABASE {db_name}")
        cursor = conn.execute(
        "INSERT INTO clientes (nombre, apellido, cedula, telefono, direccion, correo_electronico, nota, fecha) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            nombre,
            apellido,
            cedula,
            telefono,
            direccion,
            correo_electronico,
            nota,
            fecha_variable,
        ),
    )
    nombre_completo = f"{nombre}, {apellido}"
    return nombre_completo

def add_message_cars(selectbox,brand,model,year,plate,comments):
    seleccion = selectbox
    marca = brand
    modelo = model
    anual =year
    placa = plate
    comentarios = comments
    
    
    @contextmanager
    def open_db_connection_veintitres(db_name):
        conn = sqlitecloud.connect("sqlitecloud://cz7ig9e6sk.sqlite.cloud:8860?apikey=yvHUJJbgxNRa3bFERweuVHFvTOnhO67LgwabT0NW4TY")
        try:
            yield conn
        finally:
            conn.close()
            
    db_name = 'jhotem.db'       
    # Using the context manager to manage a database connection
    with open_db_connection_veintitres('jhotem.db') as conn:
        conn.execute(f"USE DATABASE {db_name}")
        cursor = conn.execute(
        """
    SELECT nombre, apellido FROM clientes
    """
    )
        clientes_veh = cursor.fetchall()
        print("FUNCIONO connection_veintitres")
    
    # Unificación de nombre y apellido del cliente
    temporal_veh = []
    for cliente in clientes_veh:
        nombre, apellido = cliente
        nombre_completo = f"{nombre} {apellido}"
        temporal_veh.append(nombre_completo)

    # print(temporal_veh)

    # Consulta para obtener los valores de los campos 'nombre' y 'apellido' junto con 'id' de la tabla 'clientes'
    @contextmanager
    def open_db_connection_veinticuatro(db_name):
        conn = sqlitecloud.connect("sqlitecloud://cz7ig9e6sk.sqlite.cloud:8860?apikey=yvHUJJbgxNRa3bFERweuVHFvTOnhO67LgwabT0NW4TY")
        try:
            yield conn
        finally:
            conn.close()
            
    db_name = 'jhotem.db'       
    # Using the context manager to manage a database connection
    with open_db_connection_veinticuatro('jhotem.db') as conn:
        conn.execute(f"USE DATABASE {db_name}")
        cursor = conn.execute(
        """
    SELECT id FROM clientes
    """
    )
        clientes_id_capture = cursor.fetchall()
        print("FUNCIONO connection_veinticuatro")
    
    # Convertir las tuplas en clientes_id_capture a enteros
    clientes_id_capture_cleaned = [int(str(item)[1:-2]) for item in clientes_id_capture]

    # Crear el diccionario
    result_dict = {
        key: value for key, value in zip(clientes_id_capture_cleaned, temporal_veh)
    }

    dict_inverse = {
        key: value for key, value in zip(temporal_veh, clientes_id_capture_cleaned)
    }
    
    @contextmanager
    def open_db_connection_dieciocho(db_name):
        conn = sqlitecloud.connect("sqlitecloud://cz7ig9e6sk.sqlite.cloud:8860?apikey=yvHUJJbgxNRa3bFERweuVHFvTOnhO67LgwabT0NW4TY")
        try:
            yield conn
        finally:
            conn.close()
            
    db_name = 'jhotem.db' 
    
    # Busqueda del propietario (si este fue modificado)
    nombre_buscado = seleccion
    
    # print(f"Nombre_buscado {nombre_buscado}")
    
    clave = dict_inverse.get(nombre_buscado)
    # print(clave)
    
    cliente_id = clave
    
    fecha_actual = datetime.now()

    # Formatear la fecha en el formato YYYY-MM-DD
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

    # Guardar la fecha formateada en una variable
    fecha_variable = str(fecha_formateada)

    # print (f"Este es el valor del cliente_id {cliente_id}")
    
    @contextmanager
    def open_db_connection_veintisiete(db_name):
        conn = sqlitecloud.connect("sqlitecloud://cz7ig9e6sk.sqlite.cloud:8860?apikey=yvHUJJbgxNRa3bFERweuVHFvTOnhO67LgwabT0NW4TY")
        try:
            yield conn
        finally:
            conn.close()
            
    db_name = 'jhotem.db'       
    # Using the context manager to manage a database connection
    with open_db_connection_veintisiete('jhotem.db') as conn:
        conn.execute(f"USE DATABASE {db_name}")
        cursor = conn.execute(
        "INSERT INTO vehiculos (cliente_id, marca, modelo, year, placa, fecha_entrada, observaciones) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            cliente_id,
            marca,
            modelo,
            anual,
            placa,
            fecha_variable,
            comentarios,
        ),
    )   
        conn.commit()
    print("FUNCIONO connection_veintisiete")    
    
    return nombre_completo

def get_messages():
    # Conectar a la base de datos SQLite (o crearla si no existe)
    @contextmanager
    def open_db_connection_veinte(db_name):
        conn = sqlitecloud.connect("sqlitecloud://cz7ig9e6sk.sqlite.cloud:8860?apikey=yvHUJJbgxNRa3bFERweuVHFvTOnhO67LgwabT0NW4TY")
        try:
            yield conn
        finally:
            conn.close()
            
    db_name = 'jhotem.db'       
    # Using the context manager to manage a database connection
    with open_db_connection_veinte('jhotem.db') as conn:
        conn.execute(f"USE DATABASE {db_name}")
        cursor = conn.execute("SELECT MAX(id) FROM clientes")
        max_id = cursor.fetchone()[0]
        print("FUNCIONO connection_veinte")
        
    new_register = int(max_id) + 1
    return new_register

def get_messages_login():
    # Conectar a la base de datos SQLite (o crearla si no existe)
    @contextmanager
    def open_db_connection_veinte(db_name):
        conn = sqlitecloud.connect("sqlitecloud://cz7ig9e6sk.sqlite.cloud:8860?apikey=yvHUJJbgxNRa3bFERweuVHFvTOnhO67LgwabT0NW4TY")
        try:
            yield conn
        finally:
            conn.close()
            
    db_name = 'jhotem.db'       
    # Using the context manager to manage a database connection
    with open_db_connection_veinte('jhotem.db') as conn:
        conn.execute(f"USE DATABASE {db_name}")
        cursor = conn.execute("SELECT MAX(vehiculos_id) FROM vehiculos")
        max_id = cursor.fetchone()[0]
        print("FUNCIONO connection_veinte")
        
    new_register = int(max_id) + 1
    return new_register

def get_messages_cars():
    # Conectar a la base de datos SQLite (o crearla si no existe)
    @contextmanager
    def open_db_connection_veinte(db_name):
        conn = sqlitecloud.connect("sqlitecloud://cz7ig9e6sk.sqlite.cloud:8860?apikey=yvHUJJbgxNRa3bFERweuVHFvTOnhO67LgwabT0NW4TY")
        try:
            yield conn
        finally:
            conn.close()
            
    db_name = 'jhotem.db'       
    # Using the context manager to manage a database connection
    with open_db_connection_veinte('jhotem.db') as conn:
        conn.execute(f"USE DATABASE {db_name}")
        cursor = conn.execute("SELECT MAX(vehiculos_id) FROM vehiculos")
        max_id = cursor.fetchone()[0]
        print("FUNCIONO connection_veinte")
        
    new_register = max_id + 1
    return new_register


def render_message(entry):
    
    return (
        Article(
            Header("Registro debidamente cargado"),
            P(f"Nuevo registro: {entry}"),
        ),
    )

def render_message_cars(entry):
    
    return (
        Article(
            Header("Registro debidamente cargado"),
            P(f"Nuevo registro: {entry}"),
        ),
    )


app,rt = fast_app(hdrs=(custom_styles,))

def render_message_list():
    clientes = get_messages()
    nuevo_id = clientes
    
    return Div(
        render_message(nuevo_id),
        id="message-list",
    )
    
def render_message_list_cars():
    clientes = get_messages_cars()
    nuevo_id = clientes
    
    return Div(
        render_message_cars(nuevo_id),
        id="message-list-cars",
    ) 

def render_message_login():
    menu = Div(
        Button("Entrar", type="button", onclick="location.href='/clientes'"),
        cls="menu"  # Clase CSS opcional para estilos
    )
    
    
    return Div(
        P("Bienvenido"),
        menu,
        id="message-list-login",
    ) 


def render_content():
    form = Form(
        Fieldset(
            Div(
                Input(
                    type='text',
                    name='name',
                    placeholder='Nombre',
                    required='True',
                    maxlength=15,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='lastname',
                    placeholder='Apellido',
                    required='True',
                    maxlength=50,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='identification',
                    placeholder='C.I./RIF',
                    required='True',
                    maxlength=50,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='phone_number',
                    placeholder='Telefonos',
                    required='True',
                    maxlength=50,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='address',
                    placeholder='Direccion',
                    required='True',
                    maxlength=50,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='email',
                    placeholder='Correo Electronico',
                    required='True',
                    maxlength=50,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='comments',
                    placeholder='Observaciones',
                    required='True',
                    maxlength=50,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Button("Submit", type="submit"),
                style="margin-bottom: 10px;",
            ),
            role="group",
            style="display: flex; flex-direction: column; gap: 10px;"
        ),
        method="post",
        hx_post="/submit-message",
        hx_target="#message-list",
        hx_swap="outerHTML",
        hx_on__after_request="this.reset()",
    )
    
    return Div(
        P(Em("A continuacion ingrese los datos del cliente")),
        form,
        Div(
            "Powered by Whitelabs Technologies"
        ),
        Hr(),
        render_message_list(),
    )


# Form de la pagina vehiculos
def render_content_vehiculos():
    
    @contextmanager
    def open_db_connection_veintitres(db_name):
        conn = sqlitecloud.connect("sqlitecloud://cz7ig9e6sk.sqlite.cloud:8860?apikey=yvHUJJbgxNRa3bFERweuVHFvTOnhO67LgwabT0NW4TY")
        try:
            yield conn
        finally:
            conn.close()
            
    db_name = 'jhotem.db'       
    # Using the context manager to manage a database connection
    with open_db_connection_veintitres('jhotem.db') as conn:
        conn.execute(f"USE DATABASE {db_name}")
        cursor = conn.execute(
        """
    SELECT nombre, apellido FROM clientes
    """
    )
        clientes_veh = cursor.fetchall()
        print("FUNCIONO connection_veintitres")
    
    # Unificación de nombre y apellido del cliente
    temporal_veh = []
    for cliente in clientes_veh:
        nombre, apellido = cliente
        nombre_completo = f"{nombre} {apellido}"
        temporal_veh.append(nombre_completo)

    # print(temporal_veh)

    
    selectbox = Select(name="selectbox")(
        *[Option(option, value=option) for option in temporal_veh]
    )
    
    form = Form(
                selectbox,
        Fieldset(
            Div(
                Input(
                    type='text',
                    name='brand',
                    placeholder='Marca',
                    required='True',
                    maxlength=250,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='model',
                    placeholder='Model',
                    required='True',
                    maxlength=250,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='year',
                    placeholder='Año',
                    required='True',
                    maxlength=250,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='plate',
                    placeholder='Placa',
                    required='True',
                    maxlength=250,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='comments',
                    placeholder='Comments',
                    required='True',
                    maxlength=250,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Button("Submit", type="submit"),
                style="margin-bottom: 10px;",
            ),
            role="group",
            style="display: flex; flex-direction: column; gap: 10px;"
        ),
        method="post",
        hx_post="/submit-message-cars",
        hx_target="#message-list-cars",
        hx_swap="outerHTML",
        hx_on__after_request="this.reset()",
    )
    
    return Div(
        form,
        Div(
            "Powered by Whitelabs Technologies"
        ),
        Hr(),
        render_message_list_cars(),
    )


def render_content_login():
    form = Form(
        Fieldset(
            Div(
                Input(
                    type='text',
                    name='user',
                    placeholder='Introduzca su usuario',
                    required='True',
                    maxlength=50,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Input(
                    type='text',
                    name='key_user',
                    placeholder='Introduzca su clave',
                    required='True',
                    maxlength=50,
                ),
                style="margin-bottom: 10px;",
            ),
            Div(
                Button("Submit", type="submit"),
                style="margin-bottom: 10px;text-align: center;",
            ),
            role="group",
            style="display: flex; flex-direction: column; gap: 10px;"
        ),
        method="post",
        hx_post="/submit-message-login",
        # hx_target="#error",
        hx_swap="outerHTML",
        hx_on__after_request="this.reset()",
    )
    return Div(
        form,
        Div(
            "Powered by Whitelabs Technologies",style="text-align: center;"
        ),
        Hr(),
    )
    

@rt('/')
def get():
    logo = Img(src="tigerlogo.png", alt="Logo", style="width: 243px; height: 59px; display: block; margin: 0 auto;") 
    return Container(
        Article(
            H1("Login", style="text-align: center;"),
            Div(logo,
            Br(),
            P(("Ingreso en la App",), style="text-align: center;"),
            render_content_login()),
            cls="mw-480 mx-auto"
        )
        )

@rt('/clientes')
def get(): 
    logo = Img(src="tigerlogo.png", alt="Logo", style="width: 187px; height: 45px;") 
    return Titled(
        Div(logo, " Formato de Ingreso Clientes"), 
        P(A("Cargar Vehículo", href="/change")),
        render_content())

@rt("/submit-message", methods=["POST"])
def post(name: str, lastname: str, identification:str,phone_number: str, address:str, email:str,comments:str ):
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    # Formatear la fecha en el formato YYYY-MM-DD
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

    # Guardar la fecha formateada en una variable
    fecha_variable = str(fecha_formateada)

    add_message(name, lastname, identification,phone_number, address, email, comments, fecha_variable)
    return render_message_list()


@rt("/submit-message-cars", methods=["POST"])
def post(selectbox:str,brand:str,model:str,year:str,plate:str,comments:str):

    add_message_cars(selectbox,brand,model,year,plate,comments)
    return render_message_list_cars()



@rt("/submit-message-login", methods=["POST"])
def post(user:str,key_user:str):

    if add_message_login(user, key_user) is True:
        return Div(
        render_message_login(),
    )
        
    return Div(
        P("Por favor introduzca valores de correctos para entrar"),
    ) 
    

@rt('/change')
def get():
    logo = Img(src="tigerlogo.png", alt="Logo", style="width: 187px; height: 45px;") 
    return Titled(
        Div(logo, " Formato de Ingreso Vehiculos"),
        P(A("Regresar a formulario clientes", href="/")),
        P(Em("A continuacion ingrese los datos del vehiculo")),
        P("Seleccione un Propietario"),
        render_content_vehiculos()
    )

serve()