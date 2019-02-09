$(document).ready(function() {

    let voteButtons = $(".voteButton");
    $(voteButtons).on('click', function(event) {
        let button = $(this);
        console.log(button);
        console.log(button.data('planetName'));
        $.ajax({
            url: '/vote',
            data: {
                planet_name: button.data('planetName'),
                planet_id: button.data('planetId')
            },
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        }).done(function (data){
            console.log(data);
        });
    });
});
