// Selectarea elementelor din DOM
const todoInput = document.getElementById('todo-input');
const addButton = document.getElementById('add-button');
const todoList = document.getElementById('todo-list');

// Funcția pentru a adăuga o activitate
function addTodo() {
  const taskText = todoInput.value.trim();
  if (taskText === "") {
    return;
  }

  // Crearea unui nou element de listă
  const li = document.createElement('li');
  li.className = 'todo-item';
  li.setAttribute('role', 'listitem'); // Definirea rolului pentru accesibilitate

  // Textul activității
  const span = document.createElement('span');
  span.textContent = taskText;

  // Crearea butonului de ștergere
  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'Delete';
  deleteButton.setAttribute('aria-label', `Delete ${taskText}`);
  deleteButton.onclick = function () {
    todoList.removeChild(li);
  };

  // Adăugarea elementelor la listă
  li.appendChild(span);
  li.appendChild(deleteButton);
  todoList.appendChild(li);

  // Resetarea câmpului de text și focalizarea înapoi pe acesta
  todoInput.value = '';
  todoInput.focus();
}

// Adăugarea unei activități la apăsarea butonului "Add"
addButton.onclick = addTodo;

// Adăugarea activității la apăsarea tastei Enter
todoInput.addEventListener('keypress', function (event) {
  if (event.key === 'Enter') {
    addTodo();
  }
});
