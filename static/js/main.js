/* 
|   Funciones necesarias para la vista de Resultado
*/

/* Variables */
var plain = "s-plain"
var forest = "s-forest"
var mountain = "s-mountain"
var water = "s-water"
var way = "s-way"
var start = "s-start"
var finish = "s-finish"

/* 
|   Cuando está cargada la vista con los datos que nos manda backend
*/
$(document).ready(function() {
    hiddenLoader(); // ocultamos el loader

    /* Recorremos los mapas para pintarlos */
    if( $('.wrapper-map .dataframe').length>0 ){
      $('.wrapper-map .dataframe').each(function(index) {

        var tabla = $(this);

        // recorremos hijos
        if( tabla.children("tbody").children().length>0) {
            tabla.children("tbody").children().each(function(index){
                
                var fila = $(this);

                // recorremos cuadrícula
                if( fila.children("td").length>0 ){
                    fila.children("td").each(function(index){

                        var cuadricula = $(this);
                        var value = this.innerText;
                        
                        if( value.includes('I') ){
                            cuadricula.addClass(start);
                        }
                        if( value.includes('F') ){
                            cuadricula.addClass(finish);
                        }

                        if( value.includes('X') ){
                            cuadricula.addClass(way);
                        }
                        
                        trozos = value.split("|");
                        value = trozos[trozos.length-1].trim();
                        this.innerHTML = "";

                        /* Dependiendo del valor, corresponde con una zona u otra */
                        switch( value ){
                            case "1": cuadricula.addClass(plain); this.innerText = ""; break;
                            case "2": cuadricula.addClass(forest); this.innerText = ""; break;
                            case "4": cuadricula.addClass(mountain); this.innerText = ""; break;
                            case "0": cuadricula.addClass(water); this.innerText = ""; break;
                        }

                    }); // each cuadricula
                }
            }); // each fila
        }
      }); // each tabla
    }
});

/* 
|   Código para mostrar el movimiento que se realiza en cada paso
*/
$(document).ready(function() {
    var icon = "";
    var value = "";

    if( $('.block-move').length>0 ){
        $('.block-move').each(function(index){
            value = $(this).attr("data-move");
            switch( value ){
                case '0': icon = '<i class="fas fa-arrow-left"></i>'; break;
                case '1': icon = '<i class="fas fa-arrow-right"></i>'; break;
                case '2': icon = '<i class="fas fa-arrow-up"></i>'; break;
                case '3': icon = '<i class="fas fa-arrow-down"></i>'; break;
            }
            //debugger;
            $(this).append( icon );

        });
    }
});

/* Detectamos cuando el usuario quiere ir al principio de la página */
$(".button-top").on('click', function(){
    $("html").animate({ scrollTop: 0 }, 'medium')
});


/*
|   Función para mostrar el loader
*/
function showLoader() {
    $('.wrapper-loader').removeClass("hidden");
    $('.wrapper-loader').addClass("show");
}

/*
|   Función para ocultar el loader
*/
function hiddenLoader() {
    $('.wrapper-loader').removeClass("show");
    $('.wrapper-loader').addClass("hidden");
}