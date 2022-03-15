from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL

Enlace = Flask(__name__)
BaseDatos = MySQL()
Enlace.config ['MYSQL_DATABASE_HOST'] = 'localhost'
Enlace.config ['MYSQL_DATABASE_USER'] = 'root'
Enlace.config ['MYSQL_DATABASE_DB'] = 'basedatos'
BaseDatos.init_app(Enlace)



@Enlace.route('/')
def Visual():
    Sql = "SELECT * FROM `usuario`;"
    Conexión = BaseDatos.connect()
    Cursor = Conexión.cursor()
    Cursor.execute(Sql)


    Usuarios = Cursor.fetchall()
    print(Usuarios)

    Conexión.commit()

    return render_template('Usuarios/Visual.html', Usuarios = Usuarios)

@Enlace.route('/Registrar')
def Registrar():
    return render_template('Usuarios/Registrar.html')




@Enlace.route('/Almacen', methods=['POST'])
def Almacenamineto():

    _Usuario = request.form ['txtUsuario']
    _Correo = request.form ['txtCorreo']
    _Password = request.form['txtPassword']


    Sql ="""INSERT INTO `usuario` 
        (`Usuario`, `Correo`,`Password`)
         VALUES (%s, %s, %s);"""
    
    Datos = (_Usuario,_Password,_Correo)
    
    Conexión = BaseDatos.connect()
    Cursor = Conexión.cursor()
    Cursor.execute(Sql, Datos)
    Conexión.commit()


    return render_template('Usuarios/Visual.html')

if __name__ == '__main__':
    Enlace.run(debug = True)


