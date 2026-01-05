<?php

$path = realpath('../private/.htpasswd');
if ($path) {
    echo $path;
} else {
    echo "Error: file not found!";
}

?>