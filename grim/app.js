const canvas = document.querySelector("canvas");
const lineWidth = document.querySelector("#line-width")
const color = document.querySelector("#color");
const ctx = canvas.getContext("2d");
const colorOptions = Array.from(document.querySelectorAll(".color-option"));
const modeBtn = document.querySelector("#mode-btn");
const destroybtn = document.querySelector("#destroy-btn");
const eraserbtn = document.querySelector("#eraser-btn");
const fileinput=   document.querySelector("#file");
const textInput=   document.querySelector("#text");
const savebtn=   document.querySelector("#save");

canvas.width = 800;
canvas.height = 800;
ctx.lineWidth = lineWidth.value;
ctx.lineCap = "round";
let isPainting = false;
let isFilling = false;

function onMove(e){
    if(isPainting){
        ctx.lineTo(e.offsetX,e.offsetY);
        // if(isFilling){
        //     ctx.fill();
        // }else{
        //     ctx.stroke();
        // }
        ctx.stroke();
        return;
    }
    
    ctx.moveTo(e.offsetX,e.offsetY);
}

function onMouseDown(){
    isPainting = true;
}
function cancelPainting(){
    isPainting = false;
    ctx.beginPath();
}
function onLineWidthChange(e){
    ctx.lineWidth = e.target.value;
}
function onColorChange(e){
    ctx.strokeStyle = e.target.value;
    ctx.fillStyle = e.target.value;
}
function onColorClick(e){
    //console.dir(e.target);
    const colorValue = e.target.dataset.color
    ctx.strokeStyle = colorValue;
    ctx.fillStyle = colorValue;
    color.value = colorValue;
}
function onModeClick(e){
    if(isFilling){
        isFilling = false;
        modeBtn.innerText = "Fill";
    }else{
        isFilling = true;
        modeBtn.innerText = "Draw";
    }
}
function onCanvasClick(e){
    if(isFilling){
        ctx.fillRect(0,0,800,800);
    }
    
}
function onDestroyClick(){
    ctx.fillStyle = "white";
    ctx.fillRect(0,0,800,800);
}
function onEraserClick(){
    ctx.strokeStyle = "white";
    isFilling = false;
    modeBtn.innerText = "Fill";
}
function onFileChange(e){
    const file = e.target.files[0];
    const url = URL.createObjectURL(file);
    const image = new Image();
    image.src=url;
    image.onload = function(){
        ctx.drawImage(image,0,0,800,800);
        fileinput.value= "";
    }
}
function onDoubleClick(e){
    const text = textInput.value;
    if(text !== ""){
        ctx.save(); // 현재상태저장
        ctx.lineWidth = 1;
        ctx.font = "48px serif";
        ctx.fillText(text,e.offsetX,e.offsetY);
        ctx.restore(); //되돌리기
    }
}
function onSaveClick(){ // 파일 다운받기
    const url = canvas.toDataURL(); 
    const a = document.createElement("a");
    a.href = url;
    a.download = "MyDrawing.png";
    a.click();
}
canvas.addEventListener("dblclick",onDoubleClick);
canvas.addEventListener("mousemove",onMove);
canvas.addEventListener("mousedown",onMouseDown);
canvas.addEventListener("mouseup",cancelPainting);
canvas.addEventListener("mouseleave",cancelPainting);

lineWidth.addEventListener('change',onLineWidthChange)
color.addEventListener('change',onColorChange)

colorOptions.forEach(color => color.addEventListener('click',onColorClick));

modeBtn.addEventListener('click',onModeClick);
canvas.addEventListener('click',onCanvasClick);
destroybtn.addEventListener('click',onDestroyClick);
eraserbtn.addEventListener('click',onEraserClick);
fileinput.addEventListener('change',onFileChange);
savebtn.addEventListener('click',onSaveClick);