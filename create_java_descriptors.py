#!/usr/bin/env python3
import json

# Creo il descriptor report completo con TUTTI i 18 descriptor
report = {
    "course_name": "Java - Programmazione Orientata agli Oggetti",
    "version": "2.0 - Enhanced with OOP Theory",
    "last_updated": "2025-11-14",
    "total_descriptors": 18,
    "focus_areas": ["OOP Principles", "Design Patterns", "Best Practices", "Comparison with C"],
    "coverage": {
        "chapters_analyzed": 10,
        "main_chapters": [
            "00_classi_oggetti_ereditarieta",
            "01_stream_buffer",
            "02_interfacce_classi_astratte",
            "03_eccezioni",
            "04_arraylist",
            "05_interfacce_grafiche",
            "06_model_view_controller",
            "07_lambda_expressions"
        ],
        "pages_covered": "280-300 estimated",
        "oop_focus": True,
        "design_patterns_covered": ["MVC", "Observer", "Singleton", "Factory"]
    },
    "concept_descriptors": [],
    "theoretical_explanations": {
        "oop_principles": {
            "explanation": "La Programmazione Orientata agli Oggetti (OOP) è un paradigma di programmazione che organizza il software in oggetti che contengono dati (attributi) e codice (metodi). Java è un linguaggio fortemente orientato agli oggetti dove quasi tutto è un oggetto (eccetto tipi primitivi).",
            "pillars": [
                {
                    "name": "Astrazione",
                    "description": "Capacità di concentrarsi sugli aspetti essenziali ignorando dettagli irrilevanti",
                    "java_implementation": "Classi astratte (abstract class) e interfacce (interface)"
                },
                {
                    "name": "Incapsulamento",
                    "description": "Meccanismo che lega dati e metodi e nasconde dettagli implementativi",
                    "java_implementation": "Attributi private con metodi public getter/setter"
                },
                {
                    "name": "Ereditarietà",
                    "description": "Permette a una classe di acquisire proprietà di un'altra classe",
                    "java_implementation": "Parola chiave 'extends' per ereditarietà singola"
                },
                {
                    "name": "Polimorfismo",
                    "description": "Capacità di oggetti di classi diverse di rispondere allo stesso messaggio",
                    "java_implementation": "Override di metodi + binding dinamico"
                }
            ]
        }
    }
}

# Lista di tutti i descriptor completi (18 in totale)
descriptors = [
    # 1. JAVA-OOP-001: Classi e Oggetti
    {
        "concept_id": "JAVA-OOP-001",
        "topic": "Classi e Oggetti - Fondamenti OOP",
        "category": "Object-Oriented Programming",
        "difficulty_level": "beginner",
        "explanation": "Una CLASSE è un modello (blueprint) che definisce attributi e metodi. Un OGGETTO è un'istanza concreta creata con 'new'. L'incapsulamento protegge i dati con modificatori di accesso (private, public, protected). La parola 'this' riferisce l'istanza corrente.",
        "code_example": """// Classe modello per Studente
public class Studente {
    private String matricola;
    private String nome;
    private double media;

    public Studente(String matricola, String nome, double media) {
        this.matricola = matricola;
        this.nome = nome;
        this.media = media;
    }

    public double getMedia() { return media; }
    public void setMedia(double m) {
        if (m >= 0.0 && m <= 10.0) this.media = m;
    }
}""",
        "common_mistakes": ["Non usare 'this'", "Attributi public", "No validazione setter"],
        "best_practices": ["Attributi private", "PascalCase classi", "Validazione input"],
        "learning_objectives": ["Differenza classe-oggetto", "Usare this", "Getter/setter"],
        "related_concepts": ["JAVA-INHERITANCE-001", "JAVA-STATIC-001"]
    },

    # 2. JAVA-STATIC-001: Membri Statici
    {
        "concept_id": "JAVA-STATIC-001",
        "topic": "Membri Statici - Metodi e Attributi di Classe",
        "category": "Object-Oriented Programming",
        "difficulty_level": "intermediate",
        "explanation": "Elementi STATICI appartengono alla CLASSE, non all'istanza. Condivisi da tutti gli oggetti. Utili per utility methods (Math.pow) e costanti (PI). Metodi static non possono accedere membri di istanza.",
        "code_example": """public class Studente {
    private static int contatore = 0;
    public static final double MEDIA_MIN = 6.0;

    private int id;

    public Studente() {
        contatore++;
        this.id = contatore;
    }

    public static int getTotale() {
        return contatore;
    }
}

// Uso: Studente.getTotale() senza creare oggetto""",
        "common_mistakes": ["Accedere 'this' da static", "Confondere static/instance"],
        "best_practices": ["Costanti: static final", "Utility: metodi static"],
        "learning_objectives": ["Differenza static/instance", "Contatori statici"],
        "related_concepts": ["JAVA-OOP-001", "JAVA-FINAL-001"]
    },

    # 3. JAVA-INHERITANCE-001: Ereditarietà
    {
        "concept_id": "JAVA-INHERITANCE-001",
        "topic": "Ereditarietà - Extends e Super",
        "category": "Inheritance and Polymorphism",
        "difficulty_level": "intermediate",
        "explanation": "L'EREDITARIETÀ permette a una sottoclasse di acquisire membri da superclasse con 'extends'. Relazione 'is-a'. 'super()' chiama costruttore superclasse (prima istruzione). 'super.metodo()' accede versione superclasse. Java: ereditarietà singola.",
        "code_example": """public class Veicolo {
    protected String targa;

    public Veicolo(String targa) {
        this.targa = targa;
    }

    public void mostraInfo() {
        System.out.println("Targa: " + targa);
    }
}

public class Auto extends Veicolo {
    private int posti;

    public Auto(String targa, int posti) {
        super(targa);  // Chiama costruttore Veicolo
        this.posti = posti;
    }

    @Override
    public void mostraInfo() {
        super.mostraInfo();  // Chiama versione Veicolo
        System.out.println("Posti: " + posti);
    }
}""",
        "common_mistakes": ["Dimenticare super()", "super() non prima", "Override senza @Override"],
        "best_practices": ["Usare @Override", "super() sempre prima", "protected per ereditarietà"],
        "learning_objectives": ["Usare extends", "super()", "Override metodi"],
        "related_concepts": ["JAVA-OOP-001", "JAVA-POLYMORPHISM-001"]
    },

    # 4. JAVA-POLYMORPHISM-001: Polimorfismo
    {
        "concept_id": "JAVA-POLYMORPHISM-001",
        "topic": "Polimorfismo e Binding Dinamico",
        "category": "Inheritance and Polymorphism",
        "difficulty_level": "intermediate",
        "explanation": "Il POLIMORFISMO permette a riferimento superclasse di puntare a oggetti sottoclasse. BINDING DINAMICO: JVM sceglie metodo a runtime in base al tipo reale. 'instanceof' verifica tipo runtime. Downcasting: conversione superclasse->sottoclasse.",
        "code_example": """// Array polimorfo
Veicolo[] parco = new Veicolo[3];
parco[0] = new Auto("AB123", 5);
parco[1] = new Moto("EF456", 600);
parco[2] = new Auto("IJ789", 4);

// Binding dinamico: chiama versione corretta
for (Veicolo v : parco) {
    v.mostraInfo();  // Auto o Moto in base al tipo reale
}

// instanceof e downcasting
if (parco[0] instanceof Auto) {
    Auto auto = (Auto) parco[0];
    System.out.println(auto.getPosti());
}""",
        "common_mistakes": ["Cast senza instanceof", "Confondere tipo riferimento/oggetto"],
        "best_practices": ["instanceof prima di cast", "Sfruttare polimorfismo vs if-instanceof"],
        "learning_objectives": ["Binding dinamico", "instanceof", "Downcasting sicuro"],
        "related_concepts": ["JAVA-INHERITANCE-001", "JAVA-INTERFACE-001"]
    },

    # 5. JAVA-PACKAGE-001: Package
    {
        "concept_id": "JAVA-PACKAGE-001",
        "topic": "Package e Organizzazione Codice",
        "category": "Code Organization",
        "difficulty_level": "beginner",
        "explanation": "I PACKAGE raggruppano classi correlate. Sintassi 'package it.scuola.modelli;' prima istruzione. 'import' per usare classi altri package. Directory rispecchia gerarchia package. Previene conflitti nomi.",
        "code_example": """// File: Studente.java
package it.scuola.gestionale.modelli;

public class Studente {
    // Implementazione
}

// File: MainApp.java
package it.scuola.gestionale.app;

import it.scuola.gestionale.modelli.Studente;

public class MainApp {
    public static void main(String[] args) {
        Studente s = new Studente();
    }
}

// Struttura directory:
// src/it/scuola/gestionale/modelli/Studente.java
// src/it/scuola/gestionale/app/MainApp.java""",
        "common_mistakes": ["package non prima", "Directory != package", "import package vs classi"],
        "best_practices": ["Dominio inverso: it.azienda.progetto", "Package per area funzionale"],
        "learning_objectives": ["Dichiarare package", "Import", "Organizzare directory"],
        "related_concepts": ["JAVA-ACCESS-001", "JAVA-CLASSPATH-001"]
    },

    # 6. JAVA-INTERFACE-001: Interfacce
    {
        "concept_id": "JAVA-INTERFACE-001",
        "topic": "Interfacce - Contratti e Astrazione",
        "category": "Abstraction and Interfaces",
        "difficulty_level": "intermediate",
        "explanation": "Un'INTERFACCIA definisce un contratto (metodi astratti) senza implementazione. Classi implementano interfacce con 'implements'. Una classe può implementare multiple interfacce (vs ereditarietà singola). Polimorfismo tramite interfacce.",
        "code_example": """// Interfaccia: contratto
public interface Stampabile {
    void stampa();  // Metodo astratto (no implementazione)
    default void stampaDettagli() {  // Default method (Java 8+)
        System.out.println("Dettagli generici");
    }
}

// Implementazione
public class Documento implements Stampabile {
    private String titolo;

    @Override
    public void stampa() {
        System.out.println("Stampo: " + titolo);
    }
}

// Polimorfismo via interfaccia
Stampabile s = new Documento();
s.stampa();  // Binding dinamico""",
        "common_mistakes": ["implements vs extends", "Dimenticare @Override"],
        "best_practices": ["Interfacce per API contracts", "Naming: aggettivi (-able)"],
        "learning_objectives": ["Dichiarare interfacce", "implements", "Polimorfismo interfacce"],
        "related_concepts": ["JAVA-ABSTRACT-001", "JAVA-POLYMORPHISM-001"]
    },

    # 7. JAVA-ABSTRACT-001: Classi Astratte
    {
        "concept_id": "JAVA-ABSTRACT-001",
        "topic": "Classi Astratte vs Interfacce",
        "category": "Abstraction and Interfaces",
        "difficulty_level": "intermediate",
        "explanation": "CLASSE ASTRATTA: non istanziabile, può avere metodi astratti e concreti, attributi, costruttori. INTERFACCIA: solo contratti (metodi astratti). Classe astratta per 'is-a' con codice comune, interfaccia per 'can-do' (capabilities).",
        "code_example": """// Classe astratta: codice comune + metodi astratti
public abstract class Figura {
    protected String colore;  // Attributo concreto

    public Figura(String colore) {  // Costruttore
        this.colore = colore;
    }

    public abstract double calcolaArea();  // Astratto

    public void mostraColore() {  // Concreto
        System.out.println("Colore: " + colore);
    }
}

public class Cerchio extends Figura {
    private double raggio;

    public Cerchio(String colore, double r) {
        super(colore);
        this.raggio = r;
    }

    @Override
    public double calcolaArea() {
        return Math.PI * raggio * raggio;
    }
}

// Figura f = new Figura(); // ERRORE: classe astratta!
Figura c = new Cerchio("Rosso", 5.0);  // OK""",
        "common_mistakes": ["Istanziare classe astratta", "Confondere abstract/interface"],
        "best_practices": ["Abstract per codice comune", "Interface per contratti multipli"],
        "learning_objectives": ["Dichiarare classe astratta", "Metodi astratti", "abstract vs interface"],
        "related_concepts": ["JAVA-INTERFACE-001", "JAVA-INHERITANCE-001"]
    },

    # 8. JAVA-EXCEPTION-001: Eccezioni
    {
        "concept_id": "JAVA-EXCEPTION-001",
        "topic": "Gestione Eccezioni - Try-Catch-Finally",
        "category": "Error Handling",
        "difficulty_level": "intermediate",
        "explanation": "Le ECCEZIONI gestiscono errori runtime. Try-catch cattura eccezioni. Finally esegue sempre (cleanup). Checked (obbligano try-catch o throws) vs Unchecked (RuntimeException). Throw per lanciare, throws per dichiarare.",
        "code_example": """public class GestoreFile {
    public void leggiFile(String path) {
        try {
            FileReader fr = new FileReader(path);
            BufferedReader br = new BufferedReader(fr);
            String linea = br.readLine();
            System.out.println(linea);
            br.close();
        } catch (FileNotFoundException e) {
            System.out.println("File non trovato: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("Errore I/O: " + e.getMessage());
        } finally {
            System.out.println("Operazione completata");
        }
    }

    // Try-with-resources (Java 7+)
    public void leggiFileModerno(String path) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            System.out.println(br.readLine());
        }  // Auto-close br
    }
}""",
        "common_mistakes": ["Catch generico Exception", "Finally per return", "Ignorare eccezioni"],
        "best_practices": ["Catch specifici", "Try-with-resources", "Log eccezioni"],
        "learning_objectives": ["try-catch-finally", "Checked vs unchecked", "Try-with-resources"],
        "related_concepts": ["JAVA-STREAM-001", "JAVA-CUSTOM-EXCEPTION-001"]
    },

    # 9. JAVA-STREAM-001: Stream I/O
    {
        "concept_id": "JAVA-STREAM-001",
        "topic": "Stream e Buffer - File I/O",
        "category": "File Input/Output",
        "difficulty_level": "intermediate",
        "explanation": "STREAM: flussi di dati byte (InputStream/OutputStream) o caratteri (Reader/Writer). BUFFER: memorizzazione temporanea per efficienza (BufferedReader/Writer). Try-with-resources per auto-close.",
        "code_example": """import java.io.*;

public class FileManager {
    // Lettura file con buffer
    public void leggiFile(String path) throws IOException {
        try (BufferedReader br = new BufferedReader(
                new FileReader(path))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
        }
    }

    // Scrittura file
    public void scriviFile(String path, String contenuto)
            throws IOException {
        try (BufferedWriter bw = new BufferedWriter(
                new FileWriter(path))) {
            bw.write(contenuto);
            bw.newLine();
        }
    }
}""",
        "common_mistakes": ["Non chiudere stream", "FileReader senza Buffer"],
        "best_practices": ["Try-with-resources", "Buffer per performance"],
        "learning_objectives": ["FileReader/Writer", "BufferedReader/Writer", "Try-with-resources"],
        "related_concepts": ["JAVA-EXCEPTION-001", "JAVA-SERIALIZATION-001"]
    },

    # 10. JAVA-ARRAYLIST-001: ArrayList
    {
        "concept_id": "JAVA-ARRAYLIST-001",
        "topic": "ArrayList e Generics - Collezioni Dinamiche",
        "category": "Collections and Generics",
        "difficulty_level": "beginner",
        "explanation": "ARRAYLIST: collezione dinamica ridimensionabile. GENERICS <T> per type safety. Metodi: add, remove, get, set, size. Autoboxing/unboxing per primitivi (int -> Integer).",
        "code_example": """import java.util.ArrayList;

public class GestioneStudenti {
    public static void main(String[] args) {
        // Generics: type safety
        ArrayList<String> nomi = new ArrayList<>();

        // Metodi base
        nomi.add("Mario");
        nomi.add("Anna");
        nomi.add(1, "Luca");  // Inserisce in posizione

        System.out.println(nomi.get(0));  // Mario
        System.out.println(nomi.size());  // 3

        nomi.remove("Anna");
        nomi.set(0, "Giuseppe");

        // Iterazione
        for (String nome : nomi) {
            System.out.println(nome);
        }

        // ArrayList di oggetti
        ArrayList<Studente> classe = new ArrayList<>();
        classe.add(new Studente("A001", "Mario", 7.5));
    }
}""",
        "common_mistakes": ["Raw type senza generics", "IndexOutOfBounds", "ConcurrentModification"],
        "best_practices": ["Sempre specificare <T>", "Capacità iniziale se nota"],
        "learning_objectives": ["Dichiarare ArrayList<T>", "add/remove/get", "Iterare collezioni"],
        "related_concepts": ["JAVA-GENERICS-001", "JAVA-ITERATOR-001"]
    },

    # 11. JAVA-GUI-001: Swing JFrame
    {
        "concept_id": "JAVA-GUI-001",
        "topic": "Interfacce Grafiche - Swing Components",
        "category": "Graphical User Interface",
        "difficulty_level": "intermediate",
        "explanation": "SWING: framework GUI Java. JFrame (finestra), JPanel (contenitore), JButton (pulsante), JLabel (etichetta). Layout Manager (BorderLayout, FlowLayout) per posizionamento componenti.",
        "code_example": """import javax.swing.*;
import java.awt.*;

public class FinestraBase extends JFrame {
    private JLabel etichetta;
    private JButton pulsante;

    public FinestraBase() {
        setTitle("Applicazione Swing");
        setSize(400, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        // Layout
        setLayout(new BorderLayout());

        // Componenti
        etichetta = new JLabel("Benvenuto!", SwingConstants.CENTER);
        pulsante = new JButton("Clicca");

        // Aggiunta
        add(etichetta, BorderLayout.CENTER);
        add(pulsante, BorderLayout.SOUTH);

        setVisible(true);
    }

    public static void main(String[] args) {
        new FinestraBase();
    }
}""",
        "common_mistakes": ["Dimenticare setVisible(true)", "Layout default errato"],
        "best_practices": ["BorderLayout per organizzazione", "setLocationRelativeTo(null) per centrare"],
        "learning_objectives": ["Creare JFrame", "Aggiungere componenti", "Layout Manager"],
        "related_concepts": ["JAVA-EVENT-001", "JAVA-LAYOUT-001"]
    },

    # 12. JAVA-EVENT-001: Event Handling
    {
        "concept_id": "JAVA-EVENT-001",
        "topic": "Gestione Eventi - ActionListener",
        "category": "Event-Driven Programming",
        "difficulty_level": "intermediate",
        "explanation": "EVENTI: azioni utente (click, tastiera). LISTENER: interfacce per gestire eventi (ActionListener, MouseListener). Pattern Observer: componente notifica listener registrati.",
        "code_example": """import javax.swing.*;
import java.awt.event.*;

public class Contatore extends JFrame {
    private JLabel lblContatore;
    private JButton btnIncrementa;
    private int contatore = 0;

    public Contatore() {
        setTitle("Contatore");
        setSize(300, 150);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        lblContatore = new JLabel("Click: 0", SwingConstants.CENTER);
        btnIncrementa = new JButton("Incrementa");

        // ActionListener - classe anonima
        btnIncrementa.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                contatore++;
                lblContatore.setText("Click: " + contatore);
            }
        });

        add(lblContatore, BorderLayout.CENTER);
        add(btnIncrementa, BorderLayout.SOUTH);

        setVisible(true);
    }
}""",
        "common_mistakes": ["Listener non registrato", "NullPointer su componenti"],
        "best_practices": ["Lambda per listener semplici", "Inner class per complessi"],
        "learning_objectives": ["ActionListener", "addActionListener", "Pattern Observer"],
        "related_concepts": ["JAVA-GUI-001", "JAVA-LAMBDA-001"]
    },

    # 13. JAVA-MVC-001: Model-View-Controller
    {
        "concept_id": "JAVA-MVC-001",
        "topic": "Pattern MVC - Separazione Responsabilità",
        "category": "Design Patterns",
        "difficulty_level": "advanced",
        "explanation": "MVC separa applicazione in: MODEL (dati + logica business, indipendente da GUI), VIEW (interfaccia grafica), CONTROLLER (coordina Model-View, gestisce eventi). Vantaggi: testabilità, manutenibilità, riusabilità.",
        "code_example": """// MODEL: solo dati e logica
public class TodoModel {
    private List<String> tasks = new ArrayList<>();

    public boolean addTask(String task) {
        if (task == null || task.trim().isEmpty()) return false;
        tasks.add(task.trim());
        return true;
    }

    public List<String> getAllTasks() {
        return new ArrayList<>(tasks);
    }
}

// VIEW: solo GUI
public class TodoView extends JFrame {
    private JTextArea txtArea;
    private JButton btnAdd;

    public String getInput() {
        return txtInput.getText();
    }

    public void displayTasks(List<String> tasks) {
        txtArea.setText(String.join("\\n", tasks));
    }

    public JButton getBtnAdd() { return btnAdd; }
}

// CONTROLLER: coordina Model e View
public class TodoController {
    private TodoModel model;
    private TodoView view;

    public TodoController(TodoModel model, TodoView view) {
        this.model = model;
        this.view = view;

        view.getBtnAdd().addActionListener(e -> {
            String task = view.getInput();
            if (model.addTask(task)) {
                view.displayTasks(model.getAllTasks());
            }
        });
    }
}""",
        "common_mistakes": ["Logica business in View", "View accede Model direttamente"],
        "best_practices": ["Model completamente indipendente", "Controller coordina tutto"],
        "learning_objectives": ["Separare Model/View/Controller", "Testare Model senza GUI"],
        "related_concepts": ["JAVA-GUI-001", "JAVA-OBSERVER-001"]
    },

    # 14. JAVA-LAMBDA-001: Lambda Expressions
    {
        "concept_id": "JAVA-LAMBDA-001",
        "topic": "Lambda Expressions - Programmazione Funzionale",
        "category": "Functional Programming",
        "difficulty_level": "advanced",
        "explanation": "LAMBDA: funzione anonima sintattica. Sintassi: (parametri) -> espressione. Funzionano con interfacce funzionali (1 solo metodo astratto). Sostituiscono classi anonime verbose.",
        "code_example": """import java.util.*;

public class EsempioLambda {
    public static void main(String[] args) {
        List<String> nomi = Arrays.asList("Mario", "Anna", "Luca");

        // Classe anonima (verbosa)
        Collections.sort(nomi, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return s1.length() - s2.length();
            }
        });

        // Lambda (concisa)
        Collections.sort(nomi, (s1, s2) -> s1.length() - s2.length());

        // ActionListener con lambda
        button.addActionListener(e ->
            System.out.println("Cliccato!"));

        // Predicate con lambda
        List<Integer> numeri = Arrays.asList(1, 2, 3, 4, 5);
        numeri.removeIf(n -> n % 2 == 0);  // Rimuove pari
    }
}""",
        "common_mistakes": ["Lambda su interfacce multi-metodo", "Sintassi errata"],
        "best_practices": ["Usare per Comparator, ActionListener, Predicate"],
        "learning_objectives": ["Sintassi lambda", "Interfacce funzionali", "Sostituire classi anonime"],
        "related_concepts": ["JAVA-EVENT-001", "JAVA-STREAM-API-001"]
    },

    # 15. JAVA-COMPARATOR-001: Comparator e Ordinamento
    {
        "concept_id": "JAVA-COMPARATOR-001",
        "topic": "Comparator - Ordinamento Personalizzato",
        "category": "Collections and Sorting",
        "difficulty_level": "intermediate",
        "explanation": "COMPARATOR: interfaccia per definire ordinamento personalizzato. Metodo compare(T o1, T o2): <0 (o1<o2), 0 (uguali), >0 (o1>o2). Collections.sort() accetta Comparator. Lambda per creare comparatori concisi.",
        "code_example": """import java.util.*;

class Studente {
    String nome;
    double media;

    public Studente(String nome, double media) {
        this.nome = nome;
        this.media = media;
    }
}

public class OrdinamentoStudenti {
    public static void main(String[] args) {
        List<Studente> classe = new ArrayList<>();
        classe.add(new Studente("Mario", 7.5));
        classe.add(new Studente("Anna", 8.2));
        classe.add(new Studente("Luca", 6.8));

        // Ordinamento per media (decrescente) con lambda
        classe.sort((s1, s2) ->
            Double.compare(s2.media, s1.media));

        // Ordinamento multiplo
        classe.sort(Comparator.comparing(s -> s.nome)
                              .thenComparing(s -> s.media));

        classe.forEach(s ->
            System.out.println(s.nome + ": " + s.media));
    }
}""",
        "common_mistakes": ["Ordine parametri sbagliato", "compare() senza Double.compare"],
        "best_practices": ["Lambda per comparatori semplici", "Comparator.comparing() per chaining"],
        "learning_objectives": ["Implementare Comparator", "Collections.sort()", "Ordinamenti multipli"],
        "related_concepts": ["JAVA-ARRAYLIST-001", "JAVA-LAMBDA-001"]
    },

    # 16. JAVA-ITERATOR-001: Iterator Pattern
    {
        "concept_id": "JAVA-ITERATOR-001",
        "topic": "Iterator - Iterazione Sicura",
        "category": "Collections and Iteration",
        "difficulty_level": "intermediate",
        "explanation": "ITERATOR: oggetto per iterare collezioni con rimozione sicura. Metodi: hasNext(), next(), remove(). Rimuove ConcurrentModificationException (vs for-each). Pattern Iterator per accesso sequenziale.",
        "code_example": """import java.util.*;

public class EsempioIterator {
    public static void main(String[] args) {
        ArrayList<String> nomi = new ArrayList<>();
        nomi.add("Mario");
        nomi.add("Anna");
        nomi.add("Luca");

        // Iterator per rimozione durante iterazione
        Iterator<String> it = nomi.iterator();
        while (it.hasNext()) {
            String nome = it.next();
            if (nome.equals("Anna")) {
                it.remove();  // Sicuro con Iterator
            }
        }

        // For-each non può rimuovere
        // for (String nome : nomi) {
        //     nomi.remove(nome); // ConcurrentModificationException!
        // }

        System.out.println(nomi);  // [Mario, Luca]
    }
}""",
        "common_mistakes": ["remove() senza next()", "ConcurrentModification in for-each"],
        "best_practices": ["Iterator per rimozione", "For-each per sola lettura"],
        "learning_objectives": ["Usare Iterator", "hasNext/next/remove", "Rimozione sicura"],
        "related_concepts": ["JAVA-ARRAYLIST-001", "JAVA-FOREACH-001"]
    },

    # 17. JAVA-GENERICS-001: Generics e Type Safety
    {
        "concept_id": "JAVA-GENERICS-001",
        "topic": "Generics - Parametri di Tipo",
        "category": "Type Safety and Reusability",
        "difficulty_level": "advanced",
        "explanation": "GENERICS: parametrizzazione tipi con <T>. Type safety a compile-time (vs cast runtime). Classi generiche riutilizzabili. Type erasure: info tipo rimossa a runtime. Bounded types: <T extends SuperClass>.",
        "code_example": """// Classe generica
public class Box<T> {
    private T contenuto;

    public void set(T contenuto) {
        this.contenuto = contenuto;
    }

    public T get() {
        return contenuto;
    }
}

// Bounded type parameter
public class NumericBox<T extends Number> {
    private T valore;

    public double getDouble() {
        return valore.doubleValue();  // Number ha doubleValue()
    }
}

// Utilizzo
public class TestGenerics {
    public static void main(String[] args) {
        // Type safety: compile-time check
        Box<String> boxString = new Box<>();
        boxString.set("Ciao");
        String s = boxString.get();  // No cast needed!

        Box<Integer> boxInt = new Box<>();
        boxInt.set(42);
        // boxInt.set("test"); // ERRORE COMPILAZIONE!

        NumericBox<Double> nb = new NumericBox<>();
        // NumericBox<String> err; // ERRORE: String non extends Number
    }
}""",
        "common_mistakes": ["Raw types senza <>", "Type erasure confusion", "Generics con primitivi"],
        "best_practices": ["Sempre specificare tipo generico", "Bounded types per vincoli"],
        "learning_objectives": ["Classi generiche <T>", "Bounded types", "Type safety"],
        "related_concepts": ["JAVA-ARRAYLIST-001", "JAVA-COLLECTIONS-001"]
    },

    # 18. JAVA-FINAL-001: Modificatore Final
    {
        "concept_id": "JAVA-FINAL-001",
        "topic": "Modificatore Final - Immutabilità",
        "category": "Language Features",
        "difficulty_level": "beginner",
        "explanation": "FINAL: rende immutabile. Variabile final: valore non modificabile dopo inizializzazione. Metodo final: non può essere overridden. Classe final: non può essere estesa (String, Math). Costanti: static final.",
        "code_example": """public class EsempioFinal {
    // Costante di classe: static final
    public static final double PI = 3.14159;
    public static final String APP_NAME = "MyApp";

    // Attributo final: inizializzato in costruttore
    private final int id;
    private final String nome;

    public EsempioFinal(int id, String nome) {
        this.id = id;    // Inizializzazione una sola volta
        this.nome = nome;
    }

    // Metodo final: non può essere overridden
    public final void metodoSicuro() {
        System.out.println("Implementazione fissa");
    }
}

// Classe final: non può essere estesa
public final class ClasseImmutabile {
    private final int valore;

    public ClasseImmutabile(int valore) {
        this.valore = valore;
    }

    public int getValore() { return valore; }
    // public void setValore(int v) {} // NO setter per immutabilità
}

// Variabili locali final
public void metodo() {
    final int MAX = 100;
    // MAX = 200; // ERRORE COMPILAZIONE!
}""",
        "common_mistakes": ["final su riferimenti (oggetto mutabile)", "Dimenticare inizializzazione final"],
        "best_practices": ["Costanti: static final MAIUSCOLO", "Classi immutabili: final + no setter"],
        "learning_objectives": ["final per variabili/metodi/classi", "Immutabilità", "Costanti"],
        "related_concepts": ["JAVA-STATIC-001", "JAVA-IMMUTABLE-001"]
    }
]

# Aggiungo tutti i descriptor al report
report["concept_descriptors"] = descriptors

# Salvo il JSON con encoding UTF-8
with open('/home/user/Appunti/JAVA_DESCRIPTORS_REPORT.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"✅ File JAVA_DESCRIPTORS_REPORT.json creato con successo!")
print(f"📊 Totale descriptor: {len(descriptors)}")
print(f"📚 Categorie coperte:")
for cat in set(d['category'] for d in descriptors):
    count = sum(1 for d in descriptors if d['category'] == cat)
    print(f"   - {cat}: {count} descriptors")
