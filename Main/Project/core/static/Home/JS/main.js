let eventGt1 = document.querySelector(".front-use");
let eventGt2 = document.querySelector(".getSysSel-box");

eventGt1.addEventListener("click", () => {
    eventGt2.classList.toggle("getSysSelActive");
})


// Header Carausel JS

const tabsBox = document.querySelector(".tabs-box"),
allTabs = tabsBox.querySelectorAll(".tab"),
arrowIcons = document.querySelectorAll(".icon i");

let isDragging = false;

const handleIcons = (scrollVal) => {
    let maxScrollableWidth = tabsBox.scrollWidth - tabsBox.clientWidth;
    arrowIcons[0].parentElement.style.display = scrollVal <= 0 ? "none" : "flex";
    arrowIcons[1].parentElement.style.display = maxScrollableWidth - scrollVal <= 1 ? "none" : "flex";
}

arrowIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        // if clicked icon is left, reduce 350 from tabsBox scrollLeft else add
        let scrollWidth = tabsBox.scrollLeft += icon.id === "left" ? -340 : 340;
        handleIcons(scrollWidth);
    });
});

allTabs.forEach(tab => {
    tab.addEventListener("click", () => {
        tabsBox.querySelector(".active").classList.remove("active");
        tab.classList.add("active");
    });
});

const dragging = (e) => {
    if(!isDragging) return;
    tabsBox.classList.add("dragging");
    tabsBox.scrollLeft -= e.movementX;
    handleIcons(tabsBox.scrollLeft)
}

const dragStop = () => {
    isDragging = false;
    tabsBox.classList.remove("dragging");
}

tabsBox.addEventListener("mousedown", () => isDragging = true);
tabsBox.addEventListener("mousemove", dragging);
document.addEventListener("mouseup", dragStop);



// Introduction Image Carausel JS

let activeIndex = 0;

const groups = document.getElementsByClassName("card-group");

const handleLoveClick = () => {
  const nextIndex = activeIndex + 1 <= groups.length - 1 ? activeIndex + 1 : 0;
  
  const currentGroup = document.querySelector(`[data-index="${activeIndex}"]`),
        nextGroup = document.querySelector(`[data-index="${nextIndex}"]`);
        
  currentGroup.dataset.status = "after";
  
  nextGroup.dataset.status = "becoming-active-from-before";
  
  setTimeout(() => {
    nextGroup.dataset.status = "active";
    activeIndex = nextIndex;
  });
}

const handleHateClick = () => {
  const nextIndex = activeIndex - 1 >= 0 ? activeIndex - 1 : groups.length - 1;
  
  const currentGroup = document.querySelector(`[data-index="${activeIndex}"]`),
        nextGroup = document.querySelector(`[data-index="${nextIndex}"]`);
  
  currentGroup.dataset.status = "before";
  
  nextGroup.dataset.status = "becoming-active-from-after";
  
  setTimeout(() => {
    nextGroup.dataset.status = "active";
    activeIndex = nextIndex;
  });
}


// Tugmani tanlang
const tugma = document.getElementById('love-button');

function mn() {
  setTimeout(() => {
    tugma.click();
  }, 1000);
}

setInterval(mn, 2500);



// Slick Buttons

let slickRightButton = document.querySelector(".slick-prev.slick-arrow");


// Select Languages

let dropdownBtn = document.querySelector(".dropdown-btn");
let dropdownContent = document.querySelector(".dropdown-content");

dropdownBtn.addEventListener("click", () => {
  dropdownContent.classList.toggle("show");
})

var currentPath = window.location.pathname;

let uzFlag = "/static/Home/Assets/Images/images/uz.png";
let ruFlag = "/static/Home/Assets/Images/images/ru.png";
let deFlag = "/static/Home/Assets/Images/images/de.png";
let enFlag = "/static/Home/Assets/Images/images/en.webp";

let uzLan = "O`zbek";
let ruLan = "Русский";
let deLan = "German";
let enLan = "English";

let selected_languageIcon = document.getElementById("selected_languageIcon");
let language_name = document.getElementById("language_name");

if (window.location.pathname === '/uz/' || currentPath.startsWith('/uz/')) {
  selected_languageIcon.src = uzFlag;
  language_name.innerHTML = uzLan;
} else if (window.location.pathname === '/ru/' || currentPath.startsWith('/ru/')) {
  selected_languageIcon.src = ruFlag;
  language_name.innerHTML = ruLan;
} else if (window.location.pathname === '/de/' || currentPath.startsWith('/de/')) {
  selected_languageIcon.src = deFlag;
  language_name.innerHTML = deLan;
} else if (window.location.pathname === '/en/' || currentPath.startsWith('/en/')) {
  selected_languageIcon.src = enFlag;
  language_name.innerHTML = enLan;
} else {
  // let globalError = "This is Selected Language Error";
  console.log("This is Select Language Error");
}



// if (currentPath.startsWith('/ru/')) {
//   selected_languageIcon.src = ruFlag;
//   language_name.innerHTML = ruLan;
// }