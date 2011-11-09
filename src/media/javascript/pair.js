$(document).ready(function() {

    $('.pair_times').bind("click", function() {
        var old_value = $(this).text();
        var old_value_int = parseInt(old_value);
        $(this).text("" + (++old_value_int));
        $.get('/update_times/' + $(this).attr('id'),  function(data) {
        });
        return false
    })

})