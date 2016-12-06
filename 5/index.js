var md5 = require('md5');
var readline = require('readline');

var input = "abbhdwsy"
var password = "________";

function strReplaceAt(what, index, replacement){
	if(what.length<=index || index<0)
		return what;
	// console.log(what);
	return what.substring(0,index).toString() + replacement.toString() + what.substring(index+1).toString();

}

for(var index = 0; index<100000000; ++index){
	var str = md5(input+index);
	if(str.indexOf("00000", 0)==0){
		if(str[5]>=0 && str[5]<8 && password[parseInt(str[5])] =='_'){

			password = strReplaceAt(password,parseInt(str[5]),str[6]);
			readline.clearLine();
			readline.cursorTo(process.stdout,0);
			process.stdout.write(password);

		}
	}
	if(!password.includes("_")){
		break;
	}
}

