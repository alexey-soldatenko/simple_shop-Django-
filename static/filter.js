function create_price(classname){
	var str = '';
	var val = document.getElementsByClassName(classname);
	var min = document.getElementsByName(val[0].name)[0].value;
	var max = document.getElementsByName(val[1].name)[0].value;
	
	if ((min.length == 0) && (max.length == 0)){
		str = '';
		sessionStorage.setItem('price_min', '');
		sessionStorage.setItem('price_max', '');
	}
	else{
		
		if (min == ''){
			str = classname + '_' + '0' + '-' + max + '/';
			sessionStorage.setItem('price_min', '0');
			sessionStorage.setItem('price_max', max);
		}
		else if(max == ''){
			str = classname + '_' + min + '-' + '20000' + '/';
			sessionStorage.setItem('price_min', min);
			sessionStorage.setItem('price_max', '20000');
		}
		else{
			str = classname + '_' + min + '-' + max + '/';
			sessionStorage.setItem('price_min', min);
			sessionStorage.setItem('price_max', max);
		}
		
	}
	
	return str;
}

function disabled_check(classname, kind_name){
	var kinds = document.getElementsByClassName(classname);
	for (var i = 0; i < kinds.length; i++){
		if (kinds[i].name != kind_name){
			kinds[i].disabled = 'true';
		}
	}
}

function create_path(classname){
	var kinds = document.getElementsByClassName(classname);
		var str = '';

			for(i = 0; i < kinds.length; i++){
				if (kinds[i].checked){
					if (str.length > 0){						
						str += '_or_' + kinds[i].name;
	
					}
					else{
						str += kinds[i].name;
						if(classname == 'hdd' || classname == 'weight'){
							disabled_check(classname, kinds[i].name);
						}
						
					}
					
					sessionStorage.setItem((classname+"_"+kinds[i].name), 'true');
				}
				else{
					sessionStorage.setItem((classname+"_"+kinds[i].name), 'false');
				}
			}
			if (str.length > 0){
				str = classname +'_' + str +'/';
				
			}
			return str;
		
}




function submit_form(){
		var s = '';
		var arr = ['manufacturer', 'kinds', 'price', 'diagonal', 'display', 'processor', 'ram', 'grafic', 'hdd', 'dvd', 'os', 'webcam', 'weight'];
		for(var i=0; i < arr.length; i++){
			if (arr[i] != 'price'){
				s += create_path(arr[i]);
			}
			else{
				s += create_price(arr[i]);
					
			}
			
		}

		var path =  "http://127.0.0.1:8000" + '/catalog/' + s;
		document.location.href = path;
	}


function set_chekbox(){
		var i=0;
		var key = sessionStorage.key(i);
		var kinds = key.split('_');
		var value = sessionStorage.getItem(key);

		for(var len = sessionStorage.length; i < len; i++){
			try{
			key = sessionStorage.key(i);
			kinds = key.split('_');
			value = sessionStorage.getItem(key);

			if(value == 'true'){
				var man = document.getElementsByClassName(kinds[0]);
				for(var j = 0; j < man.length; j++){
					if (man[j].name == kinds[1]){
						document.getElementsByName(man[j].name)[0].checked = true;
						}
				}
				document.getElementById("Clear-filters").style.display = 'block';
			}
			else if (value != 'false'){
				var man = document.getElementsByClassName(kinds[0]);
				if (kinds[0] == 'price' && kinds[1] == 'min'){
					document.getElementsByName(man[0].name)[0].value = value;
				}
				else if(kinds[0] == 'price' && kinds[1] == 'max'){
					document.getElementsByName(man[1].name)[0].value = value;
				}
			}
			}
			catch(e){
				continue;
			}
		}
	}

function delete_filters(){
		var arr = ['manufacturer', 'kinds', 'diagonal', 'display', 'processor', 'ram', 'grafic', 'hdd', 'dvd', 'os', 'webcam', 'weight'];
		for(var i=0; i < arr.length; i++){
			var kinds = document.getElementsByClassName(arr[i]);
			for(var j = 0; j < kinds.length; j++){
				document.getElementsByName(kinds[j].name)[0].checked = false;
				sessionStorage.setItem((arr[i]+"_"+kinds[j].name), 'false');
			}
		}
		sessionStorage.setItem('price_max', '');
		sessionStorage.setItem('price_min', '');
		document.location.href = 'http://127.0.0.1:8000' + '/catalog/';
}

function show_button(){
	document.getElementById("sub_ok").style.display = 'block';
}