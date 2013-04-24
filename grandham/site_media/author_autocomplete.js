$(document).ready(function () {
  $("#author").autocomplete(
     '/ajax/author/autocomplete/',
     {multiple: true, multipleSeparator: ' '}
  );
});
