//tesssssssssss

oxford.controller('mapController', [ '$scope', '$http','$q', function($scope, $http,$q){

    var deffer = $q.defer();
    var currentlocation = function() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (position) {
                    //if user location is needed in scope
                    $scope.userlocation = (position.coords.latitude + "," + position.coords.longitude);
                    //google maps latlng converter
                    var usergooglelatlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                    deffer.resolve(usergooglelatlng);
                });
                return deffer.promise;
            }
            else {
                // Browser doesn't support Geolocation
                handleNoGeolocation(false);
            }
        };

    //once promise is finished of current location setup map
    currentlocation().then(function(userlocation){
        var usericon = {
            url: "http://maps.gstatic.com/intl/en_ALL/mapfiles/dd-start.png"
        };

        var mapOptions = {
            zoom: 14,
            center: new google.maps.LatLng(33.9167378,-118.12982339999998),
            mapTypeId: google.maps.MapTypeId.TERRAIN
        };

        $scope.map = new google.maps.Map(document.getElementById('map'), mapOptions);

        $scope.locations = [];

        $http.get('/api/companies/').success(function(data) {
            var near_locations = [];


            data.forEach(function(company){
               var compare = new google.maps.LatLng(company.latitude, company.longitude);
                var distance = google.maps.geometry.spherical.computeDistanceBetween(userlocation, compare);
                if (distance < 1609.34) {
                    near_locations.push(company);
                }
            });

            near_locations.forEach(function (company) {
                    var marker =  {
                        name: company.name,
                        address: company.full_address,
                        link: company.link,
                        lat : company.latitude,
                        long : company.longitude
                    };
                    $scope.locations.push(marker);
            });
           }).error(function(error) {
              return error;
           }).then(function(){

        $scope.markers = [];
        var locations = $scope.locations;

        var infoWindow = new google.maps.InfoWindow();

        var createMarker = function (info){

            var marker = new google.maps.Marker({
                map: $scope.map,
                position: new google.maps.LatLng(info.lat, info.long),
                title: info.name,
                link: info.link,
                address: info.full_address
            });
            marker.content = '<div class="infoWindowContent">'  + info.address + '</div>';

            google.maps.event.addListener(marker, 'click', function(){
                infoWindow.setContent('<h2>' + '<a href="'+ marker.link + '">'+ marker.title + '</a>' + '</h2>' + marker.content);
                infoWindow.open($scope.map, marker);
            });

            $scope.markers.push(marker);

        };
            $scope.usermarker = [];

        var userMarker = function (info){

            var marker = new google.maps.Marker({
                map: $scope.map,
                position: new google.maps.LatLng(33.9167378,-118.12982339999998),
                icon: usericon
            });
            marker.content = '<div class="infoWindowContent">'  + userlocation + '</div>';

            google.maps.event.addListener(marker, 'click', function(){
                infoWindow.setContent('<h2>' + 'you are here' + '</h2>');
                infoWindow.open($scope.map, marker);
            });

            $scope.usermarker.push(marker);

        };

        for (i = 0; i < locations.length; i++){
            createMarker(locations[i]);
        }
            userMarker(userlocation);

        $scope.openInfoWindow = function(e, selectedMarker){
            e.preventDefault();
            google.maps.event.trigger(selectedMarker, 'click');
        }

        });
    });
}]);