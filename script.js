window.onload = function() {
    const maintenant = new Date().getTime(); 
    const dernierAffichage = localStorage.getItem('dernierAffichage'); 

    if (!dernierAffichage || (maintenant - dernierAffichage) >= 10 * 60 * 1000) { 
        document.getElementById('passwordModal').style.display = 'block';
        document.body.classList.add('no-scroll'); 
        localStorage.setItem('dernierAffichage', maintenant);
    }
}

function closeModal() {
    document.getElementById('passwordModal').style.display = 'none';
    document.body.classList.remove('no-scroll');
}

function checkPassword() {
    const password = document.getElementById('passwordInput').value;
    if (password === '1234') { 
        closeModal();
    } else {
        window.location.href = '/404.html';
    }
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('passwordInput').addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            checkPassword();
        }
    });
});