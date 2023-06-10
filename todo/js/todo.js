const todoForm = document.getElementById("todo-form");
const todoInput = todoForm.querySelector("input");
const toDoList = document.getElementById("todo-list");
let toDos = [];

function saveToDos(){
    localStorage.setItem("todos",JSON.stringify(toDos));
}

function deleteToDo(e){
    const li = e.target.parentElement;
    li.remove();
    toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id));
    saveToDos();
    
}

function paintToDo(newToDo){
    const li = document.createElement("li");
    li.id = newToDo.id;
    const span = document.createElement("span");
    const button = document.createElement("button");
    span.innerText = newToDo.text;
    button.innerText = "X";
    button.addEventListener("click",deleteToDo);
    li.appendChild(span);
    li.appendChild(button);
    toDoList.appendChild(li);
    
}
function handleToDoSubmit(e){
    e.preventDefault();
    const newToDo = todoInput.value;
    todoInput.value="";
    const newToDoObj = {
        text:newToDo,
        id:Date.now()
    }
    toDos.push(newToDoObj);
    saveToDos();
    paintToDo(newToDoObj);
    
    
}
todoForm.addEventListener("submit",handleToDoSubmit);



const saveToDosarr = localStorage.getItem("todos");

if(saveToDosarr != null){
    const parsedToDos = JSON.parse(saveToDosarr);
    toDos = parsedToDos;  
    parsedToDos.forEach(paintToDo);
}