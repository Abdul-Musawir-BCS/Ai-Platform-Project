from flask import Flask, render_template
from flask_cors import CORS
from database import init_db

from routes.generate import generate_bp
from routes.edit import edit_bp
from routes.analyze import analyze_bp
from routes.compare import compare_bp
from routes.chatbot import chatbot_bp
from routes.upload import upload_bp
from routes.history import history_bp

app = Flask(__name__)
CORS(app)

init_db()

# Serve frontend
@app.route("/")
def home():
    return render_template("index.html")

# Register routes
app.register_blueprint(generate_bp)
app.register_blueprint(edit_bp)
app.register_blueprint(analyze_bp)
app.register_blueprint(compare_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(history_bp)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)


