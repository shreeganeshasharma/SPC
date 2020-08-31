<?php
//print_r($_POST);

if(isset($_POST['filer'])){
	if(isset($_FILES['file'])){
		//	echo "hi";
		$file = $_FILES['file'];
		//print_r($file);
		$fileName = $file['name'];
		$fileType = $file['type'];
		$fileNameTemp = $file['tmp_name'];
		$fileError = $file['error'];
		$fileSize = $file['size'];
		//print_r($fileSize);
		$fileExt = explode('.', $fileName);
		$fileActualExt = strtolower(end($fileExt));
		//echo $fileActualExt;
		$allowed = array('txt', 'csv', 'xlsx', 'json', 'html');
		if (in_array($fileActualExt, $allowed)){
			if($fileError == 0){
				if($fileSize == 0){
					echo "Upload a non-empty file! Are you kidding me?";
				}else{
					$fileNameNew = uniqid('', true).".".$fileActualExt;
					$fileDst = '../uploads/'.$fileNameNew;
					move_uploaded_file($fileNameTemp, $fileDst);
					//echo $fileNameNew." Successfully created in ".$fileDst;
					echo "File uploaded successfully";
				}
			}else{
				echo "There was an error uploading your file!";
			}
		}else{
			echo "Please enter the data for Histogram, Scatter Plot, and Control charts. Only .txt, .csv, .xlsx, .json, .html formats are accepted.";
		}
	}else{
		echo "Please enter the data for Histogram, Scatter Plot, and Control charts. Only .txt, .csv, .xlsx, .json, .html formats are accepted.";
	}
}
//Fishbone
//TBD - like checklist.php
/*function fishbone(){
	if(isset($_POST['fishbone'])){
		if($Shifts == "Shifts"){
			echo 'yes';
		}
		if($Training == "Training"){
			echo 'yes';
		}
		if($Operators == "Operators"){
			echo 'yes';
		}
		if($Health == "Health"){
			echo 'yes';
		}
		if($Salary != ""){
			echo 'yes';
		}
	}
}*/
//fishbone();
//Checklist
//Done - To be improved on test.html page
//TBD - Let em add more fields
/*function checkList(){
	if(isset($_POST['check'])){
		echo "<h3>Checklist</h3><br/>";
		$check = 0;
		/*if(isset($_POST['Plan'])){
			echo "Planning done<br/>";
			$check++;
		}
		if(isset($_POST['Model'])){
			echo "Modelling done<br/>";
			$check++;
		}
		if(isset($_POST['Approve'])){
			echo "Model Approved<br/>";
			$check++;
		}
		if(isset($_POST['Raw'])){
			echo "Raw Materials Procured<br/>";
			$check++;
		}
		if(isset($_POST['Machine'])){
			echo "Machinery Procured<br/>";
			$check++;
		}
		if(isset($_POST['QC'])){
			echo "QC done<br/>";
			$check++;
		}
		if(isset($_POST['Pkg'])){
			echo "Goods are packed<br/>";
			$check++;
		}
		if(isset($_POST['Bill'])){
			echo "Product has been billed<br/>";
			$check++;
		}
		if(isset($_POST['Ship'])){
			echo "Product has been shipped<br/>";
			$check++;
		}
		if(isset($_POST['Pay'])){
			echo "Payment done<br/>";
			$check++;
		}
*/
//checkList();
//TBD - Pareto chart
//TBD - Defect Concentration diagram
?>
