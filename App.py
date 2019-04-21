from flask import Flask #importamos los modulos necesarios
from flask import render_template #modulo para renderizar vistas 
from flask import request  #modulo para recibir datos get y post
from flask import url_for, redirect #modulos para redireccionar 
from flask_mysqldb import MySQL #modulo para conectar a base de datos
from flask import flash #envia menajes a la vista 


app = Flask(__name__)

#pasamos parametros de configuracion para conexion a base de datos
app.config['MYSQL_HOST'] = 'localhost';
app.config['MYSQL_USER'] = 'heroku';
app.config['MYSQL_PASSWORD'] = 'heroku.2019';
app.config['MYSQL_DB'] = 'flask_crud';

#sesion 
app.secret_key = 'mysecret'
#pasamos losparametros a MySQL y almacenamos en el objeto mysql
mysql = MySQL(app)


@app.route('/') #define una ruta 
def index():

    con = mysql.connection.cursor() #instanciamos la conexion 
    con.execute('SELECT * FROM contactos') #ejecutamos consulta
    result = con.fetchall() #almacenamos el resultado de la consulta en el arreglo result recorriedola con la funcion fetchall
    #print (result)
    #retornamos los datos del array pasandolos como parametros en el render
    return render_template('index.html', contactos = result)



@app.route('/add' , methods = ['POST']) #indicamos que la ruta va recibir parametros por post
def add():
    if request.method == 'POST':

        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']

        print (nombre)
        print (telefono)
        print (email)
       
        
        con = mysql.connection.cursor() #almacenamos la conexion en el objeto con 
        con.execute('INSERT INTO contactos (nombre, telefono, email) VALUES ( %s, %s, %s)', (nombre, telefono, email)) #preparamos la consulta con el metodo execute del metodo con 
        mysql.connection.commit()
        flash('Contacto guardado!')
        return redirect(url_for('index'))#redireciona al mismo index
        

        
        

@app.route('/edit/<id>')
def edit(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM contactos WHERE id = {0}'.format(id))
    dato = con.fetchall()
    return render_template('edit.html', contacto = dato[0])



@app.route('/delete/<string:id>')
def delete(id):

    con = mysql.connection.cursor()
    con.execute('DELETE FROM contactos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado!')
    return redirect(url_for('index'))



@app.route('/update/<id>', methods = ['POST'])
def update(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']

        
    con = mysql.connection.cursor()
    con.execute("""
        UPDATE contactos
        SET nombre = %s,
            telefono = %s,
            email = %s
        WHERE id = %s
    """, (nombre, telefono, email, id))
    flash('Contacto actualizado!')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(port = 3000, debug = True)#indicamos que la aplicacion va correr en el puerto 3000 y
    # ademas ativamos el modo depuracion para no reiniciar el servidor