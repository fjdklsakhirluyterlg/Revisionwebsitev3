document.addEventListener('mousemove', (e) => {
    const mousex = e.clientX
    const mousey = e.clientY

    const tracker = document.getElementById("tracker")
    const rekt = tracker.getBoundingClientRect()
    const trackerx = rekt.left + rekt.width / 2
    const trackery = rekt.top + rekt.height / 2
})

function angle(cx, cy, ex, ey){
    const dy = ey - cy
    const dx = ex - cx
    const rad = Math.atan2(dy, dx)
    const dg = rad * 180 / Math.PI
}