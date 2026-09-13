function checkTypes() {
    var name = "Lyla";
    var score = 95;
    var isReady = true;

    document.getElementById("typeResult").innerHTML =
        "Name: " + typeof name + "<br>" +
        "Score: " + typeof score + "<br>" +
        "Is Ready: " + typeof isReady;
}
function convertTypes() {
    var marksText = "88";
    var marksNumber = Number(marksText);

    var age = 12;
    var ageText = String(age);

    document.getElementById("convertResult").innerHTML =
        '"88" as a number: ' + marksNumber + "<br>" +
        "Type: " + typeof marksNumber + "<br>" +
        "12 as a text: " + ageText + "<br>" +
        "Type: " + typeof ageText;
}
function countText() {
    var text = "Javascript makes learning easy!";

    var words = text.split(" ").length;
    var characters = text.length
    document.getElementById("countResult").innerHTML =
        "Text: " + text + "<br>" +
        "Words: " + words + "<br>" +
        "Characters: " + characters;
}
function changeCase() {
    var text = "JavaScript is easy to learn.";

    var upperText = text.toUpperCase();
    var lowerText = text.toLowerCase();

    document.getElementById("caseResult").innerHTML =
        "Original: " + text + "<br><br>" +
        "Uppercase: " + upperText + "<br>" +
        "Lowercase: " + lowerText;
}
function replaceText() {
    var sentence = "I like playing cricket because cricket is fun to play!"
    var newSentence = sentence.replace("cricket", "badminton")

    document.getElementById("replaceResult").innerHTML =
        "Original: " + sentence + "<br>" +
        "Fixed: " + newSentence;
}
function catchError() {
    try {
        var result = totalMarks + 10;
        document.getElementById("errorResult").innerHTML =
            "Result: " + result;
    }
    catch (error) {
        document.getElementById("errorResult").innerHTML =
            "Oops! An error was caught: " + error.message
    }
}