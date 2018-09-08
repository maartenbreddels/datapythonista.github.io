var subtitle = document.getElementsByClassName("blog-description")[0];
console.log(subtitle);
subtitle.innerHTML = "<a href=\"/\">" + subtitle.innerText + "</a>";
