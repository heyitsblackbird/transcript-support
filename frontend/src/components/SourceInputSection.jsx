
import React, {useState} from "react";
import {Tabs, TabsList, TabsTrigger} from "@/components/ui/tabs"
import { Field, FieldLabel } from "./ui/field";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
function SourceInputSection() {
    const [ activeTab, setActiveTab ] = useState("youTubeURL");
    const [ transcriptText, setTranscriptText ] = useState("");

    const handleInputMethodChange = (type) => {
        setActiveTab(type);
    };
    
    const handleTranscriptTextChange  = (event) => {
        setTranscriptText(event.target.value);
    }

    console.log("Active Tab:", activeTab);
    console.log("Transcript Text:", transcriptText);

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
                    <Button className="mt-5 " variant="outline">Generate</Button>
        </div>

        </div>

    );


}

export default SourceInputSection;