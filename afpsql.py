
# Christian Eduardo Rodriguez Perez
import psycopg2
import json
import os
contador = 0

# Creación de función para ingresar los datos automáticamente.
def insertar(fn,ln,e,pw,ia,rid):
	# Sentencia SQL
	sql = """INSERT INTO users(first_name,last_name,email,password,is_active,role_id) VALUES (%s,%s,%s,%s,%s,%s)"""
	conn = None
	try:
		# Conexión a la base de datos postgreSQL
		conn = psycopg2.connect(user="postgres",password="cristianlalo1",host="127.0.0.1",port="5432",database="ejemplo_dba")
		cur = conn.cursor()
		# Ejecutar la query con los parametros de la función
		cur.execute(sql,[fn,ln,e,pw,ia,rid])
		# Guardar los cambios
		conn.commit()
		# Cerrar la conexión a la base de datos.
		cur.close()
		print("Registro ingresado correctamente :)")


	# Atrapar los errores y excepciones de la base de dato y conexiones.
	except (Exception,psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

# Christian Eduardo Rodriguez Perez
# Abrir el archivo en modo de lectura
with open('data4.json') as f:
	data = json.loads(f.read())

# Extraer los datos de el archivo JSON
	for datos in data:
		nombre = datos['first_name']
		apellido = datos['last_name']
		email = datos['email']
		pswrd = datos['password']
		is_active = datos['is_active']
		rol_id = datos['role_id']
		# Ejecutar la función y enviar los parametros
		insertar(nombre,apellido,email,pswrd,is_active,rol_id)
		contador+=1

# Al terminar de insertar los datos, borrar pantalla y mostrar cuantos datos se insertaron en total.
os.system('cls')
print("Total Datos ingresados: " + str(contador))
