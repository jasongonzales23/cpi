var zoom_list = {
    "1" : 13,
    "5" : 12,
    "10" : 11,
    "15" : 11,
    "25" : 10,
    "50" : 9,
    "100" : 8,
    "250"  :6,
    "500" : 4
}
var markers = [];
var latlng = new google.maps.LatLng(38.410558,-37.265625);
var myOptions = {
  zoom: 3,
  center: latlng,
  mapTypeId: google.maps.MapTypeId.ROADMAP
};

var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);  
var infoWindow = new google.maps.InfoWindow();
var search_value = '';
document.map = map;
function clear_markers() {
    for (i in markers) {
        markers[i].setMap(null);
    }
    markers.length = 0;
}

function search_on_load(){
    clear_markers();
    //search_value = $("#locations_search_field").val();
    //var distance = $("#distance_field").val();
    //var new_zoom = zoom_list[distance];
    
    var get_lat_long_url = "/store-locator/get_lat_long/";
    var get_locations_url = "/store-locator/get_locations/";

    
    $.get(get_lat_long_url + "?q=43085", function(data) {
        var latitude = data.split(',')[2];
        var longitude = data.split(',')[3];
        //map.setZoom(new_zoom);            
        /*var marker = new google.maps.Marker({
            position: new google.maps.LatLng(latitude, longitude),
            title: search_value,
        });
        marker.setMap(map);
        markers.push(marker);*/
        //map.setCenter(new google.maps.LatLng(latitude, longitude));
        $.getJSON(get_locations_url + "?lat=38&long=37&distance=24900", function(data) {
            $.each(data, function() {
                location_info = this;
                var location_marker = new google.maps.Marker({
                    position: new google.maps.LatLng(location_info.latitude, location_info.longitude),
                    title: location_info.name
                });
                location_marker.setMap(map);
                markers.push(location_marker);
                google.maps.event.addListener(location_marker, "click", get_location_marker_click_listener(location_info, location_marker));
            });
        });
    });
}

search_on_load();

function location_search() {
    clear_markers();
    search_value = $("#locations_search_field").val();
    var distance = $("#distance_field").val();
    var new_zoom = zoom_list[distance];
    var bounds = new google.maps.LatLngBounds();
    $.get(get_lat_long_url + "?q=" + search_value, function(data) {
        var latitude = data.split(',')[2];
        var longitude = data.split(',')[3];
        //map.setZoom(new_zoom);            
        /*var marker = new google.maps.Marker({
            position: new google.maps.LatLng(latitude, longitude),
            title: search_value,
        });
        marker.setMap(map);
        markers.push(marker);*/
        map.setCenter(new google.maps.LatLng(latitude, longitude));
        $.getJSON(get_locations_url + "?lat=" + latitude + "&long=" + longitude + "&distance=500", function(data) {
            $.each(data, function() {
                location_info = this;
                var location_marker = new google.maps.Marker({
                    position: new google.maps.LatLng(location_info.latitude, location_info.longitude),
                    title: location_info.name
                });
                var lat_lng = new google.maps.LatLng(location_info.latitude, location_info.longitude);
                location_marker.setMap(map);
                markers.push(location_marker);
                bounds.extend(lat_lng);
                google.maps.event.addListener(location_marker, "click", get_location_marker_click_listener(location_info, location_marker));
                
            });
            map.fitBounds(bounds);
        });
    });
}

function get_location_marker_click_listener(location_info, location_marker) {
    return function() {
        content = "<strong>" + location_info.name + "</strong><br>" +
            location_info.address.replace(/\n/g, '<br />') + "<br>" +
            "<a href='http://maps.google.com/maps?saddr=" + search_value + "&daddr=" + location_info.address + "'>Directions</a>";
        if (location_info.url != '') { 
            content += "<br><strong>Website:</strong> <a href='" + location_info.url + "'>" + location_info.url + "</a>";
        }
        if( location_info.email != ''){
        content += "<br><a href='mailto:" + location_info.email + "'>" + location_info.email + "</a>";
        }
        if (location_info.phone != '') { 
            content += "<br><strong>Phone:</strong> " + location_info.phone;
        }
        if (location_info.description != '') { 
            content += "<br><i> " + location_info.description + "</i>";
        }

        infoWindow.setContent(content);
        infoWindow.open(map, location_marker);

    }
}

