var activetab;

$(".toolimg").click(function () {
    $("#mainimg").attr("src", $(this).attr("src"));
    $(".toolimg").css("border-color","");
    $(".toolimg").css("border-style","");
    $(this).css("border-color","#CC527A");
    $(this).css("border-style","solid");
});

function controller(){
    var input = document.querySelector("#prompt_box");
    var text=input.value;
    text= text.toLowerCase();
    
    if(text == "pictures"){
        $("#content2div").css('visibility','hidden');
        $("#content3div").css('visibility','hidden');
        $("#content1div").css('visibility','visible');
        $("#tab1span").css("background-color","#CC527A");
        $("#tab2span").css("background-color","");
        $("#tab3span").css("background-color","");
        input.value = "";
    }else if(text == "text") {
        $("#content2div").css('visibility','visible');
        $("#content3div").css('visibility','hidden');
        $("#content1div").css('visibility','hidden');
        $("#tab1span").css("background-color","");
        $("#tab2span").css("background-color","#CC527A");
        $("#tab3span").css("background-color","");
        input.value = "";
    }else if(text == "misc") {
        input.value = "";
        $("#content2div").css('visibility','hidden');
        $("#content3div").css('visibility','visible');
        $("#content1div").css('visibility','hidden');
        $("#tab1span").css("background-color","");
        $("#tab2span").css("background-color","");
        $("#tab3span").css("background-color","#CC527A");
    }
    
}

$(".editabletext").click(function(){
    var text = $(this).text();
    $(".editabletext").css("background-color","");
    $(this).css("background-color","#CC527A");
    $("#editor").val(text);
    
});

$("#prompt_box").focus();