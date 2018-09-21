(function (AlertaEnCreacion, $, undefined) {
    AlertaEnCreacion.init = function () {
        var mensaje = document.getElementById("id_en_creacion");
        var urldispositivo = $("#entrada-detalle-form").data("api");
        var primary_key = $("#entrada-detalle-form").data("key");
        $('#id_en_creacion').click(function () {
            if ($("#id_en_creacion").is(':checked')) {
                bootbox.alert("esta activado");
            } else {
                bootbox.confirm({
                            message: "Esta Seguro que quiere Terminar la Creacion de la Entrada",
                            buttons: {
                                confirm: {
                                    label: 'Si',
                                    className: 'btn-success'
                                },
                                cancel: {
                                    label: 'No',
                                    className: 'btn-danger'
                                }
                            },
                            callback: function (result) {
                                if(result == true){
                                  /**/
                                  $.ajax({
                                      type: 'POST',
                                      url: urldispositivo,
                                      dataType: 'json',
                                      data: {
                                          csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                                          primary_key :primary_key
                                      },
                                      success: function (response) {
                                          bootbox.confirm("Entrada Cuadrada",
                                          function(result){
                                             location.reload();
                                            });
                                      },
                                      error: function (response) {
                                           var jsonResponse = JSON.parse(response.responseText);
                                           bootbox.alert(jsonResponse["mensaje"]);
                                      }
                                  });
                                  /**/

                                }
                            }
                          });
            }
        });


    }

}(window.AlertaEnCreacion = window.AlertaEnCreacion || {}, jQuery));

class EntradaUpdate {
    constructor() {
        let entrada_table = $('#entrada-table');
        var url_qr = $('#entrada-detalle-form').data("apiqr");
        this.api_url = entrada_table.data("api");
        this.pk = entrada_table.data("pk");
        this.url_filtrada = this.api_url + "?entrada=" + this.pk;
        this.tabla = entrada_table.DataTable({
            searching: false,
            paging: true,
            ordering: false,
            processing: true,
            ajax: {
                url: this.url_filtrada,
                dataSrc: '',
                cache: true,
                data: this.api_url
            },
            columns: [
                {data: "tdispositivo"},
                {data: "util"},
                {data: "repuesto"},
                {data: "desecho"},
                {data: "total"},
                {data: "precio_unitario"},
                {data: "precio_subtotal"},
                {data: "precio_descontado"},
                {data: "precio_total"},
                {data:"descripcion"},
                {data: "creado_por"},
                {
                    data: "",render: function(data, type, full, meta){
                      if(full.dispositivos_creados == true ){
                          if(full.usa_triage == "False"){
                            return "<a href="+full.update_url+" class='btn btn-info btn-editar'>Editar</a>";
                          }else{
                              return "";
                          }

                      }else{
                        return "<a href="+full.update_url+" class='btn btn-info btn-editar'>Editar</a>";
                      }
                    }
                },
                {
                    data: "", render: function(data, type, full, meta){
                      if(full.tipo_entrada != "Especial"){
                          if(full.dispositivos_creados == false){
                            if(full.usa_triage == "True"){
                              return "<button class='btn btn-primary btn-dispositivo'>Crear Disp</button>";
                            }else{
                              return "";
                            }
                          }else{
                              if(full.qr_dispositivo == true){
                                if(full.usa_triage == "True"){
                                    return "<a target='_blank' rel='noopener noreferrer' href="+full.dispositivo_list+" class='btn btn-success'>Listado Dispositivo</a>";
                                }else{
                                  return " ";
                                }

                              }else{
                                if(full.usa_triage == "True"){
                                    return "<a target='_blank' rel='noopener noreferrer' href="+full.dispositivo_qr+" class='btn btn-primary btn-Qrdispositivo'>QR Dispositivo</a>";
                                }else {
                                  return " ";
                                }
                            }
                          }
                      }else{
                        return "";
                      }

                    }
                },
                {
                    data: "", render: function(data, type, full, meta){
                      if(full.tipo_entrada != "Especial"){
                        if(full.repuestos_creados == false){
                          if(full.usa_triage == "True"){
                              return "<button class='btn btn-warning btn-repuesto'>Crear Rep</button>";
                          }else{
                            return " ";
                          }
                        }else{
                          if(full.qr_repuestos == true){
                            if(full.usa_triage=="True"){
                                  return "<a target='_blank' rel='noopener noreferrer' href="+full.repuesto_list+" class='btn btn-success'>Listado Repuestos</a>";
                            }else{
                              return " ";
                            }
                          }else{
                            if(full.usa_triage=="True"){
                                return "<a target='_blank' rel='noopener noreferrer' href="+full.repuesto_qr+" class='btn btn-primary btn-Qrepuesto'>QR Repuestos</a>";
                            }else{
                              return " ";
                            }                          
                          }
                        }
                      }else{
                        return "";
                      }
                    }
                },
            ]
        });

        let tablabody = $('#entrada-table tbody');
        let tabla_temp = this;

        tablabody.on('click', '.btn-editar', function () {
            let data_fila = this.tabla.row($(this).parents('tr')).data();
            location.href = data_fila.update_url;
        });

        tablabody.on('click', '.btn-Qrdispositivo', function () {
          let data_fila = tabla_temp.tabla.row($(this).parents('tr')).data();
        $.ajax({
              type: "POST",
              url: url_qr,
              dataType: 'json',
              data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                detalles_id:data_fila.id,
                tipo:"dispositivo"
              },
              success: function (response) {
                   location.reload();
                  console.log("Qr Dispositivos imprimidos");

              },
          });

        });

        tablabody.on('click', '.btn-Qrepuesto', function () {
          let data_fila = tabla_temp.tabla.row($(this).parents('tr')).data();
        $.ajax({
              type: "POST",
              url: url_qr,
              dataType: 'json',
              data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                detalles_id:data_fila.id,
                tipo:"repuestos"
              },
              success: function (response) {
                 location.reload();
                  console.log("Qr Repuestos imprimidos");

              },
          });

        });

        tablabody.on('click', '.btn-dispositivo', function () {
            let data_fila = tabla_temp.tabla.row($(this).parents('tr')).data();
            bootbox.confirm({
                        message: "Esta seguro que desea crear estos dispositivos",
                        buttons: {
                            confirm: {
                                label: 'Si',
                                className: 'btn-success'
                            },
                            cancel: {
                                label: 'No',
                                className: 'btn-danger'
                            }
                        },
                        callback: function (result) {
                            if(result == true){
                              /**/

                                let urldispositivo = tabla_temp.api_url + data_fila.id + "/crear_dispositivos/";
                                EntradaUpdate.crear_dispositivos(urldispositivo);
                            }
                        }
                      });


        });

        tablabody.on('click', '.btn-repuesto', function () {
            let data_fila = tabla_temp.tabla.row($(this).parents('tr')).data();
          bootbox.confirm({
                      message: "Esta seguro que desea crear estos repuestos",
                      buttons: {
                          confirm: {
                              label: 'Si',
                              className: 'btn-success'
                          },
                          cancel: {
                              label: 'No',
                              className: 'btn-danger'
                          }
                      },
                      callback: function (result) {
                          if(result == true){
                            /**/

                              let urldispositivo = tabla_temp.api_url + data_fila.id + "/crear_repuestos/";
                              EntradaUpdate.crear_repuestos(urldispositivo);
                          }
                      }
                    });

        });

        /** Uso de DRF**/
        let detalle_form = $('#detalleForm');
        detalle_form.submit(function (e) {
            e.preventDefault();

            $.ajax({
                type: "POST",
                url: detalle_form.attr('action'),
                data: detalle_form.serialize(),
                success: function (response) {
                    console.log("datos ingresados correctamente");
                    tabla_temp.tabla.ajax.reload();
                },
            });
            document.getElementById("detalleForm").reset();
        });
    }

    static crear_dispositivos(urldispositivo) {
        $.ajax({
            type: 'POST',
            url: urldispositivo,
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function (response) {
                console.log("dispositivos creados exitosamente");
                bootbox.confirm("dispositivos creados exitosamente!",
                function(result){
                   location.reload();
                  });
            },
            error: function (response) {
                alert( "Error al crear los dispositivo:" + response.mensaje);
            }
        });
    }

    static crear_repuestos(url_repuestos) {
        $.ajax({
            type: 'POST',
            url: url_repuestos,
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function (response) {
                console.log("repuestos creados exitosamente");
                bootbox.confirm("repuestos creados exitosamente!",
                function(result){
                   location.reload();
                  });

            },
            error: function (response) {
                alert( "Error al crear los Repuestos:" + response.mensaje);
            }

        });
    }
}

class EntradaDetail {
    constructor() {
        let entrada_table = $('#entrada-table');
        var pk = entrada_table.data("pk");
        this.api_url = entrada_table.data("api");
        this.pk = entrada_table.data("pk");
        this.url_filtrada = this.api_url + "?entrada=" + this.pk;
        this.tabla = entrada_table.DataTable({
            searching: false,
            paging: true,
            ordering: false,
            processing: true,
            ajax: {
                url: this.url_filtrada,
                dataSrc: '',
                cache: true,
                data: function (params)
                {
                   return {
                     entrada: pk
                   };
                }
            },
            columns: [
                {data: "tdispositivo"},
                {data: "util"},
                {data: "repuesto"},
                {data: "desecho"},
                {data: "total"},
                {data: "precio_unitario"},
                {data: "precio_subtotal"},
                {data: "precio_descontado"},
                {data: "precio_total"},
                {data:"descripcion"},
                {data: "creado_por"},
                {data:" ",render: function(data, type, full, meta){
                    return "<a target='_blank' rel='noopener noreferrer' href="+full.dispositivo_list+" class='btn btn-success'>Listado Dispositivo</a>";
                }},
                {data:" " ,render: function(data, type, full, meta){
                    return "<a target='_blank' rel='noopener noreferrer' href="+full.repuesto_list+" class='btn btn-primary'>Listado Repuestos</a>";
                }}

            ]
        });

        let tablabody = $('#entrada-table tbody');
        let tabla_temp = this;

        tablabody.on('click', '.btn-editar', function () {
            let data_fila = this.tabla.row($(this).parents('tr')).data();
            location.href = data_fila.update_url;
        });

        tablabody.on('click', '.btn-dispositivo', function () {
            let data_fila = tabla_temp.tabla.row($(this).parents('tr')).data();
            let urldispositivo = tabla_temp.api_url + data_fila.id + "/crear_dispositivos/";
            EntradaUpdate.crear_dispositivos(urldispositivo);
        });

        tablabody.on('click', '.btn-repuesto', function () {
            let data_fila = tabla_temp.tabla.row($(this).parents('tr')).data();
            let urldispositivo = tabla_temp.api_url + data_fila.id + "/crear_repuestos/";
            EntradaUpdate.crear_repuestos(urldispositivo);
        });

        /** Uso de DRF**/
        let detalle_form = $('#detalleForm');
        detalle_form.submit(function (e) {
            e.preventDefault();

            $.ajax({
                type: "POST",
                url: detalle_form.attr('action'),
                data: detalle_form.serialize(),
                success: function (response) {
                    console.log("datos ingresados correctamente");
                    tabla_temp.tabla.ajax.reload();
                },
            });
            document.getElementById("detalleForm").reset();
        });
    }

    static crear_dispositivos(urldispositivo) {
        $.ajax({
            type: 'POST',
            url: urldispositivo,
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function (response) {
                console.log("dispositivos creados exitosamente");
            },
            error: function (response) {
                alert( "Error al crear los dispositivo:" + response.mensaje);
            }
        });
    }

    static crear_repuestos(url_repuestos) {
        $.ajax({
            type: 'POST',
            url: url_repuestos,
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function (response) {
                console.log("repuestos creados exitosamente");
            },
            error: function (response) {
                alert( "Error al crear los Repuestos:" + response.mensaje);
            }

        });
    }
}


(function (EntradaList, $, undefined) {
    var tabla = $('#entrada2-table').DataTable({
        dom: 'lfrtipB',
        buttons: ['excel', 'pdf'],
        processing: true,
        ajax: {
            url: $('#entrada2-list-form').attr('action'),
            deferRender: true,
            dataSrc: '',
            cache: true,
            data: function () {
                return $('#entrada2-list-form').serializeObject(true);
            }
        },
        columns: [
            {data: "id"},
            {data: "tipo"},
            {data: "fecha", className: "nowrap"},
            {data: "en_creacion", className: "nowrap"},
            {data: "creada_por", className: "nowrap"},
            {data: "recibida_por", className: "nowrap"},
            {data: "proveedor", className: "nowrap"},
            {data: "urlSi", render: function(data, type, full, meta){
              if(full.en_creacion== "Si"){
                return "<a href="+data+" class='btn btn-block btn-success'>Abrir</a>";

              }else{
                return "<a href="+full.urlNo+" class='btn btn-block btn-success'>Abrir</a>";
              }

            }}
        ]


    }).on('xhr.dt', function (e, settings, json, xhr) {
        $('#spinner').hide();
    });

    EntradaList.init = function () {

        $('#spinner').hide();
        $('#entrada2-list-form').submit(function (e) {
            e.preventDefault();
            $('#spinner').show();
            tabla.clear().draw();
            tabla.ajax.reload();
        });

        $('#entrada2-table tbody').on('click', 'button', function () {
            var data = tabla.row($(this).parents('tr')).data();
            alert("Si funciona este boton");
            console.log(data.fecha);
            console.log(data.en_creacion);
        });

    }
}(window.EntradaList = window.EntradaList || {}, jQuery));

class EntradaDetalleDetail {
  constructor() {
       var validarDispositivos = $("#id_dispositivos_creados").val();
      var validarRepuestos = $("#id_repuestos_creados").val();
      if(validarDispositivos == "True"){
        document.getElementById("id_util").disabled = true;
      }
      if(validarRepuestos == "True"){
        document.getElementById("id_repuesto").disabled = true;
      }

  }
}

(function (SalidaDetalleList, $, undefined) {
    var valor = $('#salida-table').data("api");
    var pk = $('#salida-table').data("pk");
    var urlapi = valor + "?entrada=" + pk;
    var tabla = $('#salida-table').DataTable({
        searching: false,
        paging: true,
        ordering: false,
        processing: true,
        ajax: {
            url: urlapi,
            dataSrc: '',
            cache: true,
            data: function () {
                var cont = $('#salida-table').data("api");
                return cont;
            }
        },
        columns: [
            {data: "tdispositivo"},
            {data: "cantidad"},
            {data: "desecho"},
            {data: "entrada_detalle"},
        ]
    });

    SalidaDetalleList.init = function () {
        $('#btn-terminar').click(function () {
            bootbox.confirm({
                message: "¿Esta Seguro que quiere Terminara la Creacion de la Entrada?",
                buttons: {
                    confirm: {
                        label: 'Yes',
                        className: 'btn-success'
                    },
                    cancel: {
                        label: 'No',
                        className: 'btn-danger'
                    }
                },
                callback: function (result) {
                    if (result == true) {
                        document.getElementById("id_en_creacion").checked = false;
                        document.getElementById("desechosalida-form").submit();
                    }

                }
            });


        });

        /** Uso de DRF**/
        $('#detalleForm').submit(function (e) {
            e.preventDefault()
            $.ajax({
                type: "POST",
                url: $('#detalleForm').attr('action'),
                data: $('#detalleForm').serialize(),
                success: function (response) {
                    console.log("datos ingresados correctamente");

                },
            });
            tabla.clear().draw();
            tabla.ajax.reload();
            document.getElementById("detalleForm").reset();
        });
    }
}(window.SalidaDetalleList = window.SalidaDetalleList || {}, jQuery));


class SolicitudMovimientoUpdate {
    constructor() {
        this.sel_dispositivos = $('#id_dispositivos');
        let api_url = this.sel_dispositivos.data('api-url');
        let etapa_inicial = this.sel_dispositivos.data('etapa-inicial');
        let tipo_dipositivo = this.sel_dispositivos.data('tipo-dispositivo');
        let slug = this.sel_dispositivos.data('slug');

        this.sel_dispositivos.select2({
            debug: true,
            placeholder: "Ingrese los triage",
            ajax: {
                url: api_url,
                dataType: 'json',
                data: function (params) {
                    return {
                        search: params.term,
                        etapa: etapa_inicial,
                        tipo: tipo_dipositivo,
                        buscador: slug + "-" + params.term
                    };
                },
                processResults: function (data) {
                    return {
                        results: data.map(dispositivo => {
                            return {id: dispositivo["id"], text: dispositivo['triage']};
                        })
                    };
                },
                cache: true
            },
            width : '100%'
        });
    }
}

class SolicitudEstadoTipo {
  constructor() {
    /**Uso de tablas **/
    let paquete_tabla = $('#paquetes-table');
    let api_urlpaquete =$('#asignarDispositivo').data('urlpaquete');
    let salidapk = $('#asignarDispositivo').data('pk');
    let url_filtrada = api_urlpaquete + salidapk;
    var cambios_etapa =$('#asignarDispositivo').data('urlmovimiento');
    /****/
    this.asignarDispositivo = $('#asignarDispositivo');
    var tablaSignar = paquete_tabla.DataTable({
     processing:true,
     retrieve:true,
     ajax:{
       url:api_urlpaquete,
       dataSrc:'',
       cache:false,
       deferRender:true,
       processing: true,
       data: function () {
         return {
           salida: salidapk,
           tipo_dispositivo: $('#id_tipo').val(),
           aprobado:false
         }
       }
     },
     columns:[
       {data:"id",
          render: function(data, type, full, meta){
            return '<a href="'+full.urlPaquet+'">'+data+'</a>'

          }},
       {data:"tipo_paquete"},
       {data:"asignacion",render: function( data, type, full, meta ){
            for(var i = 0; i<(full.asignacion.length);i++){
                 var asignacionDispositivos = full.asignacion[i].dispositivo.triage;
           }

           if(asignacionDispositivos==undefined){
             asignacionDispositivos = "No cuenta con dispositivos";
           }
           return asignacionDispositivos;
         }},
       {data:"aprobado", render: function( data, type, full, meta){
        if(full.aprobado == true){
           return "Aprobado";
         }else{
           return "Pendiente"
         }
       }},
       {data:"id_paquete",
       render:function(data, type, full, name){
         return "<button id='buttonAsignar'"+"data-buttonSignar='"+full.id_paquete+"'class='btn btn-info btn-aprovar'>Aprovar</button>";
       }
      },
     ]
   });
   tablaSignar.on('click','.btn-aprovar', function () {
     let data_fila = tablaSignar.row($(this).parents('tr')).data();
     bootbox.confirm({
        message: "Esta Seguro de aprovar este paquete",
        buttons: {
            confirm: {
                label: 'Si',
                className: 'btn-success'
            },
            cancel: {
                label: 'No',
                className: 'btn-danger'
            }
        },
        callback: function (result) {
          if(result==true){
            $.ajax({
              type: "POST",
              url: cambios_etapa,
              data:{
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                paquete:data_fila.id_paquete
              },
              success: function (response){
                  bootbox.alert("Paquete y Dispositivos aprovados");
                  tablaSignar.clear().draw();
                  tablaSignar.ajax.reload();
              },
            });
          }

            console.log('This was logged in the callback: ' + result);
        }
      });

   });
    var api_url = this.asignarDispositivo.data('url');
    $('#id_tipo').change(function() {
      if($('#id_tipo').val()==""){
          $('#cuerpoPaquetes').css({"display":"none"});
      }else{
        /****/
        $('#cuerpoPaquetes').css({"display":"block"});
          var tipo = $(this).val();
          var urlDispositivo = api_url+"?buscador=&tipo="+tipo+"&estado=2&etapa=2&asignaciones=0";
          tablaSignar.clear().draw();
          tablaSignar.ajax.reload();
          $.ajax({
            url:urlDispositivo,
            dataType:'json',
            data:{
              format:'json'
            },
            error:function(){
              console.log("Error");
            },
            success:function(data){
                $('#id_dispositivo').empty();
                $('#id_dispositivo').append('<option value=""'+'>'+"---------"+'</option>');
                for (var i in data){
                  $('#id_dispositivo').append('<option value='+data[i].triage + '>'+data[i].triage+'</option>');
              }
             $('#id_dispositivo').val();
            },
            type: 'GET'
          }
        );
        /****/

      }

    });
    /***/
    let dispositivoPaqueteForm = $('#dispositivoPaqueteForm');
    let tipo = $('#id_tipo').val();
    dispositivoPaqueteForm.submit(function (e) {
      e.preventDefault();
      $.ajax({
        type: "POST",
        url: dispositivoPaqueteForm.attr('action'),
        data:dispositivoPaqueteForm.serialize(),
        success: function (response){
          bootbox.alert("Asignacion correctamente");
          tablaSignar.ajax.reload();
        },
      });
    });
    /***/
  }

}

class SalidasRevisarList {
  constructor() {
    /** Uso de tabla **/
    let revision_tabla = $('#salidasrevisar-table');
    let api_url_revision = $('#salidarevisionid').data('url');
    var tablaRevision = revision_tabla.DataTable({
      processing:true,
      retrieve:true,
      ajax:{
        url:api_url_revision,
        dataSrc:'',
        cache:false,
        deferRender:true,
        processing:true,
        data: function () {
          return {
            aprobada:false
          }
        }

      },
      columns:[
        {data:"id", render: function( data, type, full, meta){
          return '<a href="'+full.urlSalida+'">'+data+'</a>'
        }},
        {data:"fecha_revision", render: function(data, type, full, meta){
         var newDate = new Date(full.fecha_revision);
         var options = {year: 'numeric', month:'long', day:'numeric', hour:'numeric',minute:'numeric'};
          return newDate.toLocaleDateString("es-Es",options);
        }},
        {data:"salida"},
        {data:"revisado_por"}
      ]

    });
  }
}
class PaquetesRevisionList {
  constructor() {
    let  paquetes_revision_tabla = $('#salida-paquetes-revision');
    let api_paquetes_revision = $('#paquetes-revision').data('url');
    var api_paquete_salida= $('#paquetes-revision').data('id');
    let api_aprobar_salida=$('#aprobar-btn').data('url')
    var  tablaPaquetes = paquetes_revision_tabla.DataTable({
      processing:true,
      retrieve:true,
      ajax:{
        url:api_paquetes_revision,
        dataSrc:'',
        cache:false,
        deferRender:true,
        processing:true,
        data: function () {
          return {
            salida:api_paquete_salida,
            aprobado:true
          }
        }
      },
      columns:[
        {data:"id", render: function( data, type, full, meta){
          return '<a href="'+full.urlPaquet+'">'+data+'</a>'
        }},
        {data:"fecha_creacion", render: function(data, type, full, meta){
          var newDate = new Date(full.fecha_creacion);
          var options = {year: 'numeric', month:'long', day:'numeric', hour:'numeric',minute:'numeric'};
           return newDate.toLocaleDateString("es-Es",options);
        }},
        {data:"tipo_paquete"} ,
      ]

    });
    /** Boton de Historial **/
    var crear_historial_salidas = function(url, id_comentario, comentario){
      var data = {
        "id_comentario":id_comentario,
        "comentario":comentario
      }

      $.post(url, JSON.stringify(data)).then(function (response){
      var fecha = new Date(response.fecha);
      var td_data = $('<td></td>').text(fecha.getDate()+"/"+(fecha.getMonth()+1)+"/"+fecha.getFullYear()+","+response.usuario);
      var td = $('<td></td>').text(response.comentario);
      var tr = $('<tr></tr>').append(td).append(td_data);
      $('#body-salidas-' + id_comentario).append(tr);
    },function(response){
      alert("Error al crear datos");
    });
    }
    $(".SalidaHistorico-btn").click( function(){
      var id_comentario = $(this).data('id');
      var url = $(this).data('url');
      bootbox.prompt({
        title: "Historial de Ofertas",
        inputType: 'textarea',
        callback: function (result) {
          if (result) {
            crear_historial_salidas(url, id_comentario, result);
          }
        }
      });
    });
    /**Botones de  Aprobacion**/
    $("#rechazar-btn").click( function(){
      bootbox.confirm({
       message: "Esta salida sera rechazada",
       buttons: {
           confirm: {
               label: 'Si',
               className: 'btn-success'
           },
           cancel: {
               label: 'No',
               className: 'btn-danger'
           }
       },
       callback: function (result) {

           console.log('This was logged in the callback: ' + result);
       }
     });

    });
    $("#aprobar-btn").click( function(){
      bootbox.confirm({
       message: "Esta  seguro que desea aprobar esta salida?",
       buttons: {
           confirm: {
               label: 'Si',
               className: 'btn-success'
           },
           cancel: {
               label: 'No',
               className: 'btn-danger'
           }
       },
       callback: function (result) {
         if(result==true){
           $.ajax({
             type: "POST",
             url: api_aprobar_salida+api_paquete_salida+"/aprobado/",
             data:{
               csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
               salida:api_paquete_salida
             },
             success: function (response){
                 bootbox.alert("Dispositivos aprovados");
             },
           });
         }

           console.log('This was logged in the callback: ' + result);
       }
     });
    });


  }
}
class PaqueteDetail {
  constructor() {
    let tablabodyRechazar = $("#rechazar-dispositivo tbody tr");
    var urlCambio = $("#salida-id").data('url');
    tablabodyRechazar.on('click','.btn-rechazar', function () {
      let data_triage = $(this).attr("data-triage");
      let data_paquete=$(this).attr("data-paquete");
      bootbox.confirm({
         message: "Esta seguro de rechazar el dispositivo",
         buttons: {
             confirm: {
                 label: 'Si',
                 className: 'btn-success'
             },
             cancel: {
                 label: 'No',
                 className: 'btn-danger'
             }
         },
         callback: function (result) {
           if(result==true){
             $.ajax({
               type: "POST",
               url: urlCambio,
               data:{
                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                 triage:data_triage,
                 paquete:data_paquete
               },
               success: function (response){
                 var id_comentario = $("#salida-id").data('id');
                 var url = $("#salida-id").data('urlhistorico');
                 bootbox.prompt({
                   title: "Por que rechazo este dispositivo?",
                   inputType: 'textarea',
                   callback: function (result) {
                     if (result) {
                       crear_historial_salidas(url, id_comentario, result);
                     }
                   }
                 });
               },
             });
           }

             console.log('This was logged in the callback: ' + result);
         }
       });
    });
    /****/
    var crear_historial_salidas = function(url, id_comentario, comentario){
      var data = {
        "id_comentario":id_comentario,
        "comentario":"El Dispositivo con Triage: "+ $("#id-rechazar").data('triage')+" del paquete no: "+$("#id-rechazar").data('idpaquete') +" "+ comentario
      }

      $.post(url, JSON.stringify(data)).then(function (response){
      var fecha = new Date(response.fecha);
      var td_data = $('<td></td>').text(fecha.getDate()+"/"+(fecha.getMonth()+1)+"/"+fecha.getFullYear()+","+response.usuario);
      var td = $('<td></td>').text(response.comentario);
      var tr = $('<tr></tr>').append(td).append(td_data);
    $('#body-salidas-' + id_comentario).append(tr);

    },function(response){
      alert("Error al crear datos");
    });
    }
    /****/
  }
}
class RepuestosList {
  constructor() {
    var url_repuestos = $("#repuesto-list").attr('action');
    let repuesto_tabla = $("#repuesto-table");
    $("#id_tipo").change(function() {
      var tipo = $(this).val();
      var tabla = repuesto_tabla.DataTable({
        destroy:true,
        searching:true,
        paging:true,
        ordering:true,
        processing:true,
        ajax:{
          url:url_repuestos,
          dataSrc:'',
          cache:true,
          data: function() {
            return{
              tipo:tipo,
              estado:1
            }
          }
        },
        columns:[
          {data:"No"},
          {data:"tipo"},
          {data:"descripcion"},
          {data:"tarima"},
          {
                data: "",
                defaultContent: "<button  id='button-repuesto' class='btn btn-info repuesto-btn'>Asignar</button>"
            }
        ]
      });
      tabla.clear().draw();
      tabla.ajax.reload();
      var tablabodyRepuesto = $("#repuesto-table tbody");
      tabla.on('click','.repuesto-btn',function () {
        let repuesto = tabla.row($(this).parents('tr')).data();
        bootbox.prompt("Ingrese el Triage del Dispositivo", function(result){
            $.ajax({
             type: "POST",
             url:url_repuestos +"asignar_repuesto/",
             data:{
               csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
               repuesto:repuesto.id,
               triage:result
             },
             success:function (response){
               tabla.ajax.reload();
             }
           });
         });
      });
    });
   }
}
class DispositivoList {
  constructor() {

    $('#dispositivo-list-form').submit(function (e) {
        e.preventDefault();
        /**/
        var tablaDispositivos = $('#dispositivo-table').DataTable({
           dom: 'lfrtipB',
           destroy:true,
           buttons: ['excel', 'pdf'],
           processing: true,
           ajax: {
               url: $('#dispositivo-list-form').attr('action'),
               deferRender: true,
               dataSrc: '',
               cache: true,
               data: function () {
                   return $('#dispositivo-list-form').serializeObject(true);
               }
           },
           columns: [

               {data: "triage", render: function(data, type, full, meta){
                 return '<a href="'+full.url+'">'+data+'</a>'

               }},
               {data: "tipo", className: "nowrap"},
               {data: "marca", className: "nowrap"},
               {data: "modelo", className: "nowrap"},
               {data: "serie", className: "nowrap"},
               {data: "tarima", className: "nowrap"},
               {data: "estado", className: "nowrap"},
               {data: "etapa", className: "nowrap"}
           ]
              });
        /**/
        tablaDispositivos.clear().draw();
        tablaDispositivos.ajax.reload();


    });

  }
}
