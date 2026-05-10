let myVariable = "Hello, World!. This is my first JavaScript programe";
console.log(myVariable);
console.log(typeof myVariable);

// String Methods

console.log(myVariable.charAt(34));
console.log(myVariable.indexOf("lo"));
console.log(myVariable.lastIndexOf("l"));

// Numbers

const myInteger = 1.7976931348623157e308;
const myFloat = 54.9;

const myString = "54ccc";

console.log(Number.MAX_VALUE);
console.log(Number.MIN_VALUE);

console.log(myInteger === myString);
console.log(Number(myString) === myInteger);

console.log(myString + 5);

console.log(Number(myString) + 5);
console.log(typeof (Number.parseInt(myString) + 5).toString());

console.log("is number '54' integer: ", Number.isInteger(myString));
console.log("is number 54 integer: ", Number.isInteger(myInteger));
console.log("is number 54.99 integer: ", Number.isInteger(myFloat));

console.log("Math Functions...");
console.log("PI : ", Math.PI);
console.log("Truncate Function : ", Math.trunc(Math.PI));
console.log("Round Function : ", Math.round(3.4));
console.log("Ceil Function : ", Math.ceil(Math.PI));
console.log("Floor Function : ", Math.floor(Math.PI));
console.log("Power Function : ", Math.pow(2, 3));
console.log("Randon Function : ", Math.floor(Math.random() * 2 + 1));

console.log(Math.floor(Math.random() * 4));
console.log(Math.floor(Math.random() * 4));
console.log(Math.floor(Math.random() * 4));
console.log(Math.floor(Math.random() * 4));
console.log(Math.floor(Math.random() * 4));

let myName = "immaduddin";
console.log(myName.charAt(Math.floor(Math.random() * myName.length)));
console.log(myName.charAt(Math.floor(Math.random() * myName.length)));
console.log(myName.charAt(Math.floor(Math.random() * myName.length)));
console.log(myName.charAt(Math.floor(Math.random() * myName.length)));

// condition is a logical expression that evaluates to true or false.
// conditions are created using comparison operators.

let country = "UK";
let age = 18;
if (country === "USA") {
	if (age >= 16) {
		console.log("You can drive.");
	}
} else {
	console.log("different rules apply.");
}

// Multiple conditions can be combined with Logical operators to make
// a complex condition.

if (country == "USA" && age >= 16) {
	console.log("you can drive.");
} else if (country == "UK" && age >= 18) {
	console.log("different rules apply.");
} else {
	console.log("i am living on mars.");
}

let pass = "pass";
let login = pass === "pass" && true;
console.log(login);

// Ternary Operator

let response = country === "USA" ? (age >= 16 ? "you can drive" : "you can not drive.") : "differnet rules apply.";

console.log(response);

// Switch
let expression = Math.floor(Math.random() * 5 + 1);
switch (expression) {
	case 1:
		console.log(1);
		break;
	case 2:
		console.log(2);
		break;
	case 3:
		console.log(3);
		break;
	default:
		console.log("Wrong value.");
}

const themeChanger = document.querySelector("#header__button");
themeChanger.addEventListener("click", () => {
	document.body.classList.toggle("dark-theme");
});
