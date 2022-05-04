<?
error_reporting(E_ERROR);
$Userid = $_GET['id'];
$type = 'easy';
$type = $_GET['type'];
if (empty($Userid)) {
    echo '{"code":"400","message":"Missing required parameters"}';
} else {
    if ($type != 'all') {
        $con = exec('python ./core/UserId.py ' . $Userid);
    } else {
        $con = exec('python ./core/UserIdAll.py ' . $Userid);
    }

    if (empty($con)) {
        echo '{"code":"1000","message":"The returned data cannot be processed by the server","ServerReturnData":"' . $con . '"}';
    } else {
        if ($con != 'login form session file success') {
            echo $con;
        } else {
            echo '{"code":"1000","message":"The returned data cannot be processed by the server","ServerReturnData":"' . $con . '"}';
        }
    }
}
