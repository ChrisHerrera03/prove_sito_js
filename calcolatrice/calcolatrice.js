let res, operando;
let input = document.getElementById("input");
let result = document.getElementById("result");

const add = (a,b) => a + b;

const minus = (a,b) => a - b;

const divide = (a,b) =>{
    if(b == 0) return "Impossibile dividere per 0";
    return a / b;
};

const mult = (a,b) => a * b;

function getInput(val){
    //senza reset
    if(val == '+' || val == '-' || val == '*' || val == '/'){
        operazione = val;
        operando = res;
        input.value = " ";
        res = 0;
    }
    else{    
        input.value += val;
        res = input.value;
    }
}

function getResult(){
    operando == undefined || isNaN(operando) ? operando = 0 :  operando = parseFloat(operando); 
    //operando = parseFloat(operando);
    res = parseFloat(res);
    result.value = operando + " " + operazione + " " + res + " = ";
    switch(operazione){
        case '+':
            input.value = add(operando,res);
        break;
        case '-':
            input.value = minus(operando,res);
        break;
        case '/':
            input.value = divide(operando,res);
        break;
        case '*':
            input.value = mult(operando,res);
        break;
        default:
        break;
    }
    res = input.value;
}
