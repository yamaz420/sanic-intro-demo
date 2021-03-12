async function fetchTodos() {
    let res = await fetch('/rest/todos')
    let todos = await res.json()

    //console.log(todos)

    for(let todo of todos) {
        addTodo(todo)
    }   
}

fetchTodos()
function addTodo(todo) {
        let todoItem = $(/*html*/`
        <div>
            <h3>${todo.text}</h3>
            <p>${new Date(todo.timestamp * 1000).toLocaleString()}</p>
        </div>
        `)
        $('#todo-list').append(todoItem)
}
$('#add-todo-btn').click(async function() {
    let textInput = $('#todo-input').val()
    let newTodo ={
        text: textInput
    }
    //POST text to the server
    let res = await fetch('rest/todos', {
        method: 'POST',
        body: JSON.stringify(newTodo)
    })

    let todo = await res.json()
    addTodo(todo)

    $('#todo-input').val('')
})