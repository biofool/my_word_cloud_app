const searchInput = document.getElementById('search-input');
const searchResults = document.getElementById('search-results');

// Function to filter quotes based on the entered keyword
function filterQuotes(keyword) {
  return quotes.filter((quote) => {
    if (quote.keywords && Array.isArray(quote.keywords)) {
      return quote.keywords.some((kw) => kw.toLowerCase().includes(keyword.toLowerCase()));
    }
    return false; // If keywords are not defined or not an array
  });
}

// Function to display the filtered quotes as search results

function displayResults(filteredQuotes) {
    let resultsHTML = '';
    filteredQuotes.forEach((quote, index) => {
        const activeClass = index === 0 ? 'active' : '';  // Make the first quote active
        resultsHTML += `<div class="carousel-item ${activeClass}">
                          <p><strong>${quote.author || "Morihei Ueshiba"}:</strong> ${quote.text}</p>
                        </div>`;
    });
    searchResults.innerHTML = resultsHTML;
}
// Event listener
// for input field
searchInput.addEventListener('input', (event) => {
  const keyword = event.target.value.trim();

  if (keyword.length === 0) {
    searchResults.innerHTML = ''; // Clear results when input is empty
  } else {
    const filteredQuotes = filterQuotes(keyword);
    displayResults(filteredQuotes);
  }
});
