const sliderWrap = document.querySelector(".slider__wrap");
const sliderImg = document.querySelector(".slider__img");       // 보여지는 영역
const sliderInner = document.querySelector(".slider__inner");   // 움직이는 영역
const slider = document.querySelectorAll(".slider");
const sliderBtn = document.querySelector(".slider__btn");    //버튼
const sliderBtnPrev = document.querySelector(".prev");       //왼쪽버튼
const sliderBtnNext = document.querySelector(".next");       //오른쪽버튼

let currentIndex = 0;                       //현재 이미지
let sliderCount = slider.length;            //이미지 갯수
let sliderWidth = sliderImg.offsetWidth;    //이미지 가로값

// 이미지 움직이는 영역
function gotoSlider(num){
    sliderInner.style.transition = "all 400ms";
    sliderInner.style.transform = "translateX("+ -sliderWidth * num +"px)";
    currentIndex = num;
}

// 왼쪽 버튼을 클릭했을 때
sliderBtnPrev.addEventListener("click", () => {
    let prevIndex = (currentIndex + (sliderCount -1)) % sliderCount
    // 4, 1, 2, 3, 4, 1, 2, ...
    gotoSlider(prevIndex);
});

// 오른쪽 버튼을 클릭했을 때
sliderBtnNext.addEventListener("click", () => {
    let nextIndex = (currentIndex + 1) % sliderCount
    // 1, 2, 3, 4, 0, 1, 2, ...
    gotoSlider(nextIndex);
});