from flask import Flask, render_template, request
from werkzeug import secure_filename
import mysql.connector
import os
import os.path
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/import/'

@app.route('/')
def index():
    return render_template('index.html', title = 'Proyecto')

@app.route('/fuente_datos')
def fuente_datos():
    return render_template('fuente_de_datos.html')

@app.route('/cargar_archivo', methods=['POST'])
def cargar_archivo():
    if request.method == 'POST':
        archivo = request.files['archivo']
        nombre = secure_filename(archivo.filename)
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre))

        return render_template('index.html', title = 'Proyecto')

@app.route('/graficos')
def graficos():
    ext = os.path.splitext(app.config['UPLOAD_FOLDER']+'worldcups.csv')[1]
        
    if ext == '.csv':
        data = pd.read_csv(app.config['UPLOAD_FOLDER']+'worldcups.csv', sep=',')
        return render_template('graficos.html', json=list(data))

@app.route('/generar_grafica', methods=['POST'])
def generar_grafica():
    #if ext == '.csv':
    data = pd.read_csv(app.config['UPLOAD_FOLDER']+'worldcups.csv', sep=',')
    grafico = request.form['grafico']
    arreglo = request.form['columnas']
    arreglo = arreglo.split(',')
    equipos = data.loc[0:4, [arreglo[0], arreglo[1]]]

    ganador = equipos[arreglo[0]]
    goles = equipos[arreglo[1]]
    fig = plt.figure(figsize=(10, 6))

    if grafico == 'Columnas':
        plt.bar(ganador, goles, width=0.3, color='#3498db')
        plt.xticks(ganador)
        plt.ylabel(arreglo[1])
        plt.xlabel(arreglo[0])
        plt.title('Estadistica Graficas en '+grafico)
    if grafico == 'Barras':
        plt.barh(ganador, goles, color='#3498db')
        plt.xticks(ganador)
        plt.ylabel(arreglo[1])
        plt.xlabel(arreglo[0])
        plt.title('Estadistica Graficas en '+grafico)
    if grafico == 'Porcentajes':
        colores = ['#1abc9c', '#c0392b', '#e67e22', '#2874a6', '#8e44ad']
        plt.pie(goles, labels=ganador, colors=colores, startangle=90, explode=(0.1, 0.1, 0.1, 0.1, 0.1), radius=1.2, autopct='%0.0f%%')
        plt.title('Estadistica Graficas en '+grafico)

    if grafico == 'Histograma':
        fig, ax = plt.subplots()
        ax.bar(ganador, goles, width=1.0)
        plt.title('Estadistica Graficas en '+grafico)

    if grafico == 'Lineal':
        plt.plot(ganador)
        plt.xlabel(arreglo[1])
        plt.ylabel(arreglo[0])
        plt.title('Estadistica Graficas en '+grafico)

    fig.savefig("./static/temp/1.png")
    route = "./static/temp/1.png"

    return route

@app.route('/consulta_info')
def consulta_info():
    ext = os.path.splitext(app.config['UPLOAD_FOLDER']+'worldcups.csv')[1]
        
    if ext == '.csv':
        data = pd.read_csv(app.config['UPLOAD_FOLDER']+'worldcups.csv', sep=',')
        return render_template('consultas.html', json=list(data))

@app.route('/generar_consultas', methods=['POST'])
def generar_consultas():
    #if ext == '.csv':
    data = pd.read_csv(app.config['UPLOAD_FOLDER']+'worldcups.csv', sep=',')
    arreglo = request.form['consultas']
    arreglo = arreglo.split(',')
    print(len(arreglo))
    equipos = data.loc[0:10, [arreglo[0], arreglo[1]]]

    table = equipos.to_html(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', border=None, table_id=None)

    return table

@app.route('/generar_exportacion')
def generar_exportacion():
    return render_template('exportar.html')

@app.route('/exportar', methods=['POST'])
def exportar():
    data = pd.read_csv(app.config['UPLOAD_FOLDER']+'worldcups.csv', sep=',')
    ext = request.form['extension']

    if ext == 'csv':
        data.to_csv('./static/export/externo.csv')
    if ext == 'xlsx':
        data.to_excel('./static/export/externo.xlsx', index = None, header=True)
    
    return 'Archivo exportado correctamente.'

@app.route('/limpiar')
def limpiar():
    ext = os.path.splitext(app.config['UPLOAD_FOLDER']+'worldcups.csv')[1]
        
    if ext == '.csv':
        data = pd.read_csv(app.config['UPLOAD_FOLDER']+'worldcups.csv', sep=',')
        return render_template('limpiar_datos.html', json=list(data))

@app.route('/generar_limpieza', methods=['POST'])
def generar_limpieza():
    if request.method == 'POST':
        ext = os.path.splitext(app.config['UPLOAD_FOLDER']+'worldcups.csv')[1]
        columna = request.form['columna']
        limpieza = request.form['limpieza']

        if ext == '.csv':
            data = pd.read_csv(app.config['UPLOAD_FOLDER']+'worldcups.csv', sep=',')
            equipos = data[[columna]]
           
            if limpieza == '1':
                data = data.dropna(subset=list(equipos))
                data.to_csv('./static/import/worldcups.csv')
            
            if limpieza == '2':
                data = data[[columna]].fillna(0)
                data.to_csv('./static/import/worldcups.csv')
                print(data)
               
        return 'Limpieza ejecutada correctamente.'

            

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)