/* Add color to table */
var plain = "s-plain"
var forest = "s-forest"
var mountain = "s-mountain"
var water = "s-water"
var way = "s-way"

$(document).ready(function() {
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

                        switch( this.innerText ){
                            case "1": cuadricula.addClass(plain); this.innerText = ""; break;
                            case "2": cuadricula.addClass(forest); this.innerText = ""; break;
                            case "4": cuadricula.addClass(mountain); this.innerText = ""; break;
                            case "0": cuadricula.addClass(water); this.innerText = ""; break;
                            case "X": cuadricula.addClass(way); this.innerHTML = ""; 
                        }
                        

                    }); // each cuadricula
                }
            }); // each fila
        }
      }); // each tabla
    }
});