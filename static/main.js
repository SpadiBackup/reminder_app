// Example: Add an onclick event to a button with id "myButton"
document.addEventListener('DOMContentLoaded', function() {
    // Menu toggle
    document.getElementById('add_button').onclick = function() {
        const menu = document.getElementById('add_reminder_menu');
        if (menu.classList.contains('active')) {
            // Start hide animation
            menu.classList.add('hiding');
            // Wait for animation (e.g., 300ms), then remove 'active' and 'hiding'
            setTimeout(() => {
                menu.classList.remove('active', 'hiding');
            }, 300); // Adjust 300 to your animation duration
        } else {
            menu.classList.add('active');
        }
    };

    // Footer hide/show
    const footer = document.getElementById('footer');
    const closeBtn = document.getElementById('close_button');

    closeBtn.onclick = function() {
        if (!footer.classList.contains('hiding')) {
            // Hide with animation
            footer.classList.add('hiding');
            setTimeout(() => {}, 300);
        } else {
            // Show again
            footer.classList.remove('hiding');
            footer.classList.add('active');
        }
    };
});
