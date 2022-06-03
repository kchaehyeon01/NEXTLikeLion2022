/* 
audio, key 변수를 html에서 select
누른 key에 play 클래스를 부여하고 제거하세요
키보드를 눌렀을때 play함수가 실행되게, 키보드를 뗀다면 pause함수가 실행되게 해주세요
Css , Html 등을 이용해 본인만의 커스텀 악기를 예쁘게 만들어주세요
*/

play = (e) =>{
    console.log(e);
    const audio = document.querySelector(`audio[data-press="${e.keyCode}"]`);
    const key = document.querySelector(`li[data-press = "${e.keyCode}"]`);
    if(audio){
        audio.play();
        key.classList.add("play");
        
    }

}
pause = (e)=>{
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    const key = document.querySelector(`li[data-key = "${e.keyCode}"]`);
    if(audio){
        audio.currentTime = 0;
        audio.pause();
        key.classList.remove("play");
        
    }
    
}

window.addEventListener("keypress",play);
window.addEventListener("keyup",pause);