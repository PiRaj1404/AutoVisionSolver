


async function uploadImage() {
   
    const backendUrl = "http://localhost:5000"
    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file first.");
        return;
    }

    document.getElementById("loader").style.display = "block";

    const formData = new FormData();
    formData.append("file", file);

    try {
        const detectResponse = await fetch(`${backendUrl}/detect_text`, {
            method: "POST",
            body: formData,
        });
        const detectData = await detectResponse.json();

        const detectedText = detectData.detected_text;

        if (!detectedText) {
            alert("No text detected in the image.");
            document.getElementById("loader").style.display = "none";
            return;
        }

        const translateResponse = await fetch(`${backendUrl}/translate_text`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ text: detectedText }),
        });
        const translateData = await translateResponse.json();
        const translatedText = translateData.translated_text;

        let prompt = `Based on the question: '${translatedText}', return a single string containing subject, topic, subtopic, final answer, and the solution steps separated by ,. No json`;
        
        const solveResponse = await fetch(`${backendUrl}/solve_problem`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ prompt}),
        });

        const solveData = await solveResponse.json();

        if (!solveData) {
            document.getElementById("result").textContent = "Refresh the page and re-enter the file.";
            document.getElementById("loader").style.display = "none";
            return;
        }

        const { subject, topic, sub_topic, final_answer, solution_steps } = solveData.solution;

        const formattedSolutionSteps = solution_steps.map(step => `<li>${step}</li>`).join("");

        document.getElementById("result").innerHTML = `
            <h2>Question:</h2>
            <p>${translatedText}</p>
            <h2>Solution:</h2>
            <h4>Final Answer</h4>
            <p>${final_answer}</p>
            <h4>Subject</h4>
            <p>${subject}</p>
            <h4>Topic</h4>
            <p>${topic}</p>
            <h4>Subtopic</h4>
            <p>${sub_topic}</p>
            <h4>Steps:</h4>
            <ul>${formattedSolutionSteps}</ul>
        `;

        

        const dataToSend = {
            subject: subject,
            topic: topic,
            sub_topic: sub_topic,
            final_answer: final_answer,
            question: translatedText,
            solution_steps: solution_steps
        };
        console.log(dataToSend)
        
        const saveDataToFile = await fetch(`${backendUrl}/save_to_file`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ text: dataToSend }),
        });
        
        
        if (saveDataToFile.ok) {
            console.log("Data saved successfully.");
        } else {
            console.error("Failed to save data:", saveDataToFile.status, saveDataToFile.statusText);
        }
        document.getElementById("loader").style.display = "none";
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
        document.getElementById("loader").style.display = "none";
    }
}
