$('document').ready(function () {
  const api = 'http://' + window.location.hostname;

  $.get(api + ':5001/api/v1/status/', function (response) {
    if (response.status === 'OK') {
      $('DIV#api_status').addClass('available');
    } else {
      $('DIV#api_status').removeClass('available');
    }
  });

  $.ajax({
    url: api + ':5001/api/v1/matches_search/',
    type: 'POST',
    data: '{}',
    contentType: 'application/json',
    dataType: 'json',
    success: appendMatches
  });

  let countries = {};
  $('.leagues > ul > h2 > input[type="checkbox"]').change(function () {
    if ($(this).is(':checked')) {
      countries[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete countries[$(this).attr('data-id')];
    }
    const lgs = Object.assign({}, countries, leagues);
    if (Object.values(lgs).length === 0) {
      $('.leagues h4').html(&nbsp);
    } else {
      $('.leagues h4').text(Object.values(lgs).join(', '));
    }
  });

  let leagues = {};
  $('.leagues > ul > ul > li input[type="checkbox"]').change(function () {
    if ($(this).is(':checked')) {
      leagues[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete leagues[$(this).attr('data-id')];
    }
    const lgs = Object.assign({}, countries, leagues);
    if (Object.values(lgs).length === 0) {
      $('.leagues h4').html('&nbsp');
    } else {
      $('.leagues h4').text(Object.values(lgs).join(', '));
    }
  });

  $('BUTTON').click(function () {
    $.ajax({
      url: api + ':5001/api/v1/matches_search/',
      type: 'POST',
      data: JSON.stringify({
	'countries': Object.keys(countries),
	'leagues': Object.keys(leagues)
      }),
      contentType: 'application/json',
      dataType: 'json',
      success: appendMatches
    });
  });

});

function appendMatches(data) {
  $('SECTION.matches').empty();
  $('SECTION.matches').append(data.map(match => {
    return `<ARTICLE>
	      <DIV class="jp_matches">
		  <p>${match.home_team}</p><p>${match.away_team}</p>
		  <DIV class="odds">
		    <p>${match.h_t_odds}</p><p>${match.x_odds}</p><p>${match.a_t_odds}</p>
		  </DIV>
		  <DIV class="results">
		    ${match.results}
	  	  </DIV>
	      <DIV class="information">
		  <UL>
		  <LI><DIV class="position">Pos.
		    <p>${match.h_t_pos}</p><p>${match.a_t_pos}</p>
		  </DIV></LI>
		  <LI><DIV class="win">Won:
	  	    <p>${match.h_t_win}</p><p>${match.a_t_win}</p>
		  </DIV></LI>
		  <LI><DIV class="draw">Drawn:
	  	    <p>${match.h_t_draw}</p><p>${match.a_t_draw}</p>
		  </DIV></LI>
		  <LI><DIV class="lost">Lost:
	  	    <p>${match.h_t_lose}</p><p>${match.a_t_lose}</p>
		  </DIV></LI>
		  <LI><DIV class="form">Form:
	  	    <p>${match.h_t_win_percent}%</p><p>${match.h_t_form}</p>
		    <p>${match.a_t_win_percent}%</p><p>${match.a_t_form}</p>
		  </DIV></LI>
		  </UL>
	      </DIV>
	    </ARTICLE>`;
  }));
}
