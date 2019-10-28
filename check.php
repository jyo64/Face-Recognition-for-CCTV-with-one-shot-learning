<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "facedb";
$name = $_POST["name"];
// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT found FROM userdata where name = '$name'";
$result = mysqli_query($conn, $sql);

while ($row = $result->fetch_assoc()) {
    echo $row['classtype']."<br>";
}


mysqli_close($conn);
?> 