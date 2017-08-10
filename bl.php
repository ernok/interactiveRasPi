<?php
$UserIP = $_SERVER['REMOTE_ADDR'];
 echo exec("sudo python /var/www/python/blueLight.py > /dev/null &");
echo exec("echo $UserIP | mail -s 'Blue Visitor' rich@rdarellano.com > /dev/null &");
?>
