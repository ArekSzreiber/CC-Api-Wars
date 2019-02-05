
function makeTableRow(person){
    let row = document.createElement('tr');
    row.innerHTML = `
        <td>${person.name}</td>
        <td>${person.height/100}</td>
        <td>${person.mass}</td>
        <td>${person.hair_color}</td>
        <td>${person.skin_color}</td>
        <td>${person.eye_color}</td>
        <td>${person.birth_year}</td>
        <td>${person.gender}</td>
    `;
    $('#residentsTableBody').append(row);
}


function makeTableBody(residentsURLs){
    $('#residentsTableBody').empty();
    for(let residentURL of residentsURLs){
        let person = new XMLHttpRequest();
        person.onreadystatechange = function(){
            if(person.readyState === 4){
                makeTableRow(JSON.parse(person.response))
            }
        };
        person.open("GET", residentURL, true);
        person.send();
    }
}


let residentsModal = $('#residentsModal')
residentsModal.on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget); // Button that triggered the modal
    let planetUrl = button.data('planetUrl'); // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    let modal = $(this);
    modal.find('.modal-title').text('Residents of ' + button.data('planetName'));
    modal.find('.modal-body input').val(planetUrl);

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(){
        if(xhr.readyState === 4){
            let planet = JSON.parse(xhr.response);
            makeTableBody(planet['residents']);
            $("#residentsTable").innerHTML = planet;
        }
    };
    xhr.open("GET", planetUrl, true);
    xhr.send();
});

residentsModal.on('hidden.bs.modal', function(){
    $("#residentsTable > tbody > tr").remove();
});
