<?php
if ($_GET['run']) {
  # This code will run if ?run=true is set.
  exec("/home/pi/RPi_Cam_Web_Interface/www/red.sh");
}
?>
