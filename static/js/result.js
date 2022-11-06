$(document).ready(function() {
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
                var rfc_receptor = $("#filter_rfc_receptor").val();
                var fecha_validacion = $("#filter_fecha").val();
                if (rfc_emisor) {
                    d.rfc_emisor = rfc_emisor;
                }
                if (rfc_receptor) {
                    d.rfc_receptor = rfc_receptor;
                }
                if (fecha_validacion) {
                    d.fecha_validacion = fecha_validacion;
                }
            },
            
        },
        columns: [ {
            data: 'rfc_emisor'
        }, {
            data: 'rfc_receptor'
        }, {
            data: 'version'
        }, {
            data: 'fecha'
        }, {
            data: 'fecha_validacion'
        }, {
            data: 'sello'
        }, {
            render: function(data, type, row, meta) {
                html = `<a href='/validate/detail/${row.id}'>detalle</a>`
                return html
            }
        }, ],
    });
    $("#filter_rfc_emisor").on("keyup", function() {
        datatable.ajax.reload();
    });
    $("#filter_rfc_receptor").on("keyup", function() {
        datatable.ajax.reload();
    });
    $("#filter_fecha").on("change", function() {
        datatable.ajax.reload();
    });
    
    
});