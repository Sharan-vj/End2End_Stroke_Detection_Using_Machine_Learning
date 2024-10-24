function makePrediction() {
    const data = {
        gender: parseFloat(document.getElementById('gender').value),
        age: parseInt(document.getElementById('age').value),
        hypertension: parseInt(document.getElementById('hypertension').value),
        heart_disease: parseFloat(document.getElementById('heartdisease').value),
        ever_married: parseFloat(document.getElementById('evermarried').value),
        work_type: parseInt(document.getElementById('worktype').value),
        residence_type: parseInt(document.getElementById('residencetype').value),
        avg_glucose_level: parseFloat(document.getElementById('avgglucoselevel').value),
        bmi: parseInt(document.getElementById('bmi').value),
        smoking_status: parseFloat(document.getElementById('smokingstatus').value)
    };

    fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = `<strong>${data.message}</strong>`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('result').innerHTML = `<span style='color: red;'>Error: ${error.message}</span>`;
        });
}