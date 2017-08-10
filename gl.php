<?php
$UserIP = $_SERVER['REMOTE_ADDR'];
 echo exec("sudo python /var/www/python/greenLight.py > /dev/null &");
echo exec("echo $UserIP | mail -s 'Green Visitor' rich@rdarellano.com > /dev/null &");
?>
