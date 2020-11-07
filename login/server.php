<?php

session_start();

//initialising the variables

$username="";
$roll_number="";

$errors=array();

//connect to db
$db=mysqli_connect('localhost','root','','tictechtoe') or die("could not connect to database");
//register users

$username=mysqli_real_escape_string($db,$_POST['username']);
$roll_number=mysqli_real_escape_string($db,$_POST['roll_number']);
$contact=mysqli_real_escape_string($db,$_POST['contact']);
$address=mysqli_real_escape_string($db,$_POST['address']);
$password_1=mysqli_real_escape_string($db,$_POST['password_1']);
$password_2=mysqli_real_escape_string($db,$_POST['password_2']);


if(empty($username)) {array_push($errors, "username is required");}
if(empty($roll_number)) {array_push($errors, "roll_number is required");}
if(empty($contact)) {array_push($errors, "contact is required");}
if(empty($address)) {array_push($errors, "address is required");}
if(empty($password_1)) {array_push($errors, "Password is required");}
if($password_1!=$password_2){array_push($errors, "Password do not match");}

$user_check_query ="SELECT * FROM user WHERE username='$username' or roll_number='$roll_number' LIMIT 1";

$results = mysqli_connect($db,$user_check_query);
$user = mysqli_fetch_assoc($result);

if($user) {
	if($user['username']=== $username) {array_push($errors, "Username already exists");}
	if($user['roll_number']=== $email) {array_push($errors, "This roll_number already has a registered username");}
}

if(count($errors) == 0) {
      
    $password=md5($password_1);
    $query ="INSERT INTO user (username,roll_number,password,contact,address) VALUES ('$username','$roll_number','$password','$contact','$address')";
    mysqli_query($db,$query);
    $_SESSION['username'] = $username;
    $_SESSION['success'] = "You are now logged in";
}
?>