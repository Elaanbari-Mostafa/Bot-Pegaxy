// ==UserScript==
// @name         Pegaxy Rent Bot algo
// @namespace    http://tampermonkey.net/
// @version      0.121
// @description  try to take over the world!
// @author       You
// @match        https://play.pegaxy.io/racing/pick-pega
// @icon         https://www.google.com/s2/favicons?domain=pegaxy.io
// @grant        GM_setValue
// @grant        GM_getValue
// @license      MIT
// ==/UserScript==

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
document.paused = false;

 document.getElementsByClassName("header-title")[2].innerText = "Ana M9awed hh";
(async function () {
    while (true){
        await sleep(2000);
        document.getElementsByClassName("header-title")[2].innerText = "Ana M9awed hh";
        var elements = document.getElementsByClassName("item-pega");//[2]
        for (var i = 0; i < elements.length; i++){
            if( elements[i].children[0].firstChild.children[2].children[1].firstChild.lastChild.firstChild.firstChild.innerText.split("/")[0] > 0){
                elements[i].click();
            }
           // break;
        }//}
    //await sleep(2000);
    //if(!(testbool)) {
       // alert("Sir T9awad");
   // }

    //const test1 = elements.children[0].firstChild.children[2].children[1].firstChild.lastChild.firstChild.firstChild;
    //if(test1.innerText.split("/")[0] > 0){
       // elements.click();


   // }





    //document.getElementsByClassName("item-pega")[2].children[0].firstChild.children[2].children[1].firstChild.lastChild.firstChild.firstChild.innerText
}
})();