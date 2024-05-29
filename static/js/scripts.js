/*!
* Start Bootstrap - Heroic Features v5.0.6 (https://startbootstrap.com/template/heroic-features)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-heroic-features/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
// When the user scrolls the page, execute myFunction
const cards = document.querySelectorAll('.card');

function toggleVisibility() {
  cards.forEach((card) => {
    const rect = card.getBoundingClientRect();
    const isVisible = rect.top < window.innerHeight && rect.bottom >= 0;
    if (isVisible) {
      card.classList.add('visible');
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
      card.classList.remove('visible');
    }
  });
}

// Initial check
toggleVisibility();

// Listen for scroll events
window.addEventListener('scroll', toggleVisibility);


function updateProfile() {
  var dropdown = document.getElementById("dropdown");
  var selectedValue = dropdown.value;

  if (selectedValue === "") {
      alert("Please select a major.");
      return false;
  }

  // Here, you would update your database with the selected value
  // For example, using fetch to send data to the server
  fetch('update_profile_endpoint', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ major: selectedValue })
  })
  .then(response => response.json())
  .then(data => {
      console.log('Success:', data);
      // Optionally, you can save the selected value in localStorage to simulate database persistence for this example
      localStorage.setItem('selectedMajor', selectedValue);
  })
  .catch((error) => {
      console.error('Error:', error);
  });

  return false; // Prevent form submission for this example
}

window.onload = function() {
  // On page load, check if there's a saved major and set it as selected
  var savedMajor = localStorage.getItem('selectedMajor');
  if (savedMajor) {
      document.getElementById("dropdown").value = savedMajor;
  }
};