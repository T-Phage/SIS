/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
	var x = document.getElementById("myTopnav");
	if (x.className === "topnav") {
	  x.className += " responsive";
	} else {
	  x.className = "topnav";
	}
  }

  function showpassword() {
	var x = document.getElementById("passwrd");
	if (x.type === "password") {
	  x.type = "text";
	} else {
	  x.type = "password";
	}
  } 


  /* Message Script */
function isCharacterALetter(char) {
	return (/[a-zA-Z]/).test(char)
}

function consolefunc(){
	var key = "0FXUUtZwxSNAIoLPfAMBl4syWDEqkLzkqwfl0eSy7F9P4";
	var to = document.getElementById('to').value;
	var message = document.getElementById('message').value;
	var senderid = "Sammy" //document.getElementById('sender_id').value;

	if(isCharacterALetter(to.toString()) == true){
		document.getElementById('numberror').style.display = 'block'
	} else {
		var form = document.getElementsByTagName('form')
		form[0].setAttribute("action", "https://apps.mnotify.net/smsapi?key=B8EFM3vpF4qpQFbrbOEsMoYhE&to="+to+"&msg="+message+"&sender_id="+senderid+"")

		console.log(key)
		console.log(to)
		console.log(isCharacterALetter(to.toString()))
		console.log(message)
		console.log(senderid)
		console.log()

		//document.getElementById('myform').submit();
	}
}

// console.log(document.getElementsByClassName('contact-list')[0])
function expand(){
	document.getElementsByClassName('contact-list')[0].style.height = "200px";
}

function compress(){
	document.getElementsByClassName('contact-list')[0].style.height = "0px";
}



