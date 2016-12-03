
var command = "L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2";

// var command = "R5, L5, R5, R3";
var commands = command.split(", ");

var dir = ["N", "E", "S", "W"];

function arrayRotate(arr, reverse){
  if(reverse)
    arr.unshift(arr.pop());
  else
    arr.push(arr.shift());
  return arr;
} 

var pos = [0,0];
var startpos = [pos[0], pos[1]];

var prev = [];
var count = 0;

commands.forEach(function(item){

	if(item[0]==="L"){
		arrayRotate(dir, true);
	}
	else{
		arrayRotate(dir, false);
	}

	for(var i=0; i<parseInt(item.substr(1)); ++i){
		prev.push([pos[0], pos[1]]);
		if(dir[0] === "N"){
			pos[1]++;
		}
		else if(dir[0] === "S"){
			pos[1]--;
		}
		else if(dir[0] === "E"){
			pos[0]++;
		}
		else if(dir[0] === "W"){
			pos[0]--;
		}

		if(count == 0 && wasPosPreviouslyVisited(pos)){
			console.log("Distance between first prev visited and start: " + getDistanceBetween(pos, startpos));
			count++;
		}
	}

});

function wasPosPreviouslyVisited(pos){
	var found = false;
	prev.forEach(function(item){
		if(item[0]==pos[0] && item[1] == pos[1]){
			found =  true;
		}
	});
	return found;
}

function getDistanceBetween(pos1, pos2){
	return Math.abs(pos1[0]-pos2[0])+Math.abs(pos1[1]-pos2[1]);
}


console.log("Distance between end pos and start pos: " + getDistanceBetween(startpos,pos)); 



