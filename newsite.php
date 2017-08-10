<p style="text-align:center;">
<b>Click on a color:</b><br>
<?php
if ($_GET['run1']) {
  # This code will run if ?run=true is set.
 echo exec("sudo python /var/www/python/redLight.py > /dev/null &");
echo exec("echo $UserIP | mail -s 'Red Visitor' rich@rdarellano.com > /dev/null &$
}
?>

<a href="?run1=true">Red</a>
 <br>
</p>

