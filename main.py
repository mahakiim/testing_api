from flask import Flask
from controllers.predict import predict_bp  # Import blueprint dari controllers

app = Flask(__name__)

# Registrasi blueprint ke aplikasi Flask
app.register_blueprint(predict_bp)

if __name__ == '__main__':
    app.run(debug=True)
