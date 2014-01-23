class omap
  constructor: ()->
    geoself = this
    geoself.getLocation()
  getLocation: ()->
    geoself = this
    $("#wawa").html("start get Position");
    navigator.geolocation.getCurrentPosition (position)->
      $("#wawa").html("getd Position");
      #mobile consile
      $("#wawa").html(position.coords.longitude+"+++++"+position.coords.latitude)
      geoself.setmap(position)
  setmap:(p)->
    geoself = this
    console.log p
    point = new BMap.Point p.coords.longitude, p.coords.latitude
    console.log point
    map = new BMap.Map "container"
    map.centerAndZoom point, 15
    geoself.setMapOption(map)
    geoself.setHandler(map)
  setMapOption:(map)->
    map.disableDragging()
    map.disableDoubleClickZoom()
    map.addControl new BMap.NavigationControl
    map.addControl new BMap.GeolocationControl
  setHandler:(map)->
    map.addEventListener "click", ()->
      navigator.geolocation.getCurrentPosition (position)->
        $.ajax {
          type:'POST', 
          url:'/getxy',
          data:{Y:position.coords.longitude, X:position.coords.latitude},
          #X與Y以後要改過來
          success: (data)->
            console.log data
            for a in data
              point = new BMap.Point a.position[1], a.position[0]
              ma = new BMap.Marker point
              map.addOverlay ma
              #ma.setLable a.id
              #ma.setTitle a.id
              #ma.addEventListener "click", ()->
              #  console.log okey
        }

