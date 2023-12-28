import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const geometry = new THREE.BoxGeometry(1, 3, 1);
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
// const material = [
//     new THREE.MeshStandardMaterial({ color: 0xff0000 }), // Right
//     new THREE.MeshStandardMaterial({ color: 0x00ff00 }), // Left
//     new THREE.MeshStandardMaterial({ color: 0x0000ff }), // Top
//     new THREE.MeshStandardMaterial({ color: 0xffff00 }), // Bottom
//     new THREE.MeshStandardMaterial({ color: 0xff00ff }), // Front
//     new THREE.MeshStandardMaterial({ color: 0x00ffff })  // Back
//   ];
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

camera.position.z = 5;

// function animate() {
//   requestAnimationFrame(animate);
//   cube.rotation.x += 0.01;
//   cube.rotation.y += 0.01;
//   renderer.render(scene, camera);
// }

// function animate() {
//     requestAnimationFrame(animate);

//     // Assuming you have loaded the JSON data into a variable named jsonData
//     if (jsonData && jsonData.sensor_data) {
//       // Get the latest gyroscope data
//       const latestData = jsonData.sensor_data[jsonData.sensor_data.length - 1];

//       // Update cube rotation based on gyroscope data
//       cube.rotation.x = (latestData.gyroscope.x * Math.PI) / 180;  // Convert degrees to radians
//       cube.rotation.y = (latestData.gyroscope.y * Math.PI) / 180;
//       cube.rotation.z = (latestData.gyroscope.z * Math.PI) / 180;
//     }

//     renderer.render(scene, camera);
//   }
// animate();

const jsonData = {
  "sensor_data": [
      {
          "gyroscope": {
              "x": -4,
              "y": -1,
              "z": 0
          },
          "timestamp": 1702472747.7382145
      },
      {
          "gyroscope": {
              "x": -4,
              "y": -1,
              "z": 0
          },
          "timestamp": 1702472748.7470927
      },
      {
          "gyroscope": {
              "x": -23,
              "y": -41,
              "z": -34
          },
          "timestamp": 1702472749.7558815
      },
      {
          "gyroscope": {
              "x": -8,
              "y": -88,
              "z": -32
          },
          "timestamp": 1702472750.7647488
      },
      {
          "gyroscope": {
              "x": -35,
              "y": 34,
              "z": -4
          },
          "timestamp": 1702472751.7817864
      },
      {
          "gyroscope": {
              "x": -45,
              "y": -5,
              "z": 36
          },
          "timestamp": 1702472752.8089538
      },
      {
          "gyroscope": {
              "x": -41,
              "y": -8,
              "z": 56
          },
          "timestamp": 1702472753.829953
      },
      {
          "gyroscope": {
              "x": 29,
              "y": -45,
              "z": 18
          },
          "timestamp": 1702472754.8510377
      },
      {
          "gyroscope": {
              "x": 103,
              "y": -81,
              "z": -78
          },
          "timestamp": 1702472755.8721051
      },
      {
          "gyroscope": {
              "x": 40,
              "y": 110,
              "z": -36
          },
          "timestamp": 1702472756.8941088
      },
      {
          "gyroscope": {
              "x": -48,
              "y": -13,
              "z": 21
          },
          "timestamp": 1702472757.9194376
      },
      {
          "gyroscope": {
              "x": -27,
              "y": 84,
              "z": 48
          },
          "timestamp": 1702472758.9411047
      },
      {
          "gyroscope": {
              "x": 26,
              "y": -76,
              "z": 12
          },
          "timestamp": 1702472759.962777
      },
      {
          "gyroscope": {
              "x": -20,
              "y": 40,
              "z": -25
          },
          "timestamp": 1702472760.9845905
      },
      {
          "gyroscope": {
              "x": 0,
              "y": -5,
              "z": 35
          },
          "timestamp": 1702472762.0065055
      },
      {
          "gyroscope": {
              "x": -4,
              "y": -1,
              "z": 0
          },
          "timestamp": 1702472763.0327394
      }
  ]
};

// Create a variable to store the current rotation
const currentRotation = { x: 0, y: 0, z: 0 };
const delayBetweenFrames = 2000;

async function animate() {
  requestAnimationFrame(animate);

  // Update the cube's rotation using the gyroscope data from the JSON file
  for (let i = 0; i < jsonData.sensor_data.length; i++) {
    const latestData = jsonData.sensor_data[i].gyroscope;

    currentRotation.x += latestData.x * 0.0001; // Adjust the scaling factor as needed
    // currentRotation.x += 1 * 0.001;
    currentRotation.y += latestData.y * 0.0001;
    // currentRotation.y += 1 * 0.001;
    currentRotation.z += latestData.z * 0.0001;
    // currentRotation.z += 1 * 0.001;

    cube.rotation.x = currentRotation.x;
    cube.rotation.y = currentRotation.y;
    cube.rotation.z = currentRotation.z;

    console.log(latestData);

    // cube.rotation.x += latestData.x * 0.00025;
    // cube.rotation.y += latestData.y * 0.00025;
    // cube.rotation.z += latestData.z * 0.00025;

    renderer.render(scene, camera);
    await new Promise((resolve) => setTimeout(resolve, delayBetweenFrames));

    // currentRotation.x = 0;
    // currentRotation.y = 0;
  }
}

animate();

// // Load the JSON file
// fetch("basic_viewpublicmpu6050_data.json")
//   .then((response) => response.json())
//   .then((data) => {
//     jsonData = data;
//     animate(); // Start the animation loop after loading the JSON data
//   })
//   .catch((error) => console.error("Error loading JSON file:", error));
