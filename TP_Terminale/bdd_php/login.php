<?php



// on teste si les variables sont définies

if (isset($_POST['login']) && isset($_POST['pwd'])) {

	try
	{
		require('acces_base.php');
		$conn = new PDO($dsn);
		if($conn)
		{
			$sql = 'SELECT ;';
			$results = $conn->prepare($sql);
			$results->execute();
			$res = $results->fetchOne();
			foreach($res as $r)
			{
				$pw = $r['mot_passe'];
			}
			if(empty($pw))
			{  
				echo '<meta http-equiv="refresh" content="0;URL=index.htm">';
				header ('location: non.php');
			} 
			else
			{
				// on redirige l'utilisateur vers la page 2.
				session_start();
				$_SESSION["id"] = session_id();
				header ('location: oui.php');
			}
		}
	}
	catch (PDOException $e)
	{
		echo $e->getMessage();
	}


}

else {

	echo 'Les variables du formulaire ne sont pas déclarées.';

}

?>
