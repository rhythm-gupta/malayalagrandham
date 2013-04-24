$(document).ready(function () {
  $("#title").autocomplete(
     '/ajax/title/autocomplete/',
     {multiple: true, multipleSeparator: ' '}
  );
});
