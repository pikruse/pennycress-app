from flask import Flask, jsonify, request

# set app name
app = Flask(__name__)

@app.route('/')
def home():
    return "Among Us Balls"

@app.route('/upload', methods=['POST'])
def upload_img():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    return jsonify({'message': 'Image uploaded successfully'}), 200    

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    print(f"Starting Flask app at http://{host}:{port}")
    app.run(debug=True, host=host, port=port)
