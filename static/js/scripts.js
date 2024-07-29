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
    document.getElementById("friend_addresses_container").appendChild(input);
    initializeAutocomplete(input.id);
  });

  document
    .getElementById("delete_friend")
    .addEventListener("click", function () {
      if (friendCount > 1) {
        let friendContainer = document.getElementById(
          "friend_addresses_container"
        );
        friendContainer.removeChild(friendContainer.lastElementChild);
        friendCount -= 1;
      }
    });
});
