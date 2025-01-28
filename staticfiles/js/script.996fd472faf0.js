document.addEventListener("DOMContentLoaded", function () {
    if (!sessionStorage.getItem("introShown")) {
      setTimeout(function () {
        document.getElementById("intro-overlay").style.opacity = "0";
        setTimeout(function () {
          document.getElementById("intro-overlay").style.display = "none";
        }, 1000);
      }, 2500);
      sessionStorage.setItem("introShown", "true");
    } else {
      document.getElementById("intro-overlay").style.display = "none";
    }
  });


function toggleSearch() {
    const searchInput = document.getElementById('searchInput');
    const closeSearchButton = document.getElementById('closeSearch');
    if (searchInput.style.display === 'none') {
        searchInput.style.display = 'block';
        closeSearchButton.style.display = 'block';
        searchInput.focus();
    } else {
        searchInput.style.display = 'none';
        closeSearchButton.style.display = 'none';
        searchInput.value = '';
        searchTable(); // Reset the table when search is hidden
    }
}


function searchTable() {
    const input = document.getElementById('searchInput');
    const filter = input.value.toLowerCase();
    const table = document.querySelector('table tbody');
    const rows = table.querySelectorAll('tr');

    rows.forEach(row => {
        const itemName = row.querySelector('.item-name').textContent.toLowerCase();
        if (itemName.includes(filter)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

function sortTable(column) {
    const table = document.querySelector('table tbody');
    const rows = Array.from(table.querySelectorAll('tr')).filter(row => !row.querySelector('th'));

    rows.sort((a, b) => {
        const aCell = a.querySelector(`.${column}`);
        const bCell = b.querySelector(`.${column}`);

        if (!aCell || !bCell) {
            return 0;
        }

        const aText = aCell.textContent.trim();
        const bText = bCell.textContent.trim();

        if (column === 'expiry_date') {
            
            const [aDay, aMonth, aYear] = aText.split('/');
            const [bDay, bMonth, bYear] = bText.split('/');
            const aDate = new Date(aYear, aMonth - 1, aDay);
            const bDate = new Date(bYear, bMonth - 1, bDay);
            
            return aDate - bDate;
        } else if (column === 'category') {
            return aText.localeCompare(bText);
        }
    });

    rows.forEach(row => table.appendChild(row));
}




    document.addEventListener('DOMContentLoaded', function() {
        const itemLinks = document.querySelectorAll('.item-link');
        const modalBody = document.querySelector('#itemModal .modal-body');
        const modalTitle = document.querySelector('#itemModalLabel');

        itemLinks.forEach(link => {
            link.addEventListener('click', function() {
                const itemId = this.dataset.itemId;

                // Clear previous modal content
                modalBody.innerHTML = '<p>Loading...</p>';

                // Fetch item details via AJAX
                fetch(`/items/${itemId}/details/`)
                    .then(response => response.json())
                    .then(data => {
                        modalTitle.textContent = data.name;
                        modalBody.innerHTML = `
                            <p><strong>Quantity:</strong> ${data.quantity}${data.unit}</p>
                            <p><strong>Category:</strong> ${data.category}</p>
                            <p><strong>Expiry Date:</strong> ${data.expiry_date}</p>
                            
                        `;
                    })
                    .catch(error => {
                        console.error('Error fetching item details:', error);
                    });

                // Show the modal
                const itemModal = new bootstrap.Modal(document.getElementById('itemModal'));
                itemModal.show();

                // Add event listener to hide the modal and remove the backdrop
                itemModal._element.addEventListener('hidden.bs.modal', function () {
                    document.querySelector('.modal-backdrop').remove();
                });
            });
        });
    });
    const messages = document.querySelectorAll('.fade-message');

    // Loop through each message and add a fade-out effect after 3 seconds
    messages.forEach((message) => {
        setTimeout(() => {
            message.style.transition = "opacity 1s";
            message.style.opacity = 0;
        }, 3000); // 3000ms = 3 seconds

        // Optional: Remove the message from the DOM after the fade-out
        setTimeout(() => {
            message.remove();
        }, 4000); // 4000ms = 1 second after fade-out starts
    });