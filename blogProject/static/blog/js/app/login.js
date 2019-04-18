let bt = document.getElementsByClassName("button");
let div = document.getElementsByClassName("inner");
div[0].style.height = "500px";
for(let i = 0;i < bt.length;i++){
	bt[i].onclick = function(){
		// console.log(this)
		for(let j = 0;j < div.length;j++){
			if(i == j){
				// console.log(j,getComputedStyle(div[j]).display)
				// div[j].style.display = "block";
				div[j].style.transition = "height 1s";
				div[j].style.overflow = "visible";
				div[j].style.height = "500px";
				// div[j].style.backgroundColor = "lightgray";
			}
			else{
				div[j].style.height = "0px";
				// div[j].style.display = "none";
				div[j].style.overflow = "hidden";
			}
		}
	}
	bt[i].ondblclick = function(){
		div[i].style.height = "0px";
		// div[i].style.display = "none";
		div[i].style.overflow = "hidden";
	}
}