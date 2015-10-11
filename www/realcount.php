<html>
<body>

Welcome <?php $handle = popen("/var/www/launchcount.sh" + $_GET["direction"] + " " + $_GET["direction"], "r") ?>


</body>
</html> 
