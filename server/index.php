<?php
if (isset($_GET['page'])){
  $page = $_GET['page'] ;
} else {
  $page = "" ;
}

include("../mysqli-connect.php") ;

if ($page == "api"){
  if ($_GET['method'] == "savestationtext"){
    $payload = $_POST['payload'] ;
    file_put_contents("stations.txt",$payload) ;
  } else if ($_GET['method'] == "savequeue"){
    $payload = $_POST['payload'] ;
    file_put_contents("queue.txt",$payload) ;
  } else if ($_GET['method'] == "clearqueue"){
    file_put_contents("queue.txt","[]") ;
  } else if ($_GET['method'] == "readdata"){
    if (isset($_POST['lastrun'])){
      $lastrun = $_POST['lastrun'] ;
      file_put_contents("lastrun.txt",$lastrun) ;
    }
    echo '{"status":"ok","stations":'.file_get_contents("stations.txt").',"queue":'.file_get_contents("queue.txt").'}' ;
    file_put_contents("queue.txt","[]") ;
  }
} else {
  if (false){ //if not logged in go back to login page
    $page = "login" ;
  }

  if ($page == ""){
    echo "<script>";
    echo "const stationFileContents = \"".preg_replace( "/\r|\n/", "",addslashes(file_get_contents("stations.txt")))."\";";
    echo "const lastRunFileContents = \"".preg_replace( "/\r|\n/", "",addslashes(file_get_contents("lastrun.txt")))."\";";
    echo "</script>" ;
    echo file_get_contents("controller.htm") ;

  
  }

  if ($page == "login"){
    echo "This is the login page" ;
  }

  if ($page == "server"){

  }
}
?>