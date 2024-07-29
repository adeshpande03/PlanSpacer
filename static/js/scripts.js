let friendCount = 1;


function initializeAutocomplete(id) {
  let input = document.getElementById(id);
  let autocomplete = new google.maps.places.Autocomplete(input);

  // Observer to apply styles dynamically
  let observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      if (mutation.addedNodes.length) {
        mutation.addedNodes.forEach(function (node) {
          if (node.className.includes("pac-item")) {
            node.style.backgroundColor = "#fff"; // Example style
          }
        });
      }
    });
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true,
  });
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
    input.className = "input friend-input";
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
