$(document).ready(function () {
  
  const HOST = '0.0.0.0';

  //API status
  $.get(`http://${HOST}:5001/api/v1/status/`, data => {
    if (data.status == "OK") {
      $('DIV#api_status').addClass("available");
    } else {
      $('DIV#api_status').removeClass("available");
    }
  });

  // Update h4 tag with selected leagues
  function updateLeagues(countries, leagues) {
    const lgs = Object.assign({}, countries, leagues);
    if (Object.values(lgs).length === 0) {
      $('.leagues h4').html('$nbsp;');
    } else {
      $('.leagues h4').text(Object.values(lgs).join(', '));
    }
  }

  // Obtain selected countries
  const countries = {};
  $('.leagues ul h2 input[type="checkbox"]').click(function () {
    if ($(this).is(":checked")) {
      countries[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete countries[$(this).attr('data-id')];
    }
    updateLeagues(countries, leagues);
  });

  // Obtain selected leagues
  const leagues = {};
  $('.leagues ul ul li input[type="checkbox"]').click(function () {
    if ($(this).is(":checked")) {
      leagues[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete leagues[$(this).attr('data-id')];
    }
  });

  function search (filters = {}) {
    $.ajax({
      type: 'POST',
      url: `http://${HOST}:5001/api/v1/matches_search`,
      data: JSON.stringify(filters),
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {
	$('SECTION.matches').empty();
      }
    });
  };

  // Search event with selected filters
  $('#search').click(function () {
    const filters = {
      'countries': Object.keys(countries),
      'leagues': Object.keys(leagues)
    };
    search(filters);
  });
});
