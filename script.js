let count=0; let goal=2;

async function fetchProgressData(){
  try{
    console.log("Buscando dados da API local...");
    const countResponse=await fetch("http://localhost:5000/count");
    const countData=await countResponse.json();
    console.log("Dados de goal recebidos:", countData);
    const count=countData.count;

    const goalResponse=await fetch("http://localhost:5000/goal");
    const goalData=await goalResponse.json();
    console.log("Dados de count recebidos:", goalData);
    const goal=goalData.goal;

    updateProgressBar(count, goal);
  }catch(error){
    console.error("Erro ao buscar dados da API:",error);
  }
}

function updateProgressBar(count, goal){
  console.log(`Atualizando barra: count=${count}, goal=${goal}`);
  const progressBar=document.getElementById("progress-bar");
  progressBar.innerHTML="";

  for(let i=0;i<goal;i++){
    const segment=document.createElement("div");
    segment.classList.add("segment");
    if(i<count){segment.classList.add("filled");}
    progressBar.appendChild(segment);
  }

  document.getElementById("count").innerText=count;
  document.getElementById("goal").innerText=goal;
}

updateProgressBar(count,goal);
setInterval(fetchProgressData, 60000);
fetchProgressData();