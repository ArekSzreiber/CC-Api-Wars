$('#residentsModal').on('show.bs.modal', function (event) {
  let button = $(event.relatedTarget); // Button that triggered the modal
  let planetName = button.data('planetName'); // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  let modal = $(this);
  console.log(button);
  modal.find('.modal-title').text('Residents of ' + planetName);
  modal.find('.modal-body input').val(planetName);
});
