<?php

session_start();

//initialising the variables

$username="";
<<<<<<< HEAD
$roll_number="";
=======
$email="";
>>>>>>> 677a7cfc5304d092272624ab688b2a74f37d1e80

$errors=array();

//connect to db
$db=mysqli_connect('localhost','root','','tictechtoe') or die("could not connect to database");
//register users

$username=mysqli_real_escape_string($db,$_POST['username']);
<<<<<<< HEAD
$roll_number=mysqli_real_escape_string($db,$_POST['roll_number']);
$contact=mysqli_real_escape_string($db,$_POST['contact']);
$address=mysqli_real_escape_string($db,$_POST['address']);
=======
$email=mysqli_real_escape_string($db,$_POST['email']);
>>>>>>> 677a7cfc5304d092272624ab688b2a74f37d1e80
$password_1=mysqli_real_escape_string($db,$_POST['password_1']);
$password_2=mysqli_real_escape_string($db,$_POST['password_2']);


if(empty($username)) {array_push($errors, "username is required");}
<<<<<<< HEAD
if(empty($roll_number)) {array_push($errors, "roll_number is required");}
if(empty($contact)) {array_push($errors, "contact is required");}
if(empty($address)) {array_push($errors, "address is required");}
if(empty($password_1)) {array_push($errors, "Password is required");}
if($password_1!=$password_2){array_push($errors, "Password do not match");}

$user_check_query ="SELECT * FROM user WHERE username='$username' or roll_number='$roll_number' LIMIT 1";
=======
if(empty($email)) {array_push($errors, "email is required");}
if(empty($password_1)) {array_push($errors, "Password is required");}
if($password_1!=$password_2){array_push($errors, "Password do not match");}

$user_check_query ="SELECT * FROM user WHERE username='$username' or email='$email' LIMIT 1";
>>>>>>> 677a7cfc5304d092272624ab688b2a74f37d1e80

$results = mysqli_connect($db,$user_check_query);
$user = mysqli_fetch_assoc($result);

if($user) {
	if($user['username']=== $username) {array_push($errors, "Username already exists");}
<<<<<<< HEAD
	if($user['roll_number']=== $email) {array_push($errors, "This roll_number already has a registered username");}
=======
	if($user['email']=== $email) {array_push($errors, "This email already has a registered username");}
>>>>>>> 677a7cfc5304d092272624ab688b2a74f37d1e80
}

if(count($errors) == 0) {
      
    $password=md5($password_1);
<<<<<<< HEAD
    $query ="INSERT INTO user (username,roll_number,password,contact,address) VALUES ('$username','$roll_number','$password','$contact','$address')";
=======
    $query ="INSERT INTO user (username,email,password) VALUES ('$username','$email','$password')";
>>>>>>> 677a7cfc5304d092272624ab688b2a74f37d1e80
    mysqli_query($db,$query);
    $_SESSION['username'] = $username;
    $_SESSION['success'] = "You are now logged in";
}
?>