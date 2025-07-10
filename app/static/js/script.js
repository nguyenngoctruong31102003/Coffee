let menu = document.querySelector("#menu-icon");
let menuList = document.querySelector(".nav-list");

menu.onclick = () => {
  menu.classList.toggle("bx-x");
  menuList.classList.toggle("open");
};

// preloader
window.addEventListener("load", () => {
  const loader = document.querySelector(".loader");
  if (loader) {
    // Đảm bảo hiệu ứng loading kéo dài ít nhất 1 giây
    setTimeout(() => {
      loader.style.transition = "opacity 0.5s ease-out";
      loader.style.opacity = "0";

      setTimeout(() => {
        loader.style.display = "none";
      }, 500); // Ẩn hẳn sau khi hoàn thành hiệu ứng mờ
    }, 1000); // Chờ 1 giây trước khi bắt đầu mờ dần
  }
});
