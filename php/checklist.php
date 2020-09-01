<?php

function checkList(){
	if(isset($_POST['check']) or isset($_POST['submit'])){
		echo "<h3>Checklist</h3><br/>";
		$check = 0;
		$checkList = array('Plan', 'Model', 'Approve', 'Raw','Machine','Mfg','QC','Pkg','Bill','Ship','Pay');
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
		//print_r($checkIndex);
		echo '&#x2611;' . $check. " steps are complete";
		echo "<br/>";
		echo '&#x2612;' . (sizeof($checkList) - $check) . " steps are incomplete";
		echo "<br/>";
		if($check == sizeof($checkList)){
			echo '&#x2611;' . "Project Completed<br/>";
		}
	}
}

checkList();
?>