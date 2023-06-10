const loginForm = document.querySelector("#login-form");
const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("button");
const greeting = document.querySelector("#greeting");

function onLoginSubmit(e){
    e.preventDefault();
    const username = loginInput.value;
    localStorage.setItem("username",username);
    loginForm.classList.add("hidden");
    paintGreetings(username);
}

function paintGreetings(username){
    greeting.classList.remove("hidden");
    greeting.innerText = `Hello ${username}`;
}


const savedUsername = localStorage.getItem("username");
if(savedUsername === null){
    loginForm.classList.remove("hidden");
    loginForm.addEventListener("submit",onLoginSubmit);
}else{
    paintGreetings(savedUsername);
}
// h1.addEventListener('click',function(){
//     this.classList.toggle("active"); // 생겼다가 다시 누르면 없어짐!!
// })

// window.addEventListener("resize",handleWindowResize);
// window.addEventListener("copy",handleWindoCopy);
// window.addEventListener("offline",handleWindowOffline); //바뀔때 나옴
// window.addEventListener("online",handleWindowOnline);