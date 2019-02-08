$(document).ready(function() {

    let voteButtons = $(".voteButton");
    $(voteButtons).on('click', function(event) {
        let button = $(event.relatedTarget);
        console.log(button);
        $.ajax({
            url: '/vote',
            data: {
                planet_name: button.data('planetName')
            },
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        }).done(function (data){
            console.log('asdsa');
        });
    });
});
