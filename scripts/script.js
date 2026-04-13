import * as THREE from "https://unpkg.com/three@0.161.0/build/three.module.js";
console.log("Three.js script start");

/* SCÉNA, KAMERA, RENDERER */

const canvas = document.getElementById("bg");

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000);

const camera = new THREE.PerspectiveCamera(
  60,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);

// ====== KAMERA – pevná pozice, žádné kroužení ======
camera.position.set(0, 0, 60);

const renderer = new THREE.WebGLRenderer({
  canvas,
  antialias: true,
});
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);

/* SVĚTLO */

const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const dirLight = new THREE.DirectionalLight(0xffffff, 1);
dirLight.position.set(30, 40, 20);
scene.add(dirLight);

/* TEXTURE LOADER – společný pro hvězdy i planety */

const textureLoader = new THREE.TextureLoader();

/* =========================================================
   HVĚZDY – více vrstev různé velikosti
   ========================================================= */

function createStarsLayer(count, size) {
  const starGeometry = new THREE.BufferGeometry();
  const positions = new Float32Array(count * 3);

  const radius = 200;
  const offsetZ = 80; // hvězdná koule posunutá dozadu (za planety)

  for (let i = 0; i < count; i++) {
    const i3 = i * 3;

    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(2 * Math.random() - 1);

    const x = radius * Math.sin(phi) * Math.cos(theta);
    const y = radius * Math.sin(phi) * Math.sin(theta);
    const z = radius * Math.cos(phi) - offsetZ;

    positions[i3 + 0] = x;
    positions[i3 + 1] = y;
    positions[i3 + 2] = z;
  }

  starGeometry.setAttribute(
    "position",
    new THREE.BufferAttribute(positions, 3)
  );

  const starTexture = textureLoader.load("../Obrázky/stars.png");

  const starMaterial = new THREE.PointsMaterial({
    map: starTexture,
    color: 0xffffff,
    size,
    sizeAttenuation: true,
    transparent: true,
    opacity: 0.95,
    depthWrite: false,
  });

  const stars = new THREE.Points(starGeometry, starMaterial);
  scene.add(stars);
  return stars;
}

const starsLayers = [
  createStarsLayer(1200, 0.4),
  createStarsLayer(600, 0.8),
  createStarsLayer(240, 1.4),
  createStarsLayer(200, 6.4),
  createStarsLayer(50, 10.4),
];

/* SPOLEČNÝ GLOW */

const glowTexture = textureLoader.load(
  "https://raw.githubusercontent.com/mrdoob/three.js/master/examples/textures/lensflare/lensflare0_alpha.png"
);

/* =========================================================
   PLANETA #1 – zprava doleva (nejblíž a nejčastěji)
   ========================================================= */

const planet1Texture = textureLoader.load("../Obrázky/liveplanet1.jpg");

const planet1Radius = 8;
const PLANET1_START_X = 120;
const PLANET1_END_X   = -120;
const PLANET1_Y       = -18;
const PLANET1_Z       = -20;

let planet1Speed      = 1;
let planet1RotSpeedY  = 0.0003;
let planet1RotSpeedX  = 0.0001;

let planet1TimeSinceLastFlight = 0;
let planet1NextFlightDelay     = 4 + Math.random() * 4; // 4–8 s
let planet1IsFlying            = true; // startuje hned

const planet1Geometry = new THREE.SphereGeometry(planet1Radius, 64, 64);
const planet1Material = new THREE.MeshStandardMaterial({
  map: planet1Texture,
  roughness: 0.9,
  metalness: 0.0,
});
const planet1Mesh = new THREE.Mesh(planet1Geometry, planet1Material);
scene.add(planet1Mesh);

const glowMaterial1 = new THREE.SpriteMaterial({
  map: glowTexture,
  color: new THREE.Color(0x88aaff),
  transparent: true,
  opacity: 0.7,
  depthWrite: false,
});
const glowSprite1 = new THREE.Sprite(glowMaterial1);
glowSprite1.scale.set(planet1Radius * 4, planet1Radius * 4, 1);
planet1Mesh.add(glowSprite1);

function resetPlanet1() {
  planet1Mesh.position.set(PLANET1_START_X, PLANET1_Y, PLANET1_Z);
  planet1IsFlying = false;
  planet1TimeSinceLastFlight = 0;
  planet1NextFlightDelay = 4 + Math.random() * 4;
}

/* =========================================================
   PLANETA #2 – zprava doleva (výš a dál)
   ========================================================= */

const planet2Texture = textureLoader.load("../Obrázky/liveplanet2.png");

const planet2Radius = 3;
const PLANET2_START_X = 130;
const PLANET2_END_X   = -130;
const PLANET2_Y       = -10;
const PLANET2_Z       = -35;

let planet2Speed      = 1.0;
let planet2RotSpeedY  = 0.0003;
let planet2RotSpeedX  = 0.0001;

let planet2TimeSinceLastFlight = 0;
let planet2NextFlightDelay     = 16 + Math.random() * 8; // 16–24 s
let planet2IsFlying            = false; // nestartuje hned

const planet2Geometry = new THREE.SphereGeometry(planet2Radius, 64, 64);
const planet2Material = new THREE.MeshStandardMaterial({
  map: planet2Texture,
  roughness: 0.9,
  metalness: 0.0,
});
const planet2Mesh = new THREE.Mesh(planet2Geometry, planet2Material);
scene.add(planet2Mesh);

const glowMaterial2 = new THREE.SpriteMaterial({
  map: glowTexture,
  color: new THREE.Color(0x88ffcc),
  transparent: true,
  opacity: 0.35,
  depthWrite: false,
});
const glowSprite2 = new THREE.Sprite(glowMaterial2);
glowSprite2.scale.set(planet2Radius * 4, planet2Radius * 4, 1);
planet2Mesh.add(glowSprite2);

function resetPlanet2() {
  planet2Mesh.position.set(PLANET2_START_X, PLANET2_Y, PLANET2_Z);
  planet2IsFlying = false;
  planet2TimeSinceLastFlight = 0;
  planet2NextFlightDelay = 16 + Math.random() * 8;
}

/* =========================================================
   PLANETA #3 – zprava doleva (NEJDÁL A NEJPOZDĚJI)
   ========================================================= */

const planet3Texture = textureLoader.load("../Obrázky/gasplanet.png");

const planet3Radius = 3;
const PLANET3_START_X = 140;
const PLANET3_END_X   = -140;
const PLANET3_Y       = -5;
const PLANET3_Z       = -60;

let planet3Speed      = 0.7;
let planet3RotSpeedY  = 0.0004;
let planet3RotSpeedX  = 0.00015;

let planet3TimeSinceLastFlight = 0;
// 60–100 s
let planet3NextFlightDelay     = 60 + Math.random() * 40;
let planet3IsFlying            = false; // nestartuje hned

const planet3Geometry = new THREE.SphereGeometry(planet3Radius, 64, 64);
const planet3Material = new THREE.MeshStandardMaterial({
  map: planet3Texture,
  roughness: 0.9,
  metalness: 0.0,
});
const planet3Mesh = new THREE.Mesh(planet3Geometry, planet3Material);
scene.add(planet3Mesh);

const glowMaterial3 = new THREE.SpriteMaterial({
  map: glowTexture,
  color: new THREE.Color(0xffaa88),
  transparent: true,
  opacity: 0.3,
  depthWrite: false,
});
const glowSprite3 = new THREE.Sprite(glowMaterial3);
glowSprite3.scale.set(planet3Radius * 4, planet3Radius * 4, 1);
planet3Mesh.add(glowSprite3);

function resetPlanet3() {
  planet3Mesh.position.set(PLANET3_START_X, PLANET3_Y, PLANET3_Z);
  planet3IsFlying = false;
  planet3TimeSinceLastFlight = 0;
  planet3NextFlightDelay = 80 + Math.random() * 40; // 80–120 s
}

/* ========================================================= */

const clock = new THREE.Clock();

// počáteční pozice
planet1Mesh.position.set(PLANET1_START_X, PLANET1_Y, PLANET1_Z);
planet2Mesh.position.set(PLANET2_START_X, PLANET2_Y, PLANET2_Z);
planet3Mesh.position.set(PLANET3_START_X, PLANET3_Y, PLANET3_Z);

function animate() {
  requestAnimationFrame(animate);

  const delta = clock.getDelta();
  const time = performance.now() * 0.001;

  camera.lookAt(0, 0, 0);

  // hvězdy – rotace
  for (const layer of starsLayers) {
    layer.rotation.y += 0.00025;
    layer.rotation.x += 0.00005;
  }

  updatePlanet1(delta, time);
  updatePlanet2(delta, time);
  updatePlanet3(delta, time);

  renderer.render(scene, camera);
}

/* LOGIKA PLANETY #1 – zprava doleva */

function updatePlanet1(delta, time) {
  if (!planet1IsFlying) {
    planet1TimeSinceLastFlight += delta;
    if (planet1TimeSinceLastFlight >= planet1NextFlightDelay) {
      planet1IsFlying = true;
      planet1Mesh.position.set(PLANET1_START_X, PLANET1_Y, PLANET1_Z);
    }
    return;
  }

  planet1Mesh.position.x -= planet1Speed * delta;
  planet1Mesh.position.y = PLANET1_Y + Math.sin(time * 0.3) * 2;

  planet1Mesh.rotation.y += planet1RotSpeedY;
  planet1Mesh.rotation.x += planet1RotSpeedX;

  if (planet1Mesh.position.x < PLANET1_END_X) {
    resetPlanet1();
  }
}

/* LOGIKA PLANETY #2 – zprava doleva */

function updatePlanet2(delta, time) {
  if (!planet2IsFlying) {
    planet2TimeSinceLastFlight += delta;
    if (planet2TimeSinceLastFlight >= planet2NextFlightDelay) {
      planet2IsFlying = true;
      planet2Mesh.position.set(PLANET2_START_X, PLANET2_Y, PLANET2_Z);
    }
    return;
  }

  planet2Mesh.position.x -= planet2Speed * delta;
  planet2Mesh.position.y = PLANET2_Y + Math.sin(time * 0.28 + 1.5) * 1.8;

  planet2Mesh.rotation.y += planet2RotSpeedY;
  planet2Mesh.rotation.x += planet2RotSpeedX;

  if (planet2Mesh.position.x < PLANET2_END_X) {
    resetPlanet2();
  }
}

/* LOGIKA PLANETY #3 – zprava doleva, nejdál a nejpozději */

function updatePlanet3(delta, time) {
  if (!planet3IsFlying) {
    planet3TimeSinceLastFlight += delta;
    if (planet3TimeSinceLastFlight >= planet3NextFlightDelay) {
      planet3IsFlying = true;
      planet3Mesh.position.set(PLANET3_START_X, PLANET3_Y, PLANET3_Z);
    }
    return;
  }

  planet3Mesh.position.x -= planet3Speed * delta;
  planet3Mesh.position.y = PLANET3_Y + Math.sin(time * 0.22 + 3.1) * 1.5;

  planet3Mesh.rotation.y += planet3RotSpeedY;
  planet3Mesh.rotation.x += planet3RotSpeedX;

  if (planet3Mesh.position.x < PLANET3_END_X) {
    resetPlanet3();
  }
}

animate();

/* RESIZE */

window.addEventListener("resize", () => {
  const w = window.innerWidth;
  const h = window.innerHeight;
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  renderer.setSize(w, h);
});