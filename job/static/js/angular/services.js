oxford.factory('companies', ['$http', function($http) {
       $http.get('/api/companies/').success(function(data) {
            return data;
       }).error(function(error) {
          return error;
       });
}]);
