$(document).ready(function () {
    var datatable = $('#example').DataTable({
        processing: true,
        serverSide: true,
        "searching": false,
        ajax: {
            url: 'http://127.0.0.1:8000/validate/validateresult/',
            type: 'POST',
            data: (d) => {
                d.csrfmiddlewaretoken = csrftoken;
                var rfc_emisor = $("#filter_rfc_emisor").val();
                if (rfc_emisor) {
                    d.rfc_emisor = rfc_emisor;
                }
            },
        },
        columns: [
            { data: 'id' },
            { data: 'rfc_emisor' },
            { data: 'rfc_receptor' },
            { data: 'version' },
            { data: 'fecha' },
            { data: 'fecha_validacion' },
            { data: 'sello' },
        ],
    });

    $("#id_get").on("click", function() {
        datatable.ajax.reload();
    })

    $("#filter_rfc_emisor").on("keyup", function() {
        datatable.ajax.reload();
    })
});
