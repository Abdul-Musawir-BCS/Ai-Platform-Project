let currentImage="";
let selectedImages=[];
let mode="live";
let timeline=[];

// TAB SWITCH
function switchTab(e,id){
    document.querySelectorAll(".tab").forEach(t=>t.classList.remove("active"));
    document.getElementById(id).classList.add("active");

    document.querySelectorAll(".nav-links button").forEach(b=>b.classList.remove("active"));
    e.target.classList.add("active");
}

// MODE
function setMode(m){
    mode=m;
    liveBtn.classList.remove("active");
    demoBtn.classList.remove("active");
    document.getElementById(m+"Btn").classList.add("active");
}

// LOADER
function showLoader(){
    loader.classList.remove("hidden");
    loaderText.innerText="Processing...";
}
function hideLoader(){
    loader.classList.add("hidden");
}

// TIMELINE
function log(text){
    timeline.push(text);
    document.getElementById("timeline").innerHTML =
        timeline.map(t=>`<div>${t}</div>`).join("");
}

// GENERATE
async function generate(){
    log("Generated image");

    showLoader();

    let res=await fetch("/generate",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({prompt:prompt.value})
    });

    let data=await res.json();

    currentImage=data.image;

    outputImage.src=data.image;
    analyzePreview.src=data.image;

    hideLoader();
}

// ANALYZE
async function analyze(){
    log("Analyzed image");

    showLoader();

    let res=await fetch("/analyze",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({image_path:currentImage})
    });

    let data=await res.json();
    analysis.innerText=data.analysis;

    hideLoader();
}

// UPLOAD ANALYZE
async function uploadAndAnalyze(){
    let file=uploadInput.files[0];

    let form=new FormData();
    form.append("file",file);

    showLoader();

    let res=await fetch("/analyze",{method:"POST",body:form});
    let data=await res.json();

    analysis.innerText=data.analysis;

    hideLoader();
}

// LOAD HISTORY
async function loadHistory(){
    let res=await fetch("/history");
    let data=await res.json();

    let html="";

    data.forEach(i=>{
        html+=`<img src="${i[3]}" onclick="selectImage(this,'${i[3]}')">`;
    });

    historyGrid.innerHTML=html;
    compareGrid.innerHTML=html;
}

// SELECT IMAGE
function selectImage(el,path){
    el.classList.toggle("selected");

    if(selectedImages.includes(path)){
        selectedImages=selectedImages.filter(p=>p!==path);
    } else {
        if(selectedImages.length<2){
            selectedImages.push(path);
        }
    }
}

// COMPARE
async function compareSelected(){
    if(selectedImages.length!==2){
        alert("Select exactly 2 images");
        return;
    }

    showLoader();

    let res=await fetch("/compare",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({
            img1:selectedImages[0],
            img2:selectedImages[1]
        })
    });

    let data=await res.json();

    compareResult.innerText=data.result;

    hideLoader();
}
