let baseUrl = "http://127.0.0.1:5000/"
globalMissions = []

$(document).ready(() => {
    renderTable()
})

$("#btnCadastrarMissao").on("click", () => {
    const missionName = document.getElementById('missionName').value;
    const missionLaunchDate = document.getElementById('missionLaunchDate').value;
    const missionDestination = document.getElementById('missionDestination').value;
    const missionStatus = document.getElementById('missionStatus').value;
    const missionCrew = document.getElementById('missionCrew').value;
    const missionPayload = document.getElementById('missionPayload').value;
    const missionDuration = document.getElementById('missionDuration').value;
    const missionCost = document.getElementById('missionCost').value;
    const missionStatusDescription = document.getElementById('missionStatusDescription').value;

    const newMissionData = {
        name: missionName,
        launch_date: missionLaunchDate,
        destination: missionDestination,
        status: missionStatus,
        crew: missionCrew,
        payload: missionPayload,
        duration: missionDuration,
        cost: missionCost,
        status_description: missionStatusDescription
    };

    if (missionStatus == "0" || missionStatus == ""){
        alert("Selecione o estado da missão!")
        return
    }

    registerMission(newMissionData)
})

$("#btnEditarMissao").on("click", async () => {
    const missionId = document.getElementById('editMissionId').value;
    const missionName = document.getElementById('editMissionName').value;
    const missionLaunchDate = document.getElementById('editMissionLaunchDate').value;
    const missionDestination = document.getElementById('editMissionDestination').value;
    const missionStatus = document.getElementById('editMissionStatus').value;
    const missionCrew = document.getElementById('editMissionCrew').value;
    const missionPayload = document.getElementById('editMissionPayload').value;
    const missionDuration = document.getElementById('editMissionDuration').value;
    const missionCost = document.getElementById('editMissionCost').value;
    const missionStatusDescription = document.getElementById('editMissionStatusDescription').value;

    const updatedMissionData = {
        id: missionId,
        name: missionName,
        launch_date: missionLaunchDate,
        destination: missionDestination,
        status: missionStatus,
        crew: missionCrew,
        payload: missionPayload,
        duration: missionDuration,
        cost: missionCost,
        status_description: missionStatusDescription
    };


    if (missionStatus == "0" || missionStatus == ""){
        alert("Selecione o estado da missão!")
        return
    }

    let updated = await updateMission(updatedMissionData)
    if (updated) {
        alert("Missão atualizada com sucesso!")
        $("#btnFecharEditModal").trigger('click')
        renderTable()
    } else {
        alert("Ocorreu um error ao atualizar a missão!")
    }
})


$("#btnFiltrar").on("click", async () => {
    let dataInicial = $("#dataInicial").val()
    let dataFinal = $("#dataFinal").val()
    let missions = await searchByDate(dataInicial, dataFinal)
    
    $("#tBodyMissions").html("")
    globalMissions = missions.missions
    missions.missions.map(mission => { addMissionInTable(mission) })
})

$("#dataInicial").on("change", () => {
    let dataInicial = new Date($("#dataInicial").val())

    if (!dataInicial) {
        $("#dataFinal").attr("disabled", "true");
        return
    } else {
        $("#dataFinal").removeAttr("disabled");
    }    

    $("#dataFinal").attr("min", $("#dataInicial").val())
    if ($("#dataFinal").val() < $("#dataInicial").val()) {
        $("#dataFinal").val($("#dataInicial").val());
    }
})

$("#dataFinal").on("blur", () => {
    if ($("#dataFinal").val() < $("#dataFinal").attr("min")) {
        $("#dataFinal").val($("#dataInicial").val());
    }
})

$("#btnLimparFiltro").on("click", () => { 
    $("#dataInicial").val("")
    $("#dataFinal").val("")
    renderTable()
})

async function renderTable() {
    $("#tBodyMissions").html("")
    $("#info").html("")

    let missions = await getMissions()
    if (missions?.missions?.length == 0 || missions?.missions == undefined) {
        $("#info").html("<span class='d-flex justify-content-center p-4'>Sem Missões Atualmente</span>")
        return
    } 
    globalMissions = missions.missions
    missions.missions.map(mission => { addMissionInTable(mission) })
}


async function registerMission(data = { name: "", launch_date: "", destination: "", status: "", crew: "", payload: "", duration: "", cost: 0, status_description: ""}) {
    let url = `${baseUrl}/missions`
    await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
        .then(result => { 
            if (result.status == 201) {
                $("#btnCloseRegisterModal").trigger('click')
                $("#formRegister").trigger('reset');
                renderTable()
                alert("Missão registrada com sucesso!")
            } else {
                alert("Ocorreu um error ao registrar a missão!")
            }
        })
        .catch(err => {
            console.log("Ocorreu um error", err)
            alert("Ocorreu um error ao registrar a missão!")
        })
}

async function getMissions(){
    let missions = null
    let url = `${baseUrl}/missions`
    await fetch(url)
        .then(result => {
            if (result.status == 200) {
                missions = result.json()
            } else {
                alert("Ocorreu um error ao buscar as missões!")
            }
        })
        .catch(err => {
            console.log("Ocorreu um error", err)
            alert("Ocorreu um error ao buscar as missões!")
        })
    
    return missions
}

async function getMissionsById(missionId){
    let mission = null
    let url = `${baseUrl}/missions/${missionId}`
    await fetch(url)
        .then(result => mission = result.json())
        .catch(err => {
            console.log("Ocorreu um error ao buscar missão por id", err)
        })
    
    return mission
}

async function updateMission(mission = { name: "", launch_date: "", destination: "", status: "", crew: "", payload: "", duration: "", cost: 0, status_description: ""}) {
    let url = `${baseUrl}/missions`
    let updated = null
    await fetch(url, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(mission)
    })
        .then(result => {
            if (result.status == 200){
                updated = true
            }  else {
                updated = false
            }
        })
        .catch(err => {
            console.log("Ocorreu um error", err)
            updated = false
        })

    return updated
}


async function deleteMission(data = {id: null}) {
    if (!data?.id) return false
    let deleted = null
    let url = `${baseUrl}/missions`
    await fetch(url, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
        .then(result =>  {
            result.status == 200 ? deleted = true : deleted = false
        })
        .catch(err => {
            console.log("Ocorreu um error", err)
            deleted = false
        })
    return deleted
}

async function searchByDate(initialDate, finalDate) {
    let missions = null
    let url = `${baseUrl}/missions?initialDate=${initialDate}&finalDate=${finalDate}`
    await fetch(url)
        .then(result => missions = result.json())
        .catch(err => {
            console.log("Ocorreu um error", err)
            alert("Ocorreu um error ao buscar as missões!")
        })
    
    return missions
}

function addMissionInTable(mission) {
    let row = `<tr> 
        <td class='align-middle'>${mission.id}</td>
        <td class='align-middle'>${mission.name}</td>
        <td class='align-middle'>${mission.launch_date}</td>
        <td class='align-middle'>${mission.destination}</td>
        <td class='align-middle'>${mission.duration}</td>
        <td class='align-middle'>${mission.status}</td>
        <td class='align-middle'>
            <button class="edit" onclick="openModalEdit(${mission.id})">EDITAR</button>
            <button class="delete" onclick="btnDeleteMission(${mission.id})">DELETAR</button>
        </td>
    </tr>`

    document.getElementById("tBodyMissions").innerHTML += row
}

async function openModalEdit(missionId) {
    let {mission} = await getMissionsById(missionId)
    if (!mission) alert("Não foi possivel abrir modal para editar essa missão!")

    $('#editMissionId').val(mission.id);
    $('#editMissionName').val(mission.name);
    $('#editMissionLaunchDate').val(mission.launch_date);
    $('#editMissionDestination').val(mission.destination);
    $('#editMissionStatus').val(mission.status);
    $('#editMissionCrew').val(mission.crew);
    $('#editMissionPayload').val(mission.payload);
    $('#editMissionDuration').val(mission.duration);
    $('#editMissionCost').val(mission.cost);
    $('#editMissionStatusDescription').val(mission.status_description);

    $('#editModal').modal('show');
}

async function btnDeleteMission(id) {
    if (!confirm('Você tem certeza que deseja deletar essa missão?')) {
        return
    }

    let deleted = await deleteMission({id})
    if (deleted) {
        alert("Missão deletada com sucesso")
        renderTable()
    } else {
        alert("Ocorreu um error ao deletar a missão!")
    }
}