let 이름 :string | number[] = 'kim';
let arr : string[] = ['kim','kang'];
let obj : {name?:string} | 내타입 = {name:'kim'} //?0또는1
type 내타입 = string | number;
function 함수(x:number):number{ //number리턴
    return x*x;
}
type member = [number,boolean];
let john:member = [3,false];
type Member = {
    [key :string] : string,
}
let john1 : Member = {name:'kim',age:'123'}
class user{
    name: string;
    constructor(name:string){
        this.name = name;
    }
}
let 제목 = document.querySelector('#title') as Element; // Element요소로만듬
if(제목 != null){
    제목.innerHTML = '반가워요';
}
if(제목 instanceof Element){
    제목.innerHTML = '반가워요1';
}
if(제목?.innerHTML != undefined){ //제목에 innerHTML있으면 바꿈
    제목.innerHTML = '반가워요2';
}
let 링크 = document.querySelector('.link');
if(링크 instanceof HTMLAnchorElement){
    링크.href = "https://kakao.com"
}
let 버튼 = document.querySelector('#button');
버튼?.addEventListener('click',function(){

})
