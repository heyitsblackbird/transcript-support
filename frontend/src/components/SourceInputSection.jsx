
import React, {useState} from "react";
import {Tabs, TabsList, TabsTrigger} from "@/components/ui/tabs"
import { Field, FieldLabel } from "@/components/ui/field";
import {Input} from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import generateTranscriptSummary from "@/lib/api";

function SourceInputSection({setSummary, setFlashcards}) {
    const [ activeTab, setActiveTab ] = useState("youTubeURL");
    const [ transcriptText, setTranscriptText ] = useState("");

    const handleInputMethodChange = (type) => {
        setActiveTab(type);
    };
    
    const handleTranscriptTextChange  = (event) => {
        setTranscriptText(event.target.value);
    }

    const handleGenerate = async () => {
        // Implement the logic to generate the summary based on the active tab and input data
        console.log("Generating summary for:", activeTab);
        console.log("Transcript Text:", transcriptText);

        // Call API to generate summary
        try{
            const summary = await generateTranscriptSummary(transcriptText);
            console.log("Generated Summary:", summary);
            setSummary(summary.summary);
            setFlashcards(summary.flashcards);
        }
        catch(error){
            console.error("Error generating summary:", error);
        }
    }

    return (
        <div className="m-5 p-5 bg-white rounded-lg shadow-md content-center w-full md:w-2/5">
            <Tabs defaultValue="youTubeURL" onValueChange={handleInputMethodChange}>
                <TabsList variant="line">
                    <TabsTrigger value="youTubeURL">YouTube URL</TabsTrigger>
                    <TabsTrigger value="pasteText">Paste Text</TabsTrigger>
                    <TabsTrigger value="uploadFile">Upload File</TabsTrigger>
                </TabsList>
            </Tabs>

            {activeTab === "youTubeURL" && (
                <div className="mt-5">
                    <Field>
                        <FieldLabel htmlFor="youTubeURL">YouTube URL</FieldLabel>
                        <Input id="youTubeURL" type="text" placeholder="Enter YouTube URL here" />
                    </Field>
                </div>
            )}
            {activeTab === "pasteText" && (
                <div className="mt-5">
                    <Field>
                        <FieldLabel htmlFor="pasteText">Paste Text</FieldLabel>
                        <Input id="pasteText" type="text" placeholder="Enter transcript text here" value={transcriptText} onChange={handleTranscriptTextChange} />
                    </Field>
                </div>
            )}
            {activeTab === "uploadFile" && (
                <div className="mt-5">
                    <Field>
                        <FieldLabel htmlFor="uploadFile">Upload File</FieldLabel>
                        <Input id="uploadFile" type="file" placeholder="Upload transcript file here" />
                    </Field>
                </div>
            )}
        <div className="flex flex-wrap items-center md:flex-row">
                <Button className="mt-5 " variant="outline" onClick={handleGenerate}>Generate</Button>
        </div>

        </div>

    );


}

export default SourceInputSection;