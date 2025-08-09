document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");   //form đăng ký
  const nameInput = document.getElementById("name"); //Tên khách hàng
  const phoneInput = document.getElementById("phone"); //Số điện thoại
  const passwordInput = document.getElementById("password"); //Mật khẩu
  const nameError = document.getElementById("name-error");
  const phoneError = document.getElementById("phone-error");
  const passwordError = document.getElementById("password-error");

  // Hàm kiểm tra tính hợp lệ của các trường nhập liệu
  function validateName() {
    const value = nameInput.value.trim();
    const regex = /^[A-Za-zÀ-ỹà-ỹ\s]{2,}$/;
    if (!regex.test(value)) {
      nameError.textContent =
        "Vui lòng nhập họ tên hợp lệ (ít nhất 2 ký tự, cho phép dấu tiếng Việt).";
      return false;
    } else {
      nameError.textContent = "";
      return true;
    }
  }

  function validatePhone() {
    const value = phoneInput.value.trim();
    const regex = /^[0-9]{10}$/;
    if (!regex.test(value)) {
      phoneError.textContent = "Vui lòng nhập đúng số điện thoại (10 số).";
      return false;
    } else {
      phoneError.textContent = "";
      return true;
    }
  }

  function validatePassword() {
    const value = passwordInput.value;
    if (value.length < 6) {
      passwordError.textContent = "Mật khẩu phải có ít nhất 6 ký tự.";
      return false;
    } else {
      passwordError.textContent = "";
      return true;
    }
  }

  nameInput.addEventListener("input", validateName);
  phoneInput.addEventListener("input", validatePhone);
  passwordInput.addEventListener("input", validatePassword);

  form.addEventListener("submit", function (e) {
    let valid = true;
    if (!validateName()) valid = false;
    if (!validatePhone()) valid = false;
    if (!validatePassword()) valid = false;
    if (!valid) e.preventDefault();
  });
});

// Popup thông báo
window.addEventListener("DOMContentLoaded", function () {
  var popup = document.getElementById("popup-message");
  if (popup) {
    popup.style.display = "block";
    setTimeout(function () {
      popup.style.display = "none";
    }, 2500);
  }
});