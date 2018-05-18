var myApp = angular.module('myApp', ['ngRoute']);

myApp.component('postList', {
	templateUrl: "/static/main/postList.template.html",
	controller: function($scope, postService) {
		$scope.posts = postService.all();
	}
});

myApp.component('postDetail', {
	templateUrl:"/static/main/postDetail.template.html",
	controller: function($scope,$routeParams,postService){
		$scope.postId = $routeParams.postId;
		$scope.post=postService.get($scope.postId);
	},
});

myApp.config(function($routeProvider){
	$routeProvider.
		when('/',{
			template:'<post-list></post-list>'
		}).
		when('/:postId', {
			template: '<post-detail></post-detail>'
		}).
		otherwise('/');
});

myApp.service('postService', function(){
	var posts = [{
		  id: 1,
		  title: 'My trip to Amsterdam',
		  text: 'I had a great time in Amsterdam over spring break!'
		}, {
		  id: 2,
		  title: 'Almost done!',
		  text: 'There are only five weeks left in the semester.'
		}]

	return {
		all: function() {return posts;},
		get: function(postId) {
			return posts.find(function(post){
				return post.id == postId;
			});
		}
	};
});
