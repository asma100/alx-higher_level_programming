$(document).ready(function() {
    $('#btn_translate').click(function() {
      const langCode = $('#language_code').val();
      const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode;
  
      $.get(apiUrl, function(data) {
        $('#hello').text(data.hello);
      });
    });
  });
  
  