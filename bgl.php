<?php
$UserIP = $_SERVER['REMOTE_ADDR'];
 echo exec("sudo python /var/www/python/bluegreenLight.py > /dev/null &");
echo exec("echo $UserIP | mail -s 'Bluegreen Visitor' rich@rdarellano.com > /dev/null &");
?>
