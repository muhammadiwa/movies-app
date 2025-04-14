document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search-input")
    const movieContainer = document.getElementById("movie-container")
  
    // Function to perform search
    function performSearch() {
      const query = searchInput.value.trim()
  
      // Make AJAX request to search endpoint
      fetch(`/search/?query=${encodeURIComponent(query)}`)
        .then((response) => response.json())
        .then((data) => {
          // Clear current movies
          movieContainer.innerHTML = ""
  
          // If no results found
          if (data.results.length === 0) {
            movieContainer.innerHTML = '<div class="no-results">No movies found</div>'
            return
          }
  
          // Add each movie to the container
          data.results.forEach((movie) => {
            const movieCard = createMovieCard(movie)
            movieContainer.appendChild(movieCard)
          })
        })
        .catch((error) => {
          console.error("Error:", error)
          movieContainer.innerHTML = '<div class="no-results">An error occurred while searching</div>'
        })
    }
  
    // Function to create a movie card element
    function createMovieCard(movie) {
      const card = document.createElement("div")
      card.className = "movie-card"
  
      card.innerHTML = `
        <a href="/movie/${movie.id}/">
          <img src="${movie.imgPath}" alt="${movie.name}">
          <h3>${movie.name}</h3>
          <p class="duration">${movie.duration} min</p>
          <p class="rating">User Rating: ${movie.user_rating}</p>
        </a>
      `
  
      return card
    }
  
    // Event listeners
    searchInput.addEventListener("keyup", (event) => {
      if (event.key === "Enter") {
        performSearch()
      }
  
      // Real-time search as user types (with small delay)
      clearTimeout(searchInput.timer)
      searchInput.timer = setTimeout(performSearch, 300)
    })
  })
  