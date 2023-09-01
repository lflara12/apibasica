from flask import Flask, jsonify
app=Flask(__name__)
from flask_cors import CORS
import numpy as np


app= Flask(__name__) 
CORS(app) 

 
@app.route("/")
def HolaFlask():
    return jsonify ("<h1>¡Hola Flask!</h1>")




@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return jsonify({"resultado": resultado})



    
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad <18:
        r= "Menor de edad"
    elif (edad<60): 
        r="Adulto"
    else:
        r="Adulto mayor"
    return jsonify({"resultado": r})




@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0, columnas=0, filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas, columnas))
        
    return jsonify({"arreglo": arreglo.tolist()})


if __name__=='__main__':
    
    app.run(debug=True)





    


    
    