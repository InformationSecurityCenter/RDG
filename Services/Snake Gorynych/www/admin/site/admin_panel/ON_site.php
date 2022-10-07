<?php
    require_once($_SERVER['DOCUMENT_ROOT'].'/admin_panel/include/users.php');
    require_once($_SERVER['DOCUMENT_ROOT'].'/admin_panel/include/execute_module.php');
    $ip_address  = $_SERVER['HTTP_HOST']; 
    $args_arr = array(
        $_POST['Org_ID'],
        $_POST['Act'],
    );
    header("Location: http://$ip_address/admin_panel/sites.html?start=1");
    $script_path = $_SERVER['DOCUMENT_ROOT'].'/admin_panel/moduls/virtualhost/addvirtualhost.py';
    $switch = array(
        "State = NOT State"
    );

    $new_state = 0;
    if ($_POST['Act'] == "ON") {
        $new_state = 1;
    }

    execute_PYmodule($script_path, $args_arr);
    change_org($new_state, $_POST['Org_ID']);


?>
