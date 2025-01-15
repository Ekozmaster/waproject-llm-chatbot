document.getElementById("start-new-chat").addEventListener("click", function () {
    document.getElementById("main-page").style.display = "none";
    document.getElementById("chat-window").style.display = "flex";
});

document.getElementById("back-to-main").addEventListener("click", function () {
    document.getElementById("chat-window").style.display = "none";
    document.getElementById("main-page").style.display = "flex";
});
