var scene = new THREE.Scene();
//scene.background = new THREE.ImageUtils.loadTexture('img/s1200.webp')
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);

document.getElementById('planet').appendChild(renderer.domElement);
// document.body.appendChild(renderer.domElement);

var RADIUS_SPHERE = 3;
var geometry = new THREE.SphereGeometry(RADIUS_SPHERE, 100, 100)
var material = new THREE.MeshPhongMaterial();
material.map = THREE.ImageUtils.loadTexture('static/img/earthcloudmap.jpeg');
var sphere = new THREE.Mesh(geometry, material);
var light = new THREE.DirectionalLight(0xffffff);
light.position.set(0, 0, 1).normalize();
scene.add(light);
scene.add(sphere);


var d1 = 10;
camera.position.z = d1;
var render = function () {
    requestAnimationFrame(render);

    //sphere.rotation.y += 0.01;
    sphere.rotation.y += 1 / 16 * 0.01
    //
    sphere.rotation.x += 1 / 16 * 0.002

    renderer.render(scene, camera);//renderer.setClearColor( 0x000000, 0 ); 
};

render();


window.addEventListener('click', function (e) {

    var lat = 90 - (Math.acos(e.clientY / RADIUS_SPHERE)) * 180 / Math.PI;
    var lon = ((270 + (Math.atan2(e.clientX, camera.position.z)) * 180 / Math.PI) % 360) - 180;
    var keyob = Object.keys(sphere);
    if (document.addEventListener) {

        if ('onwheel' in document) {
            // IE9+, FF17+, Ch31+
            document.addEventListener("wheel", onWheel);
        } else if ('onmousewheel' in document) {
            // устаревший вариант события
            document.addEventListener("mousewheel", onWheel);
        } else {
            // Firefox < 17
            document.addEventListener("MozMousePixelScroll", onWheel);
        }
    } else { // IE8-
        document.attachEvent("onmousewheel", onWheel);
    }

    function onWheel(e) {
        e = e || window.event;

        // wheelDelta не дает возможность узнать количество пикселей
        var delta = e.deltaY || e.detail || e.wheelDelta;

        if (delta > d1) {
            d1 = d1 - 0.1
            sphere.position.z -= 0.1;

        } else {
            d1 = d1 + 0.1
            sphere.position.z += 0.1;
        }

        e.preventDefault ? e.preventDefault() : (e.returnValue = false);
    }

    // console.log(Object.keys(sphere));
    //
    //
    // console.log(sphere.position);

}, false);