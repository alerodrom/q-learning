/* 
|   Funciones necesarias para la vista de Crear Mapa 
*/

/* Variables */
var map_result = "";

var init_x = 0;
var init_y = 0;
var end_x = 0;
var end_y = 0;

var y = 0;
var x = 0;


/* Al cargar la página cambiamos el label y obtenemos el mapa por defecto */
$(document).ready( function() {
    if( $('#form-create-map p label').length>0 ){
        $('#form-create-map p label')[0].innerText = "Pon nombre al mapa";
    }
    getMapResult();

});

/* Detectamos cuando el usuario termina la creación del mapa */
$('#finish-map').on('click', function() {
    getMapResult();
    $('#form-create-map').submit();
});

// Deshabilitar seleccionar texto con valores del mapa
$('.create-map').attr('unselectable', 'on').css('user-select', 'none').on('selectstart dragstart', false);

var data_assign = "";
var badge_active = "";

/* Detectamos cuando el usuario quiere a añadir la casilla de inicio o fin */
$('.badge-button').on('click', function() {
    badge_active = this;
    $(this).addClass("highlighted");
    data_assign = $(this).attr("data-assign");
    removeDataAssign( data_assign );
});

/* Detectamos los cambios sobre el mapa para pintar las distintas zonas */
$('.create-map td').on('click', function() {
    var cuadricula = $(this);

    if( data_assign==""){
        var value = this.innerText;

        switch( value ){
            case "1": cuadricula.removeClass(plain); cuadricula.addClass(forest); this.innerHTML = 2; break;
            case "2": cuadricula.removeClass(forest); cuadricula.addClass(mountain); this.innerHTML = 4; break;
            case "4": cuadricula.removeClass(mountain); cuadricula.addClass(water); this.innerHTML = 0; break;
            case "0": cuadricula.removeClass(water); cuadricula.addClass(plain); this.innerHTML = 1; break;
        }
    }else{
        cuadricula.addClass( data_assign );
        data_assign = "";
        $(badge_active).removeClass( "highlighted");
    }
});

/* 
|   Función que transforma el mapa visual a una cadena de texto,
|   esta cadena de texto se envía (junto con otros parámetros) al
|   controlador de backend
*/
function getMapResult() {
    map_result = "";

    if( $('.create-map td').length>0 ){
        $('.create-map td').each(function(index){
            var cuadricula = $(this);
            var value = this.innerText;

            switch( value ){
                case "1": cuadricula.addClass(plain); break;
                case "2": cuadricula.addClass(forest); break;
                case "4": cuadricula.addClass(mountain); break;
                case "0": cuadricula.addClass(water); break;
            }

            map_result += value + ","
        });
    }

    if(map_result != ""){
        $("#id_path").val( map_result.substring(0, map_result.length - 1) );
        getPositionsStartFinish();
    }
}




/* 
|   Función que transforma las posiciones visuales (inicio y fin)
|   a las coordenadas necesarias en el controlador
*/
function getPositionsStartFinish() {
    if( $('.create-map').length>0 ){
        $('.create-map').each(function(index) {
  
          var tabla = $(this);
  
          // recorremos hijos
          if( tabla.children("tbody").children().length>0) {
              y = 0;

              tabla.children("tbody").children().each(function(index){
                  
                  var fila = $(this);
                    

                  // recorremos cuadrícula
                  if( fila.children("td").length>0 ){
                      x = 0;
                      fila.children("td").each(function(index){
                        
                          var cuadricula = $(this);
                          if( cuadricula.hasClass('s-finish') ){
                            end_x = x;
                            end_y = y;
                          }
                          if( cuadricula.hasClass('s-start') ){
                            init_x = x;
                            init_y = y;
                          }

                            // posición x
                            x++;
  
                      }); // each cuadricula

                      // posición y
                      y++;
                  }
              }); // each fila
          }
        }); // each tabla

        $("#id_pos_init_x").val( init_x );
        $("#id_pos_init_y").val( init_y );

        $("#id_pos_end_x").val( end_x );
        $("#id_pos_end_y").val( end_y );

      }
}

/* 
|   Función que elimina del mapa la casilla inicial o final 
|   antes de colocar el nuevo valor
*/
function removeDataAssign( value ){
    $('.create-map td.' + value ).removeClass( value );
}