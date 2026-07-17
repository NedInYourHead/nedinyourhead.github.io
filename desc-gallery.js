  const allParas = document.getElementById("desc-list").getElementsByTagName("li");
  const prevButton = document.getElementById("prevButton");
  const nextButton = document.getElementById("nextButton");
  var listIndex = 0;

  switchDescription(0)
    
	function switchDescription(byAmount) {
      if ((-1 < listIndex + byAmount) && (listIndex + byAmount < allParas.length))
      {
      	listIndex += byAmount
      	document.getElementById("desc-output").innerHTML = allParas.item(listIndex).innerHTML;
        document.getElementById("title-output").innerHTML = allParas.item(listIndex).getAttribute("data-title");
        document.getElementById("date-output").innerHTML = allParas.item(listIndex).getAttribute("data-date");
      }
      
      if (listIndex == 0)
      {
      	prevButton.style.visibility= "hidden";
      } else {
      	prevButton.style.visibility= "visible";
      	prevButton.title= allParas.item(listIndex-1).getAttribute("data-title");
      }
      
      if (listIndex == allParas.length-1) {
      	nextButton.style.visibility= "hidden";
      } else {
      	nextButton.style.visibility= "visible";
      	nextButton.title=allParas.item(listIndex+1).getAttribute("data-title");
      }
	
    }