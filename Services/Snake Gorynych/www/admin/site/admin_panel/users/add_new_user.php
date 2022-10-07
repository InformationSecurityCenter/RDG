<?php
    require_once($_SERVER['DOCUMENT_ROOT'].'/admin_panel/include/users.php');
    $ip_address  = $_SERVER['HTTP_HOST']; 

    if ($_SERVER['REQUEST_METHOD'] == "POST") {
        $OS = array(
            "Linux",
            "Windows"
        );

/*        $file1 = "Default";
        if (isset($_FILES[$OS[1]]))
            $file1 =  $_FILES[$OS[1]]['name'];

        $file2 = "Default";
        if (isset($_FILES[$OS[0]]))
            $file2 =  $_FILES[$OS[0]]['name'];
*/
        $Password_flag = replace_quotes($_POST["Password_flag"]);
        $inserted_org = array(
            "'".replace_quotes($_POST['Password_flag'])."', ",
            "'".date("Y-m-d H:i:s")."', ",
            "'".replace_quotes($_POST['email'])."', ",
            "'".replace_quotes($_POST['full_name'])."', ",
            "'".replace_quotes($_POST['payment_method'])."'"

        );
        $error = add_new_organization($inserted_org, $Password_flag);
        if ($error == false)
            header("Location: http://$ip_address/admin_panel/users.html?error=1");
        else {
            header("Location: http://$ip_address/admin_panel/users.html?change=1");
        }
    }
    else
        header("Location: http://$ip_address/errors/method_error.html");
?>
