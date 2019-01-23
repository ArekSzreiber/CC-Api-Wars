const logo = document.getElementById('logo');
const logo_text = 'Quoridor Skrypciaki';

logo.textContent = logo_text;

const infoBar = document.getElementById('information-bar');
const infoHTML = '<strong>Hello, User</strong>';

infoBar.innerHTML = infoHTML;
//changing attribute of element
infoBar.style.height = '98px';
infoBar.style.width = '648px';


//check if div logo has a class
//console.log(logo.classList.contains(logo.classList));
//console.log(logo.classList);
//zmiana klasy elementu
//let containers = document.querySelectorAll(".container");
//containers[0].classList.add("kontener");
//containers[0].classList.remove("container");
//console.log(containers[0].classList);

//zmiana data- atrybutów
let informationBar = document.getElementById("information-bar");
informationBar.dataset.columns = 11;
informationBar.dataset.cosTam = "asdasdas";

function ustawCzas(elementID){
    let element = document.getElementById(elementID);
    element.dataset.czasStworzenia = "2018-12-26";
}

ustawCzas("logo");

//extending DOM
const paragraph = document.createElement("p");
paragraph.textContent = "Welcome!";
document.querySelector("#cokolwiek").appendChild(paragraph);

//events


function clickHandler(event){
    console.log('Przycisk został mlaśnięty.');
    this.classList.toggle('.fence-middle-clicked');
    this.style.backgroundColor = 'rebeccapurple';
}

let walls = document.querySelectorAll('.fence-middle');

for(wall of walls){
    wall.addEventListener('click', clickHandler);
}

function buttonClickHandler(event){
    this.style.backgroundColor = 'blue';
}

function make_button(id){
    let button = document.createElement("button");
    button.id = id;
    button.addEventListener('click', buttonClickHandler);
    return button;
}

infoBar.appendChild(make_button('button-id'));

const gameBoard = document.getElementById('content');

function boardClickHandler(event){
    if(event.target.classList.contains('fence-vertical') ||
       event.target.classList.contains('fence-horizontal')){
        event.target.style.backgroundColor = 'pink';
    }
}

gameBoard.addEventListener('click', boardClickHandler);

//events test knowledge

const navbar = document.getElementById('navbar');
//let przyciski = navbar.querySelectorAll('.fence-horizontal');

function updatePoleCounter(event){
    //console.log('keykey');
    //wez dlugosc zawartosci polatekstowego
    let poleTekstowe = document.querySelector('#pole1');
    let tekst = poleTekstowe.value;
    //wez dlugosc tego stringa
    //wpierdol to do diva licznik
    let licznik = document.querySelector('#pole-counter');
    //console.log(poleTekstowe);
    licznik.textContent = String(tekst).length+'/500';
    localStorage.setItem("opis", String(tekst));
}


let pole = navbar.querySelector("#pole1");
console.log(pole.value);
pole.value = localStorage.getItem('opis');
console.log(pole.textContent);
pole.addEventListener('keypress', updatePoleCounter);


//web storage


//5 SI


















