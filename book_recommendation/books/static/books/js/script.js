document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('search-form');
    const resultsContainer = document.getElementById('results');

    // Ensure form is defined
    if (!form) {
        console.error('Form element not found!');
        return;
    }

    form.addEventListener('submit', function (event) {
        event.preventDefault();  // Prevent default form submission

        const query = new URLSearchParams(new FormData(form)).toString();
        console.log('Query:', query);  // Log the query parameter

        fetch(`/api/search/?${query}`)
            .then(response => {
                console.log('Response Status:', response.status);  // Log the status code
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('Data:', data);  // Log the received data
                if (data.items && Array.isArray(data.items)) {
                    resultsContainer.innerHTML = data.items.map(book => `
                        <div class="book">
                            <h3>${book.volumeInfo.title}</h3>
                            <p><strong>Authors:</strong> ${book.volumeInfo.authors ? book.volumeInfo.authors.join(', ') : 'N/A'}</p>
                            <p><strong>Published Date:</strong> ${book.volumeInfo.publishedDate}</p>
                            <img src="${book.volumeInfo.imageLinks ? book.volumeInfo.imageLinks.thumbnail : 'https://via.placeholder.com/128x193'}" alt="${book.volumeInfo.title}" />
                            <p><a href="${book.volumeInfo.infoLink}" target="_blank">More Info</a></p>
                        </div>
                    `).join('');
                } else {
                    resultsContainer.innerHTML = '<p>No results found.</p>';
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                resultsContainer.innerHTML = '<p>An error occurred while fetching results.</p>';
            });
    });
});
