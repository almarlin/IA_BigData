<?php
$servername = "db"; // nombre del servicio de la base de datos
$username = "user";  // nombre de usuario de la base de datos
$password = "test";  // contraseña de la base de datos
$dbname = "xemp_db"; // nombre de la base de datos

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Comprobar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Realizar una consulta
$sql = "SELECT * FROM users";
$result = $conn->query($sql);
$rows = [];


while ($row = $result->fetch_object()) {
    $rows[] = $row; // Almacena cada fila en el array $rows
}

// Cerrar conexión
$conn->close();
?>