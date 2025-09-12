$(document).ready(init);

const HOST = '0.0.0.0';
const matchObj = {};

function init () {
  apiStatus();
  fetchMatches();
}

function apiStatus () {
  const API_URL = `http://${HOST}:5001/api/v1/status/`;
  $.get(API_URL, (data, textStatus) => {
    if (textStatus === 'success' && data.status === 'OK') {
      $('#api_status').addClass('available');
    } else {
      $('#api_status').removeClass('available');
    }
  });
}

function fetchMatches () {
  const MATCHES_URL = `http://${HOST}:5001/api/v1/matches_search`;
  $.ajax({
    url: MATCHES_URL,
    type: 'POST',
    headers: { 'Content-Type': 'application/json' },
    data: JSON.stringify({ matches: Object.values(matchObj) }),
    success: function (response) {
      $('SECTION.matches').empty();
      for (const r of response) {
        const article = ['<article>',
	'<div class="jp_matches">',
	`<p>${r.home_team}</p> - <p>${r.away_team}</p>`,
	`<div class="odds">`,
	`<p>${r.h_t_odds}</p> <p>${r.x_odds}</p> <p>${r.a_t_odds}</p>`,
	'</div>',
	'<div class="results">',
	`${r.results}`,
	'</div>',
	'</div>',
	'<div class="information">',
	'<ul>',
	`<li><div class="position">Pos.<p>${r.h_t_pos}</p>`,
	`<p>${r.a_t_pos}</p></div></li>`,
	`<li><div class="win">Won:<p>${r.h_t_win}</p>`,
	`<p>${r.a_t_win}</p></div></li>`,
	`<li><div class="draw">Drawn:<p>${r.h_t_draw}</p>`,
	`<p>${r.a_t_draw}</p></div></li>`,
	`<li><div class="lost">Lost:<p>${r.h_t_lose}</p>`,
	`<p>${r.a_t_lose}</p></div></li>`
	`<li><div class="form">Form:<p>${r.h_t_win_percent}`,
	`${r.h_t_form}</p><p>${r.a_t_win_percent}${r.a_t_form}`,
	'</p></div></li>',
	'</ul>',
	'</div>',
	'</article>'];
	$('SECTION.places').append(article.join(''));
      }
    },
    error: function (error) {
      console.log(error);
    }
  });
}
