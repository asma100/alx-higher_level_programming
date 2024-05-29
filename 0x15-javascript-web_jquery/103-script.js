$(document).ready(function() {
    function fetchHello() {
      const langCode = $('#language_code').val();
      const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode;
  
      $.get(apiUrl, function(data) {
        $('#hello').text(data.hello);
      });
    }
  
    $('#btn_translate').click(function() {
      fetchHello();
    });
  
    $('#language_code').keypress(function(event) {
      if (event.which === 13) { // Enter key pressed
        fetchHello();
      }
    });
  });
  