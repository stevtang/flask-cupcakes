"use strict";

const BASE_URL = "http://localhost:5001/"

const $cupcakesList = $("#all-cupcake-list");
const $addCupcakeButton = $("#add-cupcake-button")
const $cupcakeForm = $("#add-cupcake-form")
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
            <img src="${cupcake.image}"></img>
            <p>Flavor: ${cupcake.flavor}<br>
            Size: ${cupcake.size}<br>
            Rating: ${cupcake.rating}</p>
        </li>
    
    `)

}

async function addCupcake(evt) {

    evt.preventDefault();

    const flavor = $("#flavor-input").val();
    const size = $("#size-input").val();
    const rating = $("#rating-input").val();
    const image = $("#image-input").val();

    console.log(flavor, size, rating);
    console.log(jsonObject);

    const response = await axios.post(
        `${BASE_URL}api/cupcakes`,
        {
            flavor,
            size,
            rating,
            image
        }
    );

    showAllCupcakes();
}

$cupcakeForm.on("submit", addCupcake);

showAllCupcakes();