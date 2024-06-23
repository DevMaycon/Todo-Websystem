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
    url = 'https://devmaycon.pythonanywhere.com/getall'
    let request = await fetch(url).then((res) => (res.json()))
    setTodos(request)
}

async function getTodo(id) {
    url='https://devmaycon.pythonanywhere.com/search/'+id
    let request = fetch(url)
    let response = await (await request).json()
    return response
}

async function setTodos(todos) {
    let new_todos = []
    for (let x=0; x < todos.length; x++) {
        if (todos[x] !== 'last_id') {
            let todo = await getTodo(todos[x]);
            new_todos.push(todo);
            let content = `
                <div class="todo-item" style="background-color: ${todo.color};">
                    <div class="todo-info">
                        <p class="todo-info-title">${todo.title}</p>
                        <p class="todo-info-description">${todo.description}</p>
                        <p class="todo-info-autor">${todo.autor}</p>
                    </div>
                    <div class="checkbox" style="visibility: ${todo.finished};">
                        <img src="images/ok_white.png">
                        <img src="images/ok_white.png">
                        <img src="images/ok_white.png">
                    </div>
                </div>`;
            document.getElementById('todo').innerHTML += content;
        }
    };
}