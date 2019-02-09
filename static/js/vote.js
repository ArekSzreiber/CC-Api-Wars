$(document).ready(function() {

    let voteButtons = $(".voteButton");
    $(voteButtons).on('click', function(event) {
        let button = $(this);
        $.ajax({
            url: '/vote',
            data: {
                planet_name: button.data('planetName'),
                planet_id: button.data('planetId')
            },
            type: 'POST',
            success: function (response) {
                document.getElementById('errorModalLabel').textContent = response.header;
                document.getElementById('errorModalBody').textContent = response.body;
                $("#errorModal").modal('show');
            },
            error: function (error) {
                //console.log(error);
            }
        });
    });
});
