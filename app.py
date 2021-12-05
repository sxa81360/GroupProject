from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
@app.route('/')
def edit():
    #Data to pass to our templates/index.html file
    data = 6

    
    return render_template('index.html', game_data = data)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug = True)
