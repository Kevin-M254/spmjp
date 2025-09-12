document.ready(function () {
  const HOST = "0.0.0.0:5001";
  const countries = {};
  const leagues = {};

  $('ul li input[type="checkbox"]').bind("change", (e) => {
    const el = e.target;
    let tt;
    switch (el.id) {
      case "country_filter":
	tt = countries;
	break;
      case "league_filter":
	tt = leagues;
	break;
    }
    if (el.checked) {
      tt[el.dataset.name] = el.dataset.id;
    } else {
      delete tt[el.dataset.name];
    }
    $(".leagues h4").text(
	Object.keys(Object.assign({}, countries, leagues)).sort().join(", "));
  });

  //API status
  $.getJSON("0.0.0.0:5001/api/v1/status/", (data) => {
    if (data.status === "OK") {
      $("div#api_status").addClass("available");
    } else {
      $("div#api_status").removeClass("available");
    }
  });

  // Fetch data about matches
  $.post({
    url: `${HOST}/api/v1/matches_search`,
    data: JSON.stringify({}),
    headers: {
      "Content-Type": "application/json",
    },
    success: (data) => {
	data.forEach((match) =>
	  $("section.matches").append(
		`<ARTICLE>
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
	      </ARTICLE>`
	  )
	);
    },
    dataType: "json",
  });

  // search matches
  $(".filters button").bind("click", fetchMatches);
  fetchMatches()
});
