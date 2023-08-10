var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(50, 500 / 400, 0.1, 1000);

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild(renderer.domElement);
var RADIUS_SPHERE = 3;
var geometry   = new THREE.SphereGeometry(5, 100, 100)
var material  = new THREE.MeshPhongMaterial()
material.map    = THREE.ImageUtils.loadTexture('static/img/earthcloudmap.jpeg')
var sphere = new THREE.Mesh( geometry, material );
var light = new THREE.DirectionalLight( 0xffffff );
light.position.set(0, 0, 1 ).normalize();
scene.add(light);
scene.add( sphere );
var vec = new THREE.Vector3( );

var z = 16
camera.position.z = 16;
var render = function () {
    requestAnimationFrame(render);

   //sphere.rotation.y += 0.01;
   
    renderer.render(scene, camera);
};


render();

window.addEventListener('click', function(e) {
    var lat = 90 - (Math.acos(e.clientY / RADIUS_SPHERE)) * 180 / Math.PI;
var lon = ((270 + (Math.atan2(e.clientX , z)) * 180 / Math.PI) % 360) -180;
var keyob = Object.keys(sphere);


 //  console.log(Object.keys(sphere));
 //
 //
 // console.log(sphere.p);
   
}, false);