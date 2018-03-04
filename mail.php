<?php
		
$status = $_GET['status'];
$message = $_GET['message'];
		
if ($status==='1')
{	
require 'phpmailer/PHPMailerAutoload.php';
$email = "ausmartparking@gmail.com";
$password = "poiuylkjhg";
$to_id = "vatsal2727@gmail.com";

$message = "User Sent emergency notification: <br> $message";
$subject = "Emergency Mail!";
$mail = new PHPMailer;
$mail->isSMTP();
//$mail->SMTPDebug = 2;
$mail->Host = 'smtp.gmail.com';
$mail->Port = 587;
$mail->SMTPSecure = 'tls';
$mail->SMTPAuth = true;
$mail->Username = $email;
$mail->Password = $password;
$mail->FromName = "Emergency!";
$mail->addAddress($to_id);
$mail->Subject = $subject;
$mail->msgHTML($message);
$mail->SMTPOptions = array(
    'ssl' => array(
        'verify_peer' => false,
        'verify_peer_name' => false,
        'allow_self_signed' => true
    )
);
if (!$mail->send()) {
$error = "Mailer Error: " . $mail->ErrorInfo;
echo '<p id="para">'.$error.'</p>';
}
else {
echo '<p id="para">Email has been sent to doctor!</p>';
}
}
?>	
