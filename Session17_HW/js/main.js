import { openModal, closeModal } from "./modal.js";

const $ = (selector) => document.querySelector(selector);
const modal = document.querySelector(".modal");
const title = document.querySelector(".h1");
const img = document.querySelector(".fig");
const span = document.querySelector(".close");

// 해야하는 것
// 1. 기본 공지사항 (처음 볼때부터 띄우기)
// 2. 오소리 설명 : 제목 누르면 나오게.
// 1. 이미지 클릭 시 모달 띄우기


// 이미지를 클릭하면 모달 창을 띄운다
img.addEventListener('click', ()=>{
    modalDisplay("block");
});

// 닫기 창, 공백 클릭 시 Modal display를 none으로 바꾼다
span.addEventListener('click', ()=>{
    modalDisplay("none");
});
modal.addEventListener('click', ()=>{
    modalDisplay("none");
});

// text로 받은 값을 display 값으로 변경
function modalDisplay(text){
    modal.style.display = text;
}