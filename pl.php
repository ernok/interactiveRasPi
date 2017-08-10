<?php
$UserIP = $_SERVER['REMOTE_ADDR'];
 echo exec("sudo python /var/www/python/purpleLight.py > /dev/null &");
echo exec("echo $UserIP | mail -s 'Purple Visitor' rich@rdarellano.com > /dev/null &");
?>
