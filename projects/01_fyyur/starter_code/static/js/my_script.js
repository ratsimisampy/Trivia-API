// create venue
const name = document.getElementById('name');
const city = document.getElementById('city');
const state = document.getElementById('state');
const address = document.getElementById('address');
const phone = document.getElementById('phone');
const genres = document.getElementById('genre');
document.getElementById('form').onsubmit() = function(e) {
    console.log('event', e);
}