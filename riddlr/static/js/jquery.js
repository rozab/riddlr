var url = $( '#selection-form' ).attr( 'action' );
$("selection-button").click(function(e) {
    e.preventDefault();
    $.ajax({
        type: "GET",
        url: url,
        data: {
            id: $('#sort').val();
        },
        success: function(result) {
            alert('ok');
        },
        error: function(result) {
            alert('error');
        }
    });
});