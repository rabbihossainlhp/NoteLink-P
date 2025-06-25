document.addEventListener("DOMContentLoaded", function () {
    // Toastr Configuration
    toastr.options = {
        "closeButton": true,
        "progressBar": true,
        "positionClass": "toast-top-right",
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };

    // Get Django messages from the hidden script tag
    let messagesElement = document.getElementById("django-messages");
    if (messagesElement) {
        let messages = JSON.parse(messagesElement.textContent);

        messages.forEach(msg => {
            toastr[msg.tags](msg.message);
        });
    }
});