let tasks = document.getElementById("to-do"); 
function createNew(){ let descrizione = document.getElementById("task_description").value; 
    let elemento = '<div class = "task"><input type="checkbox"> <p>'+ descrizione +'</p></div>'; 
    tasks.innerHTML += elemento; 
    settingLocalStorage(descrizione); } 


    function mostra(div){ let el = document.getElementById(div); el.style.display == "none" ? el.style.display = "block" : el.style.display = "none"; }
    let arrayTasks = []; 
    function settingLocalStorage(descrizione){ 
        checkRepeat(descrizione);
        arrayTasks.push(descrizione); 
        localStorage.setItem("tasks", JSON.stringify(arrayTasks)); 
    } 
    
    function getListTask(){ 
        let tasks = JSON.parse(localStorage.getItem("tasks")); 
        let addItems = document.getElementById("to-do"); 
        for(let i = 0; i < tasks.length; i++){ 
            addItems.innerHTML += "<div class = 'task'><input type='checkbox'> <p>"+ tasks[i] +"</p></div>"; } 
    }