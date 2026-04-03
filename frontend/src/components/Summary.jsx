import React,{useState} from "react";
import Flashcards from "./Flashcards";

const Summary = ({summary, flashcards}) =>{
    return(
        <div className="m-5 p-5  bg-white rounded-lg shadow-md content-center w-full md:w-3/5 align-bottom">
            <h2 className=" font-bold text-xl">Summary</h2>
            <div className="m-2 bg-slate-100 p-3 rounded-lg">
                <h3 className="text-lg font-medium mb-2">AI Summary</h3>
                <div className="overflow-y-auto h-50">
                    {summary || "Your summary will appear here after you generate it."}
                </div>
            </div>
            <div className="flex-1 border-t-3 mx-2"></div>
            <div className="m-2">
                <h2 className="font-bold text-xl">Flashcards</h2>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    {flashcards?.map((flashcard, idx) => (
                        <Flashcards flashcard={flashcard} idx={idx} />
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Summary;