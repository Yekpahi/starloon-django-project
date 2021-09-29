"use strict";

function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _nonIterableSpread(); }

function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance"); }

function _iterableToArray(iter) { if (Symbol.iterator in Object(iter) || Object.prototype.toString.call(iter) === "[object Arguments]") return Array.from(iter); }

function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = new Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } }

/* 
this javascript is only to change the "actpage" attribut on the .cdp div
*/
window.onload = function () {
  var paginationPage = parseInt($('.cdp').attr('actpage'), 10);
  $('.cdp_i').on('click', function () {
    var go = $(this).attr('href').replace('#!', '');

    if (go === '+1') {
      paginationPage++;
    } else if (go === '-1') {
      paginationPage--;
    } else {
      paginationPage = parseInt(go, 10);
    }

    $('.cdp').attr('actpage', paginationPage);
  });
}; // Search Bar

/**
 * Fetches mock user data from an API. You can disregard this part
 * of the code.
 */


var USER_API = "https://randomuser.me/api";

var fetchUsers = function fetchUsers() {
  var results,
      response,
      body,
      _args = arguments;
  return regeneratorRuntime.async(function fetchUsers$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          results = _args.length > 0 && _args[0] !== undefined ? _args[0] : 100;
          _context.next = 3;
          return regeneratorRuntime.awrap(fetch("".concat(USER_API, "?results=").concat(results)));

        case 3:
          response = _context.sent;
          _context.next = 6;
          return regeneratorRuntime.awrap(response.json());

        case 6:
          body = _context.sent;
          return _context.abrupt("return", body.results);

        case 8:
        case "end":
          return _context.stop();
      }
    }
  });
}; // -------------------------------------------------------------
// Main logic
// -------------------------------------------------------------


var input = document.querySelector(".input");
var autoCompleteList = document.querySelector(".auto-complete-list");
/*
  The below expression is an IIFE, or an Immediately Invoked Function
  Expression. I use this because I needed to make an asynchronous call
  to fetch the mock user data.

  Because I'm using async/await instead of Promises and because Javascript
  doesn't support global async/await (not yet anyways), I need to wrap it in
  a set of parentheses before immediately invoking it.

  The signature of an IIFE looks like this:
  (() => { ... })()

  Where there is an anonymous function wrapped around a set of parentheses 
  and invoked by appending another set of parentheses after it.

  Optionally, the same thing can be achieved by doing:
  
  const main = async () => { <event listener logic goes here> }
  main()

  OR

  const main = () => {
    fetchUsers()
      .then(users => { 
        <event listener logic goes here> 
      })
  }
  main()
*/

(function _callee() {
  var users;
  return regeneratorRuntime.async(function _callee$(_context2) {
    while (1) {
      switch (_context2.prev = _context2.next) {
        case 0:
          _context2.next = 2;
          return regeneratorRuntime.awrap(fetchUsers());

        case 2:
          users = _context2.sent;
          // Manipulates the data to better suit my example's needs
          users = users.map(function (user) {
            return {
              name: user.name.first + " " + user.name.last,
              avatar: user.picture.thumbnail
            };
          }); // Adds an event listener that is invoked upon every keystroke

          input.addEventListener("input", function (e) {
            removeAllAutoCompleteListItems(); // Exit the function if there is no input

            if (!input.value) return;
            /*
              This process is for demonstration purposes only. It definitely
              isn't optimized. If you do use this code, you should consider
              the following optimizations:
              1. I'm deleting ALL autocomplete list item entries whenever a change
                 happens on the input field. I will explain why this is problematic
                 using the following example. 
                
                 Suppose the user wants to search for the username with the last name
                 "Thompson". The user currently has "Tho" typed in the input field.
                 Currently, the code will display all usernames containing "tho", which
                 includes any username with the last name "Thompson". 
                
                 Now, when the user types the next character, "m", all entries are 
                 deleted, including the entries where the username has the last name
                 "Thompson". Those same entries are then recreated.
                
                 This may or may not cause issues with performance.
                
                
              2. Currently, ALL matched usernames are displayed. This means if you were
                 to enter a really common character, such as "a" or "e", the majority
                 of usernames will be displayed in the list. It's recommended to set
                 a limit on how many items can be displayed at one time.
                
                
              Some other things I left out:
              - I didn't bold the matched characters. You can probably achieve this
                by altering the `createAutoCompleteListItem()` helper function to include
                <b> tags around the matched characters.
              - A user cannot use the arrow keys to select the autocomplete options.
            */

            users.forEach(function (user) {
              if (user.name.toLowerCase().includes(input.value.toLowerCase())) {
                var li = createAutoCompleteListItem(user);
                autoCompleteList.appendChild(li);
              }
            });
          });

        case 5:
        case "end":
          return _context2.stop();
      }
    }
  });
})(); // -------------------------------------------------------------
// Helper functions
// -------------------------------------------------------------

/**
 * Creates a new auto-complete list entry. The HTML for the constructed
 * element looks like this:
 *
 * @example
 * <li class="auto-complete-list__item">
 *     <span
 *           class="auto-complete-list__item__avatar"
 *           style="background-image: url(...);"
 *     />
 *     <span>John Smith</span>
 * </li>
 */


var createAutoCompleteListItem = function createAutoCompleteListItem(user) {
  var li = document.createElement("li");
  var avatar = document.createElement("span");
  var nameText = document.createElement("span");
  li.classList.add("auto-complete-list__item");
  avatar.classList.add("auto-complete-list__item__avatar");
  avatar.style.backgroundImage = "url(".concat(user.avatar, ")");
  nameText.innerHTML = user.name;
  li.appendChild(avatar);
  li.appendChild(nameText);
  return li;
};
/**
 * Resets the auto-complete form.
 */


var removeAllAutoCompleteListItems = function removeAllAutoCompleteListItems() {
  // The following syntax:
  // [...autoCompleteList.children] is using the spread operator.
  // I use this because `autoCompleteList.children` is an array-like
  // object, not an array.
  // I cannot use any array methods, such as `.forEach()`, on this
  // array-like object, so I have to convert it into an array first before
  // using `.forEach()`.
  // @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax
  _toConsumableArray(autoCompleteList.children).forEach(function (child) {
    autoCompleteList.removeChild(child);
  });
};