# Routes go here
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import pyodbc
import hashlib

login_bp = Blueprint('login', __name__)

@login_bp.route('/logout')
def logout():
    session.pop('ten_khachhang', None)
    flash('Bạn đã đăng xuất thành công!')
    return redirect(url_for('index.index_page'))

CONNECTION_STRING = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=NNGOC-TRUONG-\HOST;DATABASE=CoffeeShop;UID=admin_coffee;PWD=0965758330'

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

@login_bp.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        so_dien_thoai = request.form.get('username')
        mat_khau = request.form.get('password')
        if not (so_dien_thoai and mat_khau):
            flash('Vui lòng nhập đầy đủ thông tin!')
            return render_template('login.html')
        try:
            conn = pyodbc.connect(CONNECTION_STRING)
            cursor = conn.cursor()
            cursor.execute('SELECT Ten_khachhang, Mat_khau FROM KhachHang WHERE So_dien_thoai = ?', so_dien_thoai)
            row = cursor.fetchone()
            if row and row.Mat_khau == hash_password(mat_khau):
                session['ten_khachhang'] = row.Ten_khachhang
                flash('Chào mừng bạn đến với CoffeeShop')
                return redirect(url_for('index.index_page'))
            else:
                flash('Số điện thoại hoặc mật khẩu không đúng!')
                return render_template('login.html')
        except Exception as e:
            flash(f'Lỗi đăng nhập: {e}')
            return render_template('login.html')
    return render_template('login.html')