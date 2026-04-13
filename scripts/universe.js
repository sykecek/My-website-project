const canvas = document.getElementById("universe-bg");
const ctx = canvas.getContext("2d");

let width = window.innerWidth;
let height = window.innerHeight;

canvas.width = width;
canvas.height = height;

window.addEventListener("resize", () => {
  width = window.innerWidth;
  height = window.innerHeight;
  canvas.width = width;
  canvas.height = height;
  initStars();
});

// ====== STATIC STARS ======

const STAR_COUNT = 300;
const stars = [];

function initStars() {
  stars.length = 0;
  for (let i = 0; i < STAR_COUNT; i++) {
    stars.push({
      x: Math.random() * width,
      y: Math.random() * height,
      radius: Math.random() * 1.2 + 0.3,
      alphaBase: Math.random() * 0.5 + 0.4,
      twinkleSpeed: Math.random() * 0.0015 + 0.0005,
      twinkleOffset: Math.random() * Math.PI * 2,
    });
  }
}

// ====== SHOOTING STARS ======

const shootingStars = [];
let lastShootTime = 0;

function spawnShootingStar(time) {
  // ~4 za 10 s
  if (time - lastShootTime < 1500) return;
  if (Math.random() > 0.02) return;

  lastShootTime = time;

  const scenario = Math.floor(Math.random() * 3); // 0,1,2

  let startX, startY, angleDeg;

  const length = 200 + Math.random() * 150;
  const speed = 600 + Math.random() * 200;

  if (scenario === 0) {
    // zleva doprava dolů
    startX = -100;
    startY = Math.random() * (height * 0.7);
    angleDeg = 20 + Math.random() * 20; // 20–40°
  } else if (scenario === 1) {
    // zprava doleva dolů
    startX = width + 100;
    startY = Math.random() * (height * 0.7);
    angleDeg = 160 + Math.random() * 20; // 160–180° (šikmo vlevo dolů)
  } else {
    // shora dolů mírně doprava nebo doleva
    startX = Math.random() * width;
    startY = -80;
    angleDeg = 80 + Math.random() * 20; // 80–100° (téměř svisle)
  }

  const angle = (Math.PI / 180) * angleDeg;
  const vx = Math.cos(angle) * speed;
  const vy = Math.sin(angle) * speed;

  shootingStars.push({
    x: startX,
    y: startY,
    vx,
    vy,
    length,
    life: 0,
    maxLife: 1.2 + Math.random() * 0.6,
  });
}

// ====== RENDER LOOP ======

let lastTime = performance.now();

function render(now) {
  requestAnimationFrame(render);

  const delta = (now - lastTime) / 1000;
  lastTime = now;

  const gradient = ctx.createRadialGradient(
    width * 0.5,
    height * 0.2,
    0,
    width * 0.5,
    height * 0.6,
    Math.max(width, height)
  );
  gradient.addColorStop(0, "#05051a");
  gradient.addColorStop(1, "#000000");
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, width, height);

  drawStars(now);
  updateAndDrawShootingStars(delta, now);
}

function drawStars(time) {
  for (const s of stars) {
    const twinkle = Math.sin(time * s.twinkleSpeed + s.twinkleOffset) * 0.3;
    const alpha = Math.max(0, Math.min(1, s.alphaBase + twinkle));

    ctx.beginPath();
    ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
    ctx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
    ctx.fill();
  }
}

function updateAndDrawShootingStars(delta, now) {
  spawnShootingStar(now);

  for (let i = shootingStars.length - 1; i >= 0; i--) {
    const s = shootingStars[i];
    s.life += delta;

    if (s.life > s.maxLife) {
      shootingStars.splice(i, 1);
      continue;
    }

    s.x += s.vx * delta;
    s.y += s.vy * delta;

    const progress = s.life / s.maxLife;
    const opacity = 1 - progress;

    const len = s.length * (1 - progress * 0.6);
    const mag = Math.hypot(s.vx, s.vy) || 1;
    const tailX = s.x - (s.vx / mag) * len;
    const tailY = s.y - (s.vy / mag) * len;

    const grad = ctx.createLinearGradient(s.x, s.y, tailX, tailY);
    grad.addColorStop(0, `rgba(120, 210, 255, ${opacity})`);
    grad.addColorStop(1, `rgba(120, 210, 255, 0)`);

    ctx.strokeStyle = grad;
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(s.x, s.y);
    ctx.lineTo(tailX, tailY);
    ctx.stroke();
  }
}

initStars();
requestAnimationFrame((t) => {
  lastTime = t;
  render(t);
});