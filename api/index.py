import json
from flask import Flask,  jsonify, request
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
import psycopg2


""" conM = psycopg2.connect(host="sist3_postgresql-master_1", database='tienda', user='postgres',
    password='123')
conS = psycopg2.connect(host="sist3_postgresql-slave_1", database='tienda', user='postgres',
password='123')



with conM:
    
    cur = conM.cursor()
    cur.execute("select * from information_schema.tables where table_name=%s", ('prods',))
    if(bool(cur.rowcount) == False):
        cur.execute('''CREATE TABLE prods (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        precio INTEGER NOT NULL
                        )''')
        cur.close()
        conM.commit()
    cur = conM.cursor()    
    cur.execute('SELECT version()')    
    version = cur.fetchone()[0]
    print('Se esta ejecutando la version: ',version,' de psycopg2')
    cur.close() """


app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

@app.route('/',methods=['GET'])
def alo():
    return 'xd'

@app.route('/api/getprod/<pname>',methods=['GET'])
def get_prods(pname):
    cur = conS.cursor()
    cur.execute("select * from prods WHERE '%s' LIKE '%' || name || '%';",(pname))
    prods = cur.fetchall()
    cur.close()
    return jsonify(prods)

    

@app.route('/api/addprod',methods=['POST'])
def addprod():
    name = request.form.get('name')
    precio = request.form.get('precio')
    cur = conM.cursor()
    cur.execute("INSERT INTO prods(name, price) VALUES(%s, %d)",(name,int(precio)))
    cur.close()
    conM.commit()  
    return 'Producto Agregado'

    
    
       
    

if __name__ == '__main__':   
    
    app.run(debug=True,port=3050)