//recibe los inputs del html o crea un arr vacio
// JSON parse pasa de str a arr
const todos = JSON.parse(localStorage.getItem('todos')) || [];

// funcion que sincroniza todos y el ul y espera clicks para resync
const render = () => {
    // refiere el ul del html en una ctte
    // crea un arr con los elementos de todos mas las etiquetas de li
    // une los <li>elem</li> en una gran string, se sincroniza todos
    const todoList = document.getElementById('todo-list');
    const todosTemplate = todos.map(t => '<li>' + t +'</li>');
    todoList.innerHTML = todosTemplate.join('');
    // creamos una ctte con los elementos del ul todo list
    // entramos en los elementos de elementos con su indice
    const elementos = document.querySelectorAll('#todo-list li') // ID es con #
    elementos.forEach((elemento, i) => {
        // escuchamos si hay un click
        // parentNode es el ul, porque el padre puede eliminar al hijo
        // splice recibe el indice y cantidad de elementos a eliminar
        // actualiza todos en el local storage
        // vuelve a renderizar listas con el todos actualizado
        elemento.addEventListener('click', () => {
            elemento.parentNode.removeChild(elemento)
            todos.splice(i, 1)
            updateTodos(todos)
            render()
        })
    })
}

const updateTodos = (todos) => {
    // transformamos los todos en una str
    // Lo guardamos en el local storage
    const todoStrings = JSON.stringify(todos)
    localStorage.setItem('todos',todoStrings)
}

// precarga el html
window.onload = () => {
    // sincroniza las listas
    render()
    // js recibe el form
    // cambiamos que hace submit
    const form = document.getElementById('todo-form');
    form.onsubmit = (e) => {
        // previene el refresh
        // refiere el input del html
        // guarda el valor del input
        // modifica el value del html a vacio de nuevo
        // guarda el valor del input en el arreglo de js
        // guarda todos como str en el local storage
        // toma la lista todos y las renderiza en html esperando clicks
        e.preventDefault();
        const todo = document.getElementById('todo');
        const todoText = todo.value;
        if (todoText != '') {
            todo.value = '';
            todos.push(todoText);
            updateTodos(todos)
            render()
        }
    }
}