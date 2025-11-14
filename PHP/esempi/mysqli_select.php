<?php
// Nota tecnica: rimosso strict_types per compatibilità degli esempi.

$mysqli = new mysqli('localhost', 'utente', 'password', 'database');
if ($mysqli->connect_errno) {
    throw new RuntimeException('Connessione fallita: ' . $mysqli->connect_error);
}

$stmt = $mysqli->prepare('SELECT id, nome FROM utenti WHERE email = ?');
if ($stmt === false) {
    throw new RuntimeException('Prepare fallito: ' . $mysqli->error);
}

$email = 'ada@example.com';
$stmt->bind_param('s', $email);
$stmt->execute();
$result = $stmt->get_result();
while ($row = $result->fetch_assoc()) {
    printf("%d %s\n", $row['id'], $row['nome']);
}
$stmt->close();
$mysqli->close();
