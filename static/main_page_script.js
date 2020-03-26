var interval = 1000;
var imageRefreshInterval = setInterval(function()
    {
    $('.main__canvas').load(document.URL + ' .main__canvas');
    $('.posts-await').load(document.URL + ' .posts-await');
    $('.posts-queue').load(document.URL + ' .posts-queue');

    }, interval);


$('.hamburger-menu').click(function () {
    $('.side-bar').toggleClass('side-bar-active');
    $('.main').toggleClass('main-inactive');
});