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

document.addEventListener('DOMContentLoaded', function() {
  const calendarDays = document.getElementById('calendarDays');
  const currentWeek = document.getElementById('currentWeek');
  const prevWeekButton = document.getElementById('prevWeek');
  const nextWeekButton = document.getElementById('nextWeek');

  let currentDate = new Date();

  function renderWeek(date) {
      calendarDays.innerHTML = '';
      const startOfWeek = getStartOfWeek(date);
      const endOfWeek = new Date(startOfWeek);
      endOfWeek.setDate(endOfWeek.getDate() + 6);

      currentWeek.textContent = `${formatDate(startOfWeek)} - ${formatDate(endOfWeek)}`;

      for (let i = 0; i < 7; i++) {
          const dayCell = document.createElement('div');
          dayCell.classList.add('day');
          const currentDay = new Date(startOfWeek);
          currentDay.setDate(currentDay.getDate() + i);
          dayCell.textContent = currentDay.getDate();

          // Add events for the current day
          events.forEach(event => {
            const eventDate = new Date(event.start_date);
            const adjustedDay = new Date(currentDay);
            adjustedDay.setDate(adjustedDay.getDate() - 1);
            if (eventDate.toDateString() === adjustedDay.toDateString()) {
                const eventDiv = document.createElement('div');
                eventDiv.classList.add('event');

                const titleDiv = document.createElement('div');
                titleDiv.classList.add('event-title');
                titleDiv.textContent = event.title;

                const nameDiv = document.createElement('div');
                nameDiv.classList.add('event-name');
                nameDiv.textContent = event.name;

                const descriptionDiv = document.createElement('div');
                descriptionDiv.classList.add('event-description');
                descriptionDiv.textContent = event.description;

                const startTime12Hour = convertTo12Hour(event.start_time);
                const timeDiv = document.createElement('div');
                timeDiv.classList.add('event-time');
                timeDiv.textContent = "Starts at " + startTime12Hour;


                eventDiv.appendChild(titleDiv);
                eventDiv.appendChild(nameDiv);
                eventDiv.appendChild(descriptionDiv);
                eventDiv.appendChild(timeDiv);
                
                
                if (event.end_time){
                    const startTime12Hour = convertTo12Hour(event.end_time);
                    const end_timeDiv = document.createElement('div');
                    end_timeDiv.classList.add('event-time');
                    end_timeDiv.textContent = "Ends at " + startTime12Hour;
                    eventDiv.appendChild(end_timeDiv);
                }

                if (event.category){
                    const capitalizedCategory = event.category.split(' ')
                        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
                        .join(', ');
                    const tagsDiv = document.createElement('div');
                    tagsDiv.classList.add('event-tags');
                    tagsDiv.textContent = "Tags : " + capitalizedCategory;
                    eventDiv.appendChild(tagsDiv);
                }
                dayCell.appendChild(eventDiv);
            }
        });

          calendarDays.appendChild(dayCell);
      }
  }

  function convertTo12Hour(time) {
    const [hours, minutes] = time.split(':');
    let period = 'AM';
    let hour = parseInt(hours);

    if (hour >= 12) {
        period = 'PM';
        if (hour > 12) {
            hour -= 12;
        }
    }
    if (hour === 0) {
        hour = 12;
    }

    return `${hour}:${minutes} ${period}`;
}

  function getStartOfWeek(date) {
      const day = date.getDay();
      const diff = date.getDate() - day;
      const startOfWeek = new Date(date);
      startOfWeek.setDate(diff);
      return startOfWeek;
  }

  function formatDate(date) {
      return date.toLocaleDateString('en-US', {
          month: 'short',
          day: 'numeric',
          year: 'numeric'
      });
  }

  function changeWeek(offset) {
      currentDate.setDate(currentDate.getDate() + offset * 7);
      renderWeek(currentDate);
  }

  prevWeekButton.addEventListener('click', function() {
      changeWeek(-1);
  });

  nextWeekButton.addEventListener('click', function() {
      changeWeek(1);
  });

  renderWeek(currentDate);
});