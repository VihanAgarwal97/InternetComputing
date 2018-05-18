var colors = new Array();

colors[0] = "rgb(255, 0, 255)";
colors[1] = "rgb(0, 0, 0)";
colors[2] = "rgb(255, 0, 0)";
colors[3] = "rgb(0, 255, 0)";
colors[4] = "rgb(0, 0, 255)";
colors[5] = "rgb(0, 255, 255)";
colors[6] = "rgb(255, 255, 0)";

$(document).on('click',".button",function () {
    console.log("clicked");
    var thisElem = $(this).attr("for");
    console.log(thisElem);
    var thisColor = $("."+ thisElem).css("color");
    console.log(thisColor);
    var thisIndex = colors.indexOf(thisColor);
    console.log(thisIndex);
    thisIndex+=1;
    if(thisIndex == colors.length){
        thisIndex=0;
    }
    $("."+thisElem).css("color",colors[thisIndex]);
});
