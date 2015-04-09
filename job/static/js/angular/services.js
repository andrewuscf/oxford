oxford.factory('companies', ['$http', function($http) {
  return $http.get('http://localhost:8000/api/companies/?format=json')
            .success(function(data) {
              return data;
            })
            .error(function(err) {
              return err;
            });
}]);