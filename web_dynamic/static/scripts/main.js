$(document).ready(function () {
  
  const HOST = '0.0.0.0';

  // Get api status
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
      $('.leagues h4').html('&nbsp;');
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

  // Obtain slected leagues
  const leagues = {};
  $('.leagues ul ul li input[type="checkbox"]').click(function () {
    if ($(this).is(":checked")) {
      leagues[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete leagues[$(this).attr('data-id')];
    }
    updateLeagues(countries, leagues);
  });

  // Display each match that matches the filters
  function search (filters = {}) {
    $.ajax({
      type: 'POST',
      url: `http://${HOST}:5001/api/v1/matches_search`,
      data: JSON.stringify(filters),
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {
	$('SECTION.matches').empty();
        $('SECTION.matches').append(data.map(match => {
          return `<ARTICLE>
                    <DIV class="jp_matches">
                      <p>${match.home_team}</p> - <p>${match.away_team}</p>
                       <DIV class="odds">
                         <p>${match.h_t_odds}</p><p>${match.x_odds}</p><p>${match.a_t_odds}</p>
                       </DIV>
                       <DIV class="results">
                         ${match.results}
                       </DIV>
		    </DIV>
                       <DIV class="information">
                         <UL>
                           <LI><DIV class="position"><p>Pos.</p>
                             <p>${match.h_t_pos}</p><p>${match.a_t_pos}</p>
                           </DIV></LI>
                           <LI><DIV class="win"><p>Won:</p>
                              <p>${match.h_t_win}</p><p>${match.a_t_win}</p>
                           </DIV></LI>
                           <LI><DIV class="draw"><p>Drawn:</p>
                              <p>${match.h_t_draw}</p><p>${match.a_t_draw}</p>
                           </DIV></LI>
                           <LI><DIV class="lost"><p>Lost:</p>
		              <p>${match.h_t_lose}</p><p>${match.a_t_lose}</p>
                           </DIV></LI>
                           <LI><DIV class="form"><p>Form:</p>
                              <p>${match.h_t_win_percent}%</p><p>${match.h_t_form}</p>
                              <p>${match.a_t_win_percent}%</p><p>${match.a_t_form}</p>
                           </DIV></LI>
                         </UL>
                       </DIV>
                  </ARTICLE>`
	}));
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

  // Display all matches
  search();
});
