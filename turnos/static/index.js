$("#btnTurnos").click(function () {
  $("#formClientes").trigger("reset");
  $(".modal-header").css("background-color", "#0D3745");
  $(".modal-header").css("color", "white");
  $(".modal-title").text("Rellena los campos de contacto");
  $("#btnSubmit").text("Enviar");
  $("#formClientes").attr("data-action", "guardar");
  $("#modalCRUD").modal("show");
});

document.addEventListener("DOMContentLoaded", function () {
  // Obtener referencia al botón
  const btnContinuar = document.getElementById("btnContinuarTurno");

  // Función para verificar el email
  function esEmailValido(email) {
    // Expresión regular para validar email
    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regexEmail.test(email);
  }

  // Agregar evento de click al documento para verificar campos
  document.addEventListener("click", function () {
    // Obtener todos los campos requeridos dentro del formulario
    const camposRequeridos = document.querySelectorAll("#formTurno [required]");
    let formValido = true;

    // Verificar si todos los campos requeridos están llenos
    camposRequeridos.forEach(function (campo) {
      if (!campo.value.trim()) {
        // Si el valor está vacío
        formValido = false;
      }
    });

    // Verificar si el campo de email es válido
    const emailCampo = document.getElementById("inputEmailTurno");
    if (!esEmailValido(emailCampo.value)) {
      formValido = false;
    }

    // Si todos los campos requeridos están llenos y el email es válido, activar el botón
    if (formValido) {
      btnContinuar.disabled = false;
    } else {
      // Si no todos los campos están llenos, asegurarse de que el botón esté desactivado
      btnContinuar.disabled = true;
    }
  });

  // También verificar los campos al cargar la página inicialmente
  document.dispatchEvent(new Event("click"));
});
