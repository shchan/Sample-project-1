var $ = require('jquery');
$(function() {
  var searchForm = $('#search-form');
  var inputs = searchForm.find('input');

  /* set up datepickers for the search */
  // $('.datepicker').datepicker({
  //   orientation: "top auto"
  // });

  /* set up actions for submitting the search form */
  searchForm.on('submit', function(e) {
    e.preventDefault();
    keyValues = inputs.map(getKeyValue);
    urlParams = $.makeArray(keyValues).join('&');
    window.location.search = '?' + urlParams;
  })

  function getKeyValue(_, input) {
      return [input.id, input.value].join('=');
  }
});
