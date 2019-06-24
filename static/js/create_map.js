var map_result = "";
        
$(document).ready( function() {
    // recorremos cuadrícula
    getMapResult();
});

$('#finish-map').on('click', function() {
    getMapResult();
});

// Deshabilitar seleccionar texto con valores del mapa
$('.create-map').attr('unselectable', 'on').css('user-select', 'none').on('selectstart dragstart', false);

var data_assign = "";
var badge_active = "";

$('.badge-button').on('click', function() {
    badge_active = this;
    $(this).addClass("highlighted");
    data_assign = $(this).attr("data-assign");
    removeDataAssign( data_assign );
});

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
}

function removeDataAssign( value ){
    $('.create-map td.' + value ).removeClass( value );
}