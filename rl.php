<?php
$UserIP = $_SERVER['REMOTE_ADDR'];
 echo exec("sudo python /var/www/python/redLight.py > /dev/null &");
echo exec("echo $UserIP | mail -s 'Red Visitor' rich@rdarellano.com > /dev/null &");
?>
