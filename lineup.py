// =====================================
// GLOBAL STATE
// =====================================
let currentCaptain = null;
let assignedPlayers = {};
let drawingMode = false;
let connections = [];
let selectedSlot = null;
let freeDrawMode = false;
let isDrawing = false;
let currentPath = null;
let ballElement = null;
let isExporting = false; // prevents double export
// =====================================
// ENSURE SVG LAYER
// =====================================
function ensureSvgLayer() {
 const pitch = document.querySelector(".pitch");
 if (!pitch) return null;
 let svg = pitch.querySelector("#lines-layer");
 if (!svg) {
   svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
svg.id = "lines-layer";
   Object.assign(svg.style, {
     position: "absolute",
     top: 0,
     left: 0,
     width: "100%",
     height: "100%",
     pointerEvents: "none",
     zIndex: 5
   });
   pitch.appendChild(svg);
 }
 return svg;
}
// =====================================
// INIT
// =====================================
document.addEventListener("DOMContentLoaded", () => {
 ensureSvgLayer();
 document.querySelectorAll(".position-slot").forEach(slot => {
   slot.setAttribute("draggable", "true");
 });
 const observer = new MutationObserver(() => {
   const proxy = document.querySelector("#captain-proxy");
   if (!proxy) return;
   const newCaptain = proxy.textContent;
   if (newCaptain !== currentCaptain) {
     currentCaptain = newCaptain;
     updateAllCaptains();
   }
 });
 observer.observe(document.body, { subtree: true, childList: true });
});
// =====================================
// UPDATE CAPTAINS
// =====================================
function updateAllCaptains() {
 Object.keys(assignedPlayers).forEach(player => {
   const slot = assignedPlayers[player];
   if (slot) renderPlayerInSlot(slot, player);
 });
}
// =====================================
// DRAG START (SUPER FIXED)
// =====================================
document.addEventListener("dragstart", (e) => {
 const slot = e.target.closest(".position-slot");
 const ball = e.target.closest(".ball");
 // PLAYER FROM TABLE
 if (e.target.classList.contains("draggable-player")) {
   e.dataTransfer.setData("type", "player");
   e.dataTransfer.setData("player", e.target.dataset.player);
   return;
 }
 // SLOT MOVE
 if (slot && slot.classList.contains("filled")) {
   e.dataTransfer.setData("type", "slot-move");
   e.dataTransfer.setData("player", slot.dataset.player);
   const rect = slot.getBoundingClientRect();
   e.dataTransfer.setData("offsetX", e.clientX - rect.left);
   e.dataTransfer.setData("offsetY", e.clientY - rect.top);
   return;
 }
 // BALL MOVE
 if (ball) {
   e.dataTransfer.setData("type", "ball-move");
   const rect = ball.getBoundingClientRect();
   e.dataTransfer.setData("offsetX", e.clientX - rect.left);
   e.dataTransfer.setData("offsetY", e.clientY - rect.top);
   return;
 }
});
// =====================================
// Allow drag everywhere on pitch
// =====================================
document.addEventListener("dragover", (e) => {
 e.preventDefault(); // THIS is what enables movement
});
// =====================================
// DROP
// =====================================
document.addEventListener("drop", (e) => {
 e.preventDefault();
 const type = e.dataTransfer.getData("type");
 const playerName = e.dataTransfer.getData("player");
 const slot = e.target.closest(".position-slot");
 const table = e.target.closest(".player-table");
 const pitch = document.querySelector(".pitch");
 // PLAYER → SLOT
 if (type === "player" && slot) {
   if (assignedPlayers[playerName]) {
     clearSlot(assignedPlayers[playerName]);
   }
   if (slot.classList.contains("filled")) {
     unassignPlayer(slot.dataset.player);
   }
   renderPlayerInSlot(slot, playerName);
   assignedPlayers[playerName] = slot;
   fadeRow(playerName);
   updateLines();
 }
 // MOVE SLOT
 if (type === "slot-move" && pitch) {
   const movingSlot = assignedPlayers[playerName];
   if (!movingSlot) return;
   const rect = pitch.getBoundingClientRect();
   const x = ((e.clientX - rect.left) / rect.width) * 100;
   const y = ((e.clientY - rect.top) / rect.height) * 100;
   movingSlot.style.left = `${x}%`;
   movingSlot.style.top = `${y}%`;
   updateLines();
 }
 // BACK TO TABLE
 if (type === "player" && table) {
   unassignPlayer(playerName);
   updateLines();
 }
});
// =====================================
// CLICK HANDLER
// =====================================
document.addEventListener("click", function (e) {

 const slot = e.target.closest(".position-slot");

// EXPORT
if (e.target.id === "export-btn") {
   const pitch = document.querySelector(".pitch");
   if (!pitch) return alert("Pitch not found");
   if (typeof html2canvas === "undefined") return alert("html2canvas missing");
   let formation = document.querySelector("#formation-proxy")?.textContent || "lineup";
   let captain = document.querySelector("#captain-proxy")?.textContent || "no-captain";
   const fileName = `lineup_${formation}_${captain}`
     .replace(/\s+/g, "_")
     .replace(/[^a-z0-9_\-]/gi, "")
     .toLowerCase() + ".png";
   // Force repaint for labels
   document.querySelectorAll(".player-label").forEach(el => {
     el.style.opacity = "0.99";
   });
   pitch.offsetHeight;
   setTimeout(() => {
     html2canvas(pitch, {
       useCORS: true,
       backgroundColor: null,
       scale: 3
     }).then(canvas => {
       const link = document.createElement("a");
       link.download = fileName;
       link.href = canvas.toDataURL("image/png");
       link.click();
     });
   }, 400);
   return;
 }

 // BUTTONS
 if (e.target.id === "draw-lines-btn") {
   drawingMode = !drawingMode;
   freeDrawMode = false;
   selectedSlot = null;
   return;
 }

 if (e.target.id === "free-draw-btn") {
   freeDrawMode = !freeDrawMode;
   drawingMode = false;
   return;
 }

 if (e.target.id === "clear-draw-btn") {
   const svg = ensureSvgLayer();
   if (svg) svg.innerHTML = "";
   connections = [];
   return;
 }

 // BALL
if (e.target.id === "add-ball-btn") {
    if (ballElement) return;
    
    const pitch = document.querySelector(".pitch");
    
    const ball = document.createElement("img");
    ball.src = "/assets/ball.png";
    ball.className = "ball";
    
    ball.draggable = true;
    ball.style.position = "absolute";
    ball.style.left = "50%";
    ball.style.top = "50%";
    ball.style.width = "30px";
    ball.style.height = "30px";
    ball.style.marginLeft = "-15px";
    ball.style.marginTop = "-15px";

    pitch.appendChild(ball);
    ballElement = ball;
    
    return;
}

 if (e.target.classList.contains("ball")) {
   e.target.remove();
   ballElement = null;
   return;
 }

 // DRAW CONNECTIONS
 if (drawingMode && slot && slot.classList.contains("filled")) {

   if (!selectedSlot) {
     selectedSlot = slot;
     slot.classList.add("selected-line");
     return;
   }

   if (selectedSlot === slot) {
     selectedSlot.classList.remove("selected-line");
     selectedSlot = null;
     return;
   }

   connections.push([selectedSlot, slot]);

   selectedSlot.classList.remove("selected-line");
   selectedSlot = null;

   drawLines();
   return;
 }

 // REMOVE PLAYER
 if (!drawingMode && slot && slot.classList.contains("filled")) {
   unassignPlayer(slot.dataset.player);
   updateLines();
 }
});
// =====================================
// BALL DRAG (REAL FIX)
// =====================================
let isDraggingBall = false;
let ballOffsetX = 0;
let ballOffsetY = 0;

document.addEventListener("mousedown", (e) => {
    if (!e.target.classList.contains("ball")) return;
    
    const ball = e.target;
    const rect = ball.getBoundingClientRect();
    
    isDraggingBall = true;
    ballOffsetX = e.clientX - rect.left;
    ballOffsetY = e.clientY - rect.top;
    
    e.preventDefault();
});

document.addEventListener("mousemove", (e) => {
    if (!isDraggingBall || !ballElement) return;
    
    const pitch = document.querySelector(".pitch");
    const rect = pitch.getBoundingClientRect();
    
    const x = ((e.clientX - rect.left - ballOffsetX) / rect.width) * 100;
    const y = ((e.clientY - rect.top - ballOffsetY) / rect.height) * 100;
    
    ballElement.style.left = `${x}%`;
    ballElement.style.top = `${y}%`;
});

document.addEventListener("mouseup", () => {
    isDraggingBall = false;
});

// =====================================
// FREE DRAW
// =====================================
document.addEventListener("mousedown", function (e) {
 if (!freeDrawMode) return;

 const pitch = document.querySelector(".pitch");
 if (!pitch || !pitch.contains(e.target)) return;

 const svg = ensureSvgLayer();

 isDrawing = true;

 const rect = pitch.getBoundingClientRect();

 const x = e.clientX - rect.left;
 const y = e.clientY - rect.top;

 currentPath = document.createElementNS("http://www.w3.org/2000/svg", "path");

 currentPath.setAttribute("d", `M ${x} ${y}`);
 currentPath.setAttribute("stroke", "red");
 currentPath.setAttribute("stroke-width", "3");
 currentPath.setAttribute("fill", "none");

 svg.appendChild(currentPath);
});

document.addEventListener("mousemove", function (e) {
 if (!isDrawing || !currentPath) return;

 const pitch = document.querySelector(".pitch");
 const rect = pitch.getBoundingClientRect();

 const x = e.clientX - rect.left;
 const y = e.clientY - rect.top;

 const d = currentPath.getAttribute("d");
 currentPath.setAttribute("d", d + ` L ${x} ${y}`);
});

document.addEventListener("mouseup", function () {
 isDrawing = false;
 currentPath = null;
});

// =====================================
// DRAW LINES
// =====================================
function drawLines() {
 const svg = ensureSvgLayer();
 if (!svg) return;

 svg.innerHTML = "";

 const pitch = document.querySelector(".pitch");
 const pitchRect = pitch.getBoundingClientRect();

 connections.forEach(([a, b]) => {
   if (!a || !b) return;

   const r1 = a.getBoundingClientRect();
   const r2 = b.getBoundingClientRect();

   const x1 = r1.left + r1.width / 2 - pitchRect.left;
   const y1 = r1.top + r1.height / 2 - pitchRect.top;

   const x2 = r2.left + r2.width / 2 - pitchRect.left;
   const y2 = r2.top + r2.height / 2 - pitchRect.top;

   const line = document.createElementNS("http://www.w3.org/2000/svg", "line");

   line.setAttribute("x1", x1);
   line.setAttribute("y1", y1);
   line.setAttribute("x2", x2);
   line.setAttribute("y2", y2);

   line.setAttribute("stroke", "yellow");
   line.setAttribute("stroke-width", "3");

   svg.appendChild(line);
 });
}

function updateLines() {
 drawLines();
}
// =====================================
// PLAYER RENDER
// =====================================
function renderPlayerInSlot(slot, player) {
 slot.innerHTML = "";
 const img = document.createElement("img");
 
 if (player === currentCaptain) {
 img.src = "/assets/captain.png";
 slot.classList.add("captain");
} else {
 img.src = "/assets/player.png";
 slot.classList.remove("captain");
}

 img.className = "jersey";
 const label = document.createElement("div");
 label.className = "player-label";
 label.innerText = player;
 Object.assign(label.style, {
   position: "absolute",
   bottom: "-18px",
   width: "100%",
   textAlign: "center",
   color: "white"
 });
 slot.appendChild(img);
 slot.appendChild(label);
 slot.classList.add("filled");
 slot.dataset.player = player;
 slot.draggable = true;
}
// =====================================
// CLEAR SLOT
// =====================================
function clearSlot(slot) {
 const pos = slot.dataset.original;
 slot.innerHTML = `
<img src="/assets/player.png" class="jersey">
<div class="position-label">${pos}</div>
 `;
 slot.classList.remove("filled");
 delete slot.dataset.player;
}
// =====================================
// ASSIGN / UNASSIGN
// =====================================
function unassignPlayer(player) {
 const slot = assignedPlayers[player];
 if (!slot) return;
 clearSlot(slot);
 delete assignedPlayers[player];
 unfadeRow(player);
}
// =====================================
// TABLE UI
// =====================================
function fadeRow(player) {
 document.querySelector(`[data-player-row="${player}"]`)
   ?.classList.add("player-unavailable");
}
function unfadeRow(player) {
 document.querySelector(`[data-player-row="${player}"]`)
   ?.classList.remove("player-unavailable");
}
