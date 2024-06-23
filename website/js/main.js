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

async function todoUpdate() {
    console.log('run')
    let request = new XMLHttpRequest;
    request.open("GET", "https://devmaycon.pythonanywhere.com/getall")
    let response = await request.send()
    console.log(response)
    return response
}