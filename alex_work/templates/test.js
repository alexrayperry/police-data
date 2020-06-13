var data = JSON.parse('{{ data | tojson }}');

console.log(data);



// function loadData(incident_race) {
//     d3.json("sf_police_data.json").then(function(data) {
//         var filteredData = data.filter(incident => incident.subject_race === incident_race)
//         console.log(filteredData);

//         var results = []
//         filteredData.forEach(element => {
//             var result = {}
//             result["coordinates"] = [element.lat, element.lng]
            
//             results.push(result)

//         });
//         return results;
//     })
// }
// var hispanicData = loadData("hispanic");

