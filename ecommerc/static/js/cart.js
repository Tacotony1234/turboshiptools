// This function would be triggered when adding an item to the cart.
function addToCart(productId) {
    fetch('/add_to_cart/' + productId + '/')
      .then(response => response.json())
      .then(data => {
        if(data.total_items) {
          // If the item was successfully added, update the total items in the cart.
          updateCartTotal(data.total_items);
  
          // Display the message to the user.
          displayMessage('Item was added');
        }
      })
      .catch(error => console.error('Error:', error));
  }
  
  // Function to update the cart total items (you may need to implement this).
  function updateCartTotal(totalItems) {
    // Update the DOM with the new total items count.
  }
  
  // Function to display a message to the user.
  function displayMessage(message) {
    // Create a message element.
    let messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageElement.className = 'cart-message'; // Add a class for styling.
  
    // Append the message element to the body or another container element.
    document.body.appendChild(messageElement);
  
    // Optionally, remove the message after a few seconds.
    setTimeout(() => {
      messageElement.remove();
    }, 3000); // 3 seconds
  }
  
  // Make sure to add appropriate CSS for the '.cart-message' class.
  