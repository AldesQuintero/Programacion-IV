from flask import Flask, jsonify, request

app = Flask(__name__)

from palabras import palabras

# Testing Route


# Get Data Routes
@app.route('/palabras')
def getPalabras():
    # return jsonify(palabras)
    return jsonify({'palabras': palabras})


@app.route('/palabras/<string:palabra_significado>')
def getPalabra(palabra_significado):
    palabrasFound = [
        palabra for palabra in palabras if palabra['palabra'] == palabra_significado.lower()]
    if (len(palabrasFound) > 0):
        return jsonify({'palabra': palabrasFound[0]})
    return jsonify({'message': ''})

# Create Data Routes
@app.route('/palabras', methods=['POST'])
def addPalabra():
    nueva_palabra = {
        'palabra': request.json['palabra'],
        'significado': request.json['significado'],
    }
    palabras.append(nueva_palabra)
    return jsonify({'palabras': palabras})

# Update Data Route
@app.route('/palabras/<string:palabra_significado>', methods=['PUT'])
def editarpalabra(palabra_significado):
    palabrasFound = [palabra for palabra in palabras if palabra['palabra'] == palabra_significado]
    if (len(palabrasFound) > 0):
        palabrasFound[0]['palabra'] = request.json['palara']
        palabrasFound[0]['significado'] = request.json['significado']
        return jsonify({
            'message': 'Palabra Actualizada',
            'palabra': palabrasFound[0]
        })
    return jsonify({'message': 'Palabra no encontrada'})

# DELETE Data Route
@app.route('/palabras/<string:palabra_significado>', methods=['DELETE'])
def eliminarpalabra(palabra_significado):
    palabrasFound = [palabra for palabra in palabras if palabra['palabra'] == palabra_significado]
    if len(palabrasFound) > 0:
        palabras.remove([palabrasFound])
        return jsonify({
            'message': 'Palabra Eliminada',
            'palabras': palabras
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)