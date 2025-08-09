# Routes go here
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.controllers.register_controller import RegisterController

register_bp = Blueprint('register', __name__)

# Thay đổi chuỗi kết nối phù hợp với SQL Server của bạn
CONNECTION_STRING = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=NNGOC-TRUONG-\HOST;DATABASE=CoffeeShop;UID=admin_coffee;PWD=0965758330'
register_controller = RegisterController(CONNECTION_STRING)

@register_bp.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        ten_khachhang = request.form.get('name')
        so_dien_thoai = request.form.get('phone')
        mat_khau = request.form.get('password')
        if not (ten_khachhang and so_dien_thoai and mat_khau):
            flash('Vui lòng nhập đầy đủ thông tin!')
            return render_template('register.html')
        try:
            result = register_controller.add_user(ten_khachhang, so_dien_thoai, mat_khau)
            if result == 'duplicate_phone':
                flash('Số điện thoại đã tồn tại!')
                return render_template('register.html')
            elif result:
                flash('Đã đăng ký thành công!')
                return redirect(url_for('login.login_page'))
            else:
                flash('Đăng ký thất bại!')
                return render_template('register.html')
        except Exception as e:
            flash(f'Đăng ký thất bại: {e}')
            return render_template('register.html')
    return render_template('register.html')