/* TABLE */
.player-table th,
.player-table td {
   text-align: center !important;
   vertical-align: middle !important;
}
.flag {
   width: 28px;
   height: 18px;
   object-fit: cover;
   border-radius: 3px;
   box-shadow: 0 0 3px rgba(0,0,0,0.3);
}
.star {
   cursor: pointer;
   font-size: 18px;
}
.captain-row {
   background-color: rgba(255, 215, 0, 0.25) !important;
   font-weight: bold;
}

/* FADE */
.player-unavailable {
   opacity: 0.35 !important;
   filter: grayscale(80%);
   transition: 0.2s ease;
}

/* PITCH */
.pitch {
   position: relative;
   width: 100%;
   height: 650px;
   z-index: 1;
   overflow: hidden;
   aspect-ratio: 16 / 9; /* maintains proper proportions */
   background-image: url("/assets/pitch.png");
   background-size: 100% 100%;
   background-position: center;
   background-repeat: no-repeat;
}

.pitch-bg {
   position: absolute;
   width: 100%;
   height: 100%;
   object-fit: contain;
   z-index: 0;
}

.positions-layer {
   position: absolute;
   width: 100%;
   height: 100%;
   z-index: 2;
}

/* PLAYER SLOT */
.position-slot {
   position: absolute;
   transform: translate(-50%, -50%);
   width: 90px;
   height: 90px;
   border-radius: 50%;
   text-align: center;
   line-height: 65px;
   font-weight: bold;
   cursor: pointer;
   z-index: 10;
}

.jersey-img {
   width: 100%;
}
.position-label {
   position: absolute;
   top: 1px;
   width: 100%;
   font-size: 14px;
   color: white;
}

.player-name {
   position: absolute;
   bottom: -18px;
   width: 100%;
   font-size: 15px;
   color: white;
   z-index: 2;
   pointer-events: none;
}
/* CAPTAIN */
.position-slot.captain .jersey-img {
   filter: drop-shadow(0 0 6px gold);
}
.captain-badge {
   position: absolute;
   top: -6px;
   right: -6px;
   width: 22px;
   height: 22px;
   color: black;
   font-weight: bold;
   border-radius: 50%;
   font-size: 12px;
   line-height: 22px;
}

.jersey {
   width: 90px;
   height: 90px;
}

.player-label {
   font-size: 15px;
   margin-top: -75px;
   width: 100%;
   will-change: transform;
   transform: translateZ(0);
   text-align: center;
   color: white;
}

.position-slot {
   cursor: grab;
}

.position-slot:active {
   cursor: grabbing;
}

/* SCROLLABLE TABLE CONTAINER */
.table-container {
   max-height: 500px;   /* adjust based on your layout */
   overflow-y: auto;
   position: relative;
   border: 1px solid rgba(0,0,0,0.1);
}
/* STICKY HEADER */
.player-table thead th {
   position: sticky;
   top: 0;
   z-index: 5;
}
/* Prevent row overlap */
.player-table {
   border-collapse: separate;
   border-spacing: 0;
}

/* SVG overlay */
.connections-layer {
   position: absolute;
   width: 100%;
   height: 100%;
   pointer-events: none; /* allows clicks to pass through */
   z-index: 2;
}
/* Lines */
.connection-line {
   stroke: #ffffff;
   stroke-width: 3;
   opacity: 0.8;
   pointer-events: auto;
   cursor: pointer;
}
/* Optional glow */
.connection-line {
   filter: drop-shadow(0 0 4px #00d4ff);
}
/* When drawing mode active */
.drawing-mode .position-slot {
   cursor: crosshair;
}

.selected-line {
   outline: 3px dashed white;
   box-shadow: 0 0 10px white;
}

#lines-layer {
   pointer-events: none;
   z-index: 5;
}

.free-draw-active {
   cursor: crosshair;
}

.ball {
   position: absolute;
   pointer-events: auto;
   width: 28px;
   height: 28px;
   cursor: grab;
   z-index: 10;
}
