<?php
    function execute_PYmodule($script_path, $args_arr=array())
    {
        $output = Null;
        $retval = Null;
        $command = $script_path;
        
        if (sizeof($args_arr) != 0)
            foreach ($args_arr as $arg)
                $command .= " ".$arg;

        $error = exec($command, $output, $retval);

        if ($error == false) {
            print_r($command);
        }
    }
?>