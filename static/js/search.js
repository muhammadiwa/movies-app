document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search-input");
    const movieContainer = document.getElementById("movie-container");

    // Function to perform search
    function performSearch() {
        const query = searchInput.value.trim();

        // If the query is empty, reset the movie list
        if (!query) {
            resetMovieList();
            return;
        }

        // Make AJAX request to the search endpoint
        fetch(`/movies/search/?query=${encodeURIComponent(query)}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then((data) => {
                // Clear current movies
                movieContainer.innerHTML = "";

                // If no results found
                if (data.results.length === 0) {
                    movieContainer.innerHTML = '<div class="no-results">No movies found</div>';
                    return;
                }

                // Add each movie to the container
                data.results.forEach((movie) => {
                    const movieCard = createMovieCard(movie);
                    movieContainer.appendChild(movieCard);
                });
            })
            .catch((error) => {
                console.error("Error:", error);
                movieContainer.innerHTML = '<div class="no-results">An error occurred while searching</div>';
            });
    }

    // Function to reset the movie list to its original state
    function resetMovieList() {
        fetch(`/movies/`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text();
            })
            .then((html) => {
                // Parse the HTML and extract the movie container content
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, "text/html");
                const originalMovies = doc.getElementById("movie-container").innerHTML;
                movieContainer.innerHTML = originalMovies;
            })
            .catch((error) => {
                console.error("Error resetting movie list:", error);
            });
    }

    // Function to create a movie card element
    function createMovieCard(movie) {
        const card = document.createElement("div");
        card.className = "movie-card";

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

    // Event listeners
    searchInput.addEventListener("keyup", (event) => {
        if (event.key === "Enter") {
            performSearch();
        }

        // Real-time search as user types (with small delay)
        clearTimeout(searchInput.timer);
        searchInput.timer = setTimeout(performSearch, 300);
    });
});