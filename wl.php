<?php
$UserIP = $_SERVER['REMOTE_ADDR'];
 echo exec("sudo python /var/www/python/whiteLight.py > /dev/null &");
echo exec("echo $UserIP | mail -s 'White Visitor' rich@rdarellano.com > /dev/null &");
?>
