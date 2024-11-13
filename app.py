from flask import Flask, render_template

# set app name
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    print(f"Starting Flask app at http://{host}:{port}")
    app.run(debug=True, host=host, port=port)
