


CREATE TABLE ΓΡΑΜΜΑΤΕΙΑ (
    Username VARCHAR(20) NOT NULL PRIMARY KEY,
    Password VARCHAR(20) NOT NULL,
    Όνομα VARCHAR(40) NOT NULL,
    Επώνυμο VARCHAR(40) NOT NULL
);

CREATE TABLE ΚΑΘΗΓΗΤΗΣ (
    Κωδικός_καθ VARCHAR(10) NOT NULL PRIMARY KEY,
    Όνομα VARCHAR(40),
    Επώνυμο VARCHAR(40),
    Email VARCHAR(40) UNIQUE,
    Βαθμίδα VARCHAR(30),
    Username_Γραμ VARCHAR(20) NOT NULL
);


CREATE TABLE ΦΟΙΤΗΤΗΣ (
    ΑΜ_φοιτητή VARCHAR(15) NOT NULL PRIMARY KEY,
    Όνομα VARCHAR(40),
    Επώνυμο VARCHAR(40),
    Email VARCHAR(40) UNIQUE,
    Διεύθυνση VARCHAR(45),
    Έτος_εισ INT NOT NULL,
    Username_Γραμ VARCHAR(20) NOT NULL
);


CREATE TABLE ΜΑΘΗΜΑ (
    Κωδικός_μαθ VARCHAR(6) NOT NULL PRIMARY KEY,
    Τίτλος VARCHAR(40) NOT NULL,
    ECTS DECIMAL(3,1) NOT NULL,
    Εξεταστική_περ VARCHAR(40) NOT NULL,
    Τύπος VARCHAR(30) NOT NULL,
    Κωδικός_καθ VARCHAR(10) NOT NULL
);


CREATE TABLE ΔΗΛΩΣΗ_ΜΑΘ (
    Κωδικός_δήλ INT NOT NULL PRIMARY KEY,
    ΑΜ_φοιτητή VARCHAR(15) NOT NULL,
    Κωδικός_μαθ VARCHAR(6) NOT NULL,
    Ημερομηνία DATE,
    Εξεταστική_περ VARCHAR(40) NOT NULL
);


CREATE TABLE ΒΑΘΜΟΛΟΓΙΑ (
    ΑΜ_φοιτητή VARCHAR(15) NOT NULL,
    Κωδικός_μαθ VARCHAR(6) NOT NULL,
    Εξεταστική_περ VARCHAR(40) NOT NULL,
    Βαθμός DECIMAL(3, 1) NOT NULL,
    PRIMARY KEY (ΑΜ_φοιτητή, Κωδικός_μαθ, Εξεταστική_περ)
);


--Θα χρησιμοποιήσω την εντολή ALTER TABLE για να προσθέσω τα Ξένα Κλειδία και να γίνει η σύνδεση των πινάκων.


-- Σύνδεση Καθηγητή με Γραμματεία

ALTER TABLE ΚΑΘΗΓΗΤΗΣ
ADD CONSTRAINT fk_kathig_grammateia
FOREIGN KEY (Username_Γραμ) REFERENCES ΓΡΑΜΜΑΤΕΙΑ(Username);


-- Σύνδεση Φοιτητή με Γραμματεία

ALTER TABLE ΦΟΙΤΗΤΗΣ
ADD CONSTRAINT fk_foititis_grammateia
FOREIGN KEY (Username_Γραμ) REFERENCES ΓΡΑΜΜΑΤΕΙΑ(Username);


--Σύνδεση Μάθημα με Καθηγητή

ALTER TABLE ΜΑΘΗΜΑ
ADD CONSTRAINT fk_mathima_kathig
FOREIGN KEY (Κωδικός_καθ) REFERENCES ΚΑΘΗΓΗΤΗΣ(Κωδικός_καθ);



-- Σύνδεση Μάθημα Φοιτητή Βαθμολογία (πολλά προς Πολλά)


ALTER TABLE ΔΗΛΩΣΗ_ΜΑΘ
ADD CONSTRAINT fk_dilosi_foititis
FOREIGN KEY (ΑΜ_φοιτητή) REFERENCES ΦΟΙΤΗΤΗΣ(ΑΜ_φοιτητή);



ALTER TABLE ΔΗΛΩΣΗ_ΜΑΘ
ADD CONSTRAINT fk_dilosi_mathima
FOREIGN KEY (Κωδικός_μαθ) REFERENCES ΜΑΘΗΜΑ(Κωδικός_μαθ);



ALTER TABLE ΒΑΘΜΟΛΟΓΙΑ
ADD CONSTRAINT fk_vathmos_foititis
FOREIGN KEY (ΑΜ_φοιτητή) REFERENCES ΦΟΙΤΗΤΗΣ(ΑΜ_φοιτητή);


-- Για το Μάθημα στη Βαθμολογία
ALTER TABLE ΒΑΘΜΟΛΟΓΙΑ
ADD CONSTRAINT fk_vathmos_mathima
FOREIGN KEY (Κωδικός_μαθ) REFERENCES ΜΑΘΗΜΑ(Κωδικός_μαθ);



--Θα χρησιμοποιήσω την εντολή ALTER TABLE για να προσθέσω τους περιορισμούς μου.

--Περιορισμός Βαθμού

ALTER TABLE ΒΑΘΜΟΛΟΓΙΑ
ADD CONSTRAINT check_vathmos
CHECK (Βαθμός >= 0 AND Βαθμός <= 10);

--Περιορισμός Μονάδων

ALTER TABLE ΜΑΘΗΜΑ
ADD CONSTRAINT check_ects
CHECK (ECTS > 0 AND ECTS <=12);

--Περιορισμός Περιόδου


ALTER TABLE ΜΑΘΗΜΑ
ADD CONSTRAINT check_periodos
CHECK (Εξεταστική_περ IN ('Χειμερινή', 'Καλοκαιρινή', 'Επαναληπτική'));

-- Το ίδιο και για τη Βαθμολογία
ALTER TABLE ΒΑΘΜΟΛΟΓΙΑ
ADD CONSTRAINT check_periodos_vathmos
CHECK (Εξεταστική_περ IN ('Χειμερινή', 'Καλοκαιρινή', 'Επαναληπτική'));


--Περιορισμός Τύπου Μαθήματος

ALTER TABLE ΜΑΘΗΜΑ
ADD CONSTRAINT check_typos
CHECK (Τύπος IN ('Υποχρεωτικό', 'Επιλογής'));

--Περιορισμός Βαθμίδας


ALTER TABLE ΚΑΘΗΓΗΤΗΣ
ADD CONSTRAINT check_vathmida
CHECK (Βαθμίδα IN ('Καθηγητής', 'Αναπληρωτής', 'Επίκουρος', 'Λέκτορας', 'ΔΕΠ'));


--Περιορισμός Εισαγωγής

ALTER TABLE ΦΟΙΤΗΤΗΣ
ADD CONSTRAINT check_etos
CHECK (Έτος_εισ >= 1980 AND Έτος_εισ <= 2026);  -- Για τον επόμενο Χρόνο(2027) πρέπει να ενημερωθεί ο περιορισμός.

--Περιορισμός Email

ALTER TABLE ΚΑΘΗΓΗΤΗΣ
ADD CONSTRAINT check_email_kathigitis
CHECK (Email LIKE '%@%');



ALTER TABLE ΦΟΙΤΗΤΗΣ
ADD CONSTRAINT check_email_foititis
CHECK (Email LIKE '%@%');