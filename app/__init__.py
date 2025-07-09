# Flask app initialization
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import và đăng ký các blueprint
    from app.routes.index import index_bp
    from app.routes.menu import menu_bp
    
    """
     Thêm các đường dẫn khác nếu cần tại đây
    """
    app.register_blueprint(index_bp) # Trang Index
    app.register_blueprint(menu_bp) # Trang Menu
    
    return app
