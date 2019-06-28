/* 
|   Funciones necesarias para la vista de Crear Problema 
*/

/* Detectamos cuando el usuario quiere resolver el problema */
$('#resolve-map').on('click', function() {
    showLoader();
    $('#create-problem').submit();
})

/* Detectamos la selección de mapa */
$('.wrapper-map').on('click', function(){
    $("#id_map_related").val( $(this).attr("data-map-id") );
    $(".dataframe.selected").removeClass("selected");
    $(this).children(".dataframe").addClass("selected");
});