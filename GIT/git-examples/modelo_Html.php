
<html>
<head>

</head>
	
<body>
	
	<center>	
	<nav>
		<div id='navegador'>
			<div class='barraNav'><a href=''>Direcc1</a></div>
			<div class='barraNav'><a href=''>Direcc2</a></div>
			<div class='barraNav'><a href=''>Direcc3</a></div>
			<div class='barraNav'><a href=''>Direcc4</a></div>
		</div>
		<div id='mensajes-error'>
			área mens error (lista - ol)
			<ol class='mensErr'>
				<li>Err 01</li>
			</ol>	
		</div>	
	</nav>
	</center>

	<center>	
	<main>
		<div id='ppal'>
			<article>
				<img src='img/creandoCuento.jpeg' alt='crear'>
				<h4><a href=''>Montar un cuento</a></h4> 
			</article>
			<article>
				<img src='img/creandoCuento.jpeg' alt='crear'>
				<h4><a href=''>Montar un cuento</a></h4> 
			</article>
			<article>
				<img src='img/creandoCuento.jpeg' alt='crear'>
				<h4><a href=''>Montar un cuento</a></h4> 
			</article>
			<article>
				<img src='img/creandoCuento.jpeg' alt='crear'>
				<h4><a href=''>Montar un cuento</a></h4> 
			</article>
		</div>
		<div id='lateral'>
			<aside>Caja de Herramientas
			</aside>
		</div>
	</main>	
	</center>
	
	<center>	
		<footer>F O O T E R
			<div id='foot'></div>
			<?php	
				// muestraFooter();	
			?>
		</footer>
	</center>	

	<?php

		/*
		 * Funcion verArreglo
		 *
		 * Presenta la lista de elementos y claves de un arreglo.
		 *
		 * @param Array				$arreglo	    Arreglo a presentar
		 * @param string			$titulo		    Titulo
		 * @param int				$nIndent        Nivel de Indentacion
		*/

		function verArreglo($arreglo, $titulo, $nIndent = 0, $color='blue', $fontS='13px') {
			if ( is_array($arreglo) && isset($arreglo) ) {
				if ( empty($titulo) ) {
					echo "" . str_repeat("\t",$nIndent) . "<ol>\n";
				} else {
					echo "" . str_repeat("\t",$nIndent) . "<b>$titulo</b><br>\n";
					echo "" . str_repeat("\t",$nIndent) . "<ol style='font-size: ". $fontS ."; color: ". $color ." '>\n";
				}
				foreach ($arreglo as $key => $value) {
					if ( is_array($value) ) {
						echo "" . str_repeat("\t",$nIndent + 1) . "<li>[" . str_replace("\0", "-", $key) . "] => Arreglo\n";
						verArreglo($value, "", $nIndent +1);
					} else if ( is_object($value) ) {
						echo "" . str_repeat("\t",$nIndent + 1) . "<li>[" . str_replace("\0", "-", $key) . "] => Objeto\n";
						verArreglo( (array) $value, "", $nIndent +1);
					} else {
						echo "" . str_repeat("\t",$nIndent + 1) . "<li>[" . str_replace("\0", "-", $key) . "] => " . $value . "\n";
					}
				}
				echo "</ol>\n";
			} else {
				echo "<br>No definido o no es arreglo.<br>\n";
			}
		}

		#
		# muestra consulta y arreglos de variables entorno
		#
		echo "<div id='arreglo'>";
			echo "<br><hr><h3 style='color:black;'><b>script consulta</b></h3>";
			echo "<p style='font-size:11px; color:blue;'>consulta-> " . $consulta . "</p>";	
			echo "<hr><h3 style='color:black;'><b>Variables de entorno</b></h3>";
			verArreglo($sesion->mostrarParametros(),'Parametros sesión'); 
			echo "<hr>";
			verArreglo($_SESSION, '$_SESSION');
			echo "<br><hr>";
			verArreglo($_GET, '$_GET');
			echo "<br><hr>";	
			verArreglo($_POST, '$_POST');
			echo "<br><hr>";
			verArreglo($_COOKIE, '$_COOKIE');
			echo "<br><hr>";
			verArreglo($_SERVER, '$_SERVER');
			echo "<br><hr>";
			verArreglo($_ENV, '$_ENV');
		echo "</div>";

	?>	
	

</body>
</html>
