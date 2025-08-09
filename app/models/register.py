import datetime

class Register:
    def __init__(self, ten_khachhang, so_dien_thoai, mat_khau, ngay_dang_ky=None):
        self.ten_khachhang = ten_khachhang
        self.so_dien_thoai = so_dien_thoai
        self.mat_khau = mat_khau
        self.ngay_dang_ky = ngay_dang_ky or datetime.datetime.now()
