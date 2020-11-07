<?php include('server.php') ?>
<!DOCTYPE html>
<html>
<head>
	<title>Registration</title>
</head>
<body>
	<div class="container">
		<div class="header">
           <h2>Register</h2>
       </div>
       <form action="registration.php" method="post">
              <?php include('errors.php') ?>
       	<div>
       		
       		<label for="username">Username:</label>
       		<input type="text" name="username" required>

       	</div>
       	<div>
       		
       		<label for="roll_number">Roll Number:</label>
       		<input type="text" name="roll_number" required>

       	</div>
       	<div>
       		
       		<label for="password">Password:</label>
       		<input type="password" name="password_1" required>
       	</div>
       	<div>
       		
       		<label for="password">Confirm Password:</label>
       		<input type="password" name="password_2" required>

       	</div>
		<div>
       		
       		<label for="contact">Parents Contact Number:</label>
       		<input type="text" name="contact" required>
       	</div>
		<div>
       		
       		<label for="Address">Parents Address:</label>
       		<input type="text area" name="addresss" required>
       	</div>
       	<button type="submit" name="reg_user">Submit</button>
              <p>Already a user?<a href="login.php"><b>Log in</b></a></p>
       	
       </form>
</div>
</body>
</html>