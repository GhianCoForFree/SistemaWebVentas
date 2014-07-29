window.onload=ejemplo;
function ejemplo(){
	var labels = document.getElementsByTagName('label')
	//var inputs = document.getElementsByTagName('input');
	var id_user = document.getElementById('id_username')
	var id_pass1 = document.getElementById('id_password1')
	var id_pass2 = document.getElementById('id_password2')
	var span = document.getElementsByTagName('span')
	span.innerHTML=''
	if (labels) {
		for(var i=0;i<labels.length;i++){
			labels[i].className='control-label'
		}
		/*for(var j=0;j<inputs.length;j++){
			inputs[j].className='form-control'
		}*/
	}
	if (id_user) {
		for (var j = 0; j < id_user.length; j++) {
			id_user[i].className='form-control'
		}
	}
}