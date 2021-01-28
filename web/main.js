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
			console.log(ext);
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
                             <h4><b>Numeros Identificados</b></h4>
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