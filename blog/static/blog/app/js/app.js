'use strict';


var app = angular.module('pgApp', [
	'ngRoute']);

app.config(['$routeProvider','$locationProvider', function ($routeProvider, $locationProvider) {
	
	$routeProvider.when('/posts', {
			templateUrl: 'static/blog/app/partials/posts.html',
			controller: 'PostListController'
			
		});


}]);


app.factory('Post', [ '$http', function($http){

	function getUrl(id){
		id = typeof id !== 'undefined' ? id : '';
		return 'http://127.0.0.1:8000/api/blog/';// + id + '?format=json';
	};


	return {

		get: function(id, callback) {
			return $http.get(getUrl(id))
				.success(callback);
		}
		
	};
}]);


app.controller('PostListController', ['$scope', 'Post', function($scope, Post){

	
		Post.get('', function(data) {
		
		$scope.posts = data;
	});
	
}]);


