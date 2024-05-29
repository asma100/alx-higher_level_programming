$(document).ready(function() {
    var header = $('header');
    $('#update_header').click(function() {
      // Update the text content of the header
      header.text('New Header!!!');
    });
});