$.ajax({
    url:"https://api.reddit.com/r/battlefield_one/search?restrict_sr=true",
    type: "GET",
    dataType: "json",
    success: function(data) {
        console.log("request succesful");
        var usefulData = data.data.children;
        parseData(usefulData);
    },
    error: function() {
        console.log("fail");
    }
});


function search(){
    var query = $("#query").val();
    $.ajax({
        url:"https://api.reddit.com/r/battlefield_one/search?restrict_sr=true&q=" + query,
        type:"GET",
        dataType: "json",
        success: function(data) {
            var usefulData=data.data.children;
            updateData(usefulData);
        },
        error: function() {
            console.log("fail");
        }
    });
}

function updateData(newdata) {
    $("body").empty();
    newdata.forEach(function(item) {
        var title = item.data.title;
        var img = item.data.thumbnail;
        var auth = item.data.author;
        var link = item.data.url;
        addToScreen(title,img,link,auth);
    });
}

function parseData(data) {
    var title;
    var img;
    var auth;
    var link;
    data.forEach(function(item) {
        title = item.data.title;
        img = item.data.thumbnail;
        link = item.data.url;
        auth = item.data.author;
        addToScreen(title,img,link,auth);
    });
}


function addToScreen(title,url,link,auth) {
    var elem=$("<div class='elem'>");
    var title=$("<p class='title'>"+title+"</p>");
    var img=$("<img class='toolImg'>");

    img.attr("src",(url=="self"? "logo.png":url));


    var url=$("<a class='toolLink'> Go To </a>");
    url.attr("href",link);
    var author = $("<p class='author'> Posted By: " + auth + "</p>" );
    elem.append(img);
    elem.append(title);
    elem.append(author);
    elem.append(url);
    $("body").append(elem);
};
