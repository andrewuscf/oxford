oxford.controller('marker',['$scope', 'companies', function($scope, companies) {
    companies.success(function(data) {
       $scope.markers = data;

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                return $scope.mylocation = (position.coords.latitude + ',' + position.coords.longitude);
            });


            //$scope.fivemile = function() {
            //    $scope.markers = [];
            //        data.forEach(function (item) {
            //            var myloc = $scope.position;
            //            var compare = new google.maps.LatLng(item.latitude, item.longititude);
            //            var distance = google.maps.geometry.spherical.computeDistanceBetween(myLatlng, compare);
            //            if (distance > 8046.72) {
            //                console.log("Your too damn far away!");
            //            else
            //                {
            //                    prettyarray = [];
            //                    prettyarray.push("<h1>" + item.username + "</h1>", item.latitude, item.longititude, item.id);
            //                    otheruser.push(prettyarray);
            //
            //                }
            //            }
            //        });
            //    }
            }
    })
}]);