// =====================================
// FORMATIONS
// =====================================
const FORMATIONS = {
    "4-3-3 (Single Pivot)": [
        ["GK", 5, 50],
        ["LB", 20, 10],
        ["CB", 14, 35],
        ["CB", 14, 65],
        ["RB", 20, 90],
        ["CM", 55, 30],
        ["CDM", 39.5, 50],
        ["CM", 55, 70],
        ["LW", 68, 10],
        ["CF", 77, 50],
        ["RW", 68, 90]
    ],
    "4-3-3 (Double Pivot)": [
       ["GK", 5, 50],
       ["LB", 20, 10], 
       ["CB", 14, 35],
       ["CB", 14, 65], 
       ["RB", 20, 90],
       ["CDM", 39.5, 65], 
       ["CDM", 39.5, 35], 
       ["CAM", 62, 50],
       ["LW", 68, 10], 
       ["CF", 77, 50], 
       ["RW", 68, 90],
   ],
   "4-4-2": [
       ["GK", 5, 50],
       ["LB", 20, 10], 
       ["CB", 14, 35],
       ["CB", 14, 65], 
       ["RB", 20, 90],
       ["LM", 62, 10], 
       ["CM", 39.5, 35],
       ["CM", 39.5, 65], 
       ["RM", 62, 90],
       ["ST", 77, 65], 
       ["ST", 77, 35],
   ],
   "4-4-2 (Diamond)": [
       ["GK", 5, 50],
       ["LB", 20, 10], 
       ["CB", 14, 35],
       ["CB", 14, 65], 
       ["RB", 20, 90],
       ["CDM", 39.5, 50],
       ["LCM", 53, 30], 
       ["RCM", 53, 70],
       ["CAM", 62, 50],
       ["ST", 77, 35], 
       ["ST", 77, 65],
   ],
   "4-4-1-1": [
       ["GK", 5, 50],
       ["LB", 20, 10], 
       ["CB", 14, 35],
       ["CB", 14, 65], 
       ["RB", 20, 90],
       ["LM", 58, 15], 
       ["LCM", 39.5, 35],
       ["RCM", 39.5, 65], 
       ["RM", 58, 85],
       ["CAM", 62, 50],
       ["CF", 77, 50],
   ],
   "4-3-2-1": [
       ["GK", 5, 50],
       ["LB", 20, 10], 
       ["CB", 14, 35],
       ["CB", 14, 65], 
       ["RB", 20, 90],
       ["LCM", 53, 30], 
       ["CDM", 39.5, 50],
       ["RCM", 53, 70],
       ["LAM", 68, 35], 
       ["RAM", 68, 65],
       ["CF", 77, 50],
   ],
   "4-2-3-1": [
       ["GK", 5, 50],
       ["LB", 20, 10], 
       ["CB", 14, 35],
       ["CB", 14, 65], 
       ["RB", 20, 90],
       ["CDM", 39.5, 35], 
       ["CDM", 39.5, 65],
       ["LW", 58, 10], 
       ["CAM", 62, 50], 
       ["RW", 58, 90],
       ["CF", 77, 50],
   ],
   "4-5-1": [
       ["GK", 5, 50],
       ["LB", 20, 10], 
       ["CB", 14, 35],
       ["CB", 14, 65], 
       ["RB", 20, 90],
       ["LM", 62, 10],
       ["LCM", 53, 35], 
       ["CDM", 39.5, 50], 
       ["RCM", 53, 65],
       ["RM", 62, 90],
       ["CF", 77, 50],
   ],
   "3-4-3": [
       ["GK", 5, 50],
       ["LCB", 14, 25], 
       ["CB", 14, 50], 
       ["RCB", 14, 75],
       ["LM", 53, 20], 
       ["LCM", 39.5, 35],
       ["RCM", 39.5, 65], 
       ["RM", 53, 80],
       ["LW", 68, 10], 
       ["CF", 77, 50], 
       ["RW", 68, 90],
   ],
   "3-5-2": [
       ["GK", 5, 50],
       ["LCB", 14, 25], 
       ["CB", 14, 50], 
       ["RCB", 14, 75],
       ["LM", 62, 10],
       ["LCM", 53, 35], 
       ["CDM", 39.5, 50], 
       ["RCM", 53, 65],
       ["RM", 62, 90],
       ["ST", 77, 35], 
       ["ST", 77, 65],
   ],
   "3-6-1": [
       ["GK", 5, 50],
       ["LCB", 14, 25], 
       ["CB", 14, 50], 
       ["RCB", 14, 75],
       ["LM", 62, 10],
       ["LCM", 53, 30], 
       ["CDM", 39.5, 50], 
       ["RCM", 53, 70],
       ["RM", 62, 90],
       ["CAM", 62, 50],
       ["CF", 77, 50],
   ],
   "5-3-2": [
       ["GK", 5, 50],
       ["LWB", 28, 10],
       ["LCB", 14, 30], 
       ["CB", 14, 50], 
       ["RCB", 14, 70],
       ["RWB", 28, 90],
       ["LCM", 53, 30], 
       ["CDM", 39.5, 50], 
       ["RCM", 53, 70],
       ["ST", 77, 35], 
       ["ST", 77, 65],
   ],
   "5-4-1": [
       ["GK", 5, 50],
       ["LWB", 28, 10],
       ["LCB", 14, 30], 
       ["CB", 14, 50], 
       ["RCB", 14, 70],
       ["RWB", 28, 90],
       ["LM", 62, 15], 
       ["LCM", 39.5, 35],
       ["RCM", 39.5, 65], 
       ["RM", 62, 85],
       ["CF", 77, 50],
   ],
};
const MOBILE_FORMATIONS = {
    "4-3-3 (Single Pivot)": [
        ["GK", 13, 42],
        ["LB", 30, 4],
        ["CB", 22, 25],
        ["CB", 22, 60],
        ["RB", 30, 80],
        ["CM", 43, 25],
        ["CDM", 31, 42],
        ["CM", 43, 60],
        ["LW", 62, 4],
        ["CF", 68, 42],
        ["RW", 62, 80]
    ],
    "4-3-3 (Double Pivot)": [
        ["GK", 13, 42],
        ["LB", 30, 4],
        ["CB", 22, 25],
        ["CB", 22, 60],
        ["RB", 30, 80],
        ["CDM", 34, 28],
        ["CDM", 34, 56],
        ["CAM", 47, 42],
        ["LW", 62, 4],
        ["CF", 68, 42],
        ["RW", 62, 80]
    ],
    "4-4-2": [
        ["GK", 13, 42],
        ["LB", 30, 4],
        ["CB", 22, 25],
        ["CB", 22, 60],
        ["RB", 30, 80],
        ["LM", 62, 4],
        ["CM", 43, 25],
        ["CM", 43, 60],
        ["RM", 62, 80],
        ["ST", 68, 30],
        ["ST", 68, 54]
    ],
    "4-4-2 (Diamond)": [
        ["GK", 13, 42],
        ["LB", 30, 4],
        ["CB", 22, 25],
        ["CB", 22, 60],
        ["RB", 30, 80],
        ["CDM", 33, 42],
        ["LCM", 49, 20],
        ["RCM", 49, 65],
        ["CAM", 55, 42],
        ["ST", 68, 30],
        ["ST", 68, 54]
    ],
    "4-4-1-1": [
        ["GK", 13, 42],
        ["LB", 30, 4],
        ["CB", 22, 25],
        ["CB", 22, 60],
        ["RB", 30, 80],
        ["LM", 62, 4],
        ["LCM", 41, 25],
        ["RCM", 41, 60],
        ["RM", 62, 80],
        ["CAM", 49, 42],
        ["CF", 68, 42]
    ],
    "4-3-2-1": [
        ["GK", 13, 42],
        ["LB", 30, 4],
        ["CB", 22, 25],
        ["CB", 22, 60],
        ["RB", 30, 80],
        ["LCM", 44, 19],
        ["CDM", 39, 42],
        ["RCM", 44, 66],
        ["LAM", 61, 23],
        ["RAM", 61, 61],
        ["CF", 68, 42]
    ],
    "4-2-3-1": [
        ["GK", 13, 42],
        ["LB", 30, 4],
        ["CB", 22, 25],
        ["CB", 22, 60],
        ["RB", 30, 80],
        ["CDM", 36, 28],
        ["CDM", 36, 56],
        ["LW", 61, 4],
        ["CAM", 49, 42],
        ["RW", 61, 80],
        ["CF", 68, 42]
    ],
    "4-4-1": [
        ["GK", 13, 42],
        ["LB", 30, 4],
        ["CB", 22, 25],
        ["CB", 22, 60],
        ["RB", 30, 80],
        ["LM", 63, 4],
        ["LCM", 50, 25],
        ["CDM", 39, 42],
        ["RCM", 50, 60],
        ["RM", 63, 80],
        ["CF", 68, 42]
    ],
    "3-4-3": [
        ["GK", 13, 42],
        ["LCB", 28, 18],
        ["CB", 28, 42],
        ["RCB", 28, 66],
        ["LM", 49, 10],
        ["LCM", 41, 28],
        ["RCM", 41, 56],
        ["RM", 49, 74],
        ["LW", 61, 4],
        ["CF", 68, 42],
        ["RW", 61, 80]
    ],
    "3-5-2": [
        ["GK", 13, 42],
        ["LCB", 28, 18],
        ["CB", 28, 42],
        ["RCB", 28, 66],
        ["LM", 61, 4],
        ["LCM", 49, 25],
        ["CDM", 41, 42],
        ["RCM", 49, 60],
        ["RM", 61, 80],
        ["ST", 68, 30],
        ["ST", 68, 54]
    ],
    "3-6-1": [
        ["GK", 13, 42],
        ["LCB", 28, 18],
        ["CB", 28, 42],
        ["RCB", 28, 66],
        ["LM", 61, 4],
        ["LCM", 49, 22],
        ["CDM", 41, 42],
        ["RCM", 49, 62],
        ["RM", 61, 80],
        ["CAM", 55, 42],
        ["CF", 68, 42]
    ],
    "5-3-2": [
        ["GK", 13, 42],
        ["LWB", 39, 2],
        ["LCB", 28, 20],
        ["CB", 28, 42],
        ["RCB", 28, 64],
        ["RWB", 39, 82],
        ["LCM", 49, 24],
        ["CDM", 41, 42],
        ["RCM", 49, 60],
        ["ST", 68, 30],
        ["ST", 68, 54]
    ],
    "5-4-1": [
        ["GK", 13, 42],
        ["LWB", 39, 2],
        ["LCB", 28, 20],
        ["CB", 28, 42],
        ["RCB", 28, 64],
        ["RWB", 39, 82],
        ["LM", 61, 4],
        ["LCM", 47, 25],
        ["RCM", 47, 60],
        ["RM", 61, 80],
        ["CF", 68, 42]
    ]
};
// =====================================
// COLLISION DISTANCE
// =====================================
function getMinPlayerDistance() {

    // Smaller spacing for mobile
    if (isMobileView()) {
        return 6.5;
    }

    // Default desktop spacing
    return 12;
}
// =====================================
// MOBILE ADAPTIVE COORDINATES
// =====================================
function isMobileView() {
    return window.innerWidth <= 768;
}
// =====================================
// MOBILE FORMATION TRANSFORM
// =====================================
function transformMobileCoordinate(x, y) {

    // DESKTOP
    if (!isMobileView()) {
        return { x, y };
    }

    // =====================================
    // MOBILE X TRANSFORM
    // =====================================

    // Compress vertically
    let mobileX =
        (x * 0.78) - 1;

    // =====================================
    // MOBILE Y TRANSFORM
    // =====================================

    let mobileY;

    // Left side
    if (y < 50) {

        mobileY =
            42 - ((50 - y) * 0.76);

    // Right side
    } else {

        mobileY =
            42 + ((y - 50) * 0.76);
    }

    return {
        x: mobileX,
        y: mobileY
    };
}
function getCurrentFormationName() {

    const proxy =
        document.querySelector("#formation-proxy");

    return proxy?.textContent?.trim() ||
        "4-3-3 (Single Pivot)";
}
function getMobileFormationCoordinates(formationName) {

    if (!isMobileView()) {
        return null;
    }

    return MOBILE_FORMATIONS[formationName] || null;
}
function getResponsiveCoordinate(formationName, index, x, y) {

    const mobileFormation =
        getMobileFormationCoordinates(formationName);

    if (
        mobileFormation &&
        mobileFormation[index]
    ) {
        return {
            x: mobileFormation[index][1],
            y: mobileFormation[index][2]
        };
    }

    return transformMobileCoordinate(x, y);
}
function applyPlayerResponsivePositions() {

    const formationName =
        getCurrentFormationName();

    document.querySelectorAll(".position-slot").forEach((slot, index) => {

        if (slot.dataset.manualPosition === "true") {
            return;
        }

        const originalX =
            parseFloat(slot.dataset.x || slot.style.left);

        const originalY =
            parseFloat(slot.dataset.y || slot.style.top);

        if (
            isNaN(originalX) ||
            isNaN(originalY)
        ) return;

        let nextX = originalX;
        let nextY = originalY;

        if (isMobileView()) {

            const slotIndex =
                Number.parseInt(
                    slot.dataset.index ?? index,
                    10
                );

            const mobileX =
                parseFloat(slot.dataset.mobileX);

            const mobileY =
                parseFloat(slot.dataset.mobileY);

            if (
                !isNaN(mobileX) &&
                !isNaN(mobileY)
            ) {
                nextX = mobileX;
                nextY = mobileY;
            } else {
                const transformed =
                    getResponsiveCoordinate(
                        formationName,
                        slotIndex,
                        originalX,
                        originalY
                    );

                nextX = transformed.x;
                nextY = transformed.y;
            }
        }

        slot.style.left = `${nextX}%`;
        slot.style.top = `${nextY}%`;
    });
}
// =====================================
// MIRROR POSITION FOR OPPONENTS
// =====================================
function mirrorPosition(position) {

    const swaps = {
        "LB": "RB",
        "RB": "LB",

        "LWB": "RWB",
        "RWB": "LWB",

        "LCB": "RCB",
        "RCB": "LCB",

        "LCM": "RCM",
        "RCM": "LCM",

        "LM": "RM",
        "RM": "LM",

        "LW": "RW",
        "RW": "LW",

        "LAM": "RAM",
        "RAM": "LAM",

        "LS": "RS",
        "RS": "LS"
    };

    return swaps[position] || position;
}
// =====================================
// OPPONENT COLLISION RESOLUTION
// =====================================
function resolveOpponentCollisions(
    opponentX,
    opponentY
) {

    const slots =
        document.querySelectorAll(
            ".position-slot"
        );
    
    const opponentSlots =
    document.querySelectorAll(
        ".opponent-slot"
    );

    let adjustedX = opponentX;
    let adjustedY = opponentY;

    const minDistance = getMinPlayerDistance();

    slots.forEach(slot => {

        const x =
            parseFloat(slot.style.left || slot.dataset.x);

        const y =
            parseFloat(slot.style.top || slot.dataset.y);

        if (
            isNaN(x) ||
            isNaN(y)
        ) return;

        const dx = adjustedX - x;
        const dy = adjustedY - y;

        const distance =
            Math.sqrt(dx * dx + dy * dy);

        if (
            distance <
            minDistance
        ) {

            const angle =
                Math.atan2(dy, dx);

            const push =
                minDistance - distance;

            adjustedX +=
                Math.cos(angle) * push;

            adjustedY +=
                Math.sin(angle) * push;
        }
    });

    opponentSlots.forEach(slot => {

    const x =
        parseFloat(slot.style.left || slot.dataset.x);

    const y =
        parseFloat(slot.style.top || slot.dataset.y);

    if (
        isNaN(x) ||
        isNaN(y)
    ) return;

    const dx = adjustedX - x;
    const dy = adjustedY - y;

    const distance =
        Math.sqrt(dx * dx + dy * dy);

    if (
        distance <
        minDistance
    ) {

        const angle =
            Math.atan2(dy, dx);

        const push =
            minDistance - distance;

        adjustedX +=
            Math.cos(angle) * push;

        adjustedY +=
            Math.sin(angle) * push;
    }
});

    // keep inside pitch
    adjustedX =
        Math.max(
            5,
            Math.min(95, adjustedX)
        );

    adjustedY =
        Math.max(
            5,
            Math.min(95, adjustedY)
        );

    return {
        x: adjustedX,
        y: adjustedY
    };
}
// =====================================
// GLOBAL STATE
// =====================================
let opponentsVisible = false;
let opponentFormation = "4-3-3 (Single Pivot)";
let opponentSlots = [];
let currentCaptain = null;
let jerseyColor = "green";
let assignedPlayers = {};
let drawingMode = false;
let connections = [];
let selectedSlot = null;
let freeDrawMode = false;
let isDrawing = false;
let currentPath = null;
let ballElement = null;
let isExporting = false; // prevents double export
let draggingOpponent = null;
let opponentOffsetX = 0;
let opponentOffsetY = 0;
let showFlags = false;
// =====================================
// ENSURE SVG LAYER
// =====================================
function ensureSvgLayer() {

    const pitch = document.querySelector(".pitch");

    if (!pitch) return null;

    let svg = pitch.querySelector("#lines-layer");

    if (!svg) {

        svg = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "svg"
        );

        svg.id = "lines-layer";

        Object.assign(svg.style, {
            position: "absolute",
            inset: "0",
            width: "100%",
            height: "100%",
            zIndex: 5,
            overflow: "visible",
            pointerEvents: "none"
        });

        // Tactical connections
        const connectionGroup = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "g"
        );

        connectionGroup.setAttribute(
            "id",
            "connection-group"
        );

        // Free draw group
        const drawingGroup = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "g"
        );

        drawingGroup.setAttribute(
            "id",
            "drawing-group"
        );

        svg.appendChild(connectionGroup);
        svg.appendChild(drawingGroup);

        pitch.appendChild(svg);
    }

    return svg;
}
// =====================================
// UPDATE FADING STATE
// =====================================
function updateFadingState() {

    // FIRST remove fading from ALL rows
    document.querySelectorAll("tr").forEach(row => {
        row.classList.remove("player-unavailable");
    });

    // THEN reapply fading ONLY
    // to currently assigned players
    Object.keys(assignedPlayers).forEach(player => {

        const playerCell = document.querySelector(
            `[data-player-row="${player}"]`
        );

        if (!playerCell) return;

        const row = playerCell.closest("tr");

        if (!row) return;

        row.classList.add("player-unavailable");
    });
}
// =====================================
// INIT
// =====================================
document.addEventListener("DOMContentLoaded", () => {

    console.log("Loaded formations:", FORMATIONS);

    ensureSvgLayer();
    applyPlayerResponsivePositions();
    updateOpponentDropdownVisibility();

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

        updateFadingState();
        applyPlayerResponsivePositions();
});
observer.observe(document.body, {subtree: true, childList: true});
// =====================================
// OPPONENT DROPDOWN OBSERVER*
// =====================================
function monitorOpponentDropdown() {

    const interval = setInterval(() => {

        const dropdown =
            document.getElementById(
                "opponent-formation-dropdown"
            );

        if (!dropdown) return;

        const selected =
            dropdown.querySelector(".Select-value-label") ||
            dropdown.querySelector(".Select__single-value");

        if (!selected) return;

        const value =
            selected.textContent.trim();

        if (
            value &&
            value !== opponentFormation
        ) {

            opponentFormation = value;

            if (opponentsVisible) {
                renderOpponents();
            }
        }

    }, 300);

    return interval;
}

monitorOpponentDropdown();
// =====================================
// MOBILE DRAWER*
// =====================================
const drawer =
    document.getElementById(
        "mobile-player-drawer"
    );

const handle =
    document.getElementById(
        "drawer-handle"
    );

if (drawer && handle) {

    handle.addEventListener("click", () => {

        drawer.classList.toggle("open");
    });
}

});
// =====================================
// OPPONENT DROPDOWN VISIBILITY*
// =====================================
function updateOpponentDropdownVisibility() {

    const container =
        document.getElementById(
            "opponent-dropdown-container"
        );

    if (!container) return;

    if (opponentsVisible) {

        container.classList.remove(
            "opponent-dropdown-hidden"
        );

        container.classList.add(
            "opponent-dropdown-visible"
        );

    } else {

        container.classList.remove(
            "opponent-dropdown-visible"
        );

        container.classList.add(
            "opponent-dropdown-hidden"
        );
    }
}
// =====================================
// UPDATE CAPTAINS
// =====================================
function updateAllCaptains() {

    Object.keys(assignedPlayers).forEach(player => {

        const slot = assignedPlayers[player];

        if (!slot) return;

        renderPlayerInSlot(slot, player);
    });

    refreshCaptainRowStyles();
}
function rerenderAllPlayers() {
    Object.keys(assignedPlayers).forEach(player => {
        const slot = assignedPlayers[player];
        if (slot) {
            renderPlayerInSlot(slot, player);
        }
    });

    // Update EMPTY slots too
    document.querySelectorAll(".position-slot").forEach(slot => {

        if (slot.classList.contains("filled")) return;

        const pos = slot.dataset.original;

        const img = slot.querySelector("img");

        if (!img) return;

        if (pos === "GK") {

            img.src = "/assets/goalkeeper_player.webp";

        } else {

            img.src =
                jerseyColor === "green"
                    ? "/assets/green_player.webp"
                    : "/assets/white_player.webp";
        }

        // TEXT COLOR
        const label = slot.querySelector(".position-label");

        if (label) {

            label.style.color =
                (pos === "GK" || jerseyColor === "white")
                    ? "black"
                    : "white";
        }
    });
}
// =====================================
// REFRESH CAPTAIN ROW STYLES
// =====================================
function refreshCaptainRowStyles() {

    // Find ALL elements marked as player rows
    const playerElements =
        document.querySelectorAll(
            "[data-player-row]"
        );

    // Reset ALL table rows first
    document.querySelectorAll("tr").forEach(tr => {

        tr.classList.remove(
            "captain-row",
            "fw-bold"
        );

        tr.style.fontWeight = "normal";

        tr.querySelectorAll("*").forEach(el => {

            el.style.fontWeight = "normal";

            el.classList.remove(
                "fw-bold",
                "captain-row"
            );
        });
    });

    // Apply captain style ONLY to active captain
    playerElements.forEach(el => {

        const playerName =
            el.dataset.player;

        if (
            currentCaptain &&
            playerName === currentCaptain
        ) {

            // style the REAL table row
            const tr = el.closest("tr");

            if (!tr) return;

            tr.classList.add(
                "captain-row"
            );

            tr.style.fontWeight = "bold";

            tr.querySelectorAll("*").forEach(child => {
                child.style.fontWeight = "bold";
            });
        }
    });
}
// =====================================
// CLEAR CAPTAIN STARS
// =====================================
function resetCaptainStars() {

  const stars = document.querySelectorAll('[id*="captain-toggle"]');

  stars.forEach(star => {
    star.classList.remove("captain-active");
    star.style.color = "";
    star.innerHTML = "☆";
  });
}
// =====================================
// DRAG START
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

   const draggedPlayer =
    document.querySelector(
        `[data-player="${playerName}"]`
    );
    
    const flagUrl =
    draggedPlayer?.dataset.flag || "";
    
    slot.dataset.flag = flagUrl;
    
    renderPlayerInSlot(slot, playerName);
    assignedPlayers[playerName] = slot;
    updateFadingState();
    updateLines();

 }
// MOVE SLOT
if (type === "slot-move" && pitch) {

    const playerName = e.dataTransfer.getData("player");
    const movingSlot = assignedPlayers[playerName];

    if (!movingSlot) return;

    const rect = pitch.getBoundingClientRect();

    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;

    movingSlot.style.left = `${x}%`;
    movingSlot.style.top = `${y}%`;
    movingSlot.dataset.manualPosition = "true";

    drawLines();
}
 // BACK TO TABLE
 if (type === "player" && table) {
   unassignPlayer(playerName);
   updateLines();
 }
});
// =====================================
// RESET BOARD
// =====================================
function resetBoard() {
    
    // =====================================
    // REMOVE PLAYERS
    // =====================================

    // Create SAFE copy first
    const playersToClear = Object.entries(assignedPlayers);
    
    // Clear all assigned slots
    playersToClear.forEach(([player, slot]) => {
        
        if (slot) {
            clearSlot(slot);
        }
    });
    // Reset assigned players object
    assignedPlayers = {};
    
    // Rebuild fading state
    updateFadingState();

    // =====================================
    // REMOVE CAPTAIN
    // =====================================

    const captainProxy =
    document.querySelector(
        "#captain-proxy"
    );
    
    if (captainProxy) {

    // clear Dash → JS sync source first
    captainProxy.textContent = "";
}
// reset global state
currentCaptain = null;
// reset ALL captain stars in table
resetCaptainStars();
// remove captain styling
refreshCaptainRowStyles();
// rerender players without captain jerseys
updateAllCaptains();

    // =====================================
    // REMOVE OPPONENTS
    // =====================================

    opponentsVisible = false;

    clearOpponents();

    updateOpponentDropdownVisibility();

    // reset opponent button
    const opponentBtn =
        document.getElementById(
            "opponent-toggle-btn"
        );

    if (opponentBtn) {

        opponentBtn.src =
            "/assets/opponent_white.png";
    }

    // =====================================
    // REMOVE FLAGS
    // =====================================

    showFlags = false;

    const flagBtn =
        document.getElementById(
            "flag-toggle-btn"
        );

    if (flagBtn) {

        flagBtn.src =
            "/assets/flag_white.png";
    }

    // =====================================
    // REMOVE DRAWING MODE
    // =====================================

    drawingMode = false;

    selectedSlot = null;

    const lineBtn =
        document.getElementById(
            "draw-lines-btn"
        );

    if (lineBtn) {

        lineBtn.src =
            "/assets/line_white.png";
    }

    // =====================================
    // REMOVE FREE DRAW MODE
    // =====================================

    freeDrawMode = false;

    const penBtn =
        document.getElementById(
            "free-draw-btn"
        );

    if (penBtn) {

        penBtn.src =
            "/assets/pen_white.png";
    }

    // =====================================
    // REMOVE TACTICAL CONNECTIONS
    // =====================================

    connections = [];

    const connectionGroup =
        document.querySelector(
            "#connection-group"
        );

    if (connectionGroup) {

        connectionGroup.innerHTML = "";
    }

    // =====================================
    // REMOVE FREE DRAW LINES
    // =====================================

    const drawingGroup =
        document.querySelector(
            "#drawing-group"
        );

    if (drawingGroup) {

        drawingGroup.innerHTML = "";
    }

    // =====================================
    // REMOVE BALL
    // =====================================

    if (ballElement) {

        ballElement.remove();

        ballElement = null;
    }

    // =====================================
    // RESET SVG STATE
    // =====================================

    isDrawing = false;

    currentPath = null;

    document.querySelectorAll(".position-slot").forEach(slot => {
        delete slot.dataset.manualPosition;
    });

    applyPlayerResponsivePositions();

    // =====================================
    // RERENDER PLAYERS
    // =====================================

    rerenderAllPlayers();
    drawLines();
}
// =====================================
// CLICK HANDLER
// =====================================
document.addEventListener("click", function (e) {

 const slot = e.target.closest(".position-slot");

// EXPORT
if (e.target.closest("#export-btn")) {

    if (isExporting) return; // prevent double click
    isExporting = true;

    const pitch = document.querySelector(".pitch");
    if (!pitch) {
        isExporting = false;
        return;
    }

    let formation = document.querySelector("#formation-proxy")?.textContent || "lineup";
    let captain = document.querySelector("#captain-proxy")?.textContent || "no-captain";

    const fileName = `lineup_${formation}_${captain}`
        .replace(/\s+/g, "_")
        .replace(/[^a-z0-9_\-]/gi, "")
        .toLowerCase() + ".png";

    document.querySelectorAll(".player-label").forEach(el => {
        el.style.opacity = "0.99";
    });

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

            isExporting = false; // release lock
        });
    }, 300);

    return;
}

// BUTTONS
// JERSEY TOGGLE
 if (e.target.id === "jersey-toggle-btn") {

    const btn = e.target;

    jerseyColor =
        jerseyColor === "green"
            ? "white"
            : "green";

    btn.src =
        jerseyColor === "green"
            ? "/assets/green_toggle.png"
            : "/assets/white_toggle.png";

    rerenderAllPlayers();

    return;
}
// FREE DRAWING
 if (e.target.id === "draw-lines-btn") {
  drawingMode = !drawingMode;

  // Disable free draw when activating lines
  if (drawingMode) {
    freeDrawMode = false;
    
    // reset free draw icon
    const penBtn = document.getElementById("free-draw-btn");
    if (penBtn) penBtn.src = "/assets/pen_white.png";
  }

  selectedSlot = null;

  // VISUAL TOGGLE (white ↔ green)
  const btn = e.target;

  if (drawingMode) {
    btn.src = "/assets/line_green.png";
  } else {
    btn.src = "/assets/line_white.png";
  }

  return;
}

 if (e.target.id === "free-draw-btn") {
  freeDrawMode = !freeDrawMode;

  // Disable line drawing if activating free draw
  if (freeDrawMode) {
    drawingMode = false;
  }

  const btn = e.target;

  // Toggle icon
  if (freeDrawMode) {
    btn.src = "/assets/pen_green.png";
  } else {
    btn.src = "/assets/pen_white.png";
  }

  // Reset draw-lines icon if switching modes
  const lineBtn = document.getElementById("draw-lines-btn");
  if (lineBtn && freeDrawMode) {
    lineBtn.src = "/assets/line_white.png";
  }

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

// TOGGLE OPPONENTS
if (e.target.id === "opponent-toggle-btn") {

    opponentsVisible = !opponentsVisible;

    updateOpponentDropdownVisibility();

    e.target.src = opponentsVisible
        ? "/assets/opponent_green.png"
        : "/assets/opponent_white.png";

    if (opponentsVisible) {
        renderOpponents();
    } else {
        clearOpponents();
    }

    return;
}

// FLAG TOGGLE
if (e.target.id === "flag-toggle-btn") {

    showFlags = !showFlags;

    e.target.src =
        showFlags
            ? "/assets/flag_green.png"
            : "/assets/flag_white.png";

    rerenderAllPlayers();

    return;
}

// RESET BOARD
if (e.target.id === "reset-btn") {

    resetBoard();

    return;
}

});
// =====================================
// BALL DRAG
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

    // Prevent drawing when clicking existing path
    if (
        e.target.tagName === "path"
    ) {
        return;
    }

    const svg = ensureSvgLayer();

    const drawingGroup =
        svg.querySelector("#drawing-group");

    if (!drawingGroup) return;

    isDrawing = true;

    const rect =
        pitch.getBoundingClientRect();

    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const path =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "path"
        );

    path.setAttribute("d", `M ${x} ${y}`);

    path.setAttribute("stroke", "red");
    path.setAttribute("stroke-width", "4");
    path.setAttribute("fill", "none");

    path.setAttribute(
        "pointer-events",
        "stroke"
    );

    path.style.cursor = "pointer";

    // REMOVE DRAWING
    path.addEventListener(
        "pointerdown",
        function (ev) {

            // only remove when NOT drawing
            if (isDrawing) return;

            ev.stopPropagation();
            ev.preventDefault();

            path.remove();
        }
    );

    drawingGroup.appendChild(path);

    currentPath = path;
});

document.addEventListener("mousemove", function (e) {

    if (!isDrawing || !currentPath) return;

    const pitch =
        document.querySelector(".pitch");

    const rect =
        pitch.getBoundingClientRect();

    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const d =
        currentPath.getAttribute("d");

    currentPath.setAttribute(
        "d",
        d + ` L ${x} ${y}`
    );
});

document.addEventListener("mouseup", function () {

    isDrawing = false;

    setTimeout(() => {

        currentPath = null;

    }, 50);
});

// =====================================
// DRAW TACTICAL CONNECTIONS
// =====================================
function drawLines() {

    const svg = ensureSvgLayer();

    if (!svg) return;

    const connectionGroup =
        svg.querySelector("#connection-group");

    if (!connectionGroup) return;

    // ONLY clear tactical lines
    connectionGroup.innerHTML = "";

    const pitch = document.querySelector(".pitch");

    const pitchRect =
        pitch.getBoundingClientRect();

    connections.forEach(([slotA, slotB], index) => {

        if (!slotA || !slotB) return;

        const rectA =
            slotA.getBoundingClientRect();

        const rectB =
            slotB.getBoundingClientRect();

        const x1 =
            rectA.left +
            rectA.width / 2 -
            pitchRect.left;

        const y1 =
            rectA.top +
            rectA.height / 2 -
            pitchRect.top;

        const x2 =
            rectB.left +
            rectB.width / 2 -
            pitchRect.left;

        const y2 =
            rectB.top +
            rectB.height / 2 -
            pitchRect.top;

        const line = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "line"
        );

        line.setAttribute("x1", x1);
        line.setAttribute("y1", y1);

        line.setAttribute("x2", x2);
        line.setAttribute("y2", y2);

        line.setAttribute("stroke", "yellow");
        line.setAttribute("stroke-width", "5");

        line.style.pointerEvents = "stroke";
        line.style.cursor = "pointer";

        // Remove line
        line.addEventListener("click", (e) => {

            e.stopPropagation();

            connections.splice(index, 1);

            drawLines();
        });

        connectionGroup.appendChild(line);
    });
}
// =====================================
// PLAYER RENDER
// =====================================
function renderPlayerInSlot(slot, player) {

    slot.innerHTML = "";

    const img = document.createElement("img");

    const pos = slot.dataset.original;

    const isGoalkeeper = pos === "GK";

    const isCaptain = player === currentCaptain;

    // =====================================
    // IMAGE SELECTION
    // =====================================

    if (isGoalkeeper) {

        img.src = isCaptain
            ? "/assets/goalkeeper_captain.webp"
            : "/assets/goalkeeper_player.webp";

    } else {

        if (jerseyColor === "green") {

            img.src = isCaptain
                ? "/assets/green_captain.webp"
                : "/assets/green_player.webp";

        } else {

            img.src = isCaptain
                ? "/assets/white_captain.webp"
                : "/assets/white_player.webp";
        }
    }

    img.className = "jersey-img";

    const label = document.createElement("div");

    label.className = "player-label";

    label.innerText = player;

    // =====================================
    // TEXT COLOR
    // =====================================

    label.style.color =
        (isGoalkeeper || jerseyColor === "white")
            ? "black"
            : "white";

    Object.assign(label.style, {
        position: "absolute",
        bottom: "-18px",
        width: "100%",
        textAlign: "center"
    });

    slot.appendChild(img);

    const flagUrl = slot.dataset.flag;
    
    if (showFlags && flagUrl) {

    const flag =
        document.createElement("img");

    flag.src = flagUrl;

    flag.className = "player-flag";

    slot.appendChild(flag);
}

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

    let jersey = "/assets/green_player.webp";

    if (pos === "GK") {

        jersey = "/assets/goalkeeper_player.webp";

    } else {

        jersey =
            jerseyColor === "green"
                ? "/assets/green_player.webp"
                : "/assets/white_player.webp";
    }

    slot.innerHTML = `
        <img src="${jersey}" class="jersey">
        <div class="position-label"
             style="color:${(pos === "GK" || jerseyColor === "white") ? "black" : "white"}">
             ${pos}
        </div>
    `;

    slot.classList.remove("filled");

    delete slot.dataset.player;

    delete slot.dataset.flag;
}
// =====================================
// ASSIGN / UNASSIGN
// =====================================
function unassignPlayer(player) {
 const slot = assignedPlayers[player];
 if (!slot) return;
 clearSlot(slot);
 delete assignedPlayers[player];
 updateFadingState();
}
// =====================================
// OPPONENT RENDERER
// =====================================
function renderOpponents() {

    console.log(
        "Rendering opponents:",
        opponentFormation
    );

    const layer = document.getElementById("opponents-layer");

    if (!layer) {

        console.error(
            "Opponents layer missing"
        );

        return;
    }

    layer.innerHTML = "";

    opponentSlots = [];

    const formation =
        getMobileFormationCoordinates(opponentFormation) ||
        FORMATIONS[opponentFormation];
    
    if (!formation) {
        console.error("Missing formation:", opponentFormation);
        return;
    }

    formation.forEach(([pos, x, y], index) => {

    const slot =
        document.createElement("div");

    slot.className =
        "opponent-slot";

    const desktopFormation =
        FORMATIONS[opponentFormation] || formation;

    const desktopPoint =
        desktopFormation[index] || [pos, x, y];

    const transformed =
        getResponsiveCoordinate(
            opponentFormation,
            index,
            desktopPoint[1],
            desktopPoint[2]
        );

    // Mirror vertically
    const mirroredX =
        100 - transformed.x;

    const resolved =
        resolveOpponentCollisions(
            mirroredX,
            transformed.y
        );

    const mirroredPosition =
        mirrorPosition(pos);

    // IMPORTANT:
    // left = horizontal
    // top = vertical
    slot.style.left =
        `${resolved.x}%`;

    slot.style.top =
        `${resolved.y}%`;

    slot.dataset.position =
        mirroredPosition;

    const img =
        document.createElement("img");

    img.src =
        pos === "GK"
            ? "/assets/opponent_goalkeeper.webp"
            : "/assets/opponent_player.webp";

    const label =
        document.createElement("div");

    label.className =
        "opponent-label";

    label.innerText =
        mirroredPosition;

    slot.appendChild(img);
    slot.appendChild(label);

    layer.appendChild(slot);

    opponentSlots.push(slot);
    });
}
// =====================================
// CLEAR OPPONENTS
// =====================================
function clearOpponents() {

    const layer = document.getElementById("opponents-layer");

    if (layer) {
        layer.innerHTML = "";
    }

    opponentSlots = [];
}
// =====================================
// OPPONENT DRAG
// =====================================
document.addEventListener("mousedown", (e) => {

    const slot = e.target.closest(".opponent-slot");

    if (!slot) return;

    draggingOpponent = slot;

    const rect = slot.getBoundingClientRect();

    opponentOffsetX = e.clientX - rect.left;
    opponentOffsetY = e.clientY - rect.top;

    e.preventDefault();
});
// OPPONENT MOVE
document.addEventListener("mousemove", (e) => {

    if (!draggingOpponent) return;

    const pitch = document.querySelector(".pitch");

    const rect = pitch.getBoundingClientRect();

    const x = ((e.clientX - rect.left - opponentOffsetX) / rect.width) * 100;

    const y = ((e.clientY - rect.top - opponentOffsetY) / rect.height) * 100;

    draggingOpponent.style.left = `${x}%`;
    draggingOpponent.style.top = `${y}%`;
});
// OPPONENT DROP
document.addEventListener("mouseup", () => {

    draggingOpponent = null;
});
// =====================================
// HANDLE RESIZE
// =====================================
window.addEventListener("resize", () => {

    applyPlayerResponsivePositions();

    if (opponentsVisible) {
        renderOpponents();
    }
});
