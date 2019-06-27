$('#resolve-map').on('click', function() {
    showLoader();
    $('#create-problem').submit();
})

$('.wrapper-map').on('click', function(){
    $("#id_map_related").val( $(this).attr("data-map-id") );
    $(".dataframe.selected").removeClass("selected");
    $(this).children(".dataframe").addClass("selected");
});