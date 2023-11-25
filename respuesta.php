<?php
session_start();
$armonicos = $_POST['armonicos'];


if($armonicos>0){
    //Comando
    //$comando = sprintf("python /var//www/html/ProyectoServidorFourier/Fourier.py --x=%d",$armonicos);
    $comando = sprintf("python3 Fourier.py --x=%d",$armonicos);
    
    // en la variable session se guarda el numero de cuenta esto para poder acarrearla
    $_SESSION['armonicos']=$armonicos;
    
    echo shell_exec($comando);
    
    //header("location: /var//www/html/ProyectoServidorFourier/dashboard.php");
    header("location: dashboard.php");
}else{
    //header("location: /var//www/html/ProyectoServidorFourier/index_error.php");
    header("location: index_error.php");
   
}

?>