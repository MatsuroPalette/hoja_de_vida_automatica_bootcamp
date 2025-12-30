// Espera a que cargue el DOM
document.addEventListener("DOMContentLoaded", () => {

    /* =========================
       SCROLL SUAVE ENTRE SECCIONES
       ========================= */
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();

            const targetId = this.getAttribute("href");
            const target = document.querySelector(targetId);

            if (target) {
                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        });
    });


    /* =========================
       EFECTO SUTIL AL APARECER
       ========================= */
    const sections = document.querySelectorAll(".section");

    const observer = new IntersectionObserver(
        entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                }
            });
        },
        { threshold: 0.15 }
    );

    sections.forEach(section => observer.observe(section));


    /* =========================
       AÑO AUTOMÁTICO EN FOOTER
       ========================= */
    const footer = document.querySelector("footer p");
    if (footer) {
        const year = new Date().getFullYear();
        footer.innerHTML = footer.innerHTML.replace("2025", year);
    }

});




/* =========================
   CERTIFICADOS (MOSTRAR / OCULTAR)
   ========================= */
document.addEventListener("DOMContentLoaded", () => {

    const btnCertificados = document.getElementById("ver-certificados");
    const seccionCertificados = document.getElementById("certificados");
    const btnCerrar = document.getElementById("cerrar-certificados");

    if (!btnCertificados || !seccionCertificados || !btnCerrar) return;

    btnCertificados.addEventListener("click", (e) => {
        e.preventDefault();

        seccionCertificados.classList.remove("oculto");

        seccionCertificados.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    });

    btnCerrar.addEventListener("click", () => {
        seccionCertificados.classList.add("oculto");
    });

});





document.addEventListener("DOMContentLoaded", () => {
    const btnAbrir = document.getElementById("ver-certificados");
    const btnCerrar = document.getElementById("cerrar-certificados");
    const seccion = document.getElementById("certificados");

    if (btnAbrir && seccion) {
        btnAbrir.addEventListener("click", () => {
            seccion.classList.remove("oculto");
        });
    }

    if (btnCerrar && seccion) {
        btnCerrar.addEventListener("click", () => {
            seccion.classList.add("oculto");
        });
    }
});
