
<?php
if ($_GET['run']) {
  # This code will run if ?run=true is set.
 echo exec("python /var/www/redLighttest.py 2>&1");
}
?>

<!-- This link will add ?run=true to your URL, myfilename.php?run=true -->
<a href="?run=true">Red Light</a>
