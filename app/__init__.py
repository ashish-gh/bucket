import os

from .main import create_app
from .main.controller.search_controller import search_bp

# 
URL_PREFIX = 'api/v1/bucket'

app = create_app(os.getenv("FLASK_ENV", "test"))

# Resister blueprints
app.register_blueprint(search_bp)

if __name__ == "__main__":
    app.run()
