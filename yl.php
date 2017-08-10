<?php
$UserIP = $_SERVER['REMOTE_ADDR'];
 echo exec("sudo python /var/www/python/yellowLight.py > /dev/null &");
echo exec("echo $UserIP | mail -s 'Yellow Visitor' rich@rdarellano.com > /dev/null &");
?>
