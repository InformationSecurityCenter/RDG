<?php
    require_once "select_from_BD.php";
    require_once "execute_module.php";

    function replace_quotes($string)
    {
        $str = str_replace('\'', '\\\'', $string);
        $str = str_replace('--', '', $str);

        return $str;
    }

    function organization_list(int $offset, int $limit)
    {
        $query = "SELECT * FROM shared_hosting_users ORDER BY id DESC LIMIT ?, ?";


        return select_query($query, "ii", $offset, $limit);
    }

    function add_new_organization($inserted_org, $domain)
    {
        $values = "";

        foreach ($inserted_org as $value)
            $values .= $value;
        $query = "INSERT INTO `shared_hosting_users` (`ID`, `Password_flag`, `Time_of_creation`, `email`, `full_name`, `payment_method`) VALUES (NULL, $values)";

        return configure_records($query);
    }

    function change_org($new_state, $site_ID)
    {
        $values = "state=";
        $values .= $new_state;
        $query = "UPDATE sites_list SET ". $values ." WHERE id = ". $site_ID;
        
        return configure_records($query);
    }

?>
