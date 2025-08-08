# Flask app initialization
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

def create_app():
    app = Flask(__name__)
    
    # Cấu hình chuỗi kết nối SQL Server
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mssql+pyodbc://admin_coffee:0965758330@NNGOC-TRUONG-\\HOST/CoffeeShop?driver=ODBC+Driver+17+for+SQL+Server'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    # Đưa db ra ngoài để các model có thể import
    app.db = db
    
    # Import và đăng ký các blueprint
    from app.routes.index import index_bp
    from app.routes.menu import menu_bp
    from app.routes.login import login_bp
    from app.routes.register import register_bp
    
    """
     Thêm các đường dẫn khác nếu cần tại đây
    """
    app.register_blueprint(index_bp) # Trang Index
    app.register_blueprint(menu_bp) # Trang Menu
    app.register_blueprint(login_bp) # Trang Login
    app.register_blueprint(register_bp) # Trang Register

    # Kiểm tra kết nối database
    try:
        with app.app_context():
            db.session.execute(text('SELECT 1'))
        print('Kết nối database thành công!')
    except Exception as e:
        print('Kết nối database thất bại:', e)
    return app
