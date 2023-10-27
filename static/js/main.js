// Get the element where you want to display the day
const dayElement = document.getElementById("day");

// Function to update the current day
function updateCurrentDay() {
  // Get the current date
  const currentDate = new Date();

  // Format the day as a string
  const options = { weekday: 'long' };
  const formattedDay = currentDate.toLocaleDateString(undefined, options);

  // Update the content of the HTML element
  dayElement.textContent = formattedDay+',';
}

// Call the function to update the day immediately and then every day
updateCurrentDay();
setInterval(updateCurrentDay, 86400000); // Update every 24 hours (86400000 milliseconds)



const currYear = document.getElementById("currYear");

const date = new Date().getFullYear()

currYear.textContent = "@" + " " + date;


/*Toggle nav bar function */
const toggleBtn = document.querySelector('.toggle')
const toggleIcon = document.querySelector('.toggle i')
const toggleMenu = document.querySelector('.dropdown')

toggleBtn.onclick = function (){
    toggleMenu.classList.toggle('open')
    const isOpen = toggleMenu.classList.contains('open')

    toggleIcon.classList = isOpen
    ? 'fa fa-angle-double-right'
    : 'fa-solid fa-bars'
}


function toggleIconMenu() {
    var dropdownMenu = document.getElementById("dropdownMenu");
    dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
}