import react, { useState } from "react";

const Flashcards = ({ flashcard, idx }) => {
    const [showAnswer, setShowAnswer] = useState(false);

    const handleCardClick = () => {
        setShowAnswer(!showAnswer);
    };
    console.log(flashcard);
    console.log(idx);

  return (
    <div className="mt-4 max-w-sm rounded-2xl border-2 border-gray-300 overflow-hidden shadow-lg" onClick={handleCardClick}>
      <div className="px-6 py-4">
        <div className="mb-8 h-45 ">
          <p className="text-gray-900 font-bold text-l mb-2">
            {idx+1}. {flashcard.question}
          </p>
          <div className="text-gray-700 text-base h-30 overflow-y-auto" style={{ display: showAnswer ? "block" : "none" }}>
            {flashcard.answer}
          </div>
        </div>
      </div>
      <div className="px-3 pb-2">
        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
          {showAnswer ? "Tap to hide answer" : "Tap to reveal answer"}
        </span>
      </div>
    </div>
  );
};

export default Flashcards;
