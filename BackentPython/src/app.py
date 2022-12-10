from flask import Flask, jsonify, request,url_for, redirect,session
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from VALIDACIONES.validaciones import *
from CREATE.Regitros import *
from DELETE.Eliminacion import *
app = Flask(__name__)

def nombre():
    return app

# CORS(app)
CORS(app, resources={r"/registrousuario/*": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/registroproducto/*": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/login/*": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/actualizarproductos/<id_Producto>/*": {"origins": "http://localhost:4200"}})
conexion = MySQL(app)



#Metodos discoteca
@app.route('/login', methods=['POST'])
def iniciar_sesion():
    # Tomo los datos que provienen del JSON
    # request.json
    # Obtengo el correo y la contrasena de la base de datos usando el correo que me entregan por el JSON
    correo = request.json['correo']
    clave = request.json['clave']
    cursor = conexion.connection.cursor()
    sql = "SELECT correo, clave FROM usuario WHERE correo='%s'" %correo
    cursor.execute(sql)
    resultado = cursor.fetchone()
    if resultado is not None:
        if (clave == resultado[1]):
            session["usuaurio"] = correo
            return jsonify({'usuario':"usuario", 'exito': True,'nombre_usuario':resultado[0],'correo':correo}),200
        else:
            return " Contraseña Incorrecta" 
    else:
        """ cursor = conexion.connection.cursor()
        sql = "SELECT correo, clave FROM  acudiente WHERE  usuario='%s'" %correo
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if resultado is not None:
            if (clave == resultado[0]):
                return jsonify({'usuario':"usuario", 'exito': True,'nombre_usuario':resultado[1],'correo':correo}),400
            else:
                return " Contraseña Incorrecta"  """
        return "Usuario no registrado"

# CERRAR SESIÓN
@app.route('/cerrarsesion',  methods=['GET'])
def cerrar_sesion():
    if "usuario" in session:
        session.pop("usuario")
        return jsonify({'mensaje':"Sesión Cerrada", 'exito':True}), 200
    return jsonify({'mensaje':"No se pudo cerrar sesión", 'exito':False}), 400


#Registros


#CRUD categoria
@app.route('/registrocategoria', methods=['POST'])
def registrar_categoria():
        try:
            if registro_categoria(request):
                return jsonify({'mensaje': "Categoria registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400
       

#CRUD Producto
@app.route('/registroproducto', methods=['POST'])
def registrar_producto():
        try:
            if registro_producto(request):
                return jsonify({'mensaje': "Producto registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

#CRUD Usuario
@app.route('/registrousuario', methods=['POST'])
def registrar_usuario():

        try:
            if registro_usuario(request):
                return jsonify({'mensaje': "Usuario registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

#CRUD Ingreso
@app.route('/registroingreso', methods=['POST'])
def registrar_Ingreso():
        try:
            if registro_ingreso(request):
                return jsonify({'mensaje': "Ingreso registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

#CRUD Factura
@app.route('/registrofactura', methods=['POST'])
def registrar_Factura():
        try:
            if registro_factura(request):
                return jsonify({'mensaje': "Factura registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

#Eliminar 

#Eliminar Categoria
@app.route('/eliminarcategoria/<Id>', methods=['DELETE'])
def Eliminar_categoria(Id):
        try:
            if Eliminar_Categoria(Id):
                return jsonify({'mensaje': "Categoria eliminar.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar la eliminacion de la categoria", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

#Eliminar usuario
@app.route('/eliminarusuario', methods=['DELETE'])
def Eliminar_Usuario(request):
        try:
            if Eliminar_Usuario(request):
                return jsonify({'mensaje': "Usuario eliminado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar la eliminacion del usuario", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

#Eliminar producto
@app.route('/eliminarproducto', methods=['DELETE'])
def Eliminar_Producto(request):
        try:
            if Eliminar_producto(request):
                return jsonify({'mensaje': "Producto eliminado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar la eliminacion del producto", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

#Eliminar factura
@app.route('/eliminarfactura', methods=['DELETE'])
def Eliminar_Factura(request):
        try:
            if Eliminar_Producto(request):
                return jsonify({'mensaje': "Factura eliminado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar la eliminacion de la factura", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

#Eliminar ingreso
@app.route('/eliminaringreso/<Id>', methods=['DELETE'])

def Eliminar_ingreso(Id):
        try:
            if Eliminar_Ingreso(Id):
                return jsonify({'mensaje': "Ingreso eliminado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar la eliminacion de la ingreso", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

#Listo            
#Listar categoria
@app.route('/listarcategoria', methods=['GET'])
def listar_categoria():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT Id_Categoria, nombre_categoria, Estado FROM categoria ORDER BY nombre_categoria ASC"
        cursor.execute(sql)
        datos = cursor.fetchall()
        listar_categoria = []
        for fila in datos:
            categorias = {'Id_Categoria': fila[0], 'nombre_categoria': fila[1], 'Estado': fila[2]}
            listar_categoria.append(categorias)
        return jsonify({'categorias': listar_categoria, 'mensaje': "Categoria listadas.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

#Listar individual
@app.route('/categoria/<Id_Categoria>', methods=['GET'])
def leer_categoria(Id_Categoria):
    try:
        cursor = conexion.connection.cursor()
        sql= "CALL listar_categoria_id('{0}')".format(Id_Categoria)
        print(sql)
        cursor.execute(sql)
        datos = cursor.fetchone()
        for fila in datos:
            categorias = {'Id_Categoria': fila[0], 'nombre_categoria': fila[1], 'Estado': fila[2]}
            return jsonify({'Id_categorias': categorias, 'mensaje': "Categoria listada.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Sin usuarios", 'exito': False})

#Listo
#Listar usuario
@app.route('/listarusuario', methods=['GET'])
def listar_usuario():
    try:
        cursor = conexion.connection.cursor()
        sql = "CALL listar_usuarios()"
        print(sql)
        cursor.execute(sql)
        datos = cursor.fetchall()
        listar_usuario = []
        for fila in datos:
            usuarios = {'Id_Usuario': fila[0], 'nombre_usuario': fila[1], 'correo': fila[2], 'clave': fila[3], 'rol': fila[4]}
            listar_usuario.append(usuarios)
        return jsonify({'usuarios': listar_usuario, 'mensaje': "Usuarios listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

#Listar individual
@app.route('/usuario/<Id_Usuario>', methods=['GET'])
def leer_usuario_db(Id_Usuario):
    try:
        cursor = conexion.connection.cursor()
        #
        sql= "CALL listar_usuarios_id('{0}')".format(Id_Usuario)
        cursor.execute(sql)
        datos = cursor.fetchall()
        print(sql)
        for fila in datos:
            usuarios = {'Id_Usuario': fila[0], 'nombre_usuario': fila[1], 'correo': fila[2], 'clave': fila[3], 'rol': fila[4]}
        return jsonify({'Id_usuarios': usuarios, 'mensaje': "Usuario listado.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Sin usuarios", 'exito': False})

#Listo
#Listar producto
@app.route('/listarproducto', methods=['GET'])
def listar_producto():
    try:
        cursor = conexion.connection.cursor()
        sql = "CALL listar_productos()"
        cursor.execute(sql)
        print(sql)
        datos = cursor.fetchall()
        listar_producto = []
        for fila in datos:
            productos = {'Id_Producto': fila[0], 'nombre_producto': fila[1], 'descripcion': fila[2], 'valor_venta': fila[3], 'cantidad_stock': fila[4],'Id_Categoria': fila[5],'Estado': fila[6]}
            listar_producto.append(productos)
        return jsonify({'productos': productos, 'mensaje': "Productos listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

#Listar individual
@app.route('/producto/<Id_Producto>', methods=['GET'])
def leer_producto_db(Id_Producto):
    try:
        cursor = conexion.connection.cursor()
        sql = "CALL listar_productos_id('{0}')".format(Id_Producto)
        cursor.execute(sql)
        print(sql)
        datos = cursor.fetchone()
        for fila in datos:
            productos = {'Id_Producto': fila[0], 'nombre_producto': fila[1], 'descripcion': fila[2], 'valor_venta': fila[3], 'cantidad_stock': fila[4],'Id_Categoria': fila[5],'Estado': fila[6]}
        return jsonify({'productos': productos, 'mensaje': "Producto listado.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})
        
#Listo
#Listar Factura
@app.route('/listarfactura', methods=['GET'])
def listar_factura():
    try:
        cursor = conexion.connection.cursor()
        sql = "CALL listar_factura()"
        cursor.execute(sql)
        datos = cursor.fetchall()
        listar_factura = []
        for fila in datos:
            facturas = {'Id_Factura': fila[0], 'fecha': fila[1], 'valor_factura': fila[2], 'iva': fila[3], 'valor_neto': fila[4],'Id_Usuario': fila[5],'Id_Producto': fila[6]}
            listar_factura.append(facturas)
        return jsonify({'facturas': facturas, 'mensaje': "Facturas listadas.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False}) 
              
#Listar individual
@app.route('/factura/<Id_Factura>', methods=['GET'])
def leer_factura_db(Id_Factura):
    try:
        cursor = conexion.connection.cursor()
        sql = "CALL listar_factura_id('{0}')".format(Id_Factura)
        cursor.execute(sql)
        datos = cursor.fetchone()
        for fila in datos:
            facturas = {'Id_Factura': fila[0], 'fecha': fila[1], 'valor_factura': fila[2], 'iva': fila[3], 'valor_neto': fila[4],'Id_Usuario': fila[5],'Id_Producto': fila[6]}
        return jsonify({'facturas': facturas, 'mensaje': "Factura listada.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

#Listar Ingreso
@app.route('/listaringreso', methods=['GET'])
def listar_ingreso():
    try:
        cursor = conexion.connection.cursor()
        sql = "CALL listar_ingresos()"
        cursor.execute(sql)
        datos = cursor.fetchall()
        listar_ingreso = []
        for fila in datos:
            ingresos = {'Id_Ingreso': fila[0], 'cantidad_ingresos': fila[1], 'fecha': fila[2], 'valor_compra': fila[3], 'Id_Producto': fila[4]}
            listar_ingreso.append(ingresos)
        return jsonify({'Ingresos': ingresos, 'mensaje': "Ingresos listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})                

#Listo
#Listar individual

@app.route('/ingresos/<Id_Ingresos>', methods=['GET'])
def leer_ingresos_db(Id_Ingresos):
    try:
        cursor = conexion.connection.cursor()
        sql = "CALL listar_ingresos_id('{0}')".format(Id_Ingresos)
        cursor.execute(sql)
        datos = cursor.fetchone()
        for fila in datos:
            ingresos = {'Id_Ingreso': fila[0], 'cantidad_ingresos': fila[1], 'fecha': fila[2], 'valor_compra': fila[3], 'Id_Producto': fila[4]}
        return jsonify({'Ingresos': ingresos, 'mensaje': "Ingresos listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False}) 

# ACTUALIZAR DATOS USUARIOS

def leer_datos_bd(Id_usuario):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT Id_usuario, nombre_usuario, correo, clave FROM usuario WHERE Id_usuario = '{0}'".format(Id_usuario)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuario = {'Id_usuario': datos[0], 'nombre_usuario': datos[1], 'correo': datos[2], 'clave': datos[3]}
            return usuario
        else:
            return None
    except Exception as ex:
        raise ex

@app.route('/actualizar/<Id_usuario>', methods=['PUT'])
def actualizar_datos(Id_usuario):
    if (validar_nombres(Id_usuario) and validar_correo(request.json['nombre_usuario']) and validar_clave(request.json['nombre_usuario'])):
        try:
            usuario = leer_datos_bd(Id_usuario)
            if usuario != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE usuario SET nombre_usuario = '{0}', correo = {1}, clave = '{2}'
                WHERE Id_usuario = '{3}'""".format(request.json['nombre_usuario'], request.json['correo'], request.json['clave'], Id_usuario)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de actualización.
                return jsonify({'mensaje': "Usuario actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})                       

# ACTUALIZAR PRODUCTOS

def leer_producto_bd(id_Producto):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id_Producto, nombre_producto FROM producto WHERE id_Producto = '{0}'".format(id_Producto)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            producto = {'id_Producto': datos[0], 'nombre_producto': datos[1]}
            return producto
        else:
            return None
    except Exception as ex:
        raise ex

@app.route('/actualizarproductos/<id_Producto>', methods=['PUT'])
def actualizar_producto(id_Producto):
    if (validar_producto(id_Producto)):
        try:
            producto = leer_producto_bd(id_Producto)
            if producto != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE producto SET nombre_producto = '{0}', descripcion = '{1}', valor_venta = '{2}', cantidad_stock = '{3}', Id_Categoria = '{4}'
                WHERE id_Producto = '{5}'""".format(request.json['nombre_producto'], request.json['descripcion'], request.json['valor_venta'], request.json['cantidad_stock'], request.json['Id_Categoria'], id_Producto)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de actualización.
                return jsonify({'mensaje': "Producto actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Producto no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ACTUALIZAR CATEGORIA

def leer_categoria_bd(Id_Categoria):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT Id_Categoria, nombre_categoria FROM categoria WHERE Id_Categoria = '{0}'".format(Id_Categoria)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            categoria = {'Id_Categoria': datos[0], 'nombre_categoria': datos[1]}
            return categoria
        else:
            return None
    except Exception as ex:
        raise ex


@app.route('/actualizarcategoria/<Id_Categoria>', methods=['PUT'])
def actualizar_categoria(Id_Categoria):
    if (validar_categoria(Id_Categoria)):
        try:
            categoria = leer_categoria_bd(Id_Categoria)
            if categoria != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE categoria SET nombre_categoria = '{0}', Estado = '{1}'
                WHERE Id_Categoria = '{2}'""".format(request.json['nombre_categoria'],  request.json['Estado'], Id_Categoria)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de actualización.
                return jsonify({'mensaje': "Categoria actualizada.", 'exito': True})
            else:
                return jsonify({'mensaje': "Categoria no encontrada.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})                           
     

def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
