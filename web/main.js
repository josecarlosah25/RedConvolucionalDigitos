async function generateMap(op) {

	ext=await eel.getData(op)()

	switch(op){

		case 1:
			elements=ext.split(",");
			var mainScreen = document.getElementById("mainScreen");
			mainScreen.remove();
			insertRowFormat(elements[0],elements[1]);
			//console.log(elements[0]);

			//alert(elements[0]);
		break;

		default:
			var mainScreen = document.getElementById("mainScreen");
			mainScreen.remove();
			insertCards(ext,ext.length)

	}
	
}

function insertRowFormat(imageSource,recognizedNumbers){

	//var src=URL.createObjectURL(imageSource);
	//alert(src)
	
	document.getElementById('home').innerHTML = `<div id="mainScreen">
            <div class="row">
                    <div class="card" style="margin-left: 11%; margin-top: 10%;">
                         <img src="temp/1/1.png" alt="number" style="max-height:100%;max-width:100%; border-radius: 15px; ">
                         <div class="container">
                             <h4><b>Identified Numbers</b></h4>
                             <p>${recognizedNumbers}</p>
                         </div>
                    </div> 
            </div>
            <div class="row" style="margin-left: 42%;margin-top: 5%;">
                <input type="button" class="reset" value="Back to start" onclick="reset()">
            <div>
        </div>`;
}

function reset(){

	location.reload()
}

function insertCards(recognizedNumbers, arraySize){

	document.getElementById('home').innerHTML =`<div id="mainScreen" class="container h-100"> </div>`;
	
	
	var i=0;
	var rowCount=0;

	while(i<arraySize){ 

		var j;
		var nameRow="row"+rowCount;
		document.getElementById('mainScreen').innerHTML +=`<div  id="${nameRow}" class="row"> </div>`;
		for(j=0; j<4;j++){

			if(i>=arraySize){
				break;
			}

			document.getElementById(nameRow).innerHTML +=`
				    <div class="card" style="max-width:15%; margin-left:3%; margin-top:1%" >
                         <img src="temp/2/${i}.png" alt="number" style="max-height:100%;max-width:100%; border-radius: 15px; ">
                         <div class="container">
                             <h4><b>Identified Number</b></h4>
                             <p>${recognizedNumbers[i]}</p>
                         </div>
                    </div> 
			`;
			i=i+1;
		}
		rowCount=rowCount+1;
	}

	document.getElementById(nameRow).innerHTML +=` <input type="button" class="reset" value="Back to start" onclick="reset()" style=" margin-top: 15%;
    margin-left: 5%;">`;
	console.log(arraySize);
	console.log(recognizedNumbers[0]);
}