import axios from "axios";

// Create the conection to the backend API 
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    headers:{
        "Content-Type": "application/json"
    }
});

export const generateTranscriptSummary = async (transcript) => {
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

export const generateTranscriptSummaryForYouTube = async (videoUrl) => {
    try{
        const response = await api.post("/api/v1/transcript/process-youtube-transcript", {
            videoUrl: videoUrl
        });
        console.log("API Response:", response.data);
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