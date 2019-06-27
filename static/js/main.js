/* Add color to table */
var plain = "s-plain"
var forest = "s-forest"
var mountain = "s-mountain"
var water = "s-water"
var way = "s-way"
var start = "s-start"
var finish = "s-finish"

$(document).ready(function() {
    hiddenLoader();
    var showChar = 700;
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
                       // this.innerHTML = "";

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

$(".button-top").on('click', function(){
    $("html").animate({ scrollTop: 0 }, 'medium')
});


function showLoader() {
    $('.wrapper-loader').removeClass("hidden");
    $('.wrapper-loader').addClass("show");
}
function hiddenLoader() {
    $('.wrapper-loader').removeClass("show");
    $('.wrapper-loader').addClass("hidden");
}