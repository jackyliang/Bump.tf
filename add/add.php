<?php
# error_reporting(1);

# define('SUCCESS', 'success.html');

$cookie = isset($_GET['inputCookie']) ? $_GET['inputCookie'] : $_POST['inputCookie'];

echo $cookie;
# echo "Hello world!"

# function redirect() {
#     header('Location: ' . SUCCESS);
# }

?>
