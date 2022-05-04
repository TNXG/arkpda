<?
$charid = $_GET['charid'];
if(empty($charid)){
    echo '{"code":"400","message":"Missing required parameters"}';
}else{
    $con = exec('python ./core/charid2charname.py ' . $charid);
    if(empty($con)){
        echo '{"code":"1000","message":"Server internal error: the correct data was not obtained"}';
    }else{
        echo $con;
    }
}
