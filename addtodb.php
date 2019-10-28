<?php
   $name = $_POST["name"];
   $filename = $_FILES['pic']['name'];
   $ext = pathinfo($filename, PATHINFO_EXTENSION);
   $target_dir = "faces/".$name.".jpg";
   move_uploaded_file( $_FILES['pic']['tmp_name'], $target_dir);

$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "facedb";

//IN CASE FOR REUSE

$name = $_POST["name"]; 
$num = $_POST["ph"];
$addr = $_POST["addr"];




try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $sql = "INSERT INTO `userdata` (`name`, `mob`, `address`) 
    VALUES ('".$_POST["name"]."','".$_POST["ph"]."','".$_POST["addr"]."')";
    
    // use exec() because no results are returned
    $conn->exec($sql);
    echo "The Details Have been Uploaded Successfully!!";
    }
catch(PDOException $e)
    {
    echo $sql . "<br>" . $e->getMessage();
    }

$conn = null;



   ?> 

<div class="jumbotron text-center">
