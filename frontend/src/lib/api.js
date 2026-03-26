import axios from "axios";

// Create the conection to the backend API 
const api = axios.create({
    baseURL: "http://localhost:8000/",
    headers:{
        "Content-Type": "application/json"
    }
});

const generateTranscriptSummary = async (transcript) => {
    try{
        const response = await api.post("/api/v1/transcript/process-transcript", {
            transcriptText: transcript
        });

        return response.data;
    }
    catch(error){
        if(error.response){
            console.error("Error response:", error.response.data);
            console.error("Status code:", error.response.status);
        }
        throw error;
    }
};


export default generateTranscriptSummary;