/* 
this javascript is only to change the "actpage" attribut on the .cdp div
*/

window.onload = function(){
    var paginationPage = parseInt($('.cdp').attr('actpage'), 10);
    $('.cdp_i').on('click', function(){
      var go = $(this).attr('href').replace('#!', '');
      if (go === '+1') {
        paginationPage++;
      } else if (go === '-1') {
        paginationPage--;
      }else{
        paginationPage = parseInt(go, 10);
      }
      $('.cdp').attr('actpage', paginationPage);
    });
  };

  

  // Search Bar
/**
 * Fetches mock user data from an API. You can disregard this part
 * of the code.
 */
 const USER_API = "https://randomuser.me/api";
 const fetchUsers = async (results = 100) => {
   const response = await fetch(`${USER_API}?results=${results}`);
   const body = await response.json();
   return body.results;
 };
 
 // -------------------------------------------------------------
 // Main logic
 // -------------------------------------------------------------
 
 const input = document.querySelector(".input");
 const autoCompleteList = document.querySelector(".auto-complete-list");
 
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
 (async () => {
   // Fetches mock user data
   let users = await fetchUsers();
 
   // Manipulates the data to better suit my example's needs
   users = users.map((user) => ({
     name: user.name.first + " " + user.name.last,
     avatar: user.picture.thumbnail
   }));
 
   // Adds an event listener that is invoked upon every keystroke
   input.addEventListener("input", (e) => {
     removeAllAutoCompleteListItems();
 
     // Exit the function if there is no input
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
     users.forEach((user) => {
       if (user.name.toLowerCase().includes(input.value.toLowerCase())) {
         const li = createAutoCompleteListItem(user);
         autoCompleteList.appendChild(li);
       }
     });
   });
 })();
 
 // -------------------------------------------------------------
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
 const createAutoCompleteListItem = (user) => {
   const li = document.createElement("li");
   const avatar = document.createElement("span");
   const nameText = document.createElement("span");
 
   li.classList.add("auto-complete-list__item");
   avatar.classList.add("auto-complete-list__item__avatar");
 
   avatar.style.backgroundImage = `url(${user.avatar})`;
   nameText.innerHTML = user.name;
 
   li.appendChild(avatar);
   li.appendChild(nameText);
 
   return li;
 };
 
 /**
  * Resets the auto-complete form.
  */
 const removeAllAutoCompleteListItems = () => {
   // The following syntax:
   // [...autoCompleteList.children] is using the spread operator.
   // I use this because `autoCompleteList.children` is an array-like
   // object, not an array.
 
   // I cannot use any array methods, such as `.forEach()`, on this
   // array-like object, so I have to convert it into an array first before
   // using `.forEach()`.
 
   // @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax
   [...autoCompleteList.children].forEach((child) => {
     autoCompleteList.removeChild(child);
   });
 };
 