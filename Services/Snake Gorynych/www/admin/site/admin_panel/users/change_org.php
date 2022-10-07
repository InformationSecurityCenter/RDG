<?php
    require_once($_SERVER['DOCUMENT_ROOT'].'/admin_panel/include/users.php');
    $ip_address  = $_SERVER['HTTP_HOST'];

    if ($_SERVER['REQUEST_METHOD'] == "POST") {
        $inserted_org = array(
            "`Organization` = '".replace_quotes($_POST['Organization'])."', ",
            "`Time_of_creation` = '".date("Y-m-d H:i:s")."', ",
            "`Domain` = '".replace_quotes($_POST['Domain'])."', ",
            "`Comment` = '".replace_quotes($_POST['Comment'])."', ",
            "`Site_template` = '".replace_quotes($_POST['Site_template'])."', "
        );

        if ($_POST["LinAct"] == "2") {
            $OS = array("Linux");
            $file = "Default";
            if (isset($_FILES[$OS[0]]))
                $file =  $_FILES[$OS[0]]['name'];
            array_push($inserted_org, "`Linux_VPNclient` = '".$file."', ");
        }

        if ($_POST['WinAct'] == "2") {
            $OS = array("Windows");
            $file = "Default";
            if (isset($_FILES[$OS[0]]))
                $file =  $_FILES[$OS[0]]['name'];
            array_push($inserted_org, "`Win_VPNclient` = '".$file."', ");
        }

        array_push($inserted_org, "`State` = 0 ");
        $error = change_org($inserted_org, $_POST['ID'], $_POST["OldDomain"], $_POST["Domain"]);
        if ($error == false)
            header("Location: http://$ip_address/admin_panel/users.html?error=1");
        else {
            if ($_POST["LinAct"] == "2") {
              $OS = array("Linux");
              upload_VPN($OS, $_POST['OldDomain'], $_FILES);
            }

            if ($_POST['WinAct'] == "2") {
              $OS = array("Windows");
              upload_VPN($OS, $_POST['OldDomain'], $_FILES);
            }

            if ($_POST["OldDomain"] != $_POST["Domain"]) {
              for ($x = 1; $x <= 2; $x++) {
                $base_dir = "/home/Honeypot/webportal/CACHE/stc/".$x."/binaries/";

                exec("mv ".$base_dir.$_POST["OldDomain"]." ".$base_dir.$_POST["Domain"]);
              }
            }

            header("Location: http://$ip_address/admin_panel/users.html?change=1");
        }
    }
    else
        header("Location: http://$ip_address/errors/method_error.html");
?>
