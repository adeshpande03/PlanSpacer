// static/js/scripts.js

let friendCount = 1;

function initializeAutocomplete(id) {
  var input = document.getElementById(id);
  var autocomplete = new google.maps.places.Autocomplete(input);
}

document.addEventListener("DOMContentLoaded", function () {
  initializeAutocomplete("user_address");
  initializeAutocomplete("friend_addresses");

  document.getElementById("add_friend").addEventListener("click", function () {
    friendCount += 1;
    let input = document.createElement("input");
    input.type = "text";
    input.name = "friend_addresses";
    input.id = `friend_address_${friendCount}`;
    input.required = true;
    input.classList.add("autocomplete");
    document.forms[0].insertBefore(input, this);
    initializeAutocomplete(input.id); // Initialize autocomplete for the new input
  });
});
