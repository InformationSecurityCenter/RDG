<?php

function GenHexString(int $length)
{
	$hex_string = "";

	$bytes = random_bytes($length);
	$hex_string = strtoupper(bin2hex($bytes));

	return $hex_string;
}

function GenSessionCookie()
{
	$res = GenHexString(30);

	return $res;
}

function Set_Cookie($cookie, int $expires=0, string $path="/")
{
	foreach ($cookie as $cooka => $value) {
		setcookie($cooka, $value, $expires, $path, "");
	}
}

function Remove_Cookie($cookie, $path="/")
{
	foreach ($cookie as $cooka)
		setcookie($cooka, "", time() - 3600, $path, "");
}
?>
