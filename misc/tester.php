<?php

//How to comment in one line
/*How to comment
in many lines*/

/*
//Print
echo "Hello, world!";
echo 32;
//Statements end with ;
echo "<br/>";

//variable, starts with $
$name = "Harry potter";
$age = 12;
$gender = 'm';

//. to print multiple variables
echo $name.$age;
echo "<br/>";

//Arithmetic
echo $age*2;
echo $age%5;
echo "<br/>";

//If else
if($age > 20){
	echo "Less";
}elseif($name == "Harry"){
	echo "More";
}else{
	echo $gender;
}
echo "<br/>";

//Switch
switch($name){
	case "Harry": print "Yes";break;
	case "Harry potter": print "No";break;
	default: print "Meh";break;
}
echo "<br/>";

//While loop
$i = 0;
while($i <= 5){
	$i = $i + 1;
	print "i = ".$i."<br/>";	
}
echo "<br/>";

//Do-while loop
$i = 0;
do{
	echo "i = ".$i."<br/>";
	$i = $i + 2;
}while($i < 10);
echo "<br/>";

//For loop
for($i = 0;$i < 30;$i = $i + 3){
	echo "i = ".$i."<br/>";
}
echo "<br/>";

//Array
$arr = array("dad","mom","son");
//echo $arr."<br/>";
echo $arr[0]."<br/>";

$arr[3] = "grandma";
echo $arr[3]."<br/>";
$arr[] = 'gf';

//Associative array ~ Dictionary
$actions = array('dad'=>60, 'mom'=>50,'son'=>25,'grandma'=>84);
echo $actions['son'];
//Can't add like this in the end to an assoc array.
//$actions[] = '21';
$actions['gf'] = 21;
echo $actions['gf']."<br/>";

//Looping through an array
print sizeof($actions);
for($x = 0;$x<sizeof($arr);$x++){
	echo $arr[$x]."<br/>";
}

foreach($arr as $x){
	echo $x;
}

//Functions
function hello(){
	echo "<br/>"."Hello from the other side"."<br/>";
}
hello();

echo hello();
echo "<br/>".hello()."<br/>";

function fun($x, $y){
	return ($x / $y);
}
echo fun(2,2.5);

*/
?>

<html>
<body>
<form action="tester.php" method="post">
Name: <input type="text" name="name">
<input type="submit">
</form>
</body>
</html>

<?php include("upload.php"); ?>
<?php
echo "<html>";
echo "<body>";
echo date("d/m*y").$_POST["name"];
echo "</body>";
echo "</html>";
?>

<?php
//Forms
//To ways to get info from a form get and post

























?>