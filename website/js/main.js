function checkItem(item) {
    let checkbox = item.childNodes[3];
    if (checkbox.style.visibility == "visible") {
        checkbox.style.visibility = "hidden";
        checkbox.style.opacity = "hidden";
    } else {
        checkbox.style.visibility = "visible";
        checkbox.style.opacity = "1";
    }
}