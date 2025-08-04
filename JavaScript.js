function toggleDetalle(id) {
  const div = document.getElementById(id);
  div.style.display = div.style.display === 'block' ? 'none' : 'block';
}

  function toggleMenu() {
    const nav = document.getElementById("navLinks");
    nav.classList.toggle("active");
  }
