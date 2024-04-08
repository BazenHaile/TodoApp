// Validate Email
function validateEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

// Validate Phone
function validatePhone(phone) {
    // This regex focuses on international formats and common separators
    const re = /^(\+\d{1,3}[-.\s]?)?(\(\d{1,3}\)|\d{1,3})[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$/;
    return re.test(String(phone).trim());
}


// Validate Name
function validateName(name) {
    return name.trim().length > 0;
}

// Form Submission
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("contactForm");
    form.addEventListener("submit", function(e) {
        const name = document.getElementById("name").value;
        const phone = document.getElementById("phone").value;
        const email = document.getElementById("email").value;

        let errorMessage = "";

        if (!validateName(name)) {
            errorMessage += "Invalid name.\n";
        }
        if (!validateEmail(email)) {
            errorMessage += "Invalid email address.\n";
        }
        if (!validatePhone(phone)) {
            errorMessage += "Invalid phone number.\n";
        }

        if (errorMessage.length > 0) {
            alert("Please correct the following errors:\n" + errorMessage);
            e.preventDefault(); // Prevent form from submitting
        }
    });
});



