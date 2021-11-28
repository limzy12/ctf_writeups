<?php

$content = file_get_contents("php://input");

echo $content."\n";
echo urldecode(date($content));

?>
