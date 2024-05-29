$(document).ready(function() {
    const list_movies = $('#list_movies');
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      dataType: 'json',
      success: function(data) {
       $.each(data.results, function(i,move){
        list_movies.append ('<li>'+move.title+'</li>')
       })
      },
    
    });
  });