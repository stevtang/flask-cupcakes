"use strict";

const BASE_URL = "http://localhost:5001/"

const $cupcakesList = $("#all-cupcake-list");
const $addCupcakeButton = $("#add-cupcake-button")

async function getAllCupcakes() {
    const response = await axios({
        url: `${BASE_URL}api/cupcakes`,
        method: 'GET',
    });

    const allCupcakes = response.data.cupcakes;

    return allCupcakes;

}

async function showAllCupcakes() {

    $cupcakesList.empty();

    let allCupcakes = await getAllCupcakes();

    for (let c of allCupcakes){
        let $cupcake = generateHTMLMarkup(c)
        $cupcakesList.append($cupcake)
    }

}

function generateHTMLMarkup(cupcake){

    return $(`
    
        <li id="${cupcake.id}">
            <p>${cupcake.flavor}</p>
            <p>${cupcake.size}</p>
            <p>${cupcake.rating}</p>
            <img src="${cupcake.image}"></img>
        </li>
    `)

}

async function addCupcake(evt) {

    evt.preventDefault();

    const flavor = $("#flavor-input").val();
    const size = $("#size-input").val();
    const rating = $("#rating-input").val();
    const image = $("#image-input").val();

    let jsonObject = {
        'flavor':flavor,
        'size':size,
        'rating':rating,
        'image':image
    };
    
    console.log(jsonObject);

    const response = await axios.post(
        `${BASE_URL}api/cupcakes`,
        jsonObject
    );

    showAllCupcakes();
}

$addCupcakeButton.on("submit", addCupcake);

showAllCupcakes();