#!/usr/bin/node

let request = “https://swapi-api.alx-tools.com/api/people/”

fetch(request).then((response) => {
    return response.json();
}).then( (data) => {
    let p = document.getElementId(“Movie”);
    console.log(data);
    p.innerHTML = JSON.stringify(data.characters);
})
