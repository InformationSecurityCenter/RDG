<?php
    require_once "select_from_BD.php";
    require_once "cookie.php";

    function Cookie($token)
    {
        $init_cookie = array(
            "token" => $token
        );

        Set_Cookie($init_cookie);
    }

    function open_session($user)
    {
        $session_cookie = GenSessionCookie();
        $time = date("Y-m-d H:i:s");
        $query = "INSERT INTO `admin_panel_sessions` VALUES(NULL, '".$user."', '".$time."', '".$session_cookie."')";
        configure_records($query);
        Cookie($session_cookie);
    }

    function validate($login, $password)
    {
        $res = validate_cred($login, $password);
        if ($res) {
            open_session($login);
        }
        
        return $res;
    }

    function check_cookie($cookie)
    {
        $query = "SELECT id FROM `admin_panel_sessions` WHERE token = '".$cookie."'";

        if (record_count($query) != 1)
            return false;
        return true;
    }
?>