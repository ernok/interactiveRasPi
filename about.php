<?php
$UserIP = $_SERVER['REMOTE_ADDR'];
echo exec("echo $UserIP | mail -s 'About-Me Visitor' rich@rdarellano.com > /dev/null &");
?>
<center>
A live feed broadcasts from my Raspberry Pi as it receives user input from a PHP button, 
<br>which then sends the user input data to a Python application via a Shell script,
<br>which then gets sent to the Rasberry Pi's GPIO pins telling them to output a specific value, 
<br>which gives the 3 LEDs a 1 (on) or 0 (off) value,
<br>and the RGB LED an XXX value where X = 1 or 0,
<br>lighting the LEDs in a color scheme according to the user's input.
<br>
<br> Contact for more information:<b> rich@rdarellano.com</b>
<br>
<br><img src="rasPi.jpg" alt="rasPi" />
<img src="rasPi2.jpg" alt="rasPi2" />
</center>
