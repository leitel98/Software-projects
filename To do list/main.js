//recibe los inputs del html o crea un arr vacio
// JSON parse pasa de str a arr
const todos = JSON.parse(localStorage.getItem('todos')) || [];

// funcion que sincroniza todos y el ul y espera clicks para resync
const render = () => {
    // refiere el ul del html en una ctte
    const todoList = document.getElementById('todo-list');
    // crea un arr con los elementos de todos mas las etiquetas de li
    const todosTemplate = todos.map(t => '<li>' + t +'</li>');
    // une los <li>elem</li> en una gran string, se sincroniza todos
    todoList.innerHTML = todosTemplate.join('');
    // creamos una ctte con los elementos del ul todo list
    const elementos = document.querySelectorAll('#todo-list li') // ID es con #
    // entramos en los elementos de elementos con su indice
    elementos.forEach((elemento, i) => {
        // escuchamos si hay un click
        elemento.addEventListener('click', () => {
            // parentNode es el ul, porque el padre puede eliminar al hijo
            elemento.parentNode.removeChild(elemento)
            // splice recibe el indice y cantidad de elementos a eliminar
            todos.splice(i, 1)
            // actualiza todos en el local storage
            updateTodos(todos)
            // vuelve a renderizar listas con el todos actualizado
            render()
        })
    })
}

const updateTodos = (todos) => {
    // transformamos los todos en una str
    const todoStrings = JSON.stringify(todos)
    // Lo guardamos en el local storage
    localStorage.setItem('todos',todoStrings)
    // sincronizamos todos con ul y escuchamos los clicks
}

// precarga el html
window.onload = () => {
    // sincroniza las listas
    render()
    // js recibe el form
    const form = document.getElementById('todo-form');
    // cambiamos que hace submit
    form.onsubmit = (e) => {
        // previene el refresh
        e.preventDefault();
        // refiere el input del html
        const todo = document.getElementById('todo');
        // guarda el valor del input
        const todoText = todo.value;
        // modifica el value del html a vacio de nuevo
        todo.value = '';
        // guarda el valor del input en el arreglo de js
        todos.push(todoText);
        // guarda todos como str en el local storage
        updateTodos(todos)
        // toma la lista todos y las renderiza en html esperando clicks
        render()
    }
}