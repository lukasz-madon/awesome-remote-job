angular.module('remotejobs', [])
  .controller('JobsCtrl', function ($scope, $http) {
    $scope.jobs = [
      {
        title: "Backend Developer",
        company: "Buffer",
        url: "http://jobs.bufferapp.com/backend",
        description: "Python, PHP"
      }, 
      {
        title: "Frontend Developer",
        company: "Buffer",
        url: "http://jobs.bufferapp.com/frontend",
        description: "Backbone, Less"
      }
    ];
    //fogcreek
    $http.jsonp("https://www.kimonolabs.com/api/2u5o83a8?apikey=Do3zKjeCcYtFNwlZAjpAZuyIHNFLM4IK&callback=JSON_CALLBACK")
      .success(function(data) {
        var obj = data.results.collection1[0].title;
        $scope.jobs.push({ title: obj.text, company: data.name, url: obj.href, description: ""});
      });
  });
