document.addEventListener("click", function (e) {

    if (e.target.id === "export-btn") {
        const pitch = document.querySelector(".pitch");
        const svg = document.querySelector("#connections-layer");
        if (!pitch || !svg) return;

        //Convert SVG → Canvas
        const svgData = new XMLSerializer().serializeToString(svg);
        const img = new Image();
        const svgBlob = new Blob([svgData], { type: "image/svg+xml;charset=utf-8" });
        const url = URL.createObjectURL(svgBlob);
        img.onload = function () {
            html2canvas(pitch, {
                useCORS: true,
                scale: 2
            }).then(canvas => {
                const ctx = canvas.getContext("2d");

                // Overlay lines manually
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                let formation = document.querySelector("#formation-proxy")?.textContent || "lineup";
                let captain = document.querySelector("#captain-proxy")?.textContent || "no-captain";
                const fileName = `lineup_${formation}_${captain}`
                    .replace(/\s+/g, "_")
                    .replace(/[^a-z0-9_\-]/gi, "")
                    .toLowerCase() + ".png";
                const link = document.createElement("a");
                link.download = fileName;
                link.href = canvas.toDataURL();
                link.click();
                URL.revokeObjectURL(url);
            });
        };
        img.src = url;
    }
});
 
