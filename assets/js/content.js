function updateContent(contentDiv, href=null){
  var hash = window.location.hash;
  if (href){
    hash = href;
  }
  console.log(hash);
  url = "";
  switch (hash) {
    case "#Acceuil":
      url = "acceuil.html"
      break;
    case "#Camera":
      url = "camera.html"
      break;
    default:
      url = "acceuil.html"
  }
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", url, true );
  xmlHttp.onreadystatechange= function() {
    if (this.readyState!==4) return;
    if (this.status!==200) return; // or whatever error handling you want
    contentDiv.innerHTML = this.responseText;
  };
  xmlHttp.send();
}

contentDiv = document.getElementById("content")
updateContent(contentDiv)

for(a of document.getElementById("menu").getElementsByTagName("a")){
  a.addEventListener("click", function(event){
     updateContent(contentDiv,href=event.target.hash)
  }, false);
}
