<?php
    require_once "select_from_BD.php";
    require_once "execute_module.php";

    function replace_quotes($string)
    {
        $str = str_replace('\'', '\\\'', $string);
        $str = str_replace('--', '', $str);

        return $str;
    }

    function sites_list(int $offset, int $limit)
    {
        $query = "SELECT * FROM sites_list ORDER BY id DESC LIMIT ?, ?";
        return select_query($query, "ii", $offset, $limit);
    }

?>
