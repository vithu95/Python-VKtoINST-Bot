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


$('.side-bar__bot-options').click(function () {
    $('.bot-options').css('display','block');
    $('.main').css('display','none');
    $('.new-group').css('display','none')
});

$('.side-bar__main').click(function () {
    $('.main').css('display','block');
    $('.bot-options').css('display','none');
    $('.new-group').css('display','none')
});

$('.side-bar__add-group-button').click(function () {
    $('.new-group').css('display','block');
    $('.main').css('display','none');
    $('.bot-options').css('display','none');
});