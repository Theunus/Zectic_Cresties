// Get the elements
const sidebar = document.getElementById('sidebar');
const menuBtn = document.getElementById('menu-btn');
const mainContent = document.getElementById('main-content');

// Toggle sidebar visibility on button click
menuBtn.addEventListener('click', function() {
    if (sidebar.style.left === '0px') {
        sidebar.style.left = '-250px';  // Hide the sidebar
        mainContent.style.marginLeft = '0';  // Adjust main content
    } else {
        sidebar.style.left = '0';  // Show the sidebar
        mainContent.style.marginLeft = '250px';  // Push the main content to the right
    }
});
