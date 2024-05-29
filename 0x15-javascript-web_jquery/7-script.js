$(document).ready(function() {
    const char = $('#character');
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
      dataType: 'json',
      success: function(data) {
        char.text(data.name);
      },
    
    });
  });