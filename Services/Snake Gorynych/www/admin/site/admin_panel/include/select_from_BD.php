<?php
    include "credential.php";

    $link = Null;

    function con_to_DB()
	{
		global $HOST, $USER, $PASSWORD, $DB;
        global $link;

		$link = mysqli_connect($HOST, $USER, $PASSWORD, $DB) or die("Error " . mysqli_error($link));
	}

    function close_con()
	{
		global $link;

		mysqli_close($link);
	}

    function select_query(string $query, string $string_of_types,
                                        int $offset, int $limit) // <-- it's custom arguments
    {
        global $link;

        con_to_DB();

        if ($stmt = mysqli_prepare($link, $query)) {
            mysqli_stmt_bind_param($stmt, "ii", $offset, $limit);
        }
        else
            close_con();

        if (!(mysqli_stmt_execute($stmt)))
            close_con();

        $result = mysqli_stmt_get_result($stmt);
		while($row = mysqli_fetch_array($result))
			$arr[] = $row;

        mysqli_stmt_close($stmt);
        close_con();

        return $arr;
    }

    function record_count($query)
    {
        global $link;

        con_to_DB();

        $result = mysqli_query($link, $query);
        $count = mysqli_num_rows($result);

        close_con();

        return $count;
    }

    function validate_cred($login, $password)
    {
        global $link;

        con_to_DB();

        $query = "SELECT user, password FROM `admin_panel_users` WHERE user = ? AND password = ?";

        if ($stmt = mysqli_prepare($link, $query)) {  
            mysqli_stmt_bind_param($stmt, "ss", $LOGIN, $PASSWORD);  //dont work
            $ip_address  = $_SERVER['HTTP_HOST']; 
            $LOGIN = $login;
            $PASSWORD = $password;
            

            if(!(mysqli_stmt_execute($stmt))) {
                /** ОШИБКА АУТЕНТИФИКАЦИИ **/

                // Cookie();
                mysqli_stmt_close($stmt);
                mysqli_close($link);
                
                header("Location: http://$ip_address/login.html?error=2");
                return false;
            }
            $RESULT = mysqli_stmt_get_result($stmt);
            $COUNT = mysqli_num_rows($RESULT);

            $query2 = "SELECT user, password FROM `admin_panel_users` WHERE user = '".$login."' AND password = '".$password."'";

            $result2 = mysqli_query($link, $query2);
            $COUNT2 = mysqli_num_rows($result2);


            
            if (strlen ($password) < 30) {
                $md5 = md5($password);

                $query3 = "SELECT user, password FROM `admin_panel_users` WHERE user = '".$login."' AND password = '".$md5."'";
                $result3 = mysqli_query($link, $query3);
                $COUNT3 = mysqli_num_rows($result3);

            }
            mysqli_stmt_close($stmt);
        }
        else {
            /** ОШИБКА АУТЕНТИФИКАЦИИ **/

            // Cookie();
            mysqli_close($link);
            header("Location: http://$ip_address/login.html?error=2");
            return false;
        }

        if ($COUNT2 != 1 and $COUNT3 != 1) {
            /** НЕВЕРНЫЙ ЛОГИН ИЛИ ПАРОЛЬ **/

            mysqli_close($link);

            return false;
        }
        else {
            return true;
        }

        close_con();
    }

    function configure_records($query)
    {
        global $link;

        con_to_DB();

        $error = mysqli_query($link, $query);

        close_con();

        return $error;
    }
?>
