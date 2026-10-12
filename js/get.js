

// Βρίσκουμε τα στοιχεία Χρησιμοποιώντας const για να φτιάξουμε σταθερές μεταβλητές
// που δεν θα αλλάξουν κατά την εκτέλεση στην συνέχεια
// Με το document.getElementById (DOM) συνδέουμε το Js αρχείο με το html αρχειο.


const Btn = document.getElementById('fereproionta');
const dataCon = document.getElementById('apotelesmata');
const tBody = document.querySelector('#pinakasproionton tbody');
const prodselect = document.getElementById('epiloghproionton');

// Φτιάχνουμε μια κενή λίστα
let fetchedProducts = [];

Btn.onclick = function() {

    //  Σύνταξη
    fetch('https://dummyjson.com/products')
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            // Εμφανίζουμε και καθαρίζουμε τα παλιά δεδομένα
            dataCon.style.display = 'block';
            tBody.innerHTML = '';
            prodselect.innerHTML = '<option value="">Select ID</option>';

            // Αποθηκεύουμε τα προϊόντα
            fetchedProducts = data.products;

            // // Χρησιμοποιούμε const επειδή σε κάθε επανάληψη φτιάχνουμε μια ολοκαίνουργια γραμμή
            // και επιλογή που υπάρχουν μόνο σε αυτή την επανάληψη
            for (let product of fetchedProducts) {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${product.id}</td>
                    <td>${product.title}</td>
                    <td>${product.description}</td>
                    <td>${product.price}</td>
                `;
                tBody.appendChild(row);

                const option = document.createElement('option');
                option.value = product.id;
                option.textContent = product.id;
                prodselect.appendChild(option);
            }
        })
        .catch(function(error) {
            console.log(error);
            alert('Αποτυχία φόρτωσης δεδομένων.');
        });
};

// Αντίστοιχα, χρησιμοποιούμε .onchange για το dropdown μενού και Βάζουμε const γιατί κάθε φορά που αλλάζει η επιλογή,
// ξανά τρέχει από την αρχή, βρίσκει νέο ID για το νέο προϊόν, και μετά εξαφανίζεται
prodselect.onchange = function(event) {
    const selectedId = event.target.value;

    if (!selectedId) return;

    // Ψάχνουμε στα προϊόντα με βάσει το ID
    let product = null;
    for (let p of fetchedProducts) {
        if (p.id == selectedId) {
            product = p;
            break; // Μόλις το βρούμε, σταματάμε το ψάξιμο
        }
    }
// Εμφάνιση μηνύματος με Alert
    if (product) {
        alert(`ID: ${product.id}\nΤίτλος: ${product.title}\nΠεριγραφή: ${product.description}\nΤιμή: ${product.price}`);
    }
};