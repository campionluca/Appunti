<?php
// Nota tecnica: rimosso strict_types per compatibilità degli esempi.

$mysqli = new mysqli('localhost', 'utente', 'password', 'database');
if ($mysqli->connect_errno) {
    throw new RuntimeException('Connessione fallita: ' . $mysqli->connect_error);
}

$stmt = $mysqli->prepare('INSERT INTO utenti (nome, email) VALUES (?, ?)');
if ($stmt === false) {
    throw new RuntimeException('Prepare fallito: ' . $mysqli->error);
}

$nome = 'Ada';
$email = 'ada@example.com';
$stmt->bind_param('ss', $nome, $email);
$stmt->execute();
printf('Inseriti %d record', $stmt->affected_rows);
$stmt->close();
$mysqli->close();
