var fontSize = "24px";
var textColor = "black";
var bgColor = "transparent";

function setFontSize(size) {
    fontSize = size;
}

function increaseFontSize()  {
    setFontSize(fontSize + 10)
}

function setPalette(text, bg) {
    textColor = color;
    bgColor = bg;
}

window.onload = function() {
    var paragraphs = $('body').text();
    paragraphs.style.fontSize = fontSize;
    paragraphs.style.color = textColor;
    
    paragraphs.style.backgroundColor = bgColor;
};

