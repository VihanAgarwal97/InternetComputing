//Author : Vihan Agarwal

var beers = ["corona", "hams", "coors", "budweiser","heineken","rolling rock", "bud light", "yuengling", "blue moon", "miller lite"];
var score = 0;
var startTime;
var inputField;

//called when start button is clicked
function start() {
    //debug
    console.log("started");
    //get input field
    inputField= document.querySelector("#promptbox");
    //enable and focus the input field
    inputField.removeAttribute("disabled");
    inputField.focus();
    //begin timing
    startTime=new Date().getTime();
}

//check if a word is part of the answer
function checkWord(){
    //debug
    console.log("checked");
    
    //get value of input field
    var word = inputField.value;
    word = word.toLowerCase();
    
    //check if word exists
    if(beers.indexOf(word)>=0){
        score+=1;
        beers.splice(beers.indexOf(word), 1);
        word = word.replace(/\s+/g, '');
        var query="#".concat(word);
        document.querySelector(query).style.visibility = "visible";
        inputField.value = "";
        document.querySelector("#score").innerHTML = score;
    }
    
    //check if game is over
    if(beers.length<=0){
        //calculate time taken
        var time=(new Date().getTime() - startTime)/1000;
        
        //disable input field and button
        inputField.value = "";
        inputField.setAttribute("disabled","");
        document.querySelector("#start").setAttribute("disabled","");
        
        //show win and time
        document.querySelector("#win").style.visibility = "visible";
        document.querySelector("#time").style.visibility = "visible";
        document.querySelector("#time").innerHTML ="You took " + time + " seconds";
        
        //popup
        function popup() { alert("YOU WIN!! You took "  + time + " seconds")};
        
        setTimeout(popup,0);
    }
    

}