document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search-input");
    const movieContainer = document.getElementById("movie-container");
    let initialContent = null;

    // Save initial content on page load
    if (movieContainer) {
        initialContent = movieContainer.innerHTML;
    }

    function performSearch() {
        const query = searchInput.value.trim();

        if (!query) {
            if (initialContent) {
                movieContainer.innerHTML = initialContent;
            }
            return;
        }

        fetch(`/movies/search/?query=${encodeURIComponent(query)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                movieContainer.innerHTML = '';
                
                if (data.results.length === 0) {
                    movieContainer.innerHTML = '<p class="no-results">No movies found</p>';
                    return;
                }

                data.results.forEach(movie => {
                    const card = createMovieCard(movie);
                    movieContainer.appendChild(card);
                });
            })
            .catch(error => {
                console.error('Search error:', error);
                movieContainer.innerHTML = '<p class="error">Error performing search</p>';
            });
    }

    function createMovieCard(movie) {
        const card = document.createElement('div');
        card.className = 'movie-card';
        card.innerHTML = `
            <a href="/movies/${movie.id}/">
                <img src="${movie.imgPath}" alt="${movie.name}">
                <h3>${movie.name}</h3>
                <p class="duration">${movie.duration} min</p>
                <p class="rating">User Rating: ${movie.user_rating}</p>
            </a>
        `;
        return card;
    }

    if (searchInput) {
        let debounceTimer;
        searchInput.addEventListener('input', () => {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(performSearch, 300);
        });
    }
});