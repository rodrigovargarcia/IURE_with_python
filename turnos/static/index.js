        // const $form = document.querySelector('#form')

        // $form.addEventListener('submit', handleSubmit)

        // async function handleSubmit(event) {
        //     event.preventDefault()
        //     const form = new FormData(this)
        //     const response = await fetch(this.action, {
        //         method: this.method,
        //         body: form,
        //         headers: {
        //             'Accept': 'application/json'
        //         }
        //     })
        //     if (response.ok) {
        //         this.reset()
        //         alert('Gracias por contactarnos, te escribiremos pronto!')
        //     }
        // }
        $("#btnTurnos").click(function () {
            $("#formClientes").trigger("reset");
            $(".modal-header").css("background-color", "#0D3745");
            $(".modal-header").css("color", "white");
            $(".modal-title").text("Rellena los campos de contacto");
            $("#btnSubmit").text("Enviar");
            $("#formClientes").attr("data-action", "guardar");
            $("#modalCRUD").modal("show");
        });