function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

$(document).ready(function () {
  var datatable = $("#example").DataTable({
    processing: true,
    serverSide: true,
    language: {
      url: "//cdn.datatables.net/plug-ins/1.10.16/i18n/Spanish.json",
    },
    searching: false,
    ajax: {
      url: "http://127.0.0.1:8000/validate/validateresult/",
      type: "POST",
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
    columns: [
      {
        data: "rfc_emisor",
      },
      {
        data: "rfc_receptor",
      },
      {
        data: "version",
      },
      {
        data: "fecha",
      },
      {
        data: "fecha_validacion",
      },
      {
        data: "sello",
      },
      {
        render: function (data, type, row, meta) {
          html = `<a href='/validate/detail/${row.id}'>detalle</a>`;
          return html;
        },
      },
    ],
  });
  $("#filter_rfc_emisor").on("keyup", function () {
    datatable.ajax.reload();
  });
  $("#filter_rfc_receptor").on("keyup", function () {
    datatable.ajax.reload();
  });
  $("#filter_fecha").on("change", function () {
    datatable.ajax.reload();
  });
});
