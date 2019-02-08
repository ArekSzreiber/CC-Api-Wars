
function makeTableRow(person) {
    let row = document.createElement('tr'),
        genderIcon;

    if (person.gender === 'male') {
        genderIcon = '<span class="genderIcon">&#9794;</span>';
    } else if (person.gender === 'female') {
        genderIcon = '<span class="genderIcon">&#9792;</span>';
    } else {
        genderIcon = 'N/A';
    }
    row.innerHTML = `
        <td>${person.name}</td>
        <td>${person.height/100}</td>
        <td>${person.mass}</td>
        <td>${person.hair_color}</td>
        <td>${person.skin_color}</td>
        <td>${person.eye_color}</td>
        <td>${person.birth_year}</td>
        <td>${genderIcon}</td>
    `;
    $('#residentsTableBody').append(row);
}


function makeTableBody(residentsURLs){
    $('#residentsTableBody').empty();
    residentsURLs.forEach(function(residentURL){
        $.get(residentURL, function(data){
            makeTableRow(data);
        });
    });
}
//todo zrobić głosowanie

let residentsModal = $('#residentsModal');
residentsModal.on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget); // Button that triggered the modal
    let planetUrl = button.data('planetUrl');

    let modal = $(this);
    modal.find('.modal-title').text('Residents of ' + button.data('planetName'));
    modal.find('.modal-body input').val(planetUrl);

    $.get(planetUrl, function(data){
        makeTableBody(data['residents']);
    }).fail(function(){
        console.log('Failure');
    });
});

residentsModal.on('hidden.bs.modal', function(){
    $("#residentsTable > tbody > tr").remove();
});
