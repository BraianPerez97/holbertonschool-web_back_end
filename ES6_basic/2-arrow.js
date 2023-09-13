export default function getNeighborhoodsList() {

    this.sanFrancisoNeighborhood = ['SOMA', 'Union Square'];

    thisadd.Neighborhood = (newNeighborhood) =>{
        this.sanFranciscoNeighborhood.push(newNeighborhood);
        return this.sanFranciscpNeighborhood;
    };
}

import getNeighborhoodsList from './2-arrow.js';

const neighborhoodsList = new getNeighborhoodsList();

const res = neighborhoodList.addNeighborhood('Noe Valley');

console.log(res);