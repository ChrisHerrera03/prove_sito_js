let tasks = document.getElementById("tasks");
let arrayTasks = JSON.parse(localStorage.getItem("tasks"));
function createNew(){
    let descrizione = document.getElementById("task_description").value;
    if(isIn(descrizione)){
        printMsg("Non puoi inserire un task già presente");
        return;
    }
    let elemento = '<div class = "task"><input type="checkbox"> <p>'+ descrizione +'</p></div>'; 
    tasks.innerHTML += elemento; 
    settingLocalStorage(descrizione); 
} 

function mostra(div){
    console.log(div);
    let el = document.getElementById(div); el.style.display == "none" ? el.style.display = "block" : el.style.display = "none"; 
}

function isIn(descrizione){
    if(arrayTasks.length == 0) return false;
    for(let i = 0; i < arrayTasks.length; i++){
        if(descrizione == arrayTasks[i])
            return true;
    }
    return false;
}
function settingLocalStorage(descrizione){ 
    arrayTasks.push(descrizione); 
    localStorage.setItem("tasks", JSON.stringify(arrayTasks)); 
}

function getListTask(){ 
    let addItems = document.getElementById("tasks");
    for(let i = 0; i < tasks.length; i++){ 
        tasks.innerHTML += `<div class = 'task'><input type='checkbox'> <p>${arrayTasks[i]}</p></div>`; } 
}

function removeAll(){
    tasks.innerHTML = "";
    localStorage.clear();
}
function printMsg(val){

}