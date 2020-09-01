<?php

function fishbone(){
	echo "<h3>Cause and Effect Diagram</h3><br/>";
	print_r($_POST);
	$check = 0;
	$checkList = array_fill(1,35,0);
	for($x = 0; $x <= 35; $x++){
		$checkList[$x] = $x;
	}
	print_r($checkList);
	$checkIndex = array_fill(0,count($checkList),0);
		
	foreach($checkList as $x){
		if(isset($_POST[$x])){
			echo "&#x2611;" . $_POST[$x]. " complete";
			echo "<br/>";
			$checkIndex[$check]++;
			$check++;
		}else{
			echo "&#x2612;" . $x. " incomplete";
			echo "<br/>";
		}
	}
	echo "<br/>";
	print_r($checkIndex);
}

fishbone();
?>