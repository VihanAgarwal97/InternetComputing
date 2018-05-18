$(document).ready(function () { 
console.log($(".delbutton"))
$(".delbutton").on("click", function() {
	var currentID = $(this).attr("data-id");
		$.ajax({
			type: "GET",
			url: "/delete",
			data: {"id": currentID },
			success: function() {
	        	alert("MOVIE DELETED");
	        	$("tr[data-id='" + currentID + "']").remove();
	        }
		});
		
	});

}); 
