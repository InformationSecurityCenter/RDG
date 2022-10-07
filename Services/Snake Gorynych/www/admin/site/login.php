<?php
$ip_address  = $_SERVER['HTTP_HOST'];
	require_once("./admin_panel/include/auth.php");

	if (isset($_POST['login']) AND isset($_POST['password'])) {
		if(validate($_POST['login'], $_POST['password'])) {
			header("Location: http://$ip_address/admin_panel/sites.html");
		}
		else
			header("Location: http://$ip_address/login.html?error=1");
	}
	else
		header("Location: http://$ip_address/login.html?error=3");
?>
