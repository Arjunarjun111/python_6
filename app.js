const mainHead = document.querySelector( '.main-head' );
const logo = document.querySelector( '.logo' );
window.addEventListener( 'scroll', function(){
    if(this.scrollY > 200){
        mainHead.classList.add( 'slidedown' );
        logo.Style.text.bgcolor = '#ffff';
    }else{
        mainHead.classList.remove( 'slidedown' );
        logo.Style.color = '#000';
    }
} )




// *scroll imges *->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>//


const slides = document.querySelector('slick-list draggable');
const buttons = document.querySelectorAll('slides');

let currentIndex = 0;

function updateSlider(index) {
    const slideWidth = slides.children[0].clientWidth;
    slides.style.transform = `translateX(-${index * slideWidth}px)`;
    currentIndex = index;
    updateActiveButton(index);
}

function updateActiveButton(index) {
    buttons.forEach((button, i) => {
        button.classList.toggle('active', i === index);
    });
}

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const index = parseInt(button.getAttribute('data-index'));
        updateSlider(index);
    });
});

// Initialize active button
updateActiveButton(currentIndex);
