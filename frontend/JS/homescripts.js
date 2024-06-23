document.addEventListener("DOMContentLoaded",function(){
    let perfil=document.getElementById("perfil-menu");
    let menu=document.getElementById("menu");

    //permite que aparezca y desaparezca cuando se clickea el logo.
    perfil.addEventListener("click",function(){
        if(menu.style.visibility==="visible"){
            menu.style.visibility="hidden";
        }
        else{
            menu.style.visibility="visible";
        }
    })

})