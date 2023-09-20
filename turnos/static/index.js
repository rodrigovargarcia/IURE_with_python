$("#btnTurnos").click(function () {
    $("#formClientes").trigger("reset");
    $(".modal-header").css("background-color", "#0D3745");
    $(".modal-header").css("color", "white");
    $(".modal-title").text("Rellena los campos de contacto");
    $("#btnSubmit").text("Enviar");
    $("#formClientes").attr("data-action", "guardar");
    $("#modalCRUD").modal("show");
});


function mostrarErrores(response){
    $('#Error').html("");
    let error = "";
    const errorString = 'Este campo es obligatorio.'
    if(response.error.includes(errorString)){
        error = ""
    }else{
        for (let item in response.error) {
            error += `<div class= "alert alert-danger"> <strong>` + response.error[item] + `</strong></div>`
    }
    }
    $('#Error').append(error)
}