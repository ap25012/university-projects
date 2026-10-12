
// Βρίσκουμε τα στοιχεία Χρησιμοποιώντας const για να φτιάξουμε σταθερές μεταβλητές που
// δεν θα αλλάξουν κατά την εκτέλεση στην συνέχεια
// Με το document.getElementById (DOM) συνδέουμε το Js αρχείο με το html αρχειο.

const btn = document.getElementById('btnkataxorisi');
const eidos = document.getElementById('titlosInput');
const etaireia = document.getElementById('etaireiaInput');


btn.onclick = function(event) {
// 1. Έλεγχος κενών πεδίων
    if (eidos.value.trim() === '' || etaireia.value.trim() === '') {
        alert('Παρακαλώ συμπληρώστε όλα τα πεδία!');
        return; // Σταματάει την εκτέλεση εδώ
    }


    // Με τη βοήθεια της σταθερής μεταβλητής (const), αντιστοιχούμε
    // τα δεδομένα στα αγγλικά ονόματα που καταλαβαίνει ο server.
    const neoproion = {
        title: eidos.value,
        brand: etaireia.value
    };

    // Στέλνουμε τα δεδομένα με τη μέθοδο POST
    fetch('https://dummyjson.com/products/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(neoproion) // Μετατροπή
    })
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Σφάλμα στην αποστολή');
            }
            return response.json();
        })
        .then(function(data) {
            // Εμφάνιση μηνύματος με alert
            alert(`Επιτυχής καταχώριση νέου προΪόντος.\nID: ${data.id}\nΕίδος: ${data.title}\nΕταιρεία: ${data.brand}`);

            eidos.value = '';
            etaireia.value = '';
        })
        .catch(function(error) {
            // Διαχείριση σφάλματος
            console.log(error);
            alert('Υπήρξε πρόβλημα κατά την αποστολή των δεδομένων.');
        });
};