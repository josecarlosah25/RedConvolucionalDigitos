async function generateMap(op) {

	ext=await eel.getData(op)()
    var mainScreen = document.getElementById("mainScreen");
	mainScreen.remove();
	alert(ext)
}

