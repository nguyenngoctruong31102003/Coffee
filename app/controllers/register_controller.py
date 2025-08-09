import pyodbc
import hashlib
import datetime
from app.models.register import Register

class RegisterController:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    # Mã hóa mật khẩu trước khi lưu vào cơ sở dữ liệu
    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Thêm thông tin khách hàng vào cơ sở dữ liệu
    def add_user(self, ten_khachhang, so_dien_thoai, mat_khau):
        mat_khau_mahoa = self.hash_password(mat_khau)
        ngay_dang_ky = datetime.datetime.now()
        year = ngay_dang_ky.strftime('%Y')
        last3phone = so_dien_thoai[-3:]
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            # Kiểm tra số điện thoại đã tồn tại chưa
            cursor.execute('SELECT COUNT(*) FROM KhachHang WHERE So_dien_thoai = ?', so_dien_thoai)
            if cursor.fetchone()[0] > 0:
                cursor.close()
                conn.close()
                return 'duplicate_phone'
            # Sinh mã ID_khachhang như cũ
            cursor.execute('''
                SELECT MAX(CAST(RIGHT(ID_khachhang, 3) AS INT))
                FROM KhachHang
                WHERE LEFT(ID_khachhang, 4) = ? AND SUBSTRING(ID_khachhang, 5, 3) = ?
            ''', year, last3phone)
            max_so = cursor.fetchone()[0]
            if max_so is None:
                max_so = 0
            max_so += 1
            stt = str(max_so).zfill(3)
            new_id = f"{year}{last3phone}{stt}"
            user = Register(ten_khachhang, so_dien_thoai, mat_khau_mahoa, ngay_dang_ky)
            cursor.execute('''
                INSERT INTO KhachHang (ID_khachhang, Ten_khachhang, So_dien_thoai, Mat_khau, Ngay_dang_ky)
                VALUES (?, ?, ?, ?, ?)
            ''', new_id, user.ten_khachhang, user.so_dien_thoai, user.mat_khau, user.ngay_dang_ky)
            conn.commit()
            print(f"Đã thêm thông tin khách hàng thành công! ID: {new_id}")
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Lỗi khi thêm khách hàng vào CSDL: {e}")
            return False
