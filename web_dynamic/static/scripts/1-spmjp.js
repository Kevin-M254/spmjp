$(document).ready(function () {
  const countries = [];
  $('input:checkbox').click(function () {
    if ($(this).is(":checked")) {
      countries.push($(this).attr('data-name'));
    } else {
      const nameIndex = countries.indexOf($(this).attr('data-name'));
      countries.splice(nameIndex, 1);
    }
    $('.leagues h4').text(countries.join(', '));
  });
});
